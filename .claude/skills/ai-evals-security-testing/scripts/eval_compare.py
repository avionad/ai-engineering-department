#!/usr/bin/env python3
"""Compare two AI eval result CSVs (baseline vs current) and return a verdict.

Part of the DDD ai-evals-security-testing skill, v0.1.0, 2026-11-08. Standard library only.

Input CSVs need columns: test_id, category, passed (true/false; also yes/no, 1/0, pass/fail).
Optional column: score (0 to 1). Extra columns are ignored. One row per test_id.

Thresholds JSON (agreed with the client and recorded; see references/eval-design.md s4):
{
  "agreed_by": "Name, role (client)",
  "agreed_on": "YYYY-MM-DD",
  "default_min_pass_rate": null,
  "max_regressions": 0,
  "categories": {
    "retrieval-answer": {"min_pass_rate": 0.9, "max_mean_score_drop": 0.05},
    "permission-leak": {"blocking": true}
  },
  "accepted_regressions": {"RAG-010": "Accepted by <name> on <date>: <reason>"}
}

Verdict rules:
  FAIL                  a blocking category has any failure; a category is below its
                        min_pass_rate; unaccepted regressions exceed max_regressions (default 0);
                        mean score dropped more than max_mean_score_drop.
  PASS WITH CONDITIONS  none of the above, but there are new failures, tests missing from the
                        current run, categories with no agreed threshold, or accepted regressions.
  PASS                  none of the above.
  NO VERDICT            thresholds not recorded (agreed_by / agreed_on missing) or bad input.

Exit codes: 0 PASS, 1 PASS WITH CONDITIONS, 2 FAIL, 3 NO VERDICT / input error.

Usage:
  python3 eval_compare.py baseline.csv current.csv --thresholds thresholds.json [--md out.md] [--json out.json]
"""

import argparse
import csv
import json
import sys

TRUE_VALUES = {"true", "yes", "y", "1", "pass", "passed"}
FALSE_VALUES = {"false", "no", "n", "0", "fail", "failed"}
REQUIRED = ("test_id", "category", "passed")


class InputError(Exception):
    pass


def load_results(path):
    rows = {}
    try:
        with open(path, newline="", encoding="utf-8-sig") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames is None:
                raise InputError(f"{path}: empty file")
            headers = [h.strip().lower() for h in reader.fieldnames]
            missing = [c for c in REQUIRED if c not in headers]
            if missing:
                raise InputError(f"{path}: missing column(s) {', '.join(missing)}")
            for line_no, raw in enumerate(reader, start=2):
                row = {k.strip().lower(): (v or "").strip() for k, v in raw.items() if k}
                tid = row["test_id"]
                if not tid:
                    raise InputError(f"{path} line {line_no}: empty test_id")
                if tid in rows:
                    raise InputError(f"{path} line {line_no}: duplicate test_id {tid}")
                passed_raw = row["passed"].lower()
                if passed_raw in TRUE_VALUES:
                    passed = True
                elif passed_raw in FALSE_VALUES:
                    passed = False
                else:
                    raise InputError(f"{path} line {line_no}: passed value '{row['passed']}' not true/false")
                score = None
                if row.get("score"):
                    try:
                        score = float(row["score"])
                    except ValueError:
                        raise InputError(f"{path} line {line_no}: score '{row['score']}' is not a number")
                rows[tid] = {"category": row["category"] or "(none)", "passed": passed, "score": score}
    except FileNotFoundError:
        raise InputError(f"{path}: file not found")
    if not rows:
        raise InputError(f"{path}: no result rows")
    return rows


def load_thresholds(path):
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        raise InputError(f"{path}: thresholds file not found")
    except json.JSONDecodeError as exc:
        raise InputError(f"{path}: invalid JSON ({exc})")
    if not isinstance(data, dict):
        raise InputError(f"{path}: thresholds must be a JSON object")
    return data


def pct(x):
    return "n/a" if x is None else f"{x * 100:.1f}%"


def summarise(rows):
    cats = {}
    for r in rows.values():
        c = cats.setdefault(r["category"], {"n": 0, "passed": 0, "scores": []})
        c["n"] += 1
        c["passed"] += 1 if r["passed"] else 0
        if r["score"] is not None:
            c["scores"].append(r["score"])
    for c in cats.values():
        c["rate"] = c["passed"] / c["n"] if c["n"] else None
        c["mean_score"] = sum(c["scores"]) / len(c["scores"]) if c["scores"] else None
    return cats


def compare(base, cur, thr):
    result = {"fail_reasons": [], "conditions": [], "warnings": []}
    agreed_by = str(thr.get("agreed_by") or "").strip()
    agreed_on = str(thr.get("agreed_on") or "").strip()
    result["agreed_by"], result["agreed_on"] = agreed_by, agreed_on
    cat_thr = thr.get("categories") or {}
    default_min = thr.get("default_min_pass_rate")
    max_reg = thr.get("max_regressions", 0)
    accepted = thr.get("accepted_regressions") or {}

    bsum, csum = summarise(base), summarise(cur)
    categories = sorted(set(bsum) | set(csum))
    table = []
    for cat in categories:
        b, c = bsum.get(cat), csum.get(cat)
        t = cat_thr.get(cat, {})
        min_rate = t.get("min_pass_rate", default_min)
        blocking = bool(t.get("blocking", False))
        max_drop = t.get("max_mean_score_drop")
        flags = []
        if c is None:
            flags.append("missing in current")
            result["conditions"].append(f"category '{cat}' has no tests in the current run")
        else:
            if blocking and c["passed"] < c["n"]:
                flags.append("FAIL blocking")
                result["fail_reasons"].append(
                    f"blocking category '{cat}': {c['n'] - c['passed']} failure(s)")
            elif min_rate is not None and c["rate"] < float(min_rate):
                flags.append("FAIL below threshold")
                result["fail_reasons"].append(
                    f"category '{cat}' pass rate {pct(c['rate'])} below agreed {pct(float(min_rate))}")
            elif min_rate is None and not blocking:
                flags.append("no agreed threshold")
                result["conditions"].append(f"category '{cat}' has no agreed threshold")
            if (max_drop is not None and b and b["mean_score"] is not None
                    and c["mean_score"] is not None
                    and (b["mean_score"] - c["mean_score"]) > float(max_drop)):
                flags.append("FAIL score drop")
                result["fail_reasons"].append(
                    f"category '{cat}' mean score fell {b['mean_score'] - c['mean_score']:.3f} "
                    f"(agreed max drop {float(max_drop):.3f})")
        table.append({
            "category": cat,
            "baseline": f"{b['passed']}/{b['n']}" if b else "-",
            "baseline_rate": b["rate"] if b else None,
            "current": f"{c['passed']}/{c['n']}" if c else "-",
            "current_rate": c["rate"] if c else None,
            "change_pts": ((c["rate"] - b["rate"]) * 100) if (b and c) else None,
            "baseline_mean_score": b["mean_score"] if b else None,
            "current_mean_score": c["mean_score"] if c else None,
            "threshold": ("blocking" if blocking else (pct(float(min_rate)) if min_rate is not None else "not agreed")),
            "status": "; ".join(flags) or "ok",
        })
    result["table"] = table

    regressions, accepted_regs, fixed, new_fail, new_pass, missing, moved = [], [], [], [], [], [], []
    for tid, c in cur.items():
        b = base.get(tid)
        if b is None:
            (new_pass if c["passed"] else new_fail).append((tid, c["category"]))
            continue
        if b["category"] != c["category"]:
            moved.append((tid, b["category"], c["category"]))
        if b["passed"] and not c["passed"]:
            (accepted_regs if tid in accepted else regressions).append((tid, c["category"]))
        elif not b["passed"] and c["passed"]:
            fixed.append((tid, c["category"]))
    for tid, b in base.items():
        if tid not in cur:
            missing.append((tid, b["category"]))

    result.update(regressions=sorted(regressions), accepted_regressions=sorted(accepted_regs),
                  fixed=sorted(fixed), new_failures=sorted(new_fail), new_passes=sorted(new_pass),
                  missing=sorted(missing), moved=sorted(moved),
                  accepted_reasons={k: accepted[k] for k, _ in accepted_regs})

    if len(regressions) > int(max_reg):
        result["fail_reasons"].append(
            f"{len(regressions)} unaccepted regression(s); agreed maximum {int(max_reg)}")
    if accepted_regs:
        result["conditions"].append(f"{len(accepted_regs)} regression(s) accepted in writing")
    if new_fail:
        result["conditions"].append(f"{len(new_fail)} new test(s) failing")
    if missing:
        result["conditions"].append(f"{len(missing)} baseline test(s) missing from the current run")
    for tid, old, new in moved:
        result["warnings"].append(f"{tid} moved category {old} -> {new}")

    if not agreed_by or not agreed_on:
        result["verdict"] = "NO VERDICT"
        result["fail_reasons"].insert(0, "thresholds not recorded: agreed_by and agreed_on are required")
    elif result["fail_reasons"]:
        result["verdict"] = "FAIL"
    elif result["conditions"]:
        result["verdict"] = "PASS WITH CONDITIONS"
    else:
        result["verdict"] = "PASS"
    result["totals"] = {
        "baseline": f"{sum(r['passed'] for r in base.values())}/{len(base)}",
        "current": f"{sum(r['passed'] for r in cur.values())}/{len(cur)}",
    }
    return result


def fmt_score(x):
    return "-" if x is None else f"{x:.3f}"


def render(res, base_path, cur_path, markdown=False):
    out = []
    h = "## " if markdown else ""
    out.append(f"{'# ' if markdown else ''}Eval comparison")
    out.append("")
    out.append(f"Baseline: {base_path} ({res['totals']['baseline']} passed)")
    out.append(f"Current:  {cur_path} ({res['totals']['current']} passed)")
    out.append(f"Thresholds agreed by: {res['agreed_by'] or 'NOT RECORDED'} on {res['agreed_on'] or 'NOT RECORDED'}")
    out.append("")
    out.append(f"{h}Per-category pass rates")
    out.append("")
    head = ["Category", "Baseline", "Rate", "Current", "Rate", "Change (pts)", "Mean score b/c", "Threshold", "Status"]
    rows = []
    for t in res["table"]:
        chg = "-" if t["change_pts"] is None else f"{t['change_pts']:+.1f}"
        rows.append([t["category"], t["baseline"], pct(t["baseline_rate"]), t["current"],
                     pct(t["current_rate"]), chg,
                     f"{fmt_score(t['baseline_mean_score'])}/{fmt_score(t['current_mean_score'])}",
                     t["threshold"], t["status"]])
    if markdown:
        out.append("| " + " | ".join(head) + " |")
        out.append("|" + "---|" * len(head))
        for r in rows:
            out.append("| " + " | ".join(r) + " |")
    else:
        widths = [max(len(str(x)) for x in col) for col in zip(head, *rows)]
        out.append("  ".join(str(x).ljust(w) for x, w in zip(head, widths)))
        for r in rows:
            out.append("  ".join(str(x).ljust(w) for x, w in zip(r, widths)))
    out.append("")

    def section(title, items, fmt):
        out.append(f"{h}{title} ({len(items)})")
        if items:
            for it in items:
                out.append(f"- {fmt(it)}")
        else:
            out.append("- none")
        out.append("")

    section("Regressions: passed at baseline, fail now", res["regressions"], lambda x: f"{x[0]} [{x[1]}]")
    section("Regressions accepted in writing", res["accepted_regressions"],
            lambda x: f"{x[0]} [{x[1]}]: {res['accepted_reasons'].get(x[0], '')}")
    section("New failures: tests not in baseline that fail", res["new_failures"], lambda x: f"{x[0]} [{x[1]}]")
    section("Fixed: failed at baseline, pass now", res["fixed"], lambda x: f"{x[0]} [{x[1]}]")
    section("Missing from current run", res["missing"], lambda x: f"{x[0]} [{x[1]}]")
    if res["warnings"]:
        section("Warnings", res["warnings"], lambda x: x)
    if res["fail_reasons"]:
        section("Blocking reasons", res["fail_reasons"], lambda x: x)
    if res["conditions"]:
        section("Conditions", res["conditions"], lambda x: x)
    out.append(f"VERDICT: {res['verdict']}")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Compare baseline and current eval result CSVs.")
    ap.add_argument("baseline")
    ap.add_argument("current")
    ap.add_argument("--thresholds", required=True, help="thresholds JSON agreed with the client")
    ap.add_argument("--md", "--out", help="write a Markdown copy of the report")
    ap.add_argument("--json", help="write the full result as JSON")
    args = ap.parse_args()
    try:
        base = load_results(args.baseline)
        cur = load_results(args.current)
        thr = load_thresholds(args.thresholds)
    except InputError as exc:
        print(f"INPUT ERROR: {exc}", file=sys.stderr)
        print("VERDICT: NO VERDICT")
        return 3
    res = compare(base, cur, thr)
    print(render(res, args.baseline, args.current), end="")
    if args.md:
        with open(args.md, "w", encoding="utf-8") as fh:
            fh.write(render(res, args.baseline, args.current, markdown=True))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=2)
    return {"PASS": 0, "PASS WITH CONDITIONS": 1, "FAIL": 2}.get(res["verdict"], 3)


if __name__ == "__main__":
    sys.exit(main())
