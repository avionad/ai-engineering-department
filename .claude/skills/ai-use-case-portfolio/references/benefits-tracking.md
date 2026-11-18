# Baseline and benefits tracking

*v0.1.0, 2026-11-08. DDD's method. Measurement principles taken from research B1 step 7
("task-level time saved (sampled, not self-reported only), quality and error rates, cost per
task, and business KPIs per use case") and the communication-style rules on decision-focused
reporting.*

## 1. What to measure (same quantities before and after)

| Quantity | How to get it | Notes |
|---|---|---|
| Volume per month | System counts (tickets, invoices, emails, calls, records) | Use the same date window length before and after; note seasonality |
| Time per item | Timed sample: 20 to 30 items timed by the people doing them, or system timestamps (opened to closed) | Self-reported estimates are recorded as such and never used alone |
| Error or rework rate | QA sample, correction logs, credit notes, re-opened tickets | Define what counts as an error before measuring |
| Cycle time | Timestamps from request to completion | Often the benefit customers notice |
| Exception rate (after only) | Items the automation sent to a human | Exceptions cost time; subtract them |
| Support and run effort (after only) | Hours spent maintaining, monitoring, fixing | Subtract from the benefit |
| Run cost (after only) | Tokens, platform, hosting invoices | From invoices, not estimates |
| Loaded hourly cost | Supplied by the client's finance team | Never assumed; PENDING until supplied |

Annual cost of the process = volume x time per item x loaded cost (x 12 if monthly), plus error
cost where the client can price it. Store `baseline` and `actual` in the register as annual AUD
so the script can compare them; keep the component quantities in the review file so the figure
can be recomputed by the R2 verifier.

## 2. Baseline rules

1. Measured **before** build starts, over a window long enough to be representative (agree it;
   four weeks is a common default but not a rule).
2. Signed off by the process owner as a fair picture of the current process.
3. Stored with its date window, method (count, timed sample, timestamps) and who supplied the
   loaded cost.
4. Never revised after go-live to make the result look better. If the baseline was wrong, say so
   in the review and show both figures (a data revision, named as one).

## 3. Monthly benefits review

For each live item:

1. Re-measure the same quantities over the same length of window.
2. Realised benefit = baseline annual cost minus current annual cost, then subtract run cost and
   support effort to give the net figure. Report both gross and net.
3. Compare with the planned range. Name the comparison period exactly ("October 2026 vs the
   baseline window 1 to 28 July 2026").
4. Separate observed results from interpretation ("this suggests") and hypotheses ("one possible
   explanation, needs confirming").
5. Distinguish a real change from month-to-month noise, a learning period after go-live, a volume
   swing, or a tracking problem. A tracking problem is never reported as poor performance.
6. Record adoption: are the people meant to use it actually using it? Low adoption explains low
   benefit more often than poor model quality.
7. Note any risk incident, complaint or near miss, and whether the risk tier still holds.

## 4. Kill and scale

See SKILL.md section 6. Every decision is recorded in the register with the date, who decided,
and the evidence. Killed items keep their row (status `killed`) and a lessons line: what was
learned, what was reused, what would need to change for the idea to come back.

## 5. What not to claim

- Hours "saved" that were not redeployed are capacity released, not cash saved. Say which.
- Do not convert time saved into headcount reduction unless the client has decided that; it
  changes the change-management and consultation picture (see `ai-enterprise-rollout`).
- Do not quote a percentage improvement on a baseline of fewer than a handful of items without
  saying the sample is small.
