# Industry pack: government

*v0.1.0, 2026-11-08. Commonwealth and state agencies, and suppliers to them. Rules point at `../regulatory-register.md`.*

The DTA policy (AU-17) is mandatory for Commonwealth non-corporate entities; suppliers will be
asked for impact-assessment inputs and transparency material. The research names Robodebt as the
lesson for ADM affecting entitlements.

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Correspondence drafting | 2 | Citizen PI; officer sends |
| 2 | FOI triage | 2 to 3 | Affects access rights; 3 if it decides release or exemption |
| 3 | Policy summarisation | 1 | Public or internal documents |
| 4 | Service-centre chat | 2 (3 if it advises on eligibility) | Citizen-facing; entitlement information |
| 5 | Internal knowledge assistant over procedures `[DDD addition]` | 1 to 2 | Classification of source material decides |
| 6 | Grant application pre-screening `[DDD addition]` | 3 | Substantially and directly related to an entitlement decision |

## Key risks

- ADM affecting entitlements without lawful authority or review (Robodebt lesson).
- Transparency failures: no transparency statement, no register entry.
- PROTECTED data processed in services that are not IRAP-assessed.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| DTA Policy for responsible use of AI in government v2.0 | AU-17 | In force (Cth NCEs); twelve-month items fall due ~15 Dec 2026 | Accountable official, transparency statement, use-case register shared with DTA every 6 months, AI impact assessment (high-risk reported to DTA), staff training |
| PSPF; ISM; IRAP for cloud | Overlay | Named in research, no row | Hosting must match data classification; IRAP-assessed services for PROTECTED |
| NSW AI Assessment Framework and other state policies | Overlay | Current version `PENDING_VERIFICATION` | Check the state's current framework before scoping |
| ADM disclosure | AU-8 | Commenced later | Applies to APP entities (agencies covered by the Privacy Act); legal adviser confirms |
| ACSC guidance, Essential Eight | AU-23 | E8 mandatory for many Cth entities | Agent service accounts inherit E8 controls |

## Controls

- AI impact assessment (DTA tool for agencies; `ai-compliance-risk` mode e for suppliers) before
  build for any in-scope use case.
- Transparency statement and register entry drafted alongside the build, not after.
- IRAP-assessed hosting where data is PROTECTED (deployment options in the research B4 table).
- Lawful authority for every automated decision point identified and recorded by the agency.
- Human review and a recourse path for every entitlement-affecting output.

## Discovery questions

1. Is the client a Commonwealth NCE, a corporate entity, a state agency or a supplier?
2. Who is the accountable official for AI, and where is the agency's use-case register?
3. What is the highest data classification the system will touch?
4. Does any output affect a person's entitlements, obligations, permits or access to services?
5. What lawful authority supports each automated step?
6. Which state AI framework applies, and which version?
7. What transparency material has the agency already published?
