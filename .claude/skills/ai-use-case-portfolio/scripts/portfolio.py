#!/usr/bin/env python3
"""portfolio.py -- rank an organisation's AI use-case portfolio and flag governance gaps.

The practice ai-automation department, ai-use-case-portfolio skill, v0.1.0 (2026-11-08).
Stdlib only. No network. The practice's own code (no harvested code adapted).

Reads a CSV with these required columns:
    id, name, owner, value_low, value_high, value_source, feasibility, risk_tier,
    time_to_value_weeks, status, baseline, actual
Optional columns (used when present):
    compliance_screen   date or reference of the ai-compliance-risk screen (blank = none)
    ai_register_id      ID in the organisation's AI register (ai-governance-program)
    notes

Units (one convention for the whole file, stated in the output):
    value_low / value_high  planned annual benefit range in AUD, from the client's own numbers
    baseline                measured annual cost of the process BEFORE the build, AUD
    actual                  measured annual cost of the process NOW (annualised), AUD
    realised benefit = baseline - actual, compared with the planned range

Ranking reuses ai-discovery-scoping/references/use-case-qualification.md section 3:
value first (sourced only), then time to value (shorter), feasibility (higher), risk tier
(lower). No composite score is invented. A value without a value_source is treated as
unknown: it is flagged and ranked with the unvalued rows, never used.

Usage:
    python3 portfolio.py portfolio.csv                 # markdown to stdout
    python3 portfolio.py portfolio.csv -o out.md       # markdown to a file
    python3 portfolio.py portfolio.csv --strict        # exit 1 if any row has an error
"""

import argparse
import csv
import sys
from datetime import date

REQUIRED = [
    "id", "name", "owner", "value_low", "value_high", "value_source", "feasibility",
    "risk_tier", "time_to_value_weeks", "status", "baseline", "actual",
]
STATUSES = ["idea", "qualified", "approved", "build", "live", "paused", "killed"]
PRE_BUILD_COMMITTED = {"approved", "build"}
PENDING_WORDS = {"", "pending", "pending_verification", "tbc", "unknown", "n/a", "na", "-"}


def blank(v):
    return (v or "").strip().lower() in PENDING_WORDS


def num(v):
    """Return a float, or None for blank/PENDING. Raise ValueError for junk."""
    if blank(v):
        return None
    return float(str(v).replace(",", "").replace("$", "").strip())


def money(x):
    return "PENDING" if x is None else "${:,.0f}".format(x)


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        missing = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            sys.exit("ERROR: CSV is missing required columns: " + ", ".join(missing))
        return [dict((k.strip(), (v or "").strip()) for k, v in row.items() if k) for row in reader]


def assess(row):
    """Parse one row. Returns a dict with parsed values, errors and flags."""
    r = {"raw": row, "errors": [], "flags": []}
    rid = row.get("id") or "?"
    r["id"], r["name"], r["owner"] = rid, row.get("name", ""), row.get("owner", "")
    r["status"] = row.get("status", "").lower()
    if r["status"] not in STATUSES:
        r["errors"].append("status '%s' not one of %s" % (row.get("status"), "/".join(STATUSES)))

    for field in ("value_low", "value_high", "baseline", "actual", "time_to_value_weeks"):
        try:
            r[field] = num(row.get(field))
        except ValueError:
            r[field] = None
            r["errors"].append("%s is not a number: '%s'" % (field, row.get(field)))

    for field, lo, hi in (("feasibility", 1, 5), ("risk_tier", 1, 4)):
        try:
            v = num(row.get(field))
            if v is not None and (v != int(v) or not lo <= v <= hi):
                raise ValueError
            r[field] = None if v is None else int(v)
        except ValueError:
            r[field] = None
            r["errors"].append("%s must be a whole number %d-%d: '%s'" % (field, lo, hi, row.get(field)))
        if r[field] is None and not any(e.startswith(field) for e in r["errors"]):
            r["flags"].append("%s missing" % field)

    lo, hi = r["value_low"], r["value_high"]
    if lo is not None and hi is not None and lo > hi:
        r["errors"].append("value_low is greater than value_high")
    has_value = lo is not None or hi is not None
    sourced = not blank(row.get("value_source"))
    r["value_known"] = has_value and sourced
    if has_value and not sourced:
        r["flags"].append("UNSOURCED VALUE: value given with no value_source; ignored for ranking")
    if not has_value:
        r["flags"].append("value PENDING: cannot be the next pilot until the client's numbers are in")
    if r["value_known"]:
        if lo is None or hi is None:
            r["mid"] = lo if hi is None else hi
        else:
            r["mid"] = (lo + hi) / 2.0
    else:
        r["mid"] = None

    if blank(r["owner"]):
        r["flags"].append("no named owner (gate 2 fails)")

    screen = not blank(row.get("compliance_screen"))
    r["screened"] = screen
    if r["risk_tier"] == 4:
        r["flags"].append("TIER 4: STOP. Do not build; record the reason and a lawful alternative")
    if r["risk_tier"] == 3 and not screen:
        r["flags"].append("TIER 3 WITHOUT COMPLIANCE SCREEN: run ai-compliance-risk mode (a) before design")
    if r["risk_tier"] is None:
        r["flags"].append("no risk tier: nothing proceeds to design (conventions s2)")

    if r["status"] in PRE_BUILD_COMMITTED and r["baseline"] is None:
        r["flags"].append("NO BASELINE: measure the current process before build starts")
    if r["status"] == "live":
        if r["baseline"] is None:
            r["flags"].append("LIVE WITHOUT BASELINE: no benefit can be claimed")
        if r["actual"] is None:
            r["flags"].append("LIVE WITHOUT ACTUAL: record this month's measurement")
        if blank(row.get("ai_register_id")) and "ai_register_id" in row:
            r["flags"].append("live but not linked to the AI register")
        if blank(row.get("ai_register_id")) and "ai_register_id" not in row:
            r["flags"].append("no ai_register_id column: live systems must be in the AI register")
    return r


def rank_key(r):
    # use-case-qualification s3: value (desc), time to value (asc), feasibility (desc), tier (asc)
    big = 10 ** 9
    return (
        0 if r["value_known"] else 1,
        -(r["mid"] or 0),
        r["time_to_value_weeks"] if r["time_to_value_weeks"] is not None else big,
        -(r["feasibility"] or 0),
        r["risk_tier"] or 9,
    )


def pilot_eligible(r):
    if not r["value_known"] or blank(r["owner"]) or r["risk_tier"] in (None, 4):
        return False
    if r["risk_tier"] == 3 and not r["screened"]:
        return False
    return not r["errors"]


def variance(r):
    if r["baseline"] is None or r["actual"] is None:
        return None, "cannot assess (missing baseline or actual)"
    realised = r["baseline"] - r["actual"]
    lo, hi = r["value_low"], r["value_high"]
    if not r["value_known"]:
        return realised, "no sourced plan to compare against"
    if lo is not None and realised < lo:
        return realised, "BELOW planned range: review (fix, rescope or kill)"
    if hi is not None and realised > hi:
        return realised, "ABOVE planned range: check the measurement, then consider scaling"
    return realised, "within planned range: candidate to scale or hold"


def render(rows, source):
    out = []
    today = date.today().isoformat()
    out.append("# AI use-case portfolio")
    out.append("")
    out.append("*Generated %s by `portfolio.py` from `%s`. Values are annual AUD from the client's own "
               "numbers; a value without a source is ignored. Ranking follows "
               "use-case-qualification.md s3 (value, then time to value, feasibility, risk tier).*"
               % (today, source))
    out.append("")
    by_status = {}
    for r in rows:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    out.append("## Summary")
    out.append("")
    out.append("| Measure | Count |")
    out.append("|---|---|")
    out.append("| Use cases | %d |" % len(rows))
    for s in STATUSES:
        if by_status.get(s):
            out.append("| Status: %s | %d |" % (s, by_status[s]))
    out.append("| Rows with errors | %d |" % sum(1 for r in rows if r["errors"]))
    out.append("| Unsourced values (ignored) | %d |" % sum(1 for r in rows if any(f.startswith("UNSOURCED") for f in r["flags"])))
    out.append("| Tier 4 (stop) | %d |" % sum(1 for r in rows if r["risk_tier"] == 4))
    out.append("| Tier 3 without compliance screen | %d |" % sum(1 for r in rows if r["risk_tier"] == 3 and not r["screened"]))
    out.append("")

    errs = [r for r in rows if r["errors"]]
    if errs:
        out.append("## Errors (fix the CSV)")
        out.append("")
        for r in errs:
            out.append("- **%s %s**: %s" % (r["id"], r["name"], "; ".join(r["errors"])))
        out.append("")

    active = [r for r in rows if r["status"] not in ("live", "killed") and r["risk_tier"] != 4]
    active.sort(key=rank_key)
    out.append("## Ranked pipeline (not yet live)")
    out.append("")
    out.append("| Rank | ID | Use case | Owner | Planned value (low to high) | Time to value (wks) | Feasibility | Tier | Status | Eligible to approve |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(active, 1):
        val = "%s to %s" % (money(r["value_low"]), money(r["value_high"])) if r["value_known"] else "PENDING"
        ttv = "PENDING" if r["time_to_value_weeks"] is None else "%g" % r["time_to_value_weeks"]
        out.append("| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            i, r["id"], r["name"], r["owner"] or "NONE", val, ttv,
            r["feasibility"] if r["feasibility"] is not None else "PENDING",
            r["risk_tier"] if r["risk_tier"] is not None else "NONE",
            r["status"], "committed" if r["status"] in PRE_BUILD_COMMITTED
            else ("yes" if pilot_eligible(r) else "no")))
    out.append("")
    out.append("Eligible to approve means: sourced value, named owner, tier 1 to 3 (tier 3 screened), "
               "no errors. 'committed' means already approved or in build. Value ranks on the midpoint "
               "of the sourced range. The three gate questions (data there, owner, 30-day pilot) are "
               "still asked in person; this table does not answer them.")
    out.append("")

    stopped = [r for r in rows if r["risk_tier"] == 4]
    if stopped:
        out.append("## Stopped (tier 4)")
        out.append("")
        for r in stopped:
            out.append("- **%s %s** (status %s): do not build. Record the reason and offer a lawful alternative." % (r["id"], r["name"], r["status"]))
        out.append("")

    live = [r for r in rows if r["status"] == "live"]
    out.append("## Live: planned vs actual")
    out.append("")
    if not live:
        out.append("No live use cases.")
    else:
        out.append("| ID | Use case | Planned (low to high) | Baseline cost | Current cost | Realised benefit | Assessment |")
        out.append("|---|---|---|---|---|---|---|")
        for r in live:
            realised, verdict = variance(r)
            planned = "%s to %s" % (money(r["value_low"]), money(r["value_high"])) if r["value_known"] else "PENDING"
            out.append("| %s | %s | %s | %s | %s | %s | %s |" % (
                r["id"], r["name"], planned, money(r["baseline"]), money(r["actual"]),
                money(realised), verdict))
        out.append("")
        out.append("The assessment is a prompt for the monthly portfolio review, not a decision. "
                   "Kill or scale is decided by the accountable owner with the review notes.")
    out.append("")

    flagged = [r for r in rows if r["flags"]]
    out.append("## Flags by use case")
    out.append("")
    if not flagged:
        out.append("None.")
    for r in flagged:
        out.append("- **%s %s**: %s" % (r["id"], r["name"], "; ".join(r["flags"])))
    out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("csv")
    ap.add_argument("-o", "--output", "--out")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any row has an error")
    a = ap.parse_args()
    rows = [assess(r) for r in load(a.csv)]
    ids = [r["id"] for r in rows]
    for d in sorted(set(i for i in ids if ids.count(i) > 1)):
        for r in rows:
            if r["id"] == d:
                r["errors"].append("duplicate id")
    md = render(rows, a.csv)
    if a.output:
        with open(a.output, "w", encoding="utf-8") as fh:
            fh.write(md + "\n")
        print("Wrote %s (%d use cases)" % (a.output, len(rows)))
    else:
        print(md)
    if a.strict and any(r["errors"] for r in rows):
        sys.exit(1)


if __name__ == "__main__":
    main()
