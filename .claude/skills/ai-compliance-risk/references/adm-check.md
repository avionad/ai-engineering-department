# Mode (c) ADM check: APP 1.7 to 1.9

*v0.1.0, 2026-11-08. Source rows: AU-8 (and AU-6) in `../../_shared/regulatory-register.md`.
Primary references: [OAIC APP 1 guidelines](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information),
[Allens on the OAIC guidance, Oct 2026](https://www.allens.com.au/insights-news/insights/2026/10/mandatory-automated-decision-making-disclosure-requirements-are-coming-key-takeaways-from-the-oaic-guidance/),
[Gilbert + Tobin](https://www.gtlaw.com.au/insights/automated-decision-making-transparency-under-the-privacy-act).
Date checked 2026-11-08.*

## The rule in one paragraph

From **10 December 2026**, an APP entity's privacy policy must disclose automated decision-making
when all three limbs below are met. Status: **commenced on a later date** (POLA Act 2024, Royal
Assent 10 Dec 2024). The duty catches everyday software, not only "AI".

**Primary source for everything in this file** (read 2026-11-08, quotations verbatim): OAIC,
*APP 1.7-1.9 Transparency Obligation Fact Sheet*, September 2026, https://www.oaic.gov.au/__data/assets/pdf_file/0021/269013/APP-1.7-1.9-Transparency-Obligation-Fact-Sheet.PDF

Four propositions, each quoted from that fact sheet, because clients and their lawyers will test
them:

1. **Commencement.** "Changes to privacy obligations for APP entities come into effect on
   10 December 2026."
2. **Human review does not automatically take a tool out of scope.** "A decision may be within
   scope of the transparency obligation even where a computer program output does not replace the
   entire decision-making process or is subject to human review." Advisory outputs count:
   "A computer program may be substantially and directly related to making a decision regardless
   of whether the nature of the output is advisory or determinative."
3. **But there is a qualified exception, and it must not be overstated.** The OAIC "considers
   machine learning or generative AI outputs used to make decisions that significantly affect the
   rights or interests of individuals would generally fall within scope of the transparency
   obligation **unless subject to extensive human oversight and control**." The fact sheet's own
   Example 3 shows what can tip a tool out of scope: staff "interrogating outputs, conducting
   further review of individual key performance indicators behind the decision, setting
   [the tool's] decision parameters more narrowly" and "documenting the reasoning why it diverged
   from the recommendation of the computer program" "could indicate that the output was not
   substantially related to the making of an individual decision". So the correct advice is never
   "a human signs off, so you are exempt", and never "human review is irrelevant" either. It is:
   routine sign-off on a recommendation keeps you in scope; genuine, documented, independent
   reconsideration may take you out, and that judgement is for the client's legal adviser on their
   facts.
4. **Who discloses when a vendor's software does it.** "The OAIC generally expects that APP 1
   transparency obligations typically remain with the APP entity who is using personal information
   to make a decision or do a thing that significantly affects the rights or interests of an
   individual." Vendors "should provide clear, high-level information about how their software can
   be used to make decisions to enable the APP entity to include appropriate information in their
   APP 1 privacy policies." So where a client uses a vendor's software, the client discloses and we
   ask the vendor for the detail it owes them. Note the limit of this answer: the fact sheet covers
   the vendor-software case, not the case where one APP entity runs the program on another APP
   entity's behalf (the agency/employer scenario) -- that split remains PENDING_VERIFICATION; see
   the traps section below.

Definitions, verbatim: "**Substantially** means where it is a key factor in facilitating the
human's decision making; and **Directly** means where the thing has a direct connection with
making the decision."

A comparison with GDPR Article 22 is **not** made by the OAIC fact sheet. It appears only in law
firm commentary, so treat it as `[secondary]` and do not put it to a client as settled.

## The three-limb test (apply per system, per decision type)

| Limb | Test | How to evidence it |
|---|---|---|
| 1. Program and decision | The entity has arranged for a computer program to make a decision, or to do a thing that is **substantially and directly related to making** a decision | Map the decision flow: what the program outputs (score, rank, flag, recommendation, draft outcome) and who acts on it |
| 2. Significant effect | The decision could reasonably be expected to **significantly affect the rights or interests** of an individual | Name the decision and the effect on the person (access to credit, insurance, a job, a tenancy, care, an entitlement, a price) |
| 3. Personal information | **Personal information** about the individual is used in the operation of the program | List the PI fields the program reads |

All three Yes = in scope. Record each limb's answer and reasoning, even when the answer is No:
the record is what shows the client did the analysis.

Common traps:
- "A person signs off, so it is not automated." Wrong test. Ask whether the program's output is
  substantially and directly related to the decision; a reviewer who routinely accepts the score
  does not break the link. The opposite overstatement is also wrong: extensive human oversight and
  control CAN take a tool out of scope (see proposition 3 and the fact sheet's Example 3). Record
  which of the two situations the client is in, with evidence, and leave the conclusion to their
  legal adviser.
- "It is just a spreadsheet." Formula-driven eligibility or scoring sheets are computer programs.
- "The vendor does it." Vendor-embedded ADM (ATS auto-reject, CRM lead scoring that gates
  service, fraud scoring) is the client's arrangement. Inventory vendor features too.
- "We rank on behalf of our client." When one business (for example a recruitment agency)
  runs the program and another (the employer) makes or relies on the decision, both may hold
  APP 1.7 obligations for their own handling. Who must disclose what is PENDING_VERIFICATION:
  record both parties in the inventory and flag it to each party's legal adviser.

## What the privacy policy must say

For in-scope systems, the policy discloses:
1. The **kinds of personal information** used in the operation of the programs.
2. The **kinds of decisions made solely by** the operation of the programs.
3. The **kinds of decisions for which a thing substantially and directly related to making the
   decision is done** by the operation of the programs.

"Kinds", not a per-system list, but specific enough that an individual can understand what
happens to them. DDD drafts wording for the client's legal adviser to review: see
`../../ai-governance-program/templates/adm-privacy-policy-wording-guide.md`.

**Not established by the research, do not assert:** the penalty or infringement-notice exposure
for a non-compliant policy (`PENDING_VERIFICATION`), and any OAIC-prescribed wording or format.

## Procedure

1. **Inventory.** List every system and spreadsheet that touches decisions about individuals,
   including vendor features (pull from the client's AI register if one exists; otherwise build
   one, `ai-governance-program`).
2. **Decision map.** For each, name the decision types it touches.
3. **Three-limb test** per decision type. Record Yes/No and reasoning.
4. **Classify** each in-scope decision type: *made solely by the program* or *program does a thing
   substantially and directly related*.
5. **Collect the PI kinds** used across in-scope systems.
6. **Gap check** against the current privacy policy.
7. **Draft wording** for legal review; list systems where the better answer is to change the
   process (e.g. remove an auto-reject) rather than disclose it.
8. **Hand over** a table the client's privacy officer can maintain when systems change.

## Output table (`adm-inventory-{client}-{YYYY-MM-DD}.md`, in `created/docs/security/`)

| System | Vendor or built | Decision type | Limb 1 | Limb 2 | Limb 3 | In scope | Solely automated or substantially related | PI kinds used | Current policy covers it? | Action |
|---|---|---|---|---|---|---|---|---|---|---|

Close with the legal disclaimer (conventions section 4) and the date the policy update must be
live: 10 December 2026.
