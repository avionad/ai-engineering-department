#!/usr/bin/env python3
# MIT License
#
# Copyright (c) 2025 Alireza Rezvani
# Copyright (c) 2026 the practice (modifications)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Attribution: adapted from alirezarezvani/claude-skills,
#   ra-qm-team/skills/iso42001-specialist/scripts/aims_gap_analyzer.py
#   at commit 8f082544116fc0d014188e521ca40304cdfc86b0 (MIT).
# What the practice changed: reframed from "certification audit severity" to readiness
#   priority (the practice prepares, it cannot certify: only ISO/IEC 42006 bodies can);
#   added the House artefact that closes each gap and its Guidance for AI Adoption
#   practice; Markdown output; size-band note. Sub-clause numbers and titles are
#   the upstream author's and have NOT been verified against the purchased
#   ISO/IEC 42001:2023 text: verify before citing them to a client.
"""iso42001_readiness_gap.py -- ISO/IEC 42001 readiness gap (Clauses 4-10) for the practice clients.

Stdlib only. Scores each requirement as documented / partial / missing from an evidence
inventory and outputs a prioritised list with the House artefact that closes each gap.

Usage:
  python3 iso42001_readiness_gap.py evidence.json [--md out.md]
  python3 iso42001_readiness_gap.py                 # embedded sample to stdout

Input:
{"organisation": "...", "size_band": "M", "date": "2026-11-08", "scope": "...",
 "evidence": {"4.3_scope_statement": "partial", "5.2_ai_policy": "missing", ...}}
Missing keys count as "missing".

READINESS ONLY. This is not a certification audit and does not predict an auditor's findings.
"""

import argparse
import json
import sys
from typing import Any, Dict

# key: (sub-clause per upstream, title per upstream, upstream priority, House artefact, GfAA practice)
REQS: Dict[str, tuple] = {
    "4.1_context_external": ("4.1", "External and internal context", "minor", "Regulatory register extract + context note", "2"),
    "4.2_interested_parties": ("4.2", "Interested parties", "minor", "Stakeholder list in governance charter", "2"),
    "4.3_scope_statement": ("4.3", "AIMS scope statement", "critical", "AI register (incl. vendor AI) + scope statement", "1"),
    "4.4_aims_processes": ("4.4", "AIMS processes and interactions", "major", "Governance charter process map", "1"),
    "5.1_leadership_commitment": ("5.1", "Leadership commitment", "major", "Charter signed by executive sponsor", "1"),
    "5.2_ai_policy": ("5.2", "AI policy", "critical", "AI policy and acceptable use policy", "1"),
    "5.3_roles_responsibilities": ("5.3", "Roles, responsibilities, authorities", "critical", "Charter RACI", "1"),
    "6.1.2_risk_assessment": ("6.1.2", "AI risk assessment", "critical", "ai-compliance-risk screen + risk register", "3"),
    "6.1.3_risk_treatment": ("6.1.3", "AI risk treatment", "critical", "Risk register treatment + residual sign-off", "3"),
    "6.1.4_impact_assessment": ("6.1.4", "AI system impact assessment", "major", "ai-compliance-risk impact assessment", "2"),
    "6.2_objectives": ("6.2", "AI objectives and planning", "minor", "Measurable objectives in AI policy", "1"),
    "7.1_resources": ("7.1", "Resources", "minor", "Charter resourcing section", "1"),
    "7.2_competence": ("7.2", "Competence", "major", "AI literacy training plan (role matrix)", "1"),
    "7.3_awareness": ("7.3", "Awareness", "minor", "All-staff literacy module + AUP acknowledgement", "4"),
    "7.4_communication": ("7.4", "Communication", "minor", "Transparency statement + incident comms", "4"),
    "7.5_documented_info": ("7.5", "Documented information", "major", "Document control for policy, register, cards", "4"),
    "8.1_operational_planning": ("8.1", "Operational planning and control", "major", "Lifecycle gates (engagement conventions s2)", "5"),
    "8.2_impact_assessment_process": ("8.2", "Impact assessment process", "major", "Screen triggers + reassessment rules", "2"),
    "8.3_ai_system_lifecycle": ("8.3", "AI system lifecycle process", "critical", "Lifecycle incl. decommission in charter", "5"),
    "8.4_third_party_relationships": ("8.4", "Third-party and customer relationships", "major", "Vendor due diligence questionnaire", "3"),
    "9.1_monitoring": ("9.1", "Monitoring, measurement, analysis, evaluation", "major", "Monitoring owners + thresholds per system", "5"),
    "9.2_internal_audit": ("9.2", "Internal audit programme", "critical", "Internal audit plan (client or third party)", "5"),
    "9.3_management_review": ("9.3", "Management review", "critical", "Council quarterly review agenda", "1"),
    "10.1_continual_improvement": ("10.1", "Continual improvement", "minor", "Improvement log from incidents and reviews", "5"),
    "10.2_nonconformity_capa": ("10.2", "Nonconformity and corrective action", "major", "Incident playbook corrective actions", "6"),
}
SCORE = {"documented": 1.0, "partial": 0.5, "missing": 0.0}
WEIGHT = {"critical": 4, "major": 2, "minor": 1}
RANK = {"critical": 0, "major": 1, "minor": 2}

SAMPLE = {"organisation": "Sample Logistics Pty Ltd (fictional)", "size_band": "L", "date": "2026-11-08",
          "scope": "Internal copilots, customer email triage, route optimisation vendor AI",
          "evidence": {"4.1_context_external": "partial", "4.3_scope_statement": "missing",
                       "5.1_leadership_commitment": "partial", "5.2_ai_policy": "partial",
                       "6.1.2_risk_assessment": "partial", "7.3_awareness": "documented",
                       "7.5_documented_info": "documented", "8.4_third_party_relationships": "partial",
                       "10.2_nonconformity_capa": "documented"}}


def analyse(p: Dict[str, Any]) -> Dict[str, Any]:
    ev = p.get("evidence", {})
    rows, tot, got = [], 0.0, 0.0
    for k, (cl, title, pr, artefact, prac) in REQS.items():
        st = ev.get(k, "missing")
        if st not in SCORE:
            st = "missing"
        w = WEIGHT[pr]
        tot += w
        got += w * SCORE[st]
        rows.append({"clause": cl, "title": title, "status": st, "priority": pr,
                     "artefact": artefact, "practice": prac})
    gaps = [r for r in rows if r["status"] != "documented"]
    gaps.sort(key=lambda r: (RANK[r["priority"]], r["status"] != "missing", r["clause"]))
    return {"org": p.get("organisation", ""), "band": p.get("size_band", ""), "date": p.get("date", ""),
            "scope": p.get("scope", ""), "readiness_pct": round(100 * got / tot, 1),
            "counts": {s: sum(1 for r in rows if r["status"] == s) for s in SCORE},
            "gaps": gaps, "total": len(rows)}


def md(r: Dict[str, Any]) -> str:
    c = r["counts"]
    out = [f"# ISO/IEC 42001 readiness gap: {r['org']}", "",
           f"Size band: {r['band']} | Date: {r['date']} | Scope: {r['scope']}", "",
           "Readiness assessment only. The practice prepares organisations for ISO/IEC 42001; "
           "certification is performed only by accredited certification bodies (ISO/IEC 42006). "
           "This is not an audit and does not predict audit findings.", "",
           f"Weighted readiness: {r['readiness_pct']}% across {r['total']} requirements "
           f"(documented {c['documented']}, partial {c['partial']}, missing {c['missing']}). "
           "Weights: critical 4, major 2, minor 1 (heuristic from the adapted upstream tool).", "",
           "| Priority | Clause | Requirement | Status | House artefact that closes it | GfAA practice |",
           "|---|---|---|---|---|---|"]
    for g in r["gaps"]:
        out.append(f"| {g['priority']} | {g['clause']} | {g['title']} | {g['status']} | {g['artefact']} | {g['practice']} |")
    out += ["", "Sub-clause numbers and titles follow the harvested upstream tool and must be checked against "
            "the client's copy of ISO/IEC 42001:2023 before they are quoted. Annex A controls are out of scope "
            "of this script."]
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="the practice ISO/IEC 42001 readiness gap (Clauses 4-10).")
    ap.add_argument("evidence", nargs="?")
    ap.add_argument("--md", "--out")
    a = ap.parse_args()
    if a.evidence:
        try:
            with open(a.evidence, encoding="utf-8") as f:
                p = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"error: {e}", file=sys.stderr)
            return 1
    else:
        p = SAMPLE
    r = analyse(p)
    text = md(r)
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"readiness {r['readiness_pct']}% | gaps {len(r['gaps'])} -> {a.md}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
