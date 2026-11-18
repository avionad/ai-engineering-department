# Industry pack: real estate

*v0.1.0, 2026-11-08. Sales agencies and property managers. Rules point at `../regulatory-register.md`.*

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Listing copy | 1 | No PI; ACL on claims |
| 2 | Virtual staging | 2 | Misleading-image risk; NSW rental disclosure (AU-25) |
| 3 | Tenant enquiry handling | 2 | Applicant PI; discrimination risk in responses |
| 4 | Lease abstraction | 1 to 2 | Commercial terms; tenant PI in residential leases |
| 5 | Tenant application pre-screening `[DDD addition]` | 3 | Substantially and directly related to a tenancy decision (AU-8); discrimination risk |
| 6 | Maintenance request triage and trade dispatch `[DDD addition]` | 2 | Tenant PI; urgency misclassification risk |

## Key risks

- Misleading AI-altered images in listings.
- Over-collection of tenant data.
- Fair housing and discrimination in tenant selection or enquiry handling.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| ACL and state fair trading Acts | AU-22 | In force | Altered images and AI copy must not mislead |
| NSW rental reforms: AI and altered image disclosure | AU-25 | Commenced later, reported from 2027; `PENDING_VERIFICATION` | Build disclosure labels into virtual staging now for NSW rentals; confirm commencement before citing dates or fines |
| NSW tenant data collection limits | AU-25 (context) | `[secondary]` | Collect only what the rules allow |
| ADM disclosure | AU-8 | Commenced later | Applicant scoring or shortlisting |
| Other states | - | Several considering similar rules (research, no detail) | Check per state |

## Controls

- Every AI-altered or virtually staged image labelled; originals kept.
- Tenant application fields limited to what is allowed; no protected attributes or proxies in
  any scoring.
- Human makes every tenancy selection decision; applicant can ask how they were assessed.
- Enquiry agent scripted to give the same information to every enquirer.

## Discovery questions

1. Which states do you list rentals in?
2. Do you use virtual staging or image editing tools, and are edited images labelled?
3. What do tenant applications collect, and through which platform?
4. Does any platform score, rank or filter applicants?
5. How many enquiries and maintenance requests per month, and who handles them?
