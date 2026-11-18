# ai-optimisation-llmops

Collects traces, eval runs, cost and usage, error queues and user overrides (Langfuse default, Opik alternative, Phoenix client self-host only); measures quality, cost per task, latency, volume, failure and override rates against baseline and last month, separating real change from noise, volume swings, vendor changes and tracking faults; classifies sampled failures; picks ONE change set by impact and risk (prompt, retrieval, model routing, caching, batching, workflow step removal, golden-set growth); ships it through staging, re-test and client approval; reports in business terms with an R2 verifier. Also model deprecation watch and drift.

**When to use:** Use when a live AI system or automation is giving wrong or inaccurate answers, has got worse, costs too much, or needs to improve over time, including urgent triage of a live failure and the monthly improvement loop sold as a fenced retainer.

**Trigger phrases:** optimise the AI, improve the AI over time, monthly AI review, why are AI costs up, AI quality has dropped, cost per task, LLMOps, AI retainer, run and improve, model drift, model deprecation, model migration, prompt optimisation, DSPy, GEPA, prompt caching, batch processing, model routing, Langfuse,...

## How SKILL.md is organised

- Department relationships
- Hard rules
- Triage mode (a live system is wrong NOW)
- The loop (mirrors `ai-optimiser` Method 1 to 5, plus implement and report)
- Standing watches (every cycle)
- Cost trend script
- Outputs and locations
- Retainer (scope only)
- Size bands
- Do not
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/cost-levers.md` | **Cost levers.** v0.1.0, 2026-11-08. Used at step 4 of the loop. **Pricing rule:** the only vendor pricing. |
| `references/drift-and-model-migration.md` | **Drift detection and model migration.** v0.1.0, 2026-11-08. Standing watches in `ai-optimisation-llmops`. Sources: web research B6. |
| `references/monthly-loop.md` | **The monthly loop in detail.** v0.1.0, 2026-11-08. Steps 1 to 6 of `ai-optimisation-llmops`, run by `ai-optimiser`. |
| `references/observability-stack.md` | **Observability stack: traces, evals, cost.** v0.1.0, 2026-11-08. Source: GitHub research area 7 (repo, licence, last push as at. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-optimisation-llmops.** v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and. |
| `references/workflow-optimisation.md` | **Workflow optimisation (not only the AI).** v0.1.0, 2026-11-08. The AI step is often not where the time goes. the practice owner's brief for this skill:. |

## Templates

| File | What it holds |
|---|---|
| `templates/change-set.md` | **Change set: {system}, {short title}.** Template v0.1.0 (ai-optimisation-llmops), 2026-11-08. One change set per cycle. |
| `templates/monthly-optimisation-report.md` | **AI systems: monthly optimisation report, {Month YYYY}.** Template v0.1.0 (ai-optimisation-llmops), 2026-11-08. |
| `templates/retainer-scope.md` | **Run and improve retainer: scope.** Template v0.1.0 (ai-optimisation-llmops), 2026-11-08. |

## Scripts

| File | What it holds |
|---|---|
| `scripts/cost_trend.py` | **!/usr/bin/env python3.** """Monthly AI cost and usage trend per system, from a usage CSV. |

*Skill version 0.1.0. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
