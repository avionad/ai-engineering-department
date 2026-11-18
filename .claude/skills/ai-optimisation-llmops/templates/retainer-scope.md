<!-- Audience: client decision-maker (via the proposal) and internal. Save as
{client}/created/docs/strategy/ai-retainer-scope-{YYYY-MM-DD}.md
SCOPE ONLY. The monthly fee is produced by ai-proposal-pricing (run-ongoing bucket) and approved by the practice owner. Never write a price here. -->

# Run and improve retainer: scope

*Template v0.1.0 (ai-optimisation-llmops), 2026-11-08.*

**Client:** {client} | **Start:** {date} | **Term and notice:** {set with the practice owner} |
**Fee:** see the quote from ai-proposal-pricing ({path}), not this document

## 1. What the retainer is for

Each month we check whether your AI systems and the workflows around them are getting better or
worse, find the cause, and ship one tested improvement, so the systems keep learning from real use
instead of standing still after launch.

## 2. Fences (every number set per client; "unlimited" is never offered)

| Fence | Included per month |
|---|---|
| Systems in scope (named below) | {N} |
| Scheduled eval cycles (golden set + relevant red-team re-run) | {N} |
| Change sets designed, built in staging, re-tested and deployed | {N} |
| Monthly report and review call | 1 report, {N}-minute call |
| Support hours (questions, small fixes, incident triage) | {H} hours |
| Response time for incidents | {set with the client; not a guarantee until agreed in writing} |
| Model deprecation watch and migration planning | Included for systems in scope; the migration build itself counts as a change set |

Unused hours: {policy set : PENDING}.

## 3. Systems in scope

| System | Purpose | Risk tier | Platform and region | Owner at client |
|---|---|---|---|---|

## 4. Not included (quoted separately)

- New systems, new use cases, new integrations or new user groups.
- Changes that raise the risk tier or need a new compliance sign-off (assessed, then quoted).
- Rebuilds forced by a vendor retirement beyond one change set.
- Content work on the client's source documents (the client's content owner fixes sources).
- Platform, hosting and token costs (see section 6).

## 5. What we need from you

- Read access to traces, usage exports and error queues for the systems in scope.
- Your measured baseline for each process (minutes per task, monthly volume) so we can report
  hours freed against your own numbers.
- A named owner who approves each change in writing before it goes live.
- Notice of process, policy or source-document changes that affect the systems.

## 6. Costs outside the fee

Model tokens, hosting and SaaS seats are paid by you directly where possible (cleaner for data
residency and accountability). Where the practice pays them, they are passed through at cost and shown on
the invoice. We report cost per task each month from the billed amounts.

## 7. How changes go live

Staging build, re-test against your golden set and security tests, your written approval, then
deployment with a rollback ready. Nothing changes in production without your approval.

## 8. Governance

This retainer supports, but does not replace, your organisation's AI governance. Compliance
findings identify regulatory considerations for review by your legal adviser; they are not legal
advice.
