# Go/Wait gates

*v0.1.0, 2026-11-08. Use-case gate adapted from anthropics/financial-services `ai-readiness`
(Apache-2.0). Organisation gate and thresholds are DDD's own. Implemented in
`scripts/readiness_score.py`; change both together.*

## Organisation gate

| Result | Rule |
|---|---|
| **Wait** | Any dimension scored 1 or 1.5 (deal-breaker), OR any dimension has no evidence, OR no candidate use case passes the use-case gate |
| **Go with conditions** | No deal-breakers, at least one use case passes, but one or more dimensions sit at 2 to 2.5. Conditions are the actions that lift those dimensions, and they run alongside the pilot |
| **Go** | Every dimension 3 or above, evidence for all, and at least one use case passes |

A deal-breaker is stated plainly in the report: AI initiatives in that area should not start until
it is addressed (OneWave rule, adopted).

## Use-case gate (per candidate)

All yes means Go; any no means Wait, with what unblocks it.

1. **Is the data there?** A clean input can be produced without a long data project first.
2. **Is there an owner?** A named person who will drive it.
3. **Can it pilot in about 30 days?** One team, one workflow, mostly existing tools.
4. **Risk tier assigned and not 4.** Tier unassigned means Wait until `ai-compliance-risk`
   screens it. Tier 3 additionally needs the compliance screen recorded as done.

## Flags that never block on their own but always rank first

- **ADM (APP 1.7).** If ADM exposure is yes or unknown and the inventory or privacy policy update
  is not done: before 10 December 2026 it is the top action ("commences 10 December 2026"); on or
  after that date it is flagged as a gap against a duty in force. Either way the report carries
  the not-legal-advice line.
- **Shadow AI with personal data** (security and privacy scored 1-2 and staff use public tools
  with business data): top-three action, because OAIC best practice is not to enter personal
  information into publicly available generative AI tools.

## Ranked 90-day action plan (how the script orders actions)

1. P1 Prerequisites: actions attached to deal-breaker dimensions and the flags above.
2. P2 Foundations: actions attached to dimensions at 2 to 2.5.
3. P3 First use cases: Go use cases, ranked by the client's value figure where known, then by
   time to value.
4. P4 Strengthen: actions attached to dimensions at 3 to 3.5.

Within a tier, higher impact first, then lower effort. Impact and effort are the assessor's
judgement, recorded per action in the input file.
