# Build vs buy

*v0.1.0, 2026-11-08. Approach adapted from the upstream `chief-ai-officer-advisor` skill, whose
files sit at `ai-kb/vendor/alirezarezvani__claude-skills/c-level-advisor/skills/chief-ai-officer-advisor/`
(`references/model_buildvsbuy_strategy.md`, `references/ai_cost_economics.md`,
`scripts/model_buildvsbuy_calculator.py` -- upstream paths, none of them files in this skill) in
alirezarezvani/claude-skills, MIT (c) 2025 Alireza Rezvani, commit
`8f082544116fc0d014188e521ca40304cdfc86b0`. What DDD kept: compare paths on multi-year total cost
of ownership from the workload profile; count the hidden costs on both sides; decide only after
an eval set exists. What DDD dropped: every price, threshold and capability figure in the
harvested files (illustrative USD prices, "monthly cost" and "tokens per month" thresholds,
benchmark gaps, team-size rules), because none are sourced for DDD's clients. DDD's paths are the
ladder rungs, not the harvested API / fine-tune / pre-train split.*

## 1. The options to compare (pick at most three)

| Option | Typical shape | Main cost lines |
|---|---|---|
| Buy SaaS | A product that does the job, per seat or per usage | Subscription, implementation, integration, training, exit |
| Configure what they have | A feature in the client's existing suite | Licence uplift (if any), configuration, training |
| Build on a hosted model | Workflow or app calling a model API in the right region | Build effort, tokens, hosting for the workflow or app, monitoring, run support |
| Build self-hosted | Open-weight model on a VPS or on-premises GPU | Build effort, hardware or GPU rental, MLOps, on-call, upgrades |
| Customise a model | Fine-tune or distil, then host | Data preparation, training compute, eval, hosting, retraining |

Pre-training a model from scratch is never a DDD option.

## 2. Eval first

Do not pick a path without an eval set (harvested source's "eval-first discipline"). Build a
small golden set from the client's real examples (with permission) and run it against the
cheapest viable options before committing. The eval result can eliminate an option outright.

## 3. TCO worksheet (manual, three years by default)

Fill one column per option. **Every unit price needs a vendor pricing URL and the date checked,
or the cell says PENDING_VERIFICATION.** Volumes come from the client's discovery numbers.
Effort comes from `ai-proposal-pricing` (hours by bucket), not from this sheet.

| Line | Driver | Option A | Option B | Option C | Source (URL, date) |
|---|---|---|---|---|---|
| Workload: tasks per month | Client discovery | | | | |
| Workload: tokens in / out per task | Measured on the eval set | | | | |
| One-off: build or implementation effort | ai-proposal-pricing | | | | |
| One-off: data preparation and clean-up | ai-proposal-pricing | | | | |
| One-off: integration | ai-proposal-pricing | | | | |
| One-off: training and change | ai-proposal-pricing | | | | |
| Recurring: subscription or seats | Vendor price x seats | | | | |
| Recurring: tokens | Vendor price x volume | | | | |
| Recurring: hosting (workflow, app, vector store, GPU) | Vendor price | | | | |
| Recurring: monitoring and eval runs | ai-optimisation-llmops scope | | | | |
| Recurring: support and maintenance effort | ai-proposal-pricing (run bucket) | | | | |
| Recurring: model version migrations | Expected cadence | | | | |
| Exit: data export, rebuild, parallel run | Estimate | | | | |
| **Three-year total** | Sum | | | | |

Show the arithmetic so the R2 verifier can recompute it. A total built on any PENDING cell is
labelled PROVISIONAL and does not go to the client.

## 4. Hidden costs (count them, do not price them from memory)

Categories adapted from the harvested cost-economics reference:

| Self-hosted or custom | Bought or API |
|---|---|
| On-call and incident response | Lock-in to one vendor's features and formats |
| Monitoring and observability tooling | Capability drift between model versions (pin versions, regression evals) |
| Model updates and re-evaluation | Rate limits at peaks |
| Capacity planning and idle hardware | Long-context or premium-feature pricing |
| Failover and redundancy | Data residency limits of the vendor's regions |
| Security patching and compliance evidence | Training and retention terms on client data |

## 5. Non-cost comparison

| Factor | Option A | Option B | Option C |
|---|---|---|---|
| Residency (where processed, stored, logged) | | | |
| Control (who can change behaviour, when) | | | |
| Lock-in and exit path | | | |
| Operational burden on the client | | | |
| Time to value | | | |
| Fit with the client's skills and suppliers | | | |
| Risk tier implications (e.g. vendor DD, impact assessment) | | | |

## 6. Decide and record

Recommend one option, give the reason in two sentences, name the strongest alternative in one
line, and write the ADR. Revisit the decision at a stated trigger (volume doubles, a residency
requirement changes, the vendor changes terms, the eval shows a gap).
