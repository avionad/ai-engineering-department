# Industry pack: insurance

*v0.1.0, 2026-11-08. General and life insurers, brokers, claims service providers. Rules point at
`../regulatory-register.md`. Several insurance-specific items are `[secondary]` or
`PENDING_VERIFICATION` in the research: keep them as discovery prompts.*

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Claims intake and triage | 3 | Routes or prioritises claims: substantially and directly related to a decision with significant effect (AU-8) |
| 2 | Fraud flagging | 3 | Flags drive investigation and possible denial; significant effect |
| 3 | Policy wording Q&A (customer or staff) | 2 | Customer-facing; misstatement risk under ACL (AU-22) |
| 4 | Underwriting submission extraction | 3 if it feeds pricing or acceptance; 2 if broker-side data entry only | Underwriting decisions significantly affect customers |
| 5 | Claims correspondence drafting with handler review `[House addition]` | 2 | Customer PI; human sends |
| 6 | Internal knowledge assistant for claims handlers over procedures `[House addition]` | 1 to 2 | Internal; 2 if it surfaces customer files |

## Key risks

- Discriminatory pricing; wrongful claim denial.
- Genetic data misuse in life underwriting.
- Opaque ADM: customers cannot see or contest how a system shaped their claim.
- Pricing promises and claims handling under ASIC focus.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| APRA CPS 230 (general and life insurers) | AU-13 | In force | AI vendors as material service providers; critical operations (claims) |
| APRA CPS 234 | AU-14 | In force | Information security over AI assets |
| APRA AI letter | AU-15 | Supervisory expectation | Risk appetite, board literacy, supplier exit, assurance |
| ADM disclosure for pricing, underwriting, claims | AU-8 | Commenced later (10 Dec 2026) | Disclose the kinds of decisions and PI |
| Genetic-information restriction in life underwriting (reported from 8 Oct 2026) | Overlay | `PENDING_VERIFICATION` on instrument | Do not let any model use genetic test results in life underwriting until the instrument is confirmed; legal adviser to confirm scope |
| GICOP re-drafted as legally enforceable (ICA consultation 24 Jun 2026) | Overlay | Proposed `[secondary]` | Treat as direction of travel |
| ASIC focus on AI in claims handling and pricing promises | Overlay ([S&P, Sep 2026](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/9/australia-s-general-insurers-scale-up-ai-as-regulators-urge-risk-management-105349445)) | Supervisory signal | Evidence that pricing and claims AI is fair and explained |

## Controls

- Human review of every claim denial and every fraud flag before customer impact.
- Explainability records: why a claim was routed, flagged or priced as it was.
- Data exclusion list enforced in pipelines (genetic information; protected attributes and
  proxies).
- Disaggregated outcome monitoring for pricing and claims models.
- Customer-facing Q&A grounded only in current policy wording, with escalation to a human.

## Discovery questions

1. Which line of business (general, life, health) and is the entity APRA-regulated?
2. Where does any system score, rank or route claims or applications today?
3. Can a claimant find out that a system contributed to a decision, and contest it?
4. Does any underwriting data include genetic test results or family history?
5. What fraud model is in use, who built it, and how often are its flags overturned?
6. Which external data sources feed pricing, and are any proxies for protected attributes?
7. What does your current privacy policy say about automated decisions?
