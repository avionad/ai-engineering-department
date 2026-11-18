<!-- Audience: internal (ai-optimiser, ai-engineer, ai-security-tester) and the client owner who
approves. Save as {client}/created/docs/strategy/ai-change-set-{system}-{YYYY-MM-DD}.md -->

# Change set: {system}, {short title}

*Template v0.1.0 (ai-optimisation-llmops), 2026-11-08. One change set per cycle.*

**ID:** CS-{client}-{YYYY-MM}-{n} | **System:** {name, current version} | **Risk tier:** {1-3}
**Proposed by:** {ai-optimiser run, date} | **Monthly report:** {path}

## 1. Problem and evidence

{What is wrong or costly, with numbers and comparison periods. Link the failure sample, trace
IDs, eval results, cost_trend output.}

## 2. Options considered (ranked by impact and risk)

| Option | Expected impact | Risk | Effort | Chosen? |
|---|---|---|---|---|

Why this one: {one paragraph}. Strongest alternative: {one line}.

## 3. The change

| Component | Current | Proposed |
|---|---|---|
| Prompt version | | |
| Model / routing | | |
| Retrieval settings | | |
| Caching / batching | | |
| Workflow step | | |
| Guardrails | | |
| Golden set (tests added) | {version} | {version, n new tests from failures} |

## 4. Expected effect and how it will be measured

| Metric | Now (period) | Expected (range, reasoning) | Measured how, when |
|---|---|---|---|

No savings figure from a vendor discount rate: realised cost change is measured from the usage
export after deploy.

## 5. Risks, compliance and rollback

- Regression risk: {which golden-set categories and red-team families must be re-run}
- Compliance trigger? {new model, vendor, region, data class, user group or autonomy level:
  if yes, ai-compliance-officer review and sign-off refresh}
- Rollback: {exact steps and the version to return to}

## 6. Verification (filled by ai-security-tester)

| Check | Result | Evidence |
|---|---|---|
| Full golden set, eval_compare verdict vs reference | PASS / PASS WITH CONDITIONS / FAIL | |
| Red-team families re-run | | |
| Regressions accepted in writing (if any) | | |

## 7. Approvals and deployment

| Step | Who | Date | Evidence |
|---|---|---|---|
| Built in staging | ai-engineer | | |
| Re-tested | ai-security-tester | | |
| Compliance review (if triggered) | ai-compliance-officer | | |
| Client approval (written) | {client owner} | | |
| Deployed to production | {who, at what time} | | |
| Versions pinned and runbook updated | ai-engineer | | |
