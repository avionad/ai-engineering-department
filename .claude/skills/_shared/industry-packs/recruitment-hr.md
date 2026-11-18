# Industry pack: recruitment and HR

*v0.1.0, 2026-11-08. Recruiters, labour hire, and the HR function of any business. Rules point at
`../regulatory-register.md`.*

Anti-discrimination law has no AI carve-out: the employer is liable for the tool's output (AU-24).
Screening and shortlisting are likely "significant" decisions under ADM (AU-8).

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | CV screening | 3 | Hiring decisions significantly affect candidates; indirect discrimination risk |
| 2 | Job ad writing | 1 | No PI; check for discriminatory wording |
| 3 | Interview scheduling | 2 | Candidate PI; no judgement |
| 4 | Candidate Q&A | 2 | Candidate-facing; accuracy |
| 5 | HR policy chatbot | 2 | Employee PI in questions; wrong-answer risk on entitlements |
| 6 | Interview note summarisation `[DDD addition]` | 2 to 3 | Recording consent; summaries feed hiring decisions |
| 7 | Rostering and workload allocation `[DDD addition]` | 3 when NSW DWS duties commence | Digital work system affecting workers (AU-21) |

## Key risks

- Indirect discrimination from training data or proxies.
- Solely automated rejection of candidates.
- Workplace surveillance through monitoring or productivity tools.
- WHS digital-work duties (workload, metrics, monitoring) once NSW proclaims them.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| AHRC AI and recruitment compliance checklist | AU-24 | Voluntary (on binding anti-discrimination law) | Disclose AI use; no candidate removed solely by an automated decision |
| Federal and state anti-discrimination Acts | AU-24 (context) | In force | Employer liable for tool output |
| ADM disclosure | AU-8 | Commenced later (10 Dec 2026) | Screening and shortlisting likely significant |
| NSW WHS Amendment (Digital Work Systems) Act 2026 | AU-21 | Commenced later (awaiting proclamation) | Plan now for NSW workers; union inspection right |
| Fair Work Act general protections; state workplace surveillance Acts | Overlay | Named in research, no row | Legal adviser confirms for the client's states |

## Controls

- Human reviews every rejection; no candidate removed solely by automation (AU-24).
- Candidate notice that AI is used, and how to ask for human review.
- Bias testing before go-live and each quarter: outcome rates by group where lawful to measure,
  proxy-variable review.
- Monitoring and productivity tools reviewed against surveillance law and the DWS Act duties.
- Vendor evidence of bias testing for any bought screening tool.

## Discovery questions

1. Which ATS or HR system do you use, and which AI features are switched on (ranking, matching,
   auto-reject)?
2. Can any candidate be rejected without a person looking at their application?
3. Do candidates know AI is used, and can they ask for a human review?
4. Which states are your workers in? (NSW DWS Act, surveillance Acts.)
5. Do you monitor worker productivity, location or communications with software?
6. How many applications per role, and how long does screening take today?
7. Has the vendor shown you any bias testing results?
