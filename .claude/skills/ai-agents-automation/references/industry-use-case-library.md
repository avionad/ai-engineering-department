# Industry automation and agent use-case library

*v0.2.0, 2026-11-08. Built from the research industry matrix (`ai-dept-web-research-2026-11-08.md`)
and the fourteen packs in `../../_shared/industry-packs/` (construction and trades, and aged care
and NDIS, added 2026-11-08; neither has a row in the research matrix, so every one of their use
cases is `[DDD addition]`). Use cases are practitioner synthesis, not
sourced ROI figures (the research says so). Never quote a saving from this table: get the
client's own numbers in discovery. Risk tier is deliberately not listed here: it lives in the
industry pack and is set per project by `../../ai-compliance-risk` mode (a), so a client never
gets two answers. Items tagged `[DDD addition]` are DDD's own pattern mapping.*

Read the industry pack before using a row: it carries the governing rules (register rows),
key risks and discovery questions.

| Industry (pack) | Automation or agent use case | Pattern | Watch-outs from the pack and matrix |
|---|---|---|---|
| Finance and banking (`finance-banking.md`) | KYC/AML document extraction | Document intake | CPS 230/234 if APRA-regulated; human sign-off on credit and advice |
| | Complaint triage and IDR drafting | Email triage + draft | Drafts reviewed before send; ADM check |
| | Call summarisation | Voice/CRM summary | Recording consent PENDING_VERIFICATION |
| Insurance (`insurance.md`) | Claims intake and triage | Document intake + routing | Human review of denials; explainability records |
| | Underwriting submission extraction | Document intake | Genetic information restriction (instrument PENDING_VERIFICATION) |
| Healthcare (`healthcare.md`) | Referral and discharge letter drafting | Draft for clinician review | Must not cross into diagnosis or treatment suggestion (TGA); health data onshore |
| | Appointment and triage chat | Support agent | Emergency escalation script; avoid voice until sovereign stack |
| | Coding and billing support | Document intake | Sensitive information |
| Legal (`legal.md`) | Matter intake | Form/email triage | Privilege; private tenancy only |
| | Contract clause extraction | Document intake | Citation and source verification step |
| Education (`education.md`) | Admin automation (enrolments, enquiries) | Email triage, document intake | Child privacy (Children's Online Privacy Code, proposed) |
| Government (`government.md`) | Correspondence drafting, FOI triage | Email triage + draft | DTA policy v2.0; IRAP-assessed hosting; entitlement decisions are ADM |
| Retail and ecommerce (`retail-ecommerce.md`) | Customer service agent | Support agent | ACL on chatbot promises; human escalation |
| | Order exception handling `[DDD addition]` | Back-office agent | Refunds and credits behind approval |
| Recruitment and HR (`recruitment-hr.md`) | Interview scheduling | Workflow | Low risk if it never filters candidates |
| | Candidate Q&A | Support agent | No screening decisions in the chat |
| | CV screening | Decision support (P11) | AHRC checklist; no solely automated rejection; bias testing; NSW DWS Act when commenced |
| Manufacturing (`manufacturing.md`) | Supplier document processing | Document intake | IP leakage |
| | SOP and maintenance assistant | Knowledge agent (with `ai-rag-engineering`) | No control of OT equipment by an agent; human override |
| Real estate (`real-estate.md`) | Tenant enquiry handling | Support or voice agent | Tenant data limits; discrimination |
| | Lease abstraction | Document intake | |
| Professional services (`professional-services.md`) | Bookkeeping categorisation | Data enrichment | Review before send; TPB guidance PENDING_VERIFICATION |
| | Client email drafting, proposal generation | Draft for review | Confidentiality |
| | AP invoice capture, reconciliation support `[DDD addition]` | Finance patterns 5 and 6 | Never initiates payment |
| Not-for-profit (`not-for-profit.md`) | Donor and member enquiry triage `[DDD addition]` | Email triage, CRM automation | General rules only (no sector rules in research) |
| Construction and trades (`construction-trades.md`) | Drawing, specification and RFI assistant `[DDD addition]` | Knowledge agent (with `ai-rag-engineering`) | Current revision only, cited in every answer; superseded documents removed from the index, not flagged |
| | Quote and estimate drafting `[DDD addition]` | Pattern 7 quote generation | Prices and dates by rule, never by the model; a person approves every quote. AI-generated numbers are ACL representations |
| | Site diary, variation and defect reports from photos and voice notes `[DDD addition]` | Document intake + draft | Site capture includes workers and the public; variations have contractual effect, so a person signs |
| | Safety documentation drafting (SWMS, toolbox talks) `[DDD addition]` | Draft for review | A competent person owns and signs it; never issued to site directly |
| | Subcontractor invoice and progress claim capture `[DDD addition]` | Document intake | Sole-trader data is personal information; never initiates payment |
| Aged care and NDIS (`aged-care-ndis.md`) | Progress note and shift-report drafting from worker dictation `[DDD addition]` | Draft for review | Sensitive information about a vulnerable person entering the care record; qualified review recorded; recording consent path and sector rules `PENDING_VERIFICATION` |
| | Rostering and shift-fill administration `[DDD addition]` | Workflow | Coordinator approves every roster; algorithmic allocation engages AU-21 for NSW workers |
| | Family and referrer enquiry handling `[DDD addition]` | Support agent | No eligibility, priority, suitability or clinical questions; escalation always visible |
| | Claim and invoice preparation support `[DDD addition]` | Document intake | Never submits, never decides claimability; government programme integrity exposure |
| | Incident report drafting `[DDD addition]` | Draft for review | No AI severity or reportability classification, no step that can delay a report; obligations and timeframes `PENDING_VERIFICATION` |
| | Policy and practice-guidance assistant for staff `[DDD addition]` | Knowledge agent (with `ai-rag-engineering`) | Scoped to reference use; refuses participant-specific care questions, proven in testing; re-screen if the scope expands |
| Any industry `[DDD addition]` | Quote generation | Pattern 7 | Prices by rule, never by model |
| Any industry `[DDD addition]` | CRM record enrichment and hygiene | Data enrichment | APP collection fairness for external sources |
| Telco and IT services (matrix row, no pack) | Ticket triage, knowledge-base agents | Email triage, support agent | Agent privilege on infrastructure; OWASP Agentic; E8 |

When a client's industry has no pack (telco and IT services is in the research matrix but has no
pack yet), use the general rules in `../../_shared/industry-packs/README.md` and note the gap in
the engagement state.
