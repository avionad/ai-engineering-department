# ai-use-case-portfolio

Runs the organisation-level AI use-case portfolio for this AI automation department: staff idea intake, scoring with the discovery qualification rules (value, feasibility, risk tier, time to value), prioritisation and sequencing, baseline measurement before any build, monthly benefits tracking after go-live (planned vs actual), kill and scale decisions, and a portfolio register linked to the AI register. Ships portfolio.py, which ranks a CSV and flags unsourced values, tier 4 stops, unscreened tier 3 items and missing baselines. No invented values.

**When to use:** Use when an organisation has more than one AI or automation idea and needs to decide what to do next, prove what the live ones are worth, or stop the ones that are not working.

**Trigger phrases:** ai use case portfolio, prioritise ai ideas, which ai project next, ai backlog, ai idea intake, staff ai ideas form, ai roadmap of use cases, rank ai use cases, ai benefits tracking, ai roi tracking, planned vs actual ai benefit, is the ai worth it, baseline before build, kill or scale ai project, ai...

## How SKILL.md is organised

- Department relationships
- The portfolio lifecycle
- Method
- Script: `scripts/portfolio.py`
- Size bands
- Output conventions
- Do not
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/benefits-tracking.md` | **Baseline and benefits tracking.** v0.1.0, 2026-11-08. The practice's method. Measurement principles taken from research B1 step 7. |
| `references/intake-form.md` | **Staff idea intake form.** v0.1.0, 2026-11-08. The practice's own design. Build it in the client's own form tool (Microsoft Forms,. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-use-case-portfolio.** v0.1.0, 2026-11-08. SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`. |

## Templates

| File | What it holds |
|---|---|
| `templates/benefits-review-template.md` | **AI portfolio review: {Client}, {Month YYYY}.** Prepared by {your practice}. Review period: {exact dates}. Baselines as recorded in the. |
| `templates/portfolio-register-template.csv` | **portfolio-register-template.**. |

## Scripts

| File | What it holds |
|---|---|
| `scripts/portfolio.py` | **!/usr/bin/env python3.** """portfolio.py -- rank an organisation's AI use-case portfolio and flag governance gaps. |

*Skill version 0.1.0. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
