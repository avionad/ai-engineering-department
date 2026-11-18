# Scope of work: {project} -- {Client} -- {YYYY-MM-DD}

*Internal scope for `ai-proposal-pricing`. Hours, not fees: no prices in this document. The line
items live in the companion CSV `scope-line-items-{project}-{YYYY-MM-DD}.csv` with columns
`line_item,bucket,assumption,low,likely,high,dependencies,risk`. Keep the table below and the CSV
identical; the R2 verifier compares them.*

## 1. Context
| Field | Value |
|---|---|
| Client, size band, industry | |
| Channel (DDD direct / Telco ICT referred) | |
| Use case(s) and pattern(s) | |
| Risk tier (provisional / confirmed, date) | |
| Deployment choice and region | |
| Solution design brief | link |
| Discovery notes | link |

## 2. Success measure
Baseline (client figure and source), target, how measured, when reviewed.

## 3. In-scope line items
Buckets: `config-saas`, `integration-workflow`, `rag-knowledge`, `custom-agent-app`,
`model-customisation`, `governance-compliance`, `change-training`, `run-ongoing`.

| # | Line item | Bucket | Assumption | Low h | Likely h | High h | Dependencies | Risk | Acceptance test | Writes to a system? |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | yes / no |

Completeness checklist (tick or explain):
- [ ] Eval baseline line (tier 2+)
- [ ] Impact assessment, ADM disclosure, red-team lines (tier 3)
- [ ] Privacy check (any personal information)
- [ ] Integration and data-cleaning effort itemised
- [ ] Handover, documentation and training itemised
- [ ] Run lines separate from build lines
- [ ] Every write action flagged and has an approval step

## 4. Staged plan
Stage 1 read-only or sandbox pilot, acceptance gate, stage 2 production-ready in staging, go-live
gate (client accountable owner approval, conventions stage 7).

## 5. Client dependencies
Access, sandbox, samples, SME time (hours per week), approvals, security questionnaire.

## 6. Assumptions
Numbered. Each one says what happens to scope if it proves false.

## 7. Out of scope
Explicit list.

## 8. Run-cost inputs for `ai-proposal-pricing`
Expected volumes (client figures), platform, region. Unit prices are sourced by the pricing skill
from vendor pages with a date checked; do not enter prices here.

| Item | Unit | Expected monthly units (client figure) | Source of the volume |
|---|---|---|---|
| | | | |

## 9. Open items
PENDING numbers and unanswered questions, with owner and due date.
