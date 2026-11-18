# Platform decision record: {project}

*Template v0.1.0 (ai-deployment-platforms), 2026-11-08. ADR format (context, options, decision,
consequences) extended for residency, security baseline and exit. Save as
`{client}/created/docs/strategy/platform-decision-record-{project}-{YYYY-MM-DD}.md`. Every model,
region, deployment type, price and assessment status below carries a vendor URL and the date and
time checked, or `PENDING_VERIFICATION` (and then it does not go to the client).*

| Field | Value |
|---|---|
| Status | Proposed / Accepted / Superseded by ____ |
| Date | |
| Decided by (DDD) | |
| Approved by (client accountable owner) | |
| Risk tier and date (`ai-compliance-risk`) | |
| Size band, industry pack | |

## 1. Summary (60 seconds, plain English)

We recommend ____ because ____. Your data will be processed in ____ and stored in ____. The main
trade-off is ____. If we ever need to move, the substitute is ____ and the effort is roughly ____.
Note: processing in Australia does not remove foreign-law access risk for US-headquartered
providers (for example the US CLOUD Act).

## 2. Context

- Use case and patterns (P1-P11):
- Users, volumes (client's figures), latency needs:
- Client's existing cloud, identity provider, procurement constraints:
- Client policies on data location or model origin:
- Sector rules (APRA CPS 230/234, DTA policy, health) per `ai-compliance-risk`:

## 3. Data classes per flow (`references/data-class-matrix.md`)

| Flow | Contents | Class (C0-C5) | Allowed platforms per matrix | Conditions |
|---|---|---|---|---|
| User prompts | | | | |
| Retrieved documents | | | | |
| Outputs | | | | |
| Logs and traces | | | | |
| Embeddings / index | | | | |
| Training or eval data | | | | |

## 4. Options compared (maximum three)

| Criterion | Option A: ____ | Option B: ____ | Option C: ____ |
|---|---|---|---|
| Residency (every component) | | | |
| Assurance (IRAP level, certifications, verified how) | | | |
| Model availability (exact model, region, deployment type) | | | |
| Control (network, keys, logging, guardrails) | | | |
| Operations burden | | | |
| Cost drivers (no prices here; run-cost sheet reference) | | | |
| Lock-in (proprietary features used) | | | |
| Exit path and switching effort | | | |
| Fit with client | | | |

## 5. Decision

- Chosen option and one-line reason:
- Strongest alternative and why not:
- Hybrid routing? Gateway, classification gate rules, fail-closed behaviour:

## 6. Verified facts (verify-live log)

| Fact | URL | Checked (date, time, by) | Account-specific? | Evidence file |
|---|---|---|---|---|
| | | | | |

## 7. Component placement

| Component | Service | Region | Deployment type / profile | Pinned version or ID |
|---|---|---|---|---|
| Generation model | | | | |
| Embedding model | | | | |
| Vector / search index | | | | |
| Document parser / OCR | | | | |
| Guardrails | | | | |
| Logs, traces, cache | | | | |
| Gateway | | | | |
| Workflow / orchestration (for example n8n) | | | | |

All components in the approved region(s): yes / no (if no, the residency claim is not made).

## 8. Security baseline (`references/security-baseline.md`)

| Control | How met | Evidence |
|---|---|---|
| B1 SSO and service identities | | |
| B2 No-training and retention terms (document, date) | | |
| B3 Secrets in Doppler / client vault | | |
| B4 Private networking | | |
| B5 Encryption and keys | | |
| B6 Logging location and access | | |
| B7 Guardrails | | |
| B8 Least agency (agents only) | | |
| B9 Version pinning and retirement tracking | | |
| B10 Budgets and quotas | | |
| B11 Environment separation | | |
| B12 Incident readiness | | |

## 9. Exit and substitution plan

- Substitute platform and model:
- What moves (data, index rebuild, prompts, evals, workflows, keys) and where it is stored (client-owned accounts):
- Estimated switching effort and who does it:
- Tested? (date, result) Required for APRA-regulated critical use (register AU-13, AU-15):
- Triggers for invoking it (model retirement, price change, vendor incident, residency change):

## 10. Consequences

- Positive:
- Negative and accepted risks (with owner):
- Follow-ups (owner, date):

## 11. Hand-offs

- Run-cost drivers sent to `ai-proposal-pricing` (date):
- Threats and vendor due diligence items sent to `ai-compliance-risk` (date):
- Setup tasks for `ai-engineer` (sandbox/staging only):
- Re-verification due date (60 days):
