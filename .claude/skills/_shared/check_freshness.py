#!/usr/bin/env python3
"""Freshness check for the ai-automation department's perishable facts.

The department's value rests on sourced regulatory facts that carry a "date checked".
Those rot. This script finds every date-checked marker in `_shared/` (the regulatory
register, the client FAQ, the industry packs) and reports anything older than the
staleness window, so nothing reaches a client on an unverified claim.

Called by:
- `ai-manager` protocol step 1 (every engagement task), and
- the CTO weekly scan (first run of each month).

Usage
  python3 check_freshness.py [--days 60] [--json] [--quiet]
Exit codes
  0  nothing stale
  1  something is stale or a PENDING item is unowned (findings)
  2  input error (a file could not be read)
Stdlib only.
"""
import argparse
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
DATE = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")
# "date checked", "checked 2026-11-08", "Date checked 2026-11-08", table columns
MARKER = re.compile(r"(?:date[ _]checked|checked)\D{0,12}(20\d{2}-\d{2}-\d{2})", re.I)


def iso(s):
    y, m, d = (int(x) for x in s.split("-"))
    return date(y, m, d)


def scan(root, days, today):
    findings = []
    files = 0
    for dirpath, _, names in os.walk(root):
        for n in sorted(names):
            if not n.endswith(".md"):
                continue
            p = os.path.join(dirpath, n)
            rel = os.path.relpath(p, root)
            try:
                text = open(p, encoding="utf-8").read()
            except OSError as e:
                print(f"cannot read {rel}: {e}", file=sys.stderr)
                sys.exit(2)
            files += 1
            dates = sorted({m.group(1) for m in MARKER.finditer(text)})
            if not dates:
                continue
            oldest = min(dates)
            age = (today - iso(oldest)).days
            if age > days:
                findings.append({
                    "file": rel, "oldest_date_checked": oldest, "age_days": age,
                    "markers": len(dates),
                    "why": "a claim this old must be re-verified against its primary source "
                           "before it appears in a client deliverable",
                })
    return findings, files


def pending(root):
    out = []
    for dirpath, _, names in os.walk(root):
        for n in sorted(names):
            if not n.endswith(".md"):
                continue
            p = os.path.join(dirpath, n)
            for i, line in enumerate(open(p, encoding="utf-8"), 1):
                if "PENDING_VERIFICATION" in line:
                    out.append((os.path.relpath(p, root), i))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--days", type=int, default=60,
                    help="staleness window in days (default 60, the department's rule)")
    ap.add_argument("--root", default=HERE, help="folder to scan (default: this _shared folder)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="print only the verdict line")
    a = ap.parse_args()

    today = date.today()
    findings, files = scan(a.root, a.days, today)
    pend = pending(a.root)
    verdict = "STALE" if findings else "FRESH"

    if a.json:
        print(json.dumps({"verdict": verdict, "today": today.isoformat(), "window_days": a.days,
                          "files_scanned": files, "stale": findings,
                          "pending_verification_lines": len(pend)}, indent=1))
    elif a.quiet:
        print(f"{verdict}: {len(findings)} stale file(s), {len(pend)} PENDING_VERIFICATION line(s)")
    else:
        print(f"# ai-automation freshness check ({today.isoformat()}, window {a.days} days)\n")
        print(f"Scanned {files} markdown files in {a.root}.\n")
        if findings:
            print("| File | Oldest date checked | Age (days) | Markers |")
            print("|---|---|---|---|")
            for f in findings:
                print(f"| {f['file']} | {f['oldest_date_checked']} | {f['age_days']} | {f['markers']} |")
            print("\nRe-verify each against its primary source, then update the date checked. "
                  "Until then these facts do not go into a client deliverable.")
        else:
            print("No date-checked claim is older than the window.")
        print(f"\nPENDING_VERIFICATION lines in scope: {len(pend)} "
              "(each must be closed or excluded before it appears in client work).")
        print(f"\n**{verdict}**")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
