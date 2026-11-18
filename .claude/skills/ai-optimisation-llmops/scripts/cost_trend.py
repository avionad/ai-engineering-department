#!/usr/bin/env python3
"""Monthly AI cost and usage trend per system, from a usage CSV.

Part of the practice ai-optimisation-llmops skill, v0.1.0, 2026-11-08. Standard library only.

It NEVER prices tokens. All money figures are sums of the cost_aud column supplied in the data
(billing export, trace store export or automation run log). Token counts are reported as volumes.

Input columns (header row required, extra columns ignored):
  date (YYYY-MM-DD), system, model, tasks, input_tokens, output_tokens, cached_input_tokens, cost_aud

cached_input_tokens is treated as the part of input_tokens read from cache (a subset). If your
export reports cached tokens separately from input_tokens, pass --cached-separate.

Output per system and month: tasks, cost, cost per task, input and output tokens per task, token
mix (input vs output share of all tokens), cache share (cached / all input tokens), model cost mix,
month-on-month change in cost per task, and flags:
  COST/TASK UP    cost per task rose more than --flag-threshold vs the previous month
                  (default 0.20 = 20%: a House default, not an industry figure; set per client)
  VOLUME SWING    tasks changed more than --volume-threshold vs previous month (context, default 0.30, House default)
  MODEL CHANGE    a model appeared or disappeared vs the previous month (context)
  PARTIAL MONTH   the latest month's data stops before the month's last day (volume swing
                  is not flagged for a partial month; cost per task still compared)
  NO TASKS        cost recorded with zero tasks (cost per task undefined)

Usage:
  python3 cost_trend.py usage.csv [--system NAME] [--flag-threshold 0.20] [--volume-threshold 0.30]
                        [--cached-separate] [--md out.md] [--json out.json]
Exit codes: 0 no COST/TASK UP flag, 1 at least one COST/TASK UP flag, 3 input error.
"""

import argparse
import calendar
import csv
import json
import sys
from collections import defaultdict
from datetime import date

REQUIRED = ("date", "system", "model", "tasks", "input_tokens", "output_tokens",
            "cached_input_tokens", "cost_aud")


class InputError(Exception):
    pass


def parse_rows(path, cached_separate, only_system=None):
    rows = []
    try:
        fh = open(path, newline="", encoding="utf-8-sig")
    except FileNotFoundError:
        raise InputError(f"{path}: file not found")
    with fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            raise InputError(f"{path}: empty file")
        headers = [h.strip().lower() for h in reader.fieldnames]
        missing = [c for c in REQUIRED if c not in headers]
        if missing:
            raise InputError(f"{path}: missing column(s) {', '.join(missing)}")
        for n, raw in enumerate(reader, start=2):
            r = {k.strip().lower(): (v or "").strip() for k, v in raw.items() if k}
            if not any(r.values()):
                continue
            try:
                d = date.fromisoformat(r["date"])
            except ValueError:
                raise InputError(f"line {n}: date '{r['date']}' is not YYYY-MM-DD")
            try:
                tasks = int(float(r["tasks"] or 0))
                inp = int(float(r["input_tokens"] or 0))
                out = int(float(r["output_tokens"] or 0))
                cached = int(float(r["cached_input_tokens"] or 0))
                cost = float(r["cost_aud"])
            except ValueError:
                raise InputError(f"line {n}: tasks, token and cost_aud columns must be numbers")
            if min(tasks, inp, out, cached) < 0 or cost < 0:
                raise InputError(f"line {n}: negative value")
            if not cached_separate and cached > inp:
                raise InputError(f"line {n}: cached_input_tokens ({cached}) > input_tokens ({inp}); "
                                 "use --cached-separate if your export counts them separately")
            total_input = inp + cached if cached_separate else inp
            if not r["system"]:
                raise InputError(f"line {n}: empty system")
            if only_system and r["system"] != only_system:
                continue
            rows.append({"date": d, "month": d.strftime("%Y-%m"), "system": r["system"],
                         "model": r["model"] or "(unknown)", "tasks": tasks,
                         "input": total_input, "output": out, "cached": cached, "cost": cost})
    if not rows:
        raise InputError("no usable rows" + (f" for system '{only_system}'" if only_system else ""))
    return rows


def aggregate(rows):
    agg = defaultdict(lambda: {"tasks": 0, "input": 0, "output": 0, "cached": 0, "cost": 0.0,
                               "models": defaultdict(float), "last_date": None, "days": set()})
    for r in rows:
        a = agg[(r["system"], r["month"])]
        a["tasks"] += r["tasks"]
        a["input"] += r["input"]
        a["output"] += r["output"]
        a["cached"] += r["cached"]
        a["cost"] += r["cost"]
        a["models"][r["model"]] += r["cost"]
        a["days"].add(r["date"])
        if a["last_date"] is None or r["date"] > a["last_date"]:
            a["last_date"] = r["date"]
    return agg


def div(a, b):
    return a / b if b else None


def build(rows, flag_threshold, volume_threshold):
    agg = aggregate(rows)
    latest_month = max(r["month"] for r in rows)
    systems = sorted({s for s, _ in agg})
    report = []
    any_cost_flag = False
    for s in systems:
        months = sorted(m for (sy, m) in agg if sy == s)
        prev = None
        for m in months:
            a = agg[(s, m)]
            y, mo = map(int, m.split("-"))
            partial = (m == latest_month and a["last_date"].day < calendar.monthrange(y, mo)[1])
            tokens = a["input"] + a["output"]
            cpt = div(a["cost"], a["tasks"])
            rec = {
                "system": s, "month": m, "tasks": a["tasks"], "cost_aud": round(a["cost"], 2),
                "cost_per_task": None if cpt is None else round(cpt, 4),
                "input_tokens_per_task": None if not a["tasks"] else round(a["input"] / a["tasks"], 1),
                "output_tokens_per_task": None if not a["tasks"] else round(a["output"] / a["tasks"], 1),
                "input_share": None if not tokens else round(a["input"] / tokens, 4),
                "output_share": None if not tokens else round(a["output"] / tokens, 4),
                "cache_share": None if not a["input"] else round(a["cached"] / a["input"], 4),
                "model_cost_mix": {k: round(v / a["cost"], 4) if a["cost"] else None
                                   for k, v in sorted(a["models"].items(), key=lambda kv: -kv[1])},
                "days_with_data": len(a["days"]),
                "cpt_change": None, "tasks_change": None, "flags": [],
            }
            if a["tasks"] == 0 and a["cost"] > 0:
                rec["flags"].append("NO TASKS")
            if prev is not None:
                if prev["cost_per_task"] and cpt is not None:
                    rec["cpt_change"] = round(cpt / prev["cost_per_task"] - 1, 4)
                    if rec["cpt_change"] > flag_threshold:
                        rec["flags"].append(f"COST/TASK UP >{flag_threshold:.0%}")
                        any_cost_flag = True
                if prev["tasks"]:
                    rec["tasks_change"] = round(a["tasks"] / prev["tasks"] - 1, 4)
                    if abs(rec["tasks_change"]) > volume_threshold and not partial:
                        rec["flags"].append(f"VOLUME SWING >{volume_threshold:.0%}")
                added = set(rec["model_cost_mix"]) - set(prev["model_cost_mix"])
                dropped = set(prev["model_cost_mix"]) - set(rec["model_cost_mix"])
                if added or dropped:
                    parts = []
                    if added:
                        parts.append("+" + ",".join(sorted(added)))
                    if dropped:
                        parts.append("-" + ",".join(sorted(dropped)))
                    rec["flags"].append("MODEL CHANGE " + " ".join(parts))
            if partial:
                rec["flags"].append(f"PARTIAL MONTH (to {a['last_date'].isoformat()}; volume not comparable)")
            report.append(rec)
            prev = rec
    return report, any_cost_flag


def f_money(x, dp=2):
    return "-" if x is None else f"{x:,.{dp}f}"


def f_pct(x, signed=False):
    if x is None:
        return "-"
    return f"{x * 100:+.1f}%" if signed else f"{x * 100:.1f}%"


def render(report, src, flag_threshold, volume_threshold, markdown=False):
    lines = []
    lines.append(("# " if markdown else "") + "AI cost and usage trend")
    lines.append("")
    lines.append(f"Source: {src}. Money = sums of the cost_aud column as supplied; no token prices applied.")
    lines.append(f"Flag threshold: cost per task up >{flag_threshold:.0%} month on month (House default 20%, "
                 f"set per client). Volume swing context flag: >{volume_threshold:.0%} (House default).")
    lines.append("")
    head = ["System", "Month", "Tasks", "Cost AUD", "Cost/task", "MoM cost/task", "MoM tasks",
            "In tok/task", "Out tok/task", "Mix in/out", "Cache share", "Top model (cost share)", "Flags"]
    body = []
    for r in report:
        top = next(iter(r["model_cost_mix"].items()), ("-", None))
        body.append([r["system"], r["month"], f"{r['tasks']:,}", f_money(r["cost_aud"]),
                     f_money(r["cost_per_task"], 4), f_pct(r["cpt_change"], True),
                     f_pct(r["tasks_change"], True),
                     f_money(r["input_tokens_per_task"], 0), f_money(r["output_tokens_per_task"], 0),
                     f"{f_pct(r['input_share'])}/{f_pct(r['output_share'])}", f_pct(r["cache_share"]),
                     f"{top[0]} ({f_pct(top[1])})", "; ".join(r["flags"]) or "-"])
    if markdown:
        lines.append("| " + " | ".join(head) + " |")
        lines.append("|" + "---|" * len(head))
        lines += ["| " + " | ".join(b) + " |" for b in body]
    else:
        widths = [max(len(x) for x in col) for col in zip(head, *body)]
        lines.append("  ".join(h.ljust(w) for h, w in zip(head, widths)))
        lines += ["  ".join(c.ljust(w) for c, w in zip(b, widths)) for b in body]
    lines.append("")
    flagged = [r for r in report if any(f.startswith("COST/TASK UP") for f in r["flags"])]
    lines.append(("## " if markdown else "") + "Cost per task flags")
    if not flagged:
        lines.append("- none")
    for r in flagged:
        ctx = [f for f in r["flags"] if not f.startswith("COST/TASK UP")]
        lines.append(f"- {r['system']} {r['month']}: cost per task {f_money(r['cost_per_task'], 4)} AUD "
                     f"({f_pct(r['cpt_change'], True)} vs previous month)"
                     + (f"; context: {'; '.join(ctx)}" if ctx else "; no volume or model change flagged: investigate prompt, retrieval and output length"))
    lines.append("")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Monthly AI cost per task and token mix from a usage CSV.")
    ap.add_argument("usage_csv")
    ap.add_argument("--system", help="only this system")
    ap.add_argument("--flag-threshold", type=float, default=0.20,
                    help="flag cost per task rises above this fraction month on month (House default 0.20)")
    ap.add_argument("--volume-threshold", type=float, default=0.30,
                    help="context flag for task volume swings (House default 0.30)")
    ap.add_argument("--cached-separate", action="store_true",
                    help="cached_input_tokens are NOT included in input_tokens in this export")
    ap.add_argument("--md", "--out", help="write a Markdown copy")
    ap.add_argument("--json", help="write the full result as JSON")
    args = ap.parse_args()
    if args.flag_threshold < 0 or args.volume_threshold < 0:
        print("INPUT ERROR: thresholds must be zero or positive", file=sys.stderr)
        return 3
    try:
        rows = parse_rows(args.usage_csv, args.cached_separate, args.system)
    except InputError as exc:
        print(f"INPUT ERROR: {exc}", file=sys.stderr)
        return 3
    report, flagged = build(rows, args.flag_threshold, args.volume_threshold)
    print(render(report, args.usage_csv, args.flag_threshold, args.volume_threshold), end="")
    if args.md:
        with open(args.md, "w", encoding="utf-8") as fh:
            fh.write(render(report, args.usage_csv, args.flag_threshold, args.volume_threshold, True))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2)
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
