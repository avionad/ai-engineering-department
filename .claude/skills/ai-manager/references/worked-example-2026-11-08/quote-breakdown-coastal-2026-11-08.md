# Quote breakdown (INTERNAL DRAFT -- not for clients)

Rate $150.00/h ex GST | confidence z=1.0 | overhead 15% | prices end in 100/300/600/700/800

**Unconfirmed hours:** 254.0 h (83% of build effort) rest on facts the client has not confirmed (rows with confirmed=no).

**Unconfirmed retainer hours:** 10.3 h/month of the run-ongoing lines rest on facts the client has not confirmed (rows with confirmed=no).

| Line item | Bucket | Low | Likely | High | Expected h |
|---|---|---|---|---|---|
| Stakeholder interviews (CIO; privacy officer; clinical governance; HR; IT security; procurement; two clinic managers) | discovery-measurement | 10 | 14 | 20 | 14.3 |
| Discovery workshops x2 (assistant; referral intake) incl prep and notes | discovery-measurement | 6 | 8 | 12 | 8.3 |
| Baseline: time to find a policy answer sampled at three clinics | discovery-measurement | 6 | 10 | 16 | 10.3 |
| Baseline: referral intake volume and minutes per referral and rework rate | discovery-measurement | 6 | 10 | 16 | 10.3 |
| Source and permission inventory (SharePoint sites; legacy file share; ACL patterns; identity sync) | discovery-measurement | 8 | 12 | 20 | 12.7 |
| PMS integration feasibility (API; test environment; vendor terms) | discovery-measurement | 4 | 8 | 16 | 8.7 |
| Buy-first comparison: golden subset against Microsoft 365 Copilot | discovery-measurement | 6 | 8 | 12 | 8.3 |
| Use-case qualification; pilot selection; discovery report and solution design brief | discovery-measurement | 8 | 12 | 16 | 12.0 |
| Risk screens confirmed with owner; applicable obligations; ADM check for referral intake | governance-compliance | 6 | 8 | 12 | 8.3 |
| Vendor due diligence for chosen platform (residency; training; incident; exit) | governance-compliance | 4 | 6 | 10 | 6.3 |
| Privacy impact assessment input (client privacy officer owns the PIA) | governance-compliance | 6 | 8 | 14 | 8.7 |
| Permission hygiene and over-sharing review of pilot SharePoint sites | governance-compliance | 8 | 12 | 24 | 13.3 |
| Golden set (100+ real questions) with SME; thresholds agreed; eval baseline | governance-compliance | 12 | 16 | 24 | 16.7 |
| Permission-leak suite (P1-P22) and revocation latency test in sandbox | governance-compliance | 10 | 14 | 20 | 14.3 |
| Threat model and Tier 2 red-team (injection; PII leakage; system prompt; misinformation) | governance-compliance | 10 | 14 | 20 | 14.3 |
| Pilot compliance sign-off checklist | governance-compliance | 3 | 4 | 6 | 4.2 |
| Azure sandbox baseline in Australia East (private networking; logging; Entra app registrations) | config-saas | 8 | 12 | 20 | 12.7 |
| SharePoint connector with ACL capture and delete handling for pilot sites | rag-knowledge | 16 | 24 | 40 | 25.3 |
| Group expansion and revocation design (ADR) for nested Entra groups | rag-knowledge | 6 | 8 | 14 | 8.7 |
| Parsing; OCR and chunking for pilot policy and procedure formats | rag-knowledge | 8 | 12 | 24 | 13.3 |
| Index with security filter; hybrid retrieval; rerank; citations; abstain | rag-knowledge | 12 | 16 | 28 | 17.3 |
| Document clean-up and de-duplication of pilot corpus | integration-workflow | 6 | 10 | 20 | 11.0 |
| Chat UI (Teams or web) with SSO; citation viewer; feedback capture | custom-agent-app | 16 | 24 | 40 | 25.3 |
| Staff communications pack addressing AI concerns plus FAQ | change-training | 4 | 6 | 10 | 6.3 |
| Pilot user training (three sessions) and champion briefing | change-training | 6 | 8 | 12 | 8.3 |
| Runbook and admin handover | change-training | 4 | 6 | 8 | 6.0 |
| Monthly eval rerun; ACL sync lag monitoring; one change set; report | run-ongoing | 8 | 10 | 14 | 10.3 |

| Bucket | Items | Expected h | SD h |
|---|---|---|---|
| config-saas | 1 | 12.7 | 2.0 |
| integration-workflow | 1 | 11.0 | 2.3 |
| rag-knowledge | 4 | 64.7 | 10.7 |
| custom-agent-app | 1 | 25.3 | 4.0 |
| governance-compliance | 8 | 86.2 | 11.8 |
| change-training | 3 | 20.7 | 2.7 |
| run-ongoing | 1 | 10.3 | 1.0 |
| discovery-measurement | 8 | 85.0 | 12.3 |

- Expected effort: **305.5 h** (SD 45.8 h)
- Range if every line hits its low / high: 199 to 474 h (spread 91% of expected)
- Quoted effort (expected + 1.0 SD, SDs summed): **351.3 h**
- Fixed fee: **$60,700 + GST ($66,770.00 inc GST)** (raw $60,605.00 before rounding; excludes run-ongoing lines)
- **This quote already includes paid discovery** and the build hours are uncertain (82% of build hours are unconfirmed (limit 50%)). Fix the price of the discovery lines now; present the build lines as an indicative range and re-run the estimator after discovery to fix them.
- Monthly retainer (run-ongoing lines, expected + 1.0 SD = 11.3 h/month): **$2,100 + GST per month ($2,310.00 inc GST)**
