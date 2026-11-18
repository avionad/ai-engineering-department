# Use-case qualification and pilot selection

*v0.1.0, 2026-11-08. Gate questions adapted from anthropics/financial-services `ai-readiness`
(Apache-2.0); ranking idea (dollar impact, speed, probability) from the same source. Scoring
scales and DDD rules are our own. See `vendored-provenance.md`.*

## 1. Score each candidate on four things

Use `../templates/use-case-scoring-template.csv`. One row per candidate.

### Value (client's numbers only)

Record the inputs, not just the answer, so the value case can be recomputed:

| Field | Example (Matthew's Timber sales lookup, illustrative structure only) |
|---|---|
| `volume_per_month` | PENDING (Ben said lookups happen; frequency not yet given) |
| `minutes_per_item` | 10-15 plus a phone call (Ben, 2026-10-30) |
| `loaded_hourly_cost_aud` | PENDING (client to confirm) |
| `error_cost_note` | PENDING |
| `revenue_note` | none stated |
| `risk_reduction_note` | none stated |

Current annual cost of the process = volume x time x loaded cost, computed only when all three are
client-supplied. The expected reduction is a range the client agrees is plausible, recorded with
who agreed it. If any input is PENDING, the value cell says `PENDING` and the missing input goes
on the follow-up list. A candidate with PENDING value can still be ranked on the other three
scores, but it cannot be the pilot until its value is known.

Never use: vendor productivity claims, survey averages, the "assume 30-50%" heuristic in the
vendored Anthropic skill, or any percentage the client did not agree.

### Feasibility (1-5)

| Score | Data | Integration | Complexity |
|---|---|---|---|
| 1 | Data does not exist or cannot be shared | No API, no export, vendor will not help | Needs judgement nobody can describe |
| 2 | Exists but scattered and inconsistent | Export only, manual | Many exception paths, undocumented |
| 3 | Exists, mostly consistent, samples supplied | API exists, access not yet granted | Documented process, some exceptions |
| 4 | Clean, consistent, samples tested | API access granted, sandbox available | Clear rules, exceptions known and rare |
| 5 | Clean, structured, already used for reporting | Native connector or tested integration | Single well-defined task |

Take the lowest of the three sub-scores, not the average. A use case is only as feasible as its
weakest leg.

### Risk tier (1-4, from conventions s6)

Provisional until `ai-compliance-risk` confirms. Tier 4 stops the candidate. Tier 3 can proceed
only after the compliance screen and with impact-assessment and human-review lines in scope.

### Time to value (weeks)

Weeks from signed scope to the first measurable result in production-like use (not to "demo").
Estimate from the pattern's effort drivers; flag dependencies that could stretch it (access,
procurement, security review).

## 2. Three gate questions (per candidate)

All three yes = **Go**. Any no = **Wait**, with what unblocks it.

1. **Is the data there?** Can the client produce a clean input for this use case without a
   months-long data project first?
2. **Is there an owner?** A named person who will drive it, not a sponsor who will "support" it.
3. **Can it pilot in about 30 days?** One team, one workflow, mostly existing tools. If the answer
   starts with "first we would need to...", it is not the pilot. (For L/XL, procurement and
   security review time is counted separately and stated, not used to excuse a large pilot.)

Plus DDD's fourth gate: **risk tier assigned and not 4.**

## 3. Pick the pilot

Rank the Go candidates by:

1. Value (client's numbers), ties broken by
2. Time to value (shorter first), then
3. Feasibility (higher first), then
4. Risk tier (lower first).

Then sanity-check the top one:
- Would success be visible to the owner and the people doing the work?
- Does it build something reusable for the next use case (data connection, identity, eval set)?
- Is it boring and valuable rather than flashy? A boring back-office automation with real hours
  beats a customer-facing chatbot with no measured value.

Record the "not doing" list too: candidates that looked good but failed a gate, with the reason.
It stops the same idea being relitigated next quarter.

## 4. Output into the scope

For the chosen pilot, carry forward: the success measure and its baseline (must-ask 2 and 8), the
human-in-the-loop tier (the H1-H4 human-in-the-loop tiers in `../../ai-agents-automation/SKILL.md`: human does with AI suggesting; AI does with human
approving each action; AI does with human sampling; autonomous within hard limits), the provisional
risk tier, and every PENDING item.
