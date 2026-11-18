# ai-readiness-assessment

DDD's paid front-door product. Scores seven dimensions 1-5 with evidence (strategy and leadership, data, technology and infrastructure, people and skills, process, governance and risk, security and privacy), scores governance against the Guidance for AI Adoption six practices and the APP 1.7 automated decision-making duty, applies Go/Wait gates to the organisation and each candidate use case, and produces a readiness report with a ranked 90-day plan plus a one-page executive summary. Scales from a 2-hour owner interview (S) to a multi-week assessment with data sampling (XL).

**When to use:** Use when a client or prospect wants to know whether they are ready for AI, does not know where to start, or leadership asks for an AI strategy starting point.

**Trigger phrases:** AI readiness, are we ready for AI, AI readiness assessment, AI maturity, where do we start with AI, AI audit of our business, AI strategy starting point, readiness scorecard, AI gap analysis, should we invest in AI yet, AI health check, readiness report, Go or Wait on AI

## How SKILL.md is organised

- Rules
- Playbook
- Use in a sales conversation
- Files

## References

| File | What it holds |
|---|---|
| `references/dimensions-rubric.md` | **Seven dimensions and scoring rubric.** v0.1.0, 2026-11-08. Level descriptors adapted from OneWave-AI `ai-readiness-assessment`. |
| `references/evidence-checklist.md` | **Evidence checklist per dimension.** v0.1.0, 2026-11-08. Ask for these before or during the assessment. For S, most evidence is a. |
| `references/gates.md` | **Go/Wait gates.** v0.1.0, 2026-11-08. Use-case gate adapted from anthropics/financial-services `ai-readiness`. |
| `references/interview-guides.md` | **Readiness interview guides per function.** v0.1.0, 2026-11-08. Each guide is 30-45 minutes (the S owner interview combines them into about. |
| `references/size-band-scaling.md` | **Size-band scaling.** v0.1.0, 2026-11-08. Bands from `_shared/engagement-conventions.md` s5. Durations are DDD's. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-readiness-assessment.** Harvest sources are read-only copies in a local vendor mirror (`ai-kb/vendor/`), pinned per. |

## Templates

| File | What it holds |
|---|---|
| `templates/executive-summary-template.md` | **AI readiness: executive summary.** {Client} | {Month YYYY} | Design Data Dynamics. |
| `templates/readiness-input-template.json` | **readiness-input-template.**. |
| `templates/readiness-report-template.md` | **AI readiness assessment: {Client}.** {Month YYYY}. Prepared by Design Data Dynamics. File as. |

## Scripts

| File | What it holds |
|---|---|
| `scripts/readiness_score.py` | **!/usr/bin/env python3.** """readiness_score.py -- DDD AI readiness scorecard and Go/Wait gate. |

*Skill version 0.1.0. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
