# Industry pack: not-for-profit

*v0.1.0, 2026-11-08. Charities, NFPs, member associations. Rules point at `../regulatory-register.md`.*

**Thin by design.** The research has **no NFP-specific AI rule and no NFP row in its industry
matrix.** This pack applies the general rules only. Use cases are all `[DDD addition]`
(practitioner synthesis). Charity regulator expectations and fundraising rules were not researched:
treat any such question as `PENDING_VERIFICATION` and add a register row before citing it.
NFPs often serve vulnerable people, so the screening questionnaire's vulnerable-population
question usually scores here.

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Grant application drafting `[DDD addition]` | 1 | Organisational content |
| 2 | Donor and member communications drafting `[DDD addition]` | 2 | Donor PI; Spam Act consent (overlay) |
| 3 | Volunteer rostering and admin automation `[DDD addition]` | 2 | Volunteer PI |
| 4 | Client intake and service referral assistance `[DDD addition]` | 3 if it decides eligibility; 2 if it only routes to staff | Often vulnerable clients; eligibility is ADM |
| 5 | Impact report and board paper drafting `[DDD addition]` | 1 | Aggregate data |
| 6 | Policy and procedure assistant for staff and volunteers `[DDD addition]` | 1 | Internal documents |

## Key risks

- Vulnerable client data in public tools or offshore services.
- Eligibility or referral decisions made or shaped by software without review.
- Low budget leading to free consumer tools with no data terms.

## Governing rules (general only)

| Rule | Register | Status | What it means |
|---|---|---|---|
| Privacy Act and APPs | AU-6 | In force | Check whether the NFP is an APP entity (the research does not state the threshold; legal adviser confirms) |
| ADM disclosure | AU-8 | Commenced later | Eligibility and intake decisions |
| OAIC AI guidance | AU-11 | Voluntary | No client PI in public tools |
| Spam Act | Overlay | Named in research (retail), no row | Donor email consent |
| Guidance for AI Adoption | AU-4 | Voluntary | Governance baseline, free templates suit NFP budgets |

## Controls

- Sanctioned tool with business data terms, so staff and volunteers have a safe alternative to
  free consumer tools.
- Human makes every eligibility and referral decision for clients.
- Volunteer onboarding includes the acceptable use policy.

## Discovery questions

1. Do you provide services to vulnerable people (children, people with disability, people in
   crisis)?
2. Are you an APP entity under the Privacy Act? (If unsure, flag for legal adviser.)
3. Which free AI tools do staff and volunteers use today?
4. Does any process decide or shape who gets a service?
5. Which funders impose data-handling conditions in grant agreements?
