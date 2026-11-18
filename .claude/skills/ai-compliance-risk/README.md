# ai-compliance-risk

Project-level compliance and risk for this AI automation department, Australia first. Screens the project into a risk tier (1 Low to 4 Stop) with a scored questionnaire, lists applicable obligations with status and source from the regulatory register and industry pack, runs the APP 1.7-1.9 automated decision-making check (10 Dec 2026), builds a per-project risk register seeded from CoSAI and NIST AI 600-1, structures an AI impact assessment, threat-models against OWASP LLM and Agentic Top 10 and MITRE ATLAS, issues a vendor due diligence questionnaire, and runs the pre-go-live compliance sign-off. Identifies obligations for the client's legal adviser; never gives legal advice.

**When to use:** Use when any AI or automation project needs to know what rules apply and how risky it is.

**Trigger phrases:** ai risk assessment, ai compliance check, what rules apply to this ai project, risk tier, ai screening, adm check, automated decision making disclosure, app 1.7, privacy policy adm, ai risk register, ai impact assessment, iso 42005, threat model ai, owasp llm, owasp agentic, mitre atlas, prompt injec...

## How SKILL.md is organised

- Department relationships
- Ground truth (R1)
- Modes
- Output conventions
- Size bands
- Do not
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/adm-check.md` | **Mode (c) ADM check: APP 1.7 to 1.9.** v0.1.0, 2026-11-08. Source rows: AU-8 (and AU-6) in `../../_shared/regulatory-register.md`. |
| `references/risk-catalogue.md` | **Risk catalogue for mode (d) risk register.** v0.1.0, 2026-11-08. Seed lists for the per-project register. `scripts/ai_risk_register.py seed`. |
| `references/screening-questionnaire.md` | **Mode (a) Screen: risk tier questionnaire.** v0.1.0, 2026-11-08. Assigns one of the four risk tiers in `../../_shared/engagement-conventions.md`. |
| `references/threat-model.md` | **Mode (f) Threat model: OWASP LLM, OWASP Agentic, MITRE ATLAS.** v0.1.0, 2026-11-08. Use with `ai-architect`'s data-flow and trust-boundary diagram. Output:. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-compliance-risk.** v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and. |

## Templates

| File | What it holds |
|---|---|
| `templates/applicable-obligations-template.md` | **Applicable obligations: {Project name}.** Client:** {Client} | **Industry pack:** {pack} | **Size band:** {S/M/L/XL} |. |
| `templates/compliance-findings-template.md` | **AI compliance and risk review -- {Client} -- {System / project} -- {YYYY-MM-DD}.** Audience: {client accountable owner and their legal adviser}. This assessment identifies. |
| `templates/compliance-signoff-checklist.md` | **Compliance sign-off checklist (pre-go-live).** v0.1.0, 2026-11-08. Mode (h). Stage 6 exit gate in `engagement-conventions.md`: no go-live. |
| `templates/impact-assessment-template.md` | **AI impact assessment: {Project name}.** Alignment note.** This template is aligned in structure to ISO/IEC 42005:2025, AI system impact. |
| `templates/vendor-due-diligence-questionnaire.md` | **Third-party AI vendor due diligence questionnaire.** v0.1.0, 2026-11-08. Mode (g) of ai-compliance-risk. Sent by the client to any vendor whose. |

## Scripts

| File | What it holds |
|---|---|
| `scripts/ai_risk_register.py` | **!/usr/bin/env python3.** """ai_risk_register.py -- per-project AI risk register for this AI automation department. |

*Skill version 0.1.1. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
