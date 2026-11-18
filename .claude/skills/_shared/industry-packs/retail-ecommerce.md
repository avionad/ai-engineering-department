# Industry pack: retail and ecommerce

*v0.1.0, 2026-11-08. Retail, ecommerce, consumer brands. Rules point at `../regulatory-register.md`.
Marketing is one use case among many here, never the frame (conventions section 1).*

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Product content generation | 1 | No PI; human reviews claims (ACL) |
| 2 | Customer service agents | 2 | Customer PI; promises and refunds; human escalation |
| 3 | Demand forecasting | 1 | Aggregate data; internal decisions |
| 4 | Review summarisation | 1 to 2 | Reviewer PI is minimal; misleading summary risk |
| 5 | Personalised email | 2 | Customer PI; Spam Act consent |
| 6 | Order, returns and stock automation across systems `[House addition]` | 2 | Customer PI; actions with financial effect need limits |
| 7 | Dynamic pricing or buy-now-pay-later eligibility `[House addition]` | 3 | ADM candidate where it significantly affects individuals (research names pricing and credit) |

## Key risks

- Misleading AI claims, AI-washing, or chatbot promises the business then has to honour (AU-22).
- Dynamic pricing fairness.
- Customer data placed in third-party tools without due diligence.
- Child users on consumer platforms (AU-9).

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| Australian Consumer Law | AU-22 | In force | Chatbot statements and AI-generated product claims are the business's statements |
| Spam Act | Overlay | Named in research, no row | Consent and unsubscribe for AI-personalised email |
| ADM disclosure (pricing or credit decisions) | AU-8 | Commenced later (10 Dec 2026) | Disclose if personalised pricing or eligibility significantly affects individuals |
| Children's Online Privacy Code | AU-9 | Proposed | Only if child users |
| OAIC AI guidance | AU-11 | Voluntary | Customer PI not in public tools |

## Controls

- Customer service agent grounded in current policies (returns, warranty, delivery) with a hard
  rule: no promises outside policy; human escalation path always visible.
- Refund and credit actions capped and logged; above the cap, a human approves.
- Human review of product claims (health, safety, origin, sustainability) before publishing.
- Vendor due diligence on every AI tool that receives customer data.

## Discovery questions

1. Which platform (Shopify, other) and which apps already use AI on customer data?
2. What can your customer service tool say or do without a human: refunds, discounts, promises?
3. Does any system set prices or eligibility per customer?
4. Do children use the site or app?
5. How many customer enquiries per month, by type, and what does each cost to handle?
6. Where do customer emails and chat logs end up, and which vendors can read them?
