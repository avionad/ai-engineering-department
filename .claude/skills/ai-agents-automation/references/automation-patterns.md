# Automation patterns

*v0.1.0, 2026-11-08. Deepens the solution patterns in
`../../ai-discovery-scoping/references/solution-patterns.md` (P1, P3, P5, P6, P8) at build level.
Deployment and residency choices stay in that file's deployment reference and with the
`ai-architect` agent. No vendor features or prices are stated here; check vendor docs at design
time (R1).*

Every pattern below shares the same skeleton: **trigger, intake, AI step with fixed schema,
validation rules, human lane, action with scoped credential, log, error queue.** What differs is
where the AI sits and which actions need approval.

## 1. Document intake (P1)

Supplier invoices, delivery dockets, purchase orders, application forms, claims, identity
documents.

- **Trigger**: dedicated mailbox, upload form, watched folder, scanner output.
- **Rules first**: identify sender by address or ABN; reject unsupported file types; de-duplicate
  by file hash (idempotency).
- **AI step**: OCR or layout parsing, then extraction to a fixed schema per document type.
- **Validation**: totals and GST add up; supplier exists; PO number matches an open PO; dates
  plausible; confidence per field.
- **Human lane**: anything failing validation or below confidence goes to a review queue with the
  document and the extracted fields side by side.
- **Action**: create a draft record in the system of record. Posting stays a human step until the
  eval on the client's own sample supports auto-posting and the owner approves it.
- **Eval set**: real documents from the client (with permission), covering every layout and the
  ugly scans.

## 2. Email triage

Shared inboxes (info@, accounts@, support@) where someone reads, sorts and forwards everything.

- **Rules first**: known senders, auto-replies, newsletters and spam filtered by rule.
- **AI step**: classify intent and urgency against the client's own category list; extract key
  fields (order number, customer); optionally draft a reply.
- **Validation**: category must be in the list; confidence threshold; "unsure" lane.
- **Action**: label, route to a queue or person, create a ticket or CRM activity. Drafted replies
  are saved as drafts for a human to send (H2) until the eval and owner allow otherwise.
- **Watch for**: prompt injection in inbound email (LLM01:2026, ASI01): email content is untrusted
  input and must never be able to change the routing rules or trigger tools beyond the
  allow-list.

## 3. CRM automation

Lead capture, de-duplication, activity logging, follow-up tasks, pipeline hygiene.

- **Rules first**: form-to-CRM mapping, assignment rules, stage-based tasks; most CRMs do this
  natively, so check the client's existing tool before building.
- **AI steps**: summarise calls or emails into the CRM record; classify lead type; draft
  follow-ups; suggest next action.
- **Action**: write notes and tasks (low risk, H3 or H4 once proven); changing stage, owner or
  value is H2 until proven; never send to a customer without approval at first.
- **Data**: personal information. Tier 2 minimum. Check that the CRM vendor's AI features and
  any external model are covered by the data-handling agreement.

## 4. Data enrichment (P6)

Cleaning, classifying, de-duplicating and enriching CRM records, product catalogues, supplier
lists. The practice's own CRM enrichment pipeline is the working reference.

- **Batch, not real time**, where possible: cheaper and easier to sample (research B6 notes
  batch pricing as a cost lever; check the vendor's current terms).
- **Staged write-back**: results go to a staging table or field, sampled by a human, then
  written; every change keeps the old value so it can be undone.
- **External sources**: confirm the terms of every data source and whether collection is fair
  under the APPs (register AU-6) before enriching personal records.

## 5. AP invoice capture (finance)

Pattern 1 applied to accounts payable, with finance controls on top.

- **Matching**: two-way (invoice to PO) or three-way (invoice, PO, receipt) by rule; AI only for
  fuzzy supplier and line matching.
- **Controls**: duplicate invoice check (supplier + number + amount); bank detail changes never
  accepted from an invoice or email (payment redirection fraud is a known pattern; route to a
  verified call-back process); approval limits per the client's delegation of authority.
- **Action**: create the bill as draft in the accounting system; approval and payment stay with
  the client's existing approvers. The automation never initiates a payment.
- **Owner**: the AP lead owns the exception queue.

## 6. Reconciliation support (finance)

Preparing, not deciding: matching bank lines to ledger entries, explaining variances, drafting
journals for review.

- **Rules first**: exact matches by amount, date window and reference.
- **AI step**: suggest matches for the remainder with reasons; group related lines; draft an
  explanation of unmatched items.
- **Action**: suggestions only (H1 or H2). Posting a journal or accepting a match is a human
  action in the accounting system. Every suggestion logged with what it was based on.
- **Accountant coordination**: the client's accountant or finance lead approves the method
  before go-live.

## 7. Quote generation

Turning a request (email, form, site measurements, call notes) into a priced quote.

- **Rules**: prices, margins, discounts and terms always come from the client's price list or
  system by lookup or formula, **never generated by the model**.
- **AI steps**: read the request, extract quantities and options, map to price-list items,
  draft the covering text, flag missing information.
- **Validation**: every line maps to a real price-list item; totals recalculated by rule; margin
  floor check.
- **Action**: draft quote for a human to review and send (H2). Customer-facing and binding once
  sent, so approval stays until the owner decides otherwise.

## 8. Customer support agent (P3)

Text chat or email agent answering from approved knowledge, with handoff.

- Knowledge from `ai-rag-engineering` (public-safe or customer-scoped sources only).
- Hard limits: no promises on price, refunds, legal or medical matters unless a rule-backed tool
  provides the answer; misstatements are covered by the ACL (register AU-22).
- Handoff to a human on request, low confidence, complaint, vulnerability signals, or repeated
  failure. The handoff carries the transcript.
- AI disclosure at the start of the conversation.

## 9. Agentic back-office (P8)

Multi-step work where the path varies: vendor onboarding, order exception handling, scheduling.
Only where a fixed workflow cannot cope. Full least-agency controls (`agent-controls.md`) and a
threat model against ASI01-ASI10 before build. Tier 2 minimum; tier 3 if it spends money, acts
externally or affects people.

## 10. Voice agent (P4)

See `voice-agents.md`.
