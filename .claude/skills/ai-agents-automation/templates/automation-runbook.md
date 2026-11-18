<!-- Audience: client operator and DDD support. Plain English. Save as
{client}/created/docs/handover/automation-runbook-{process}-{YYYY-MM-DD}.md. A runbook must let
someone who did not build it keep it running and stop it safely. -->

# Runbook: {automation name}

*Version {n}, {date}. Built by Design Data Dynamics. Agent control spec: {link}.*

## 1. What it does

{Two to four sentences in business terms: what comes in, what it does, what comes out, who
benefits.} It does **not**: {list}.

## 2. Who to contact

| Role | Name | Contact | When |
|---|---|---|---|
| Process owner (daily exceptions) | | | Error queue items, wrong outputs |
| Accountable owner | | | Stopping, restarting, changing what it is allowed to do |
| DDD support | | | Faults, changes, monthly review |
| Client IT | | | Access, credentials, outages of connected systems |

## 3. How to stop it (kill switch)

1. {Exact step.}
2. {Exact step.}
3. Tell {DDD support} and {process owner}.

Items in flight when stopped: {what happens}. How to restart safely: {steps}, including how to
check nothing was processed twice.

## 4. Daily and weekly checks

| Check | How | Expected | If not |
|---|---|---|---|
| Error queue cleared | {location} | Empty or under {n} items older than {n} hours | Work the queue; call DDD if a pattern repeats |
| Ran as scheduled | {dashboard or log} | {n} runs per {period} | Check trigger and credentials |
| Exception rate | {where} | Around {baseline range} | Review recent inputs; raise with DDD |
| Cost to date | {where} | Under {daily cap} | Check for loops or volume spike |

## 5. Monitoring and alerts

| Signal | Threshold | Alert goes to | Response |
|---|---|---|---|
| Run failures | {n in a row} | {channel} | Section 6 |
| Cap breached | Any | {channel} | Automation pauses itself; review before restart |
| No runs | {n hours} | {channel} | Check trigger |
| Approval queue ageing | {n hours} | {channel} | Approver reminded |

## 6. Common problems

| Symptom | Likely cause | Fix |
|---|---|---|
| Nothing processed | Expired credential; trigger mailbox rule changed | {steps} |
| Many items in error queue | New document layout; upstream system change | {steps}; send samples to DDD |
| Duplicate record | {should not happen: idempotency key} | Stop, report to DDD with the record IDs |
| Wrong category or field | Model or prompt issue | Correct it in the queue; log the example for the monthly review |

## 7. Credentials and access

Stored in Doppler (project {name}, config {name}); key names: {list, never values}. Rotation:
{schedule and steps}. Who has admin access to the automation platform: {roles}.

## 8. Changes

All changes go through DDD's change process: request, update the control spec, test in staging,
re-run evals, client approval, deploy, record here.

| Date | Change | Approved by | Eval re-run |
|---|---|---|---|

## 9. Monthly review inputs

Volume, exceptions, approvals, corrections captured, cost, incidents. These feed
`ai-optimisation-llmops` and the portfolio benefits review (`ai-use-case-portfolio`).

## 10. Incidents

Wrong output reaching a customer, data exposure, agent misfire or a security concern follows the
client's AI incident playbook (`ai-governance-program`): stop it (section 3), preserve logs, tell
the accountable owner and DDD, then follow the playbook.
