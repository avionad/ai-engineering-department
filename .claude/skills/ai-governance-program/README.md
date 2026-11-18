# ai-governance-program

Builds the organisation-level program for DDD's ai-automation department, sized from 5 to 500+ staff. Covers AI policy and acceptable use policy, governance charter (owner plus reviewer up to a cross-functional AI council), AI register including shadow AI discovery, ISO/IEC 42001 readiness gap (readiness only, DDD cannot certify), AI literacy plan by role including the board, AI incident response playbook, transparency statement and model card, and ADM-ready privacy policy wording for the legal adviser. Every artefact maps to the Guidance for AI Adoption six practices and cross-maps to ISO 42001 and NIST AI RMF. Australia first; not legal advice.

**When to use:** Use when an organisation needs an AI policy, acceptable use policy, AI council or AI register written, or AI governance set up or improved across the whole business rather than one project.

**Trigger phrases:** ai governance, ai policy, acceptable use policy ai, ai aup, ai governance charter, ai council, ai committee terms of reference, ai register, ai inventory, shadow ai, unapproved ai tools, iso 42001, iso 42001 readiness, aims gap analysis, ai literacy training, board ai training, ai incident response,...

## How SKILL.md is organised

- Department relationships
- Where DDD adds value (be honest about this)
- Spine: the six practices (AU-4, voluntary)
- Playbook
- Size bands
- Output conventions
- Do not
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/framework-crosswalk.md` | **Framework crosswalk: artefacts to the six practices, ISO/IEC 42001 and NIST AI RMF.** v0.1.0, 2026-11-08. The organising spine of `ai-governance-program`. Every artefact we deliver. |
| `references/shadow-ai-discovery.md` | **Shadow AI discovery method.** v0.1.0, 2026-11-08. Feeds the AI register. Why it matters (research headline 8, IBM 2026 Cost of. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-governance-program.** v0.1.0, 2026-11-08. SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`. |

## Templates

| File | What it holds |
|---|---|
| `templates/adm-privacy-policy-wording-guide.md` | **ADM-ready privacy policy wording guide (draft for the legal adviser).** v0.1.0, 2026-11-08. Register row AU-8: POLA Act 2024, APP 1.7 to 1.9, **commences 10 December. |
| `templates/ai-policy-and-aup.md` | **AI policy and acceptable use policy template.** v0.1.0, 2026-11-08. Practices 1 and 6 (AU-4); ISO/IEC 42001 Clause 5 and 7; NIST Govern. |
| `templates/ai-register-template.md` | **AI register template.** v0.1.0, 2026-11-08. Practices 1, 3, 4 (AU-4); ISO/IEC 42001 Clause 4 (4.3 scope per harvested. |
| `templates/governance-charter.md` | **AI governance charter template (scaled by size band).** v0.1.0, 2026-11-08. Practice 1 "Decide who is accountable" (AU-4); ISO/IEC 42001 Clause 5. |
| `templates/incident-response-playbook.md` | **AI incident response playbook.** v0.1.0, 2026-11-08. Practices 5 and 6 (AU-4); ISO/IEC 42001 Clause 10 (corrective action);. |
| `templates/iso42001-readiness-gap.md` | **ISO/IEC 42001 readiness gap: method and report frame.** v0.1.0, 2026-11-08. ISO/IEC 42001:2023 is voluntary and certifiable (INT-1). **DDD does readiness;. |
| `templates/literacy-training-plan.md` | **AI literacy training plan (by role, incl. board).** v0.1.0, 2026-11-08. Practices 1 and 6 (AU-4); ISO/IEC 42001 Clause 7 (competence, awareness);. |
| `templates/transparency-statement-and-model-card.md` | **Transparency statement and model or system card templates.** v0.1.0, 2026-11-08. Practice 4 "Share essential information" (AU-4); ISO/IEC 42001 Clause 7. |

## Scripts

| File | What it holds |
|---|---|
| `scripts/iso42001_readiness_gap.py` | **!/usr/bin/env python3.** """iso42001_readiness_gap.py -- ISO/IEC 42001 readiness gap (Clauses 4-10) for DDD clients. |

*Skill version 0.1.0. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
