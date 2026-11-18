# AI use-case portfolio

*Generated 2026-11-08 by `portfolio.py` from `samples/sample-portfolio-2026-11-08.csv`. Values are annual AUD from the client's own numbers; a value without a source is ignored. Ranking follows use-case-qualification.md s3 (value, then time to value, feasibility, risk tier).*

## Summary

| Measure | Count |
|---|---|
| Use cases | 11 |
| Status: idea | 4 |
| Status: qualified | 2 |
| Status: approved | 1 |
| Status: build | 1 |
| Status: live | 3 |
| Rows with errors | 1 |
| Unsourced values (ignored) | 1 |
| Tier 4 (stop) | 1 |
| Tier 3 without compliance screen | 1 |

## Errors (fix the CSV)

- **UC-11 Policy Q&A assistant for staff**: feasibility must be a whole number 1-5: '7'

## Ranked pipeline (not yet live)

| Rank | ID | Use case | Owner | Planned value (low to high) | Time to value (wks) | Feasibility | Tier | Status | Eligible to approve |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UC-10 | Claims triage recommendation | Claims manager | $50,000 to $80,000 | 12 | 2 | 3 | build | committed |
| 2 | UC-04 | Candidate shortlisting score | HR manager | $30,000 to $45,000 | 10 | 3 | 3 | qualified | no |
| 3 | UC-01 | Supplier invoice capture into the ERP | AP lead | $18,000 to $26,000 | 6 | 4 | 2 | approved | committed |
| 4 | UC-02 | Customer email triage and routing | Service manager | $9,000 to $14,000 | 5 | 3 | 2 | qualified | yes |
| 5 | UC-11 | Policy Q&A assistant for staff | NONE | $5,000 to $8,000 | 3 | PENDING | 1 | idea | no |
| 6 | UC-03 | Sales lookups in plain English over the ERP | Sales manager | PENDING | 4 | 3 | 1 | idea | no |
| 7 | UC-06 | Quote generation from site measurements | Estimating lead | PENDING | 6 | 4 | 2 | idea | no |

Eligible to approve means: sourced value, named owner, tier 1 to 3 (tier 3 screened), no errors. 'committed' means already approved or in build. Value ranks on the midpoint of the sourced range. The three gate questions (data there, owner, 30-day pilot) are still asked in person; this table does not answer them.

## Stopped (tier 4)

- **UC-05 Covert emotion detection on staff video calls** (status idea): do not build. Record the reason and offer a lawful alternative.

## Live: planned vs actual

| ID | Use case | Planned (low to high) | Baseline cost | Current cost | Realised benefit | Assessment |
|---|---|---|---|---|---|---|
| UC-07 | Bank reconciliation support | $12,000 to $16,000 | $20,800 | $6,200 | $14,600 | within planned range: candidate to scale or hold |
| UC-08 | After-hours voice receptionist | $15,000 to $22,000 | $24,000 | $14,500 | $9,500 | BELOW planned range: review (fix, rescope or kill) |
| UC-09 | CRM record enrichment | $6,000 to $9,000 | PENDING | $4,000 | PENDING | cannot assess (missing baseline or actual) |

The assessment is a prompt for the monthly portfolio review, not a decision. Kill or scale is decided by the accountable owner with the review notes.

## Flags by use case

- **UC-03 Sales lookups in plain English over the ERP**: UNSOURCED VALUE: value given with no value_source; ignored for ranking
- **UC-04 Candidate shortlisting score**: TIER 3 WITHOUT COMPLIANCE SCREEN: run ai-compliance-risk mode (a) before design
- **UC-05 Covert emotion detection on staff video calls**: value PENDING: cannot be the next pilot until the client's numbers are in; TIER 4: STOP. Do not build; record the reason and a lawful alternative
- **UC-06 Quote generation from site measurements**: value PENDING: cannot be the next pilot until the client's numbers are in
- **UC-09 CRM record enrichment**: LIVE WITHOUT BASELINE: no benefit can be claimed; live but not linked to the AI register
- **UC-11 Policy Q&A assistant for staff**: no named owner (gate 2 fails)

