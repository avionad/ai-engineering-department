# Industry pack: professional services

*v0.1.0, 2026-11-08. Accounting and bookkeeping firms, consultancies, agencies, IT services.
Rules point at `../regulatory-register.md`.*

**Thin by design.** The research has a matrix row for professional services and accounting, and
one for telco and IT services, but **no sector-specific Australian AI rule** beyond a possible Tax
Practitioners Board obligation that is `PENDING_VERIFICATION`. This pack therefore applies the
general rules only. Do not invent professional-body AI rules; if the client is a member of a
professional body, ask for that body's AI guidance and add it as a register row once verified.

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Bookkeeping categorisation | 1 to 2 | Client financial data; human reviews before lodgement |
| 2 | Client email drafting | 2 | Client confidential data; review before send |
| 3 | Proposal generation | 1 | Internal and prospect data |
| 4 | Tax research | 2 | Incorrect advice risk; practitioner verifies |
| 5 | Ticket triage (IT services) | 2 | Customer data in tickets |
| 6 | Knowledge-base agents (IT services) | 2 (3 if they act on client infrastructure) | Agent privilege on infrastructure |
| 7 | Code assistants (IT services) | 2 | Insecure generated code; client code confidentiality |
| 8 | Meeting summaries and action capture `[House addition]` | 2 | Recording consent; client confidential information |

## Key risks

- Client confidentiality breach through public tools.
- Incorrect tax or professional advice reaching a client.
- Agent privilege abuse on client infrastructure; insecure generated code.

## Governing rules (general only)

| Rule | Register | Status | What it means |
|---|---|---|---|
| Privacy Act and APPs; OAIC AI guidance | AU-6, AU-11 | In force / voluntary | Client PI not in public tools |
| ADM disclosure | AU-8 | Commenced later | Only if the firm makes decisions about individuals with software (e.g. client acceptance scoring) |
| ACL | AU-22 | In force | AI-washing in the firm's own marketing |
| Tax Practitioners Board obligations | Overlay | AI guidance `PENDING_VERIFICATION` | Ask a registered agent client what TPB expects; do not assert |
| ACSC guidance, Essential Eight | AU-23 | Voluntary | IT services agents inherit E8 controls |
| Guidance for AI Adoption | AU-4 | Voluntary | Governance baseline |

## Controls

- Review-before-send on every client-facing output (research matrix control).
- Private tenancy with no-training terms for client data.
- Least agency for any agent on client systems: scoped credentials, approval for irreversible
  actions, logging, kill switch (conventions section 2).
- Secure code review of AI-generated code before merge.

## Discovery questions

1. Which professional bodies or registrations apply (TPB, CPA, CA ANZ, other)? Do they publish
   AI guidance you follow?
2. Do engagement letters or client contracts restrict AI use or offshore processing?
3. Which client systems would an agent have credentials for?
4. Where do staff paste client documents today?
5. What volumes (transactions, tickets, proposals) per month, and the time per item?
