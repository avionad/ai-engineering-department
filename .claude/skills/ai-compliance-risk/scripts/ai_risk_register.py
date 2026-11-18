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
#   ra-qm-team/skills/iso42001-specialist/scripts/ai_risk_register_builder.py
#   at commit 8f082544116fc0d014188e521ca40304cdfc86b0 (MIT).
# What the practice changed: the practice rating scale aligned to the department's risk tiers;
#   per-risk owner, residual likelihood/impact and residual rating; tier-minimum
#   control check from engagement-conventions.md section 6; seed mode that
#   proposes starter risks from the CoSAI risk map (Apache-2.0, risk IDs and
#   titles only) and NIST AI 600-1's 12 GenAI risks; CSV and Markdown output;
#   ISO 42001 Annex A control catalogue removed (two harvested sources number
#   Annex A differently, so the practice does not cite Annex A IDs until verified against
#   the purchased standard).
"""ai_risk_register.py -- per-project AI risk register for this AI automation department.

Stdlib only. Two modes.

  seed   Propose a starter register from the project's architecture flags. Output is a JSON
         skeleton with likelihood/impact left at 0 for the consultant to score.
  build  Score a filled register: inherent rating, treatment option, treatment adequacy,
         residual rating, and a check of the project's controls against the tier minimums.
         Writes CSV and/or Markdown.

Usage:
  python3 ai_risk_register.py seed project.json [-o seeded.json]
  python3 ai_risk_register.py build register.json [--csv out.csv] [--md out.md]
  python3 ai_risk_register.py build            # embedded sample, Markdown to stdout

Input (build):
{
  "client": "Example Pty Ltd", "project": "Support chatbot", "date": "2026-11-08",
  "risk_tier": 2,                       # 1-4, from the Screen mode
  "project_controls": ["acceptable use policy", "register entry", "privacy check", ...],
  "risks": [
    {"id": "R-01", "title": "...", "category": "security|privacy|fairness|safety|legal|operational|third-party",
     "source": "CoSAI riskPromptInjection; OWASP LLM01; ATLAS AML.T0051",
     "likelihood": 4, "impact": 3,      # 1-5 each
     "controls": ["input validation", "output filtering"],
     "owner": "Client IT lead",
     "residual_likelihood": 2, "residual_impact": 3}   # optional; 0 or missing = not assessed
  ]
}

Rating scale (5x5, thresholds kept from the upstream script):
  score 1-4  -> Low        (inherits Tier 1 vocabulary)
  score 5-9  -> Moderate   (Tier 2)
  score 10-16 -> High      (Tier 3)
  score 17-25 -> Critical  (stop: escalate to the client's accountable owner before build)
The thresholds are a heuristic, not a standard. Calibrate per client risk appetite.

Not legal advice. Output identifies risks and controls for review by the client's legal adviser.
"""

import argparse
import csv
import json
import sys
from typing import Any, Dict, List

RATINGS = ["Low", "Moderate", "High", "Critical"]

# Minimum controls per tier, from engagement-conventions.md section 6. Matching is by
# case-insensitive substring so "Eval baseline v1" satisfies "eval baseline".
TIER_MINIMUMS: Dict[int, List[str]] = {
    1: ["acceptable use policy", "register entry"],
    2: ["acceptable use policy", "register entry", "privacy check", "eval baseline",
        "logging", "access control"],
    3: ["acceptable use policy", "register entry", "privacy check", "eval baseline",
        "logging", "access control", "impact assessment", "adm disclosure",
        "human review", "red-team", "monitoring", "incident plan"],
}

# ---------------------------------------------------------------- seed catalogue
# CoSAI risk IDs/titles from cosai-oasis/secure-ai-tooling risk-map/yaml/risks.yaml
# (commit 622605a13fafaa2784acbdbe3f8d23ee22da4be7, Apache-2.0). Mappings to OWASP LLM IDs
# and ATLAS IDs are CoSAI's own (ATLAS IDs are pinned to ATLAS 5.0.1 in CoSAI; see
# references/threat-model.md before citing them). NIST AI 600-1 names verified against
# https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf on 2026-11-08.
SEED: List[Dict[str, Any]] = [
    # flag "genai": any generative AI system
    {"flags": ["genai"], "title": "Confabulation: confidently stated but false output relied on",
     "category": "safety", "source": "NIST AI 600-1 #2; CoSAI riskInsecureModelOutput; OWASP LLM09"},
    {"flags": ["genai"], "title": "Human-AI configuration: automation bias or over-reliance by staff",
     "category": "operational", "source": "NIST AI 600-1 #7"},
    {"flags": ["genai"], "title": "Information security: model or integration widens attack surface",
     "category": "security", "source": "NIST AI 600-1 #9"},
    {"flags": ["genai"], "title": "Prompt injection (direct or indirect) changes system behaviour",
     "category": "security", "source": "CoSAI riskPromptInjection; OWASP LLM01; ATLAS AML.T0051"},
    {"flags": ["genai"], "title": "Insecure model output passed to downstream systems or users",
     "category": "security", "source": "CoSAI riskInsecureModelOutput; OWASP LLM05"},
    {"flags": ["third_party_model"], "title": "Value chain: third-party model change, deprecation or opaque components",
     "category": "third-party", "source": "NIST AI 600-1 #12; APRA AI letter (AU-15) supplier risk"},
    {"flags": ["third_party_model"], "title": "Supplier concentration with no tested exit or substitution plan",
     "category": "third-party", "source": "APRA AI letter (AU-15); CPS 230 (AU-13) where APRA-regulated"},
    {"flags": ["personal_data"], "title": "Data privacy: leakage or unauthorised use or disclosure of personal information",
     "category": "privacy", "source": "NIST AI 600-1 #4; CoSAI riskSensitiveDataDisclosure; OWASP LLM02; Privacy Act (AU-6)"},
    {"flags": ["personal_data"], "title": "Excessive data handling during inference (retention, logging, vendor reuse)",
     "category": "privacy", "source": "CoSAI riskExcessiveDataHandlingDuringInference; OAIC guidance (AU-11)"},
    {"flags": ["personal_data"], "title": "Personal information entered into public consumer AI tools (shadow AI)",
     "category": "privacy", "source": "OAIC guidance (AU-11); conventions s2"},
    {"flags": ["adm"], "title": "ADM disclosure missing from privacy policy from 10 Dec 2026",
     "category": "legal", "source": "POLA Act APP 1.7-1.9 (AU-8)"},
    {"flags": ["decisions_about_people"], "title": "Harmful bias: unequal outcomes across groups",
     "category": "fairness", "source": "NIST AI 600-1 #6; anti-discrimination law (AU-24 context)"},
    {"flags": ["decisions_about_people"], "title": "No contestability: affected person cannot challenge an outcome",
     "category": "fairness", "source": "ASIC REP 798 (AU-16) finding; AHRC checklist (AU-24)"},
    {"flags": ["customer_facing"], "title": "Misleading statements or promises by a customer-facing AI",
     "category": "legal", "source": "Australian Consumer Law (AU-22); OWASP LLM09"},
    {"flags": ["customer_facing"], "title": "Harmful, hateful or abusive content shown to the public",
     "category": "safety", "source": "NIST AI 600-1 #3 and #11"},
    {"flags": ["customer_facing"], "title": "Unbounded consumption or denial of wallet from public traffic",
     "category": "operational", "source": "CoSAI riskEconomicDenialOfWallet, riskDenialOfMLService; OWASP LLM10"},
    {"flags": ["generates_content"], "title": "Intellectual property: output replicates protected material",
     "category": "legal", "source": "NIST AI 600-1 #10"},
    {"flags": ["generates_content"], "title": "Information integrity: synthetic content mistaken for authentic",
     "category": "legal", "source": "NIST AI 600-1 #8; EU AI Act Art 50 if EU-facing (EU-1)"},
    {"flags": ["rag"], "title": "Retrieval or vector store poisoning",
     "category": "security", "source": "CoSAI riskRetrievalVectorStorePoisoning; OWASP LLM08"},
    {"flags": ["rag"], "title": "Permission leak: retrieval returns documents the user may not see",
     "category": "privacy", "source": "OWASP LLM08, LLM02; research B2 (permission-aware retrieval)"},
    {"flags": ["agent"], "title": "Rogue actions: agent takes unintended actions with real effect",
     "category": "security", "source": "CoSAI riskRogueActions; OWASP LLM06; OWASP ASI02"},
    {"flags": ["agent"], "title": "Agent goal hijack via retrieved or tool content",
     "category": "security", "source": "OWASP ASI01; ATLAS AML.T0051.001, AML.T0080"},
    {"flags": ["agent"], "title": "Identity and privilege abuse: over-scoped or shared agent credentials",
     "category": "security", "source": "OWASP ASI03; CoSAI riskAgenticDelegationConfusedDeputy, riskStaleAgentIdentityBinding"},
    {"flags": ["agent"], "title": "Runaway agent tool loops and cascading failures",
     "category": "operational", "source": "CoSAI riskRunawayAgentToolLoops; OWASP ASI08"},
    {"flags": ["agent"], "title": "Tool source provenance: untrusted tool or MCP server",
     "category": "security", "source": "CoSAI riskToolSourceProvenance, riskZombieShadowMCPServers; OWASP ASI04"},
    {"flags": ["agent"], "title": "Memory and context poisoning across sessions",
     "category": "security", "source": "OWASP ASI06; ATLAS AML.T0080.000"},
    {"flags": ["fine_tune"], "title": "Data poisoning of training or fine-tuning data",
     "category": "security", "source": "CoSAI riskDataPoisoning; OWASP LLM04"},
    {"flags": ["fine_tune"], "title": "Unauthorised training data (customer data used beyond APP 6 purpose)",
     "category": "privacy", "source": "CoSAI riskUnauthorizedTrainingData; OAIC training guidance (AU-12)"},
    {"flags": ["fine_tune"], "title": "Adapter or PEFT injection",
     "category": "security", "source": "CoSAI riskAdapterPEFTInjection"},
    {"flags": ["self_hosted"], "title": "Model source tampering or malicious loader in downloaded weights",
     "category": "security", "source": "CoSAI riskModelSourceTampering, riskMaliciousLoaderDeserialization; OWASP LLM03"},
    {"flags": ["self_hosted"], "title": "Model exfiltration from self-managed infrastructure",
     "category": "security", "source": "CoSAI riskModelExfiltration"},
    {"flags": ["shadow_agents"], "title": "Shadow and unknown agents operating outside the register",
     "category": "operational", "source": "CoSAI riskShadowAndUnknownAgents"},
]

SAMPLE: Dict[str, Any] = {
    "client": "Sample Clinic Group (fictional)", "project": "Appointment and booking chat", "date": "2026-11-08",
    "risk_tier": 2,
    "project_controls": ["Acceptable use policy", "Register entry", "Privacy check", "Logging"],
    "risks": [
        {"id": "R-01", "title": "Prompt injection changes chatbot behaviour", "category": "security",
         "source": "CoSAI riskPromptInjection; OWASP LLM01", "likelihood": 4, "impact": 3,
         "controls": ["Input validation", "Output filtering"], "owner": "Clinic IT lead",
         "residual_likelihood": 2, "residual_impact": 3},
    ],
}


def rating(likelihood: int, impact: int) -> str:
    if not likelihood or not impact:
        return "Not assessed"
    score = max(1, min(5, likelihood)) * max(1, min(5, impact))
    if score <= 4:
        return "Low"
    if score <= 9:
        return "Moderate"
    if score <= 16:
        return "High"
    return "Critical"


def treatment_option(r: str, n_controls: int) -> str:
    """ISO 23894-style options (modify / share / retain / avoid), heuristic from upstream."""
    if r == "Critical" and n_controls == 0:
        return "avoid or escalate"
    if r in ("High", "Critical"):
        return "modify"
    if r == "Moderate":
        return "modify" if n_controls < 2 else "retain"
    if r == "Not assessed":
        return "score first"
    return "retain"


def treatment_adequacy(r: str, n_controls: int) -> str:
    expected = {"Low": 0, "Moderate": 1, "High": 2, "Critical": 3}.get(r)
    if expected is None:
        return "-"
    if n_controls >= expected:
        return "adequate, accountable owner signs off" if r == "Critical" else "adequate on count (check quality)"
    return "more treatment needed"


def check_tier_minimums(tier: int, controls: List[str]) -> List[str]:
    if tier >= 4:
        return ["Tier 4: do not build. Explain why to the client (conventions s6)."]
    have = " | ".join(c.lower() for c in controls)
    return [m for m in TIER_MINIMUMS.get(tier, []) if m not in have]


def build(payload: Dict[str, Any]) -> Dict[str, Any]:
    rows = []
    for r in payload.get("risks", []):
        li, im = int(r.get("likelihood") or 0), int(r.get("impact") or 0)
        ctrls = list(r.get("controls") or [])
        inh = rating(li, im)
        rli, rim = int(r.get("residual_likelihood") or 0), int(r.get("residual_impact") or 0)
        rows.append({
            "id": r.get("id", ""), "title": r.get("title", ""), "category": r.get("category", ""),
            "source": r.get("source", ""), "likelihood": li, "impact": im,
            "inherent_score": li * im, "inherent_rating": inh,
            "controls": "; ".join(ctrls), "control_count": len(ctrls),
            "owner": r.get("owner") or "UNASSIGNED",
            "residual_likelihood": rli, "residual_impact": rim,
            "residual_rating": rating(rli, rim),
            "treatment_option": treatment_option(inh, len(ctrls)),
            "treatment_adequacy": treatment_adequacy(inh, len(ctrls)),
        })
    order = {"Critical": 0, "High": 1, "Moderate": 2, "Low": 3, "Not assessed": 4}
    rows.sort(key=lambda x: (order[x["inherent_rating"]], -x["inherent_score"]))
    counts = {k: sum(1 for x in rows if x["inherent_rating"] == k) for k in order}
    tier = int(payload.get("risk_tier") or 0)
    return {
        "client": payload.get("client", ""), "project": payload.get("project", ""),
        "date": payload.get("date", ""), "risk_tier": tier,
        "counts": counts, "rows": rows,
        "unowned": [x["id"] for x in rows if x["owner"] == "UNASSIGNED"],
        "needs_treatment": [x["id"] for x in rows if x["treatment_adequacy"] == "more treatment needed"],
        "missing_tier_controls": check_tier_minimums(tier, payload.get("project_controls", [])) if tier else ["risk_tier not set: run Screen mode first"],
    }


COLUMNS = ["id", "title", "category", "source", "likelihood", "impact", "inherent_score",
           "inherent_rating", "controls", "owner", "residual_likelihood", "residual_impact",
           "residual_rating", "treatment_option", "treatment_adequacy"]


def write_csv(res: Dict[str, Any], path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        for row in res["rows"]:
            w.writerow(row)


def render_md(res: Dict[str, Any]) -> str:
    c = res["counts"]
    out = [
        f"# AI risk register: {res['project']}",
        "",
        f"Client: {res['client']} | Date: {res['date']} | Project risk tier: {res['risk_tier']}",
        "",
        "This assessment identifies regulatory considerations for review by your legal adviser. "
        "It is not legal advice.",
        "",
        f"Inherent ratings: Critical {c['Critical']}, High {c['High']}, Moderate {c['Moderate']}, "
        f"Low {c['Low']}, not assessed {c['Not assessed']}.",
        "",
    ]
    if res["missing_tier_controls"]:
        out.append("**Tier minimum controls not yet evidenced:** " + ", ".join(res["missing_tier_controls"]) + ".")
        out.append("")
    if res["needs_treatment"]:
        out.append("**Risks needing more treatment:** " + ", ".join(res["needs_treatment"]) + ".")
        out.append("")
    if res["unowned"]:
        out.append("**Risks with no owner:** " + ", ".join(res["unowned"]) + ".")
        out.append("")
    out.append("| ID | Risk | Category | L | I | Inherent | Controls | Owner | Residual | Treatment |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")
    for r in res["rows"]:
        out.append(
            f"| {r['id']} | {r['title']} | {r['category']} | {r['likelihood']} | {r['impact']} | "
            f"{r['inherent_rating']} ({r['inherent_score']}) | {r['controls'] or 'none'} | {r['owner']} | "
            f"{r['residual_rating']} | {r['treatment_option']}; {r['treatment_adequacy']} |")
    out.append("")
    out.append("Sources per risk are in the CSV `source` column. Ratings use a 5x5 heuristic "
               "(1-4 Low, 5-9 Moderate, 10-16 High, 17-25 Critical) calibrated to the client's risk appetite.")
    return "\n".join(out) + "\n"


def seed(project: Dict[str, Any]) -> Dict[str, Any]:
    flags = set(project.get("flags", []))
    risks = []
    n = 0
    for s in SEED:
        if flags.intersection(s["flags"]):
            n += 1
            risks.append({"id": f"R-{n:02d}", "title": s["title"], "category": s["category"],
                          "source": s["source"], "likelihood": 0, "impact": 0, "controls": [],
                          "owner": "", "residual_likelihood": 0, "residual_impact": 0})
    return {"client": project.get("client", ""), "project": project.get("project", ""),
            "date": project.get("date", ""), "risk_tier": project.get("risk_tier", 0),
            "project_controls": project.get("project_controls", []),
            "seed_flags": sorted(flags), "risks": risks}


def load(path: str) -> Dict[str, Any]:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"error: cannot read {path}: {e}", file=sys.stderr)
        sys.exit(1)


def main() -> int:
    p = argparse.ArgumentParser(description="the practice per-project AI risk register (seed or build).")
    sub = p.add_subparsers(dest="cmd", required=True)
    ps = sub.add_parser("seed", help="propose starter risks from architecture flags")
    ps.add_argument("project")
    ps.add_argument("-o", "--output", "--out")
    pb = sub.add_parser("build", help="score a filled register")
    pb.add_argument("register", nargs="?")
    pb.add_argument("--csv")
    pb.add_argument("--md", "--out")
    a = p.parse_args()

    if a.cmd == "seed":
        res = seed(load(a.project))
        text = json.dumps(res, indent=2)
        if a.output:
            with open(a.output, "w", encoding="utf-8") as f:
                f.write(text + "\n")
            print(f"seeded {len(res['risks'])} risks from flags {res['seed_flags']} -> {a.output}")
        else:
            print(text)
        return 0

    res = build(load(a.register) if a.register else SAMPLE)
    if a.csv:
        write_csv(res, a.csv)
    md = render_md(res)
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write(md)
    if not a.csv and not a.md:
        print(md)
    else:
        print(f"{len(res['rows'])} risks | tier {res['risk_tier']} | counts {res['counts']} | "
              f"needs treatment {res['needs_treatment']} | missing tier controls {res['missing_tier_controls']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
