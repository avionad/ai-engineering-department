#!/usr/bin/env python3
"""readiness_score.py -- the practice AI readiness scorecard and Go/Wait gate.

Stdlib only. Reads a JSON assessment (see ../templates/readiness-input-template.json), validates
it, and writes a markdown scorecard with:
  - seven-dimension scorecard (1-5, half points) with evidence counts and confidence
  - governance practices (NAIC Guidance for AI Adoption, six practices) and the APP 1.7 ADM flag
  - organisation gate (Go / Go with conditions / Wait) and per-use-case gate (Go / Wait)
  - ranked 90-day action plan (P1 prerequisites, P2 foundations, P3 first use cases, P4 next)

Gate rules are documented in ../references/gates.md. Change both together.

Usage:
    python3 readiness_score.py input.json                 # markdown to stdout
    python3 readiness_score.py input.json --out card.md   # markdown to file
    python3 readiness_score.py input.json --json out.json # machine-readable result too

Exit codes: 0 = scored (any gate result), 2 = invalid input (nothing scored).
"""
import argparse
import datetime as dt
import json
import sys

DIMENSIONS = [
    ("strategy_leadership", "Strategy and leadership"),
    ("data", "Data"),
    ("technology_infrastructure", "Technology and infrastructure"),
    ("people_skills", "People and skills"),
    ("process", "Process"),
    ("governance_risk", "Governance and risk"),
    ("security_privacy", "Security and privacy"),
]
PRACTICES = [
    ("accountability", "1. Decide who is accountable"),
    ("impacts", "2. Understand impacts and plan accordingly"),
    ("risk_management", "3. Measure and manage risks"),
    ("information_sharing", "4. Share essential information"),
    ("test_monitor", "5. Test and monitor"),
    ("human_control", "6. Maintain human control"),
]
LEVELS = {1: "Not ready", 2: "Emerging", 3: "Defined", 4: "Managed", 5: "Optimised"}
PRACTICE_STATUS = {0: "Absent", 1: "Partial", 2: "In place"}
ADM_START = dt.date(2026, 12, 10)  # APP 1.7-1.9 commencement (research file A1, checked 2026-11-08)
RANK = {"high": 0, "medium": 1, "low": 2}
EFFORT = {"low": 0, "medium": 1, "high": 2}
NOT_LEGAL = ("This assessment identifies regulatory considerations for review by your legal "
             "adviser. It is not legal advice.")


def validate(d):
    errs = []
    for k in ("client", "size_band", "assessment_date", "dimensions"):
        if k not in d:
            errs.append(f"missing top-level field '{k}'")
    if errs:
        return errs
    if d["size_band"] not in ("S", "M", "L", "XL"):
        errs.append("size_band must be S, M, L or XL")
    try:
        dt.date.fromisoformat(d["assessment_date"])
    except ValueError:
        errs.append("assessment_date must be YYYY-MM-DD")
    dims = d["dimensions"]
    for key, label in DIMENSIONS:
        if key not in dims:
            errs.append(f"dimension '{key}' missing")
            continue
        s = dims[key].get("score")
        if not isinstance(s, (int, float)) or s < 1 or s > 5 or (s * 2) != int(s * 2):
            errs.append(f"{key}.score must be 1-5 in half points (got {s!r})")
        if dims[key].get("confidence", "medium") not in ("high", "medium", "low"):
            errs.append(f"{key}.confidence must be high, medium or low")
        for a in dims[key].get("actions", []):
            if "action" not in a:
                errs.append(f"{key}: every action needs an 'action' field")
            if a.get("impact", "medium") not in RANK or a.get("effort", "medium") not in EFFORT:
                errs.append(f"{key}: impact must be high/medium/low and effort low/medium/high")
    extra = set(dims) - {k for k, _ in DIMENSIONS}
    if extra:
        errs.append(f"unknown dimension keys: {sorted(extra)}")
    gp = d.get("governance_practices", {})
    for key, _ in PRACTICES:
        if key in gp and gp[key] not in (0, 1, 2):
            errs.append(f"governance_practices.{key} must be 0, 1 or 2")
    adm = d.get("adm", {})
    if adm.get("exposure", "unknown") not in ("yes", "no", "unknown"):
        errs.append("adm.exposure must be yes, no or unknown")
    for i, u in enumerate(d.get("use_cases", [])):
        if "name" not in u:
            errs.append(f"use_cases[{i}] needs a name")
        t = u.get("risk_tier")
        if t is not None and t not in (1, 2, 3, 4):
            errs.append(f"use_cases[{i}].risk_tier must be 1-4 or null")
        v = u.get("annual_value_aud")
        if v is not None and not u.get("value_source"):
            errs.append(f"use_cases[{i}] has a value but no value_source (client's numbers only)")
    w = d.get("weights")
    if w is not None:
        if set(w) != {k for k, _ in DIMENSIONS} or any(not isinstance(x, (int, float)) or x < 0 for x in w.values()):
            errs.append("weights must give a non-negative number for all seven dimensions")
        elif not d.get("weights_rationale"):
            errs.append("weights supplied without weights_rationale")
    return errs


def evidence_counts(ev):
    seen = stated = other = 0
    for e in ev or []:
        t = e.get("type") if isinstance(e, dict) else None
        if t == "seen":
            seen += 1
        elif t == "stated":
            stated += 1
        else:
            other += 1
    return seen, stated, other


def dim_status(score, has_ev):
    if not has_ev:
        return "unevidenced"
    if score <= 1.5:
        return "deal-breaker"
    if score <= 2.5:
        return "condition"
    if score <= 3.5:
        return "ok"
    return "strong"


def use_case_gate(u):
    blockers = []
    if not u.get("data_ready"):
        blockers.append("data not ready")
    if not u.get("owner"):
        blockers.append("no named owner")
    if not u.get("pilot_30_days"):
        blockers.append("cannot pilot in about 30 days")
    t = u.get("risk_tier")
    if t is None:
        blockers.append("risk tier not assigned (run ai-compliance-risk)")
    elif t == 4:
        blockers.append("risk tier 4: do not build")
    elif t == 3 and not u.get("compliance_screen_done"):
        blockers.append("tier 3 without a recorded compliance screen")
    return ("Go" if not blockers else "Wait"), blockers


def analyse(d):
    dims = d["dimensions"]
    rows, warnings = [], []
    for key, label in DIMENSIONS:
        x = dims[key]
        seen, stated, other = evidence_counts(x.get("evidence"))
        has_ev = (seen + stated + other) > 0
        conf = x.get("confidence", "medium")
        if has_ev and seen == 0 and conf == "high":
            warnings.append(f"{label}: confidence 'high' but no evidence was seen (stated only); lowered to medium")
            conf = "medium"
        if other:
            warnings.append(f"{label}: {other} evidence item(s) without type seen/stated")
        rows.append({"key": key, "label": label, "score": float(x["score"]),
                     "level": LEVELS[int(x["score"])], "confidence": conf,
                     "seen": seen, "stated": stated, "status": dim_status(float(x["score"]), has_ev),
                     "actions": x.get("actions", [])})

    w = d.get("weights") or {k: 1.0 for k, _ in DIMENSIONS}
    total_w = sum(w.values()) or 1.0
    mean = sum(r["score"] * w[r["key"]] for r in rows) / total_w

    ucs = []
    for u in d.get("use_cases", []):
        res, blockers = use_case_gate(u)
        ucs.append({**u, "gate": res, "blockers": blockers})
    go_ucs = [u for u in ucs if u["gate"] == "Go"]

    reasons = []
    breakers = [r for r in rows if r["status"] == "deal-breaker"]
    unevid = [r for r in rows if r["status"] == "unevidenced"]
    conds = [r for r in rows if r["status"] == "condition"]
    if breakers:
        reasons.append("deal-breaker in: " + ", ".join(r["label"] for r in breakers))
    if unevid:
        reasons.append("no evidence recorded for: " + ", ".join(r["label"] for r in unevid))
    if not go_ucs:
        reasons.append("no candidate use case passes the use-case gate")
    if reasons:
        org = "Wait"
    elif conds:
        org = "Go with conditions"
        reasons.append("conditions: lift " + ", ".join(r["label"] for r in conds) + " alongside the pilot")
    else:
        org = "Go"
        reasons.append("all dimensions 3 or above with evidence, and at least one use case passes")

    gp = d.get("governance_practices", {})
    practices = [(label, gp.get(key)) for key, label in PRACTICES]

    adm = d.get("adm", {})
    adate = dt.date.fromisoformat(d["assessment_date"])
    adm_flag = None
    if adm.get("exposure", "unknown") in ("yes", "unknown") and not (
            adm.get("inventory_done") and adm.get("privacy_policy_updated")):
        if adate < ADM_START:
            days = (ADM_START - adate).days
            adm_flag = (f"ADM exposure is {adm.get('exposure', 'unknown')} and the inventory or privacy "
                        f"policy update is not complete. APP 1.7-1.9 commences 10 December 2026 "
                        f"({days} days after this assessment).")
        else:
            adm_flag = (f"ADM exposure is {adm.get('exposure', 'unknown')} and the inventory or privacy "
                        f"policy update is not complete. APP 1.7-1.9 has applied since 10 December 2026.")

    # Ranked action plan
    plan = []
    if adm_flag:
        plan.append(("P1", "Complete the automated decision-making inventory and privacy policy update "
                           "(for review by the client's legal adviser)", "Governance and risk", "high", "medium"))
    if d.get("shadow_ai_with_personal_data"):
        plan.append(("P1", "Stop personal and confidential data going into unapproved public AI tools: "
                           "approve a business-terms tool and publish a tiered tool rule",
                     "Security and privacy", "high", "low"))
    tier_of = {"deal-breaker": "P1", "unevidenced": "P1", "condition": "P2", "ok": "P4", "strong": None}
    for r in rows:
        t = tier_of[r["status"]]
        if r["status"] == "unevidenced":
            plan.append(("P1", f"Collect evidence for {r['label']} and re-score", r["label"], "high", "low"))
        if t is None:
            continue
        for a in r["actions"]:
            plan.append((t, a["action"], r["label"], a.get("impact", "medium"), a.get("effort", "medium")))

    def uc_key(u):
        v = u.get("annual_value_aud")
        return (0 if v is not None else 1, -(v or 0), u.get("time_to_value_weeks") or 999)
    for u in sorted(go_ucs, key=uc_key):
        val = (f"client value figure AUD {u['annual_value_aud']:,.0f}/yr ({u['value_source']})"
               if u.get("annual_value_aud") is not None else "value PENDING")
        plan.append(("P3", f"Pilot: {u['name']} ({val})", "First use case", "high", "medium"))

    order = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}
    # P3 keeps its value ranking; other tiers sort by impact then effort
    indexed = list(enumerate(plan))
    indexed.sort(key=lambda ip: (order[ip[1][0]],
                                 0 if ip[1][0] == "P3" else RANK[ip[1][3]],
                                 0 if ip[1][0] == "P3" else EFFORT[ip[1][4]],
                                 ip[0]))
    plan = [p for _, p in indexed]

    return {"client": d["client"], "size_band": d["size_band"], "assessment_date": d["assessment_date"],
            "assessor": d.get("assessor", ""), "rows": rows, "mean": round(mean, 2),
            "weighted": bool(d.get("weights")), "org_gate": org, "org_reasons": reasons,
            "practices": practices, "adm_flag": adm_flag, "use_cases": ucs, "plan": plan,
            "warnings": warnings}


def render(r):
    L = [f"# AI readiness scorecard: {r['client']}", "",
         f"Size band {r['size_band']} | Assessed {r['assessment_date']} | {r['assessor']}", "",
         f"## Result: {r['org_gate']}", ""]
    L += [f"- {x}" for x in r["org_reasons"]]
    L += ["", f"Mean score {r['mean']:.2f} of 5 ({'agreed weights' if r['weighted'] else 'equal weights'}). "
               "The gate is set by the rules, not the mean.", "",
          "## Scorecard", "",
          "| Dimension | Score | Level | Confidence | Evidence seen / stated | Status |",
          "|---|---|---|---|---|---|"]
    for x in r["rows"]:
        L.append(f"| {x['label']} | {x['score']:g} | {x['level']} | {x['confidence']} | "
                 f"{x['seen']} / {x['stated']} | {x['status']} |")
    L += ["", "## Governance practices (Guidance for AI Adoption, voluntary)", "",
          "| Practice | Status |", "|---|---|"]
    for label, v in r["practices"]:
        L.append(f"| {label} | {PRACTICE_STATUS.get(v, 'Not assessed')} |")
    L += ["", "## Automated decision-making (APP 1.7)", "",
          r["adm_flag"] or "No open ADM action recorded.", "", NOT_LEGAL, "",
          "## Use cases", "", "| Use case | Risk tier | Gate | Blockers / what unblocks it |", "|---|---|---|---|"]
    for u in r["use_cases"]:
        tier = u.get("risk_tier") if u.get("risk_tier") is not None else "unassigned"
        why = "; ".join(u["blockers"]) or "none"
        if u.get("unblock") and u["blockers"]:
            why += f". Unblock: {u['unblock']}"
        L.append(f"| {u['name']} | {tier} | {u['gate']} | {why} |")
    L += ["", "## Ranked 90-day action plan", "",
          "| # | Priority | Action | Dimension | Impact | Effort |", "|---|---|---|---|---|---|"]
    n = 0
    for p in r["plan"]:
        if p[0] == "P4":
            continue
        n += 1
        L.append(f"| {n} | {p[0]} | {p[1]} | {p[2]} | {p[3]} | {p[4]} |")
    nxt = [p for p in r["plan"] if p[0] == "P4"]
    if nxt:
        L += ["", "### After 90 days (P4 strengthen)", ""]
        L += [f"- {p[1]} ({p[2]})" for p in nxt]
    if r["warnings"]:
        L += ["", "## Assessor warnings", ""] + [f"- {w}" for w in r["warnings"]]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--out")
    ap.add_argument("--json")
    a = ap.parse_args()
    try:
        d = json.load(open(a.path))
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR: cannot read {a.path}: {e}", file=sys.stderr)
        return 2
    errs = validate(d)
    if errs:
        print("INVALID INPUT -- nothing scored:", file=sys.stderr)
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        return 2
    r = analyse(d)
    md = render(r)
    if a.out:
        open(a.out, "w").write(md)
    else:
        sys.stdout.write(md)
    if a.json:
        json.dump(r, open(a.json, "w"), indent=2, default=str)
    print(f"GATE: {r['org_gate']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
