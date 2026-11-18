<!-- Audience: client accountable owner (first screen), client technical owner (detail); internal
copy to ai-manager. Save as {client}/reports/adhoc-report/ai-optimisation-{YYYY-MM}.md (or the
client's agreed location). Matches the Output section of ~/.claude/agents/ai-optimiser.md. Client-facing
version passes client-ops/client-voice and is rendered with tools/report-renderer/render_report.py.
More than 3 numbers: R2 verifier at scripts/verifiers/verify_ai-optimisation-{YYYY-MM}.py. -->

# AI systems: monthly optimisation report, {Month YYYY}

*Template v0.1.0 (ai-optimisation-llmops), 2026-11-08.*

**Client:** {client} | **Period:** {1 Month YYYY to last day} | **Compared with:** {previous
month} and {baseline run, date} | **Prepared by:** {name} | **Date:** {YYYY-MM-DD}
**Retainer scope:** {path to retainer scope} | **Systems in scope:** {n of N}

## Headline

{Three to five sentences a business owner can read in 60 to 90 seconds. Lead with the business
outcome: hours freed against your own baseline, cost per task, and whether quality is holding.
Then what needs attention, then what we propose. Each statement: what happened (number and
comparison period), why it matters, what next.}

| System | Tasks (month) | Hours freed (your baseline) | Cost per task (AUD) | Quality trend | Status |
|---|---|---|---|---|---|
| {system} | {n} ({+/- vs last month}) | {h} | {x} ({+/- %}) | {improving / steady / declining}, golden set {pass rate} | {on track / watch / action needed} |

How hours freed is calculated: tasks completed without rework x (your measured manual minutes
per task {m}, source {discovery note, date} minus measured review minutes per task {r}) / 60.

## 1. What changed this month and why

{Ranked by business impact. For each: the observed result, the interpretation ("this suggests"),
any hypothesis ("one possible explanation, needs confirming"), and whether action is needed.
Separate real change from: volume swings, mix shifts, vendor or model changes, our own
deployment on {date}, tracking problems, small samples, throttling.}

| Change observed | Size and comparison | Cause (evidence) | Real change or noise? | Action |
|---|---|---|---|---|

Data gaps this month: {missing days, logging changes, anything that limits a conclusion; a
tracking problem is never reported as performance}.

## 2. Quality

| System | Golden set version | Category | Last month | This month | Baseline | Threshold (agreed by, date) |
|---|---|---|---|---|---|---|

Regressions: {n, list}. New tests added this month: {n, from which failures}.
Production signals: override rate {x} ({+/-}), escalation rate {x}, failure rate {x},
negative feedback {x}. Source: eval_compare output {path}; trace export {path}.

## 3. Cost and usage

From `cost_trend.py` on {usage export path}. Costs are as billed in the export; DDD does not
estimate token prices.

| System | Month | Tasks | Cost (AUD) | Cost per task | Change vs last month | Cache share | Flags |
|---|---|---|---|---|---|---|---|

{One or two sentences: why cost per task moved, separating volume from efficiency.}

## 4. Failures reviewed

Sample: {n} failures ({worst 20 or all if fewer}) from {sources}.

| Cause | Count | Example (masked) | Lever |
|---|---|---|---|
| Retrieval | | | |
| Prompt | | | |
| Model | | | |
| Data | | | |
| Tool | | | |
| Workflow | | | |
| User | | | |

## 5. Last month's change set: did it work?

| Change set | Deployed | Expected effect | Measured effect (before vs after {date}) | Verdict |
|---|---|---|---|---|

## 6. Proposed change set for next month

{One change set, link to `ai-change-set-{system}-{date}.md`.}

| Item | Detail |
|---|---|
| Problem and evidence | |
| Change | |
| Expected effect (range, reasoning) | |
| How we will measure it next month | |
| Risks and rollback | |
| Compliance check needed? | Yes / No, why |
| Approval needed from | {client owner} by {date} |

## 7. Watches

| Watch | Status | Action |
|---|---|---|
| Model deprecation (inventory checked live on {date}, links in appendix) | | |
| Drift (input mix, retrieval hit rate, source freshness) | | |
| Workflow friction | | |
| Compliance triggers (new data, users, autonomy, vendor) | | |

## 8. Retainer usage

Systems {n of N} | Eval cycles {n of N} | Change sets {n of N} | Support hours {h of H}.
Anything outside scope: {item, recommended route: change request or new quote}.

## Appendix: sources and definitions

Data files and their dates, metric definitions (fixed since the first report), model inventory
with vendor page links and check dates, verifier path and result.
