# Industry packs (ai-automation department)

*v0.2.0, 2026-11-08. **14 packs.** Owner: ai-manager. Read `../engagement-conventions.md` and
`../regulatory-register.md` first. Every governing rule here points at a register row ID
(AU-8, EU-1 ...). If a pack and the register disagree, the register wins and the pack is fixed.
Where a rule has no register row, the pack says so in the Register column (`Overlay` for a rule
the research named, `No register row` for one it did not) and marks it `PENDING_VERIFICATION`.
A rule with no row is identified as a question for the client's legal adviser, never stated by DDD
as a requirement, a threshold or a deadline, and never filled in from memory.*

## Packs

| File | Industry | Sector rules in the research? |
|---|---|---|
| `finance-banking.md` | Banks, credit, super, financial advice, finance functions in any business | Yes: APRA, ASIC (deepest) |
| `insurance.md` | General and life insurers, brokers | Yes: APRA, ASIC; some items `PENDING_VERIFICATION` |
| `healthcare.md` | Clinics, allied health, hospitals, health tech | Yes: TGA, AHPRA |
| `legal.md` | Law firms, in-house legal | Yes: court practice notes |
| `education.md` | Schools, RTOs, universities, edtech | Yes: Children's Code (proposed), Schools Framework |
| `government.md` | Commonwealth and state agencies and their suppliers | Yes: DTA policy v2.0 |
| `retail-ecommerce.md` | Retail, ecommerce, consumer brands | Yes: ACL, Spam Act |
| `recruitment-hr.md` | Recruiters, labour hire, HR functions in any business | Yes: AHRC checklist, anti-discrimination, NSW DWS Act |
| `manufacturing.md` | Manufacturing, logistics, critical infrastructure | Yes: WHS, SOCI, ACSC OT-AI principles |
| `real-estate.md` | Agencies, property managers | Yes: NSW rental image disclosure (`PENDING_VERIFICATION`) |
| `professional-services.md` | Accounting, consulting, agencies, IT services | **No sector rules in the research**: general rules only |
| `not-for-profit.md` | Charities, NFPs, member associations | **No sector rules in the research**: general rules only |
| `construction-trades.md` | Builders, civil and commercial contractors, trade service businesses | **No construction row in the research matrix**: general rules plus WHS, ACL and NSW DWS overlays. Licensing, the NCC, security of payment and home building rules are **not in the register** |
| `aged-care-ndis.md` | Residential aged care, home care, NDIS and disability providers | Partly: health and sensitive-information rules carry over (AU-6, AU-18, AU-19). **The sector's own rules are not in the register**: Aged Care Quality Standards, NDIS Practice Standards, worker screening and reportable incident obligations are all `PENDING_VERIFICATION` |

## How every pack is structured

1. **High-ROI use cases** (5 to 8) with a **typical risk tier** (conventions section 6). Use cases
   from the research matrix are unmarked; anything DDD added is tagged `[DDD addition]` and is
   practitioner synthesis, not a sourced ROI claim. The research itself says its use cases are
   practitioner synthesis, not sourced ROI figures, so never quote a saving from a pack: get the
   client's own numbers in discovery.
2. **Key risks.**
3. **Governing rules**, each with register row and status.
4. **Controls** (minimum set on top of the tier minimums in conventions section 6).
5. **Discovery questions** specific to the industry (5 to 8), used by `ai-discovery-scoping` and
   the Screen mode of `ai-compliance-risk`.

## Rules every pack inherits (do not repeat per pack)

- **ADM (AU-8, from 10 Dec 2026):** any use case that makes, or does a thing substantially and
  directly related to, a decision that could significantly affect an individual, using their
  personal information, needs privacy policy disclosure. Human review does not exempt it. Run the
  ADM check in `ai-compliance-risk`.
- **Privacy Act and APPs (AU-6), OAIC AI guidance (AU-11, AU-12):** no personal information in
  public consumer AI tools; training or fine-tuning on customer data is limited by APP 3 and 6.
- **ACL (AU-22):** misleading AI claims and chatbot misstatements are covered.
- **Guidance for AI Adoption (AU-4):** voluntary baseline for every organisation.
- **EU AI Act (EU-1, EU-2):** only when the client has EU users, customers or output.
- **"Typical tier" is a starting point.** The Screen mode of `ai-compliance-risk` sets the actual
  tier per project. "Regulated sector" in the Tier 3 definition is applied to the regulated
  activity (advice, credit, clinical, claims, entitlements), not to every task an entity in that
  sector does: an internal policy summariser in a bank is not Tier 3 just because it is a bank.

## Change log

- 2026-11-08 v0.1.0: 12 packs built from the research industry matrix (line ~273) and overlay
  table (section A3); finance enriched from retired `ai-engineer-finance` material, re-checked
  against the research.
- 2026-11-08 v0.2.0: **14 packs.** `construction-trades.md` and `aged-care-ndis.md` added after a
  review found the two largest segments of the Sydney SMB market DDD sells into had no pack.
  Neither has a row in the research industry matrix, so both carry `[DDD addition]` on every use
  case. The aged care and NDIS pack carries a standing warning at the top: the sector's own rules
  are not in the register and are `PENDING_VERIFICATION`, so they go to the client's legal adviser
  rather than being stated by DDD. Rows for both were added to
  `../../ai-agents-automation/references/industry-use-case-library.md`.


**Narrowing the use vs adding controls (2026-11-08).** Controls never lower a tier. Narrowing
the *use* can: if the system is explicitly scoped to reference use (for example, a staff
assistant that refuses patient-specific diagnosis or treatment questions), screen it as scoped,
record the scope boundary in the risk screen, prove the refusal in testing
(`ai-evals-security-testing`), and re-screen the moment the use expands. A clinician looking up a
policy is reference use; using an answer to decide care for a specific patient is not.
