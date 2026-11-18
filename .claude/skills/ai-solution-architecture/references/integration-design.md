# Integration design

*v0.1.0, 2026-11-08. House method. Pairs with `ai-agents-automation/references/agent-controls.md`
(idempotency, retries, error queues) and the `n8n-architect` build skill.*

## 1. Entity map: one system of record per entity

For every business entity the solution touches, name the one system that owns the truth. If two
systems both think they own it, the integration will fight itself; resolve ownership with the
client before design continues.

| Entity | System of record | Other systems holding a copy | Sync direction | Frequency | Identifier used to match | Who may write |
|---|---|---|---|---|---|---|
| Customer | {CRM} | {ERP, email platform} | CRM to others | {event / hourly / nightly} | {customer ID; fallback ABN or email} | {roles, automation X (create only)} |
| Supplier invoice | {Accounting} | {Workflow staging} | Workflow to accounting (draft only) | Event | {supplier ID + invoice number} | {automation: draft; AP: approve} |

## 2. Sync rules

- **One direction per field** where possible. Two-way sync needs a conflict rule (last write
  wins, source priority, or human review) written down.
- **Match on stable IDs**, never on names alone. Where only fuzzy matching is possible (supplier
  names on invoices), it is an AI or rules step with a confidence threshold and a review lane.
- **Create vs update**: the automation creates only what it is allowed to create; updates to
  existing records are scoped field by field.
- **Deletes**: never automated without approval; prefer archive or status change.

## 3. Interfaces

| System | Interface | Auth | Scope granted | Rate limits | Sandbox available? | Owner on client side |
|---|---|---|---|---|---|---|
| {system} | {REST API / webhook / export / database view / email} | {OAuth app / service account / API key in Doppler} | {read X, write Y} | {from vendor docs, URL + date} | {yes / no} | {name} |

Systems with no API: record the fallback (scheduled export, email parsing, RPA as a last resort)
and its fragility as an effort driver and a risk.

## 4. Error handling

| Failure | Detection | Handling | Owner |
|---|---|---|---|
| Target system down | Connection error, timeout | Retry with backoff; queue; alert after {n} | Process owner |
| Validation rejected by target | API error response | Error queue with the payload and the reason | Process owner |
| Duplicate event | Idempotency key already seen | Skip and log | n/a |
| Partial multi-step write | Step failure mid-run | Staging then commit, or compensating action defined per step | The practice design |
| Credential expired or revoked | Auth error | Stop, alert, do not retry | Client IT |
| Schema change upstream | Unexpected fields or types | Fail closed to error queue; alert | practice support |

## 5. Data minimisation at each hop

For each interface, list the fields sent and why each is needed. Remove anything the receiving
step does not use, especially before a model call. This feeds the data-flow view and the privacy
check.

## 6. Effort drivers to record

Number of systems; systems without APIs or sandboxes; write access approvals; matching
complexity; two-way sync; volume and rate limits; schema volatility; the client's IT turnaround
for access. Each goes to `ai-proposal-pricing` under `integration-workflow`.
