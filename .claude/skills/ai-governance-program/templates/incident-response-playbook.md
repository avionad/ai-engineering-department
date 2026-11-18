<!-- Audience: client (incident team, system owners). Save as
created/docs/security/ai-incident-playbook-{client}-{YYYY-MM-DD}.md -->

# AI incident response playbook

*v0.1.0, 2026-11-08. Practices 5 and 6 (AU-4); ISO/IEC 42001 Clause 10 (corrective action);
NIST Manage (MANAGE 3, per harvested source). Research gap list item 9: few SMEs have one; it
links to the Notifiable Data Breaches scheme (AU-6). Integrate with the client's existing cyber
incident plan rather than running a parallel process.*

> This playbook identifies regulatory considerations for review by your legal adviser. It is not
> legal advice. Whether a breach is notifiable is the client's decision with their privacy officer
> and legal adviser.

## What counts as an AI incident

| Type | Example |
|---|---|
| A. Harmful or wrong output reached someone | Hallucinated advice, price, policy or clinical statement given to a customer; AI-drafted letter with false facts sent |
| B. Data exposure via AI | Personal or confidential data pasted into a public tool; a chatbot or retrieval system shows data to someone not entitled to it; prompt injection extracts data |
| C. Agent misfire | Agent sends, spends, deletes or changes records it should not have; runaway loop; cost spike |
| D. Unfair or unlawful decision | Biased outcome detected; solely automated rejection where policy requires human review; ADM undisclosed |
| E. Security attack on AI | Prompt injection, tool poisoning, credential theft from agent configuration, model or vendor compromise |
| F. Deepfake or impersonation | Voice or video impersonation of an executive used for fraud; synthetic content about the organisation |
| G. Vendor incident | AI vendor breach, model change that breaks behaviour, outage of a critical AI service |

## Severity

| Severity | Test | Response time |
|---|---|---|
| Critical | Personal or sensitive data exposed; money moved; safety risk; legal or regulatory exposure likely; public attention | Contain within 1 hour; accountable executive informed immediately |
| High | Wrong output reached customers at scale; agent acted outside limits without lasting harm; vendor incident affecting a Tier 3 system | Contain same business day |
| Medium | Isolated wrong output caught before harm; near miss; policy breach without data exposure | Within 2 business days |
| Low | Quality issue, no external impact | Next review cycle |

Response times are House defaults; set the client's own in the charter.

## Steps

1. **Report.** Anyone can report to {contact / channel}. Reporting early is expected.
2. **Triage** (system owner + IT/security): type, severity, systems, people affected.
3. **Contain.** Use the kill switch or pause the feature; revoke or rotate credentials (agent
   credentials are in the secrets manager, never in files); disable the integration; stop
   outbound sends; preserve logs (prompts, outputs, actions, model version).
4. **Assess data breach.** If personal information may be involved, the privacy officer runs the
   NDB assessment within the client's breach process (AU-6). For APRA-regulated clients, check
   CPS 234 incident notification duties with the risk team (AU-14; specifics not in the practice's register).
5. **Notify.** Internal escalation per severity; affected customers where appropriate; vendor;
   regulators only through the client's legal or privacy lead.
6. **Fix.** Root cause across categories: data, model or vendor change, prompt or retrieval,
   permissions, missing control, human process. Correct the output where possible (contact
   customers who received wrong information).
7. **Learn.** Post-incident review within {10} business days: update the risk register, the
   system's controls, evals (add the failing case to the golden test set), training, and the
   policy if needed. Record in the incident log.
8. **Close.** Accountable owner signs off; register entry updated.

## Incident log fields

`incident_id, date_reported, reporter_role, system_id (AI register), type (A-G), severity,
summary, people_affected, data_involved, contained_at, ndb_assessment (not required / not
notifiable / notified + date), notifications, root_cause_category, corrective_actions, eval_case_added
(Y/N), closed_by, closed_at`

## Ready-made first moves by type

| Type | First move |
|---|---|
| A | Pause the output channel or switch to human-only; identify recipients |
| B | Revoke access, remove data from the tool where possible, request vendor deletion, start NDB assessment |
| C | Kill switch; revoke agent credentials; reverse actions where possible; check spend caps |
| D | Suspend automated step; human re-review of affected decisions; check ADM disclosure |
| E | Isolate the integration; rotate secrets; review logs for other affected sessions |
| F | Verify through a second channel; stop the transaction; inform bank or platform |
| G | Invoke vendor contract terms; switch to fallback process; check exit plan |
