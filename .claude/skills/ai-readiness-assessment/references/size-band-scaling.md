# Size-band scaling

*v0.1.0, 2026-11-08. Bands from `_shared/engagement-conventions.md` s5. Durations are DDD's
planning defaults for shaping the scope, not commitments; `ai-proposal-pricing` turns the scope
into hours and a fee.*

| | S (1-19) | M (20-199) | L (200-499) | XL (500+) |
|---|---|---|---|---|
| Shape | One owner interview of about 2 hours, screen-share of 1-2 processes, light document check | Owner plus 3-5 department interviews, IT/MSP interview, document review | Sponsor, department heads, IT, risk/compliance, privacy, HR, procurement interviews; staff pulse; document review | Multi-week: interviews across all functions and business units, staff pulse, data sampling, shadow AI discovery from logs, board or executive readout |
| Evidence standard | Mostly stated, some seen | Seen for data, technology, governance | Seen for all dimensions; data samples for top use cases | Seen for all dimensions; structured data sampling; log-based shadow AI evidence |
| Governance depth | Policy and register exist or not; ADM quick check | Six practices rated; ADM inventory of obvious systems | Six practices rated with evidence; ADM inventory incl. vendor-embedded systems; vendor due diligence sample | Full six-practice review; ADM inventory across business units; ISO/IEC 42001 readiness view; board literacy check (APRA flags board literacy for regulated entities) |
| Report | Light report: scorecard, top 3 risks, 90-day plan, 1-2 first use cases; plus the one-page executive summary | Full report and executive summary | Full report, executive summary, per-function appendix | Full report, executive summary, per-business-unit appendix, readout deck |
| Hand-offs | Straight to `ai-discovery-scoping` for the first use case | Discovery for the top 2 use cases; governance basics via `ai-governance-program` | Governance program; compliance screen per use case | Governance program, enterprise rollout (planned `ai-enterprise-rollout`), compliance screens |

## What changes in method, not just volume

- **S**: the owner is strategy, process and governance at once. Do not ask for documents that do
  not exist; score honestly from what is there. Formal process documentation may not be needed at
  this size; a 2 on process is not a failure if the work is consistent and the owner can describe
  it (OneWave tailoring note, adapted).
- **M**: growth often outpaces process documentation and creates data silos between departments;
  look for both. SSO is likely; check it.
- **L**: procurement and vendor due diligence run in parallel; expect a supplier security
  questionnaire before DDD gets document access. An AI council or steering group is a realistic
  recommendation.
- **XL**: security, privacy, legal and procurement must be engaged from week one, not after the
  business interviews. Data classification, DLP, permission-aware retrieval and change management
  dominate the action plan (research B1). Govern by risk tier, not uniformly (Gartner, 26 May
  2026, per research B1).
