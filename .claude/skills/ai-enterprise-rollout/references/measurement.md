# Adoption and value measurement

*v0.1.0, 2026-11-08. Measure set from Internal web research B1 step 7 ("Adoption (weekly active users
per licence), task-level time saved (sampled, not self-reported only), quality and error rates,
cost per task, and business KPIs per use case"); adoption segmentation adapted from GitHub's AI
adoption playbook (CC BY 4.0). Benefits method shared with `ai-use-case-portfolio`.*

## 1. Principles

1. **No invented productivity multipliers.** Never apply a vendor's or survey's "x% faster" to
   the client. Every benefit figure comes from the client's own measured baseline and actuals.
2. **Adoption is a leading indicator, not value.** High use with no workflow change produces
   little. Report adoption and value separately.
3. **Sample, do not rely on self-report.** Time saved is measured by timed samples or system
   timestamps on defined tasks; surveys are context, labelled as perception.
4. **Team and use-case level.** Avoid individual-level productivity monitoring (consultation and
   surveillance considerations, `people-and-change.md` s4).
5. **Risk sits on the same scorecard.** Incidents, near misses and policy breaches are reported
   next to adoption and value, never in a separate document nobody reads.

## 2. Four measure families

| Family | Measures | Source | Cadence |
|---|---|---|---|
| Usage | Active users per licence (weekly and monthly); engaged users (multiple days per month, definition agreed with the client); segmentation into dedicated, occasional and one-off users; seats unused for 30+ days | Vendor admin reports, SSO logs | Weekly to monthly |
| Value | Per use case: baseline vs current time per task (sampled), volume, cycle time, cost per task, business KPI the use case targets; realised benefit gross and net of run cost | `ai-use-case-portfolio` register and reviews | Monthly |
| Quality | Error and rework rates on AI-assisted outputs (sampled QA), escalation and exception rates for automations, user-reported problems | QA samples, error queues, feedback | Monthly |
| Risk | Incidents and near misses by type, DLP events, public-tool uploads detected, policy breaches, agents operating outside their tier, open high findings | Incident log, DLP/CASB, council | Monthly; board quarterly |

GitHub's playbook segmentation is one workable default: dedicated users active 10+ days a month,
occasional 2 to 9 days, one-off 1 day. Agree the thresholds with the client; the trend between
segments matters more than the exact cut-offs.

## 3. Phasing the measures (GitHub playbook pattern)

1. **Breadth** (first months): active and engaged users against seats.
2. **Depth**: segmentation shift, interactions per active user, number of redesigned workflows
   in use.
3. **Business impact**: planned vs actual per use case; correlate adoption with the business
   KPIs per function.

## 4. Cost

Licence cost per active user, platform and token cost per task for automations, and support
effort. Unused seats are reported with a recommendation (reassign, train, or release at renewal).

## 5. Reporting

Monthly scorecard (`../templates/adoption-scorecard.md`) to the program owner and council;
quarterly summary to the executive and board. Comparison periods stated exactly. Separate observed
results, interpretation and hypotheses. A measurement or tracking problem is reported as such,
never as poor performance.
