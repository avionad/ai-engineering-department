# The monthly loop in detail

*v0.1.0, 2026-11-08. Steps 1 to 6 of `ai-optimisation-llmops`, run by `ai-optimiser`
(read-only), with ai-engineer and ai-security-tester for step 5. Sources: web research B6
(golden sets, regression runs, drift signals, cost levers, feedback loops); GitHub research area 7
and gap 6; harvested alirezarezvani `llm-cost-optimizer` (MIT) for the instrument-first rule and
proactive flags; DDD decision-focused reporting rules (`.claude/rules/communication-style.md`).*

## Step 0. Preconditions (first cycle only)

- An eval baseline exists (stage 6) with golden-set version, model and prompt versions.
- The client's own **manual baseline** is recorded from discovery: minutes per task done by
  hand, volume per month, error or rework rate, and who measured it. Without it, report time
  freed in task counts, not hours, and say why.
- Per-request logging exists: model, prompt version, input and output tokens (and cached input
  tokens), latency, feature or workflow step, user role, cost. If it does not, **logging is the
  first deliverable** and optimisation waits for one full period of data (llm-cost-optimizer's
  instrument-first rule).
- Access to traces and exports is granted in writing and covered by the data-handling agreement.

## Step 1. Collect

| Source | What | Typical location |
|---|---|---|
| Traces | Per request: inputs and outputs (masked), retrieval hits and scores, tool calls and results, latency per stage, tokens, model, prompt version, errors | Langfuse / Opik / Phoenix project, or platform logs (Bedrock, Azure, Vertex) |
| Eval runs | Golden-set results this month (scheduled run) as `test_id, category, passed, score` | Engagement repo `evals/results/` |
| Cost and usage | Daily or per-run rows: `date, system, model, tasks, input_tokens, output_tokens, cached_input_tokens, cost_aud` | Vendor billing export, trace store export, or the automation platform's run log |
| Error queues | Failed runs, dead-letter items, timeouts, tool errors, rate-limit retries | n8n executions, queue dashboard, app logs |
| Human signals | Escalations, overrides (human changed or rejected the output), edits to drafts, thumbs plus reason, complaints | App feedback table, approval tool logs, CRM notes |
| Change log | What changed this month: our deployments, vendor model updates, client process changes, source document changes, volume events (campaigns, seasonal peaks) | Engagement state, vendor changelogs, client |

Never generate data by calling the client's live website or production system. Mask personal
information before it leaves the client environment (Presidio AU recognisers, see
`../../ai-rag-engineering/references/pii-redaction-presidio.md`).

## Step 2. Measure against baseline and last month

**Core metrics per system** (define each precisely in the first report and keep the definitions
fixed):

| Metric | Definition |
|---|---|
| Volume | Tasks completed in the period (a task is the client's unit: a ticket, an invoice, a question) |
| Quality | Golden-set pass rate per category; faithfulness; field accuracy; plus production signals below |
| Override rate | Share of AI outputs a human changed or rejected |
| Escalation rate | Share of tasks handed to a human by design |
| Failure rate | Share of runs that errored, timed out or hit the dead-letter queue |
| Cost per task | Sum of `cost_aud` / tasks (from `scripts/cost_trend.py`) |
| Latency | Median and a high percentile per task, end to end and per stage |
| Hours freed | (tasks completed without rework) x (client's manual minutes per task minus measured review minutes per task) / 60; inputs cited |

**Separate real change from noise before writing a word:**

| Possible cause | Check | How to report it |
|---|---|---|
| Volume swing | Tasks up or down sharply; cost per task steady? | Total cost moved with volume; efficiency unchanged |
| Mix shift | Different task types or intents this month (input drift) | Quality moved because the work changed, not the system |
| Model or vendor change | New model ID in traces or usage; vendor changelog | Attribute to the vendor change; plan a re-test |
| Our change | Change set deployed mid-month | Compare before and after the deploy date, not month totals |
| Tracking problem | Missing days, logging gaps, a field suddenly zero, trace count not matching run count | Report as a data gap; never as performance |
| Small numbers | Few tasks or few eval items in a category | Say the sample is too small to conclude; keep watching |
| Throttling | Rate-limit retries in logs (SDKs can hide 429s) | Latency figures for the period are not comparable |
| Outlier days | One day driving the month | Name the day and show the month with and without it |

State each comparison period exactly ("October 2026 vs September 2026", "vs baseline run of
1 October 2026"). Platform-reported metrics are labelled with what they measure.

## Step 3. Sample and classify failures

Take at least the worst 20 failures of the period, or all if fewer: failed eval items, overrides,
escalations that should not have happened, errors, and negative feedback. For each, record one
primary cause:

| Cause | Signs | Usual lever |
|---|---|---|
| Retrieval | Right answer exists in the sources but was not retrieved, or wrong version retrieved | Chunking, metadata filters, hybrid or rerank settings, top-k, query rewrite |
| Prompt | Model had the right context but misread the task, format or policy | Prompt change, examples, output schema |
| Model | Capability limit on this task type; varies across runs | Route hard cases to a stronger model, or escalate |
| Data | Source documents wrong, stale, contradictory or missing | Client content owner fixes the source; freshness checks |
| Tool | Tool returned an error, wrong data, or timed out | Fix integration, retries, validation |
| Workflow | The step order, handoff or approval design causes the failure | Workflow change (`workflow-optimisation.md`) |
| User | Request out of scope, unclear, or misuse | Training, UI guidance, scope message |

Tally causes; the biggest bucket weighted by business cost usually picks the change set.
Keep the sample in client `data/` masked, with the classification, for next month's comparison.

## Step 4. Choose one change set

Score candidate changes on expected impact (on the client's outcome: hours, errors, cost) and on
risk (chance of regression, compliance impact, effort). Pick one set: related edits that ship and
are measured together. Typical candidates:

1. **Golden-set growth** (always included): every failure worth keeping becomes a test with the
   expected behaviour, so the same mistake cannot return unnoticed.
2. **Prompt change.** Manual edit for a clear defect; systematic optimisation with DSPy or GEPA
   (both MIT) only when a metric exists and a held-out portion of the golden set is kept out of
   optimisation. Report held-out scores.
3. **Retrieval tuning** (with `ai-rag-engineering` settings).
4. **Model routing**: easy cases to a cheaper model, hard or low-confidence cases to a stronger
   one or a human. Prove on the golden set split by difficulty before routing live traffic.
5. **Prompt caching and batch processing**: `cost-levers.md`.
6. **Output length limits and context trimming.**
7. **Workflow step removal or merge**: `workflow-optimisation.md`.
8. **Model migration** forced by a deprecation: `drift-and-model-migration.md` s3.

Write `../templates/change-set.md`: problem with evidence, change, expected effect (a range, with
reasoning), how it is measured next month, risks, rollback, compliance check, approvals.

## Step 5. Implement, re-test, approve, deploy

1. ai-engineer builds the change in staging, pins new versions, updates the runbook.
2. ai-security-tester runs the full golden set and the red-team families the change touches
   (any prompt or model change re-runs F1 to F5 at minimum; any agent or tool change re-runs F6
   and F7). `eval_compare.py` against the current reference: FAIL blocks.
3. ai-compliance-officer reviews if the change is material (new model, vendor, region, data class,
   user group or autonomy level).
4. The client's owner approves in writing; deploy at an agreed time with the rollback ready.
5. Record the deploy date: next month's comparison splits the month at that date.

## Step 6. Report in business terms

Use `../templates/monthly-optimisation-report.md`. First screen in 60 to 90 seconds: is each
system improving, what needs attention, what is proposed. Each finding: what happened (number and
its comparison period), why it matters, what next (an action, "monitoring", or "no action
needed"). Hours freed only from the client's own baseline. No savings multipliers. R2 verifier
re-reads the usage CSV, eval CSVs and baseline inputs and recomputes every number.
