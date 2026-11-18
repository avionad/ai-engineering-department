# Industry pack: finance and banking

*v0.1.0, 2026-11-08. Covers banks, credit providers, super funds, financial advisers, and the
finance function of any business. Rules point at `../regulatory-register.md`. Enriched from the
retired `ai-engineer-finance` skill (2026-08 material); anything from it not in the research is
tagged `[retired DDD material, not re-verified]`.*

**This is where enforcement teeth are.** APRA's AI letter (AU-15) says boards lack AI literacy,
AI widens the cyber attack surface, entities depend on single AI suppliers and assurance lags
adoption, and signals stronger supervisory action and, where appropriate, enforcement.

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Complaint triage and IDR response drafting | 2 (3 if it decides outcomes) | Customer PI; human sends; becomes ADM if it routes or resolves complaints without review |
| 2 | KYC/AML document extraction | 3 | Feeds onboarding decisions that significantly affect customers; regulated activity |
| 3 | Adviser file notes and SOA drafting | 3 | Regulated advice; human adviser must own the advice |
| 4 | Call summarisation | 2 | Customer PI and recording consent; output used by staff |
| 5 | Credit memo drafting | 3 | Substantially and directly related to a credit decision (AU-8) |
| 6 | AP invoice coding suggestions with human review `[DDD addition, from retired material]` | 1 to 2 | Internal; supplier PI only if sole traders |
| 7 | AR collection email drafts, human review before send `[DDD addition, from retired material]` | 2 | Customer PI; outbound communication |
| 8 | Month-end variance explanation drafts from accounting exports `[DDD addition, from retired material]` | 1 | Internal, no PI if exports are masked |

Reject-list (from retired material, still sound practice): automated journal posting without
human review; any communication to the auditor, ATO or a major customer without human review;
accounting-standard judgements (lease, revenue recognition) handed to AI.

## Key risks

- Unfair or biased credit outcomes; unlicensed advice via a chatbot.
- Third-party concentration on one AI supplier with no tested exit or substitution plan (AU-15).
- Prompt injection, data leakage and agent misuse on customer channels (AU-15 cyber area).
- No contestability arrangements and no AI-disclosure policy (AU-16 found none of 23 licensees
  had contestability arrangements).
- Override culture: staff bypass the reviewed workflow after a few months `[retired DDD material]`.

## Governing rules

| Rule | Register | Status | What it means for the project |
|---|---|---|---|
| APRA CPS 230 | AU-13 | In force | AI vendor may be a material service provider: register it, tolerance levels, BCP, exit plan |
| APRA CPS 234 | AU-14 | In force | AI system is an information asset: classify, control, test |
| APRA AI letter | AU-15 | Supervisory expectation | AI risk appetite, board literacy, AI cyber controls, supplier exit tested, assurance |
| ASIC REP 798 | AU-16 | Supervisory expectation | Governance before scale, contestability, bias and fairness policy, AI disclosure, third-party oversight |
| APRA/ASIC frontier AI statement | AU-26 | Supervisory expectation (`PENDING_VERIFICATION`) | Cite title only until verified |
| ADM disclosure | AU-8 | Commenced later (10 Dec 2026) | Credit, KYC and complaint routing are prime ADM candidates |
| CPG 230, "efficiently, honestly and fairly", DDO, anti-discrimination in credit | Overlay (no row) | Named in research, not row-verified | Discovery prompts; legal adviser confirms |
| ATO recordkeeping, AUSTRAC AML/CTF program, ASIC audit, AASB judgements | none | `[retired DDD material, not re-verified]` `PENDING_VERIFICATION` | Ask about them in discovery; do not cite specifics (e.g. retention periods) until verified |

## Controls

- Human sign-off on every advice, credit and complaint-outcome decision; documented
  contestability path for customers.
- Material service provider assessment for the AI vendor; exit and substitution plan tested,
  not just written (vendor due diligence in `ai-compliance-risk`, mode g).
- Board AI literacy session (governance program literacy plan) where APRA-regulated.
- Bias testing on credit and complaint models; disaggregated results kept as evidence.
- Prompt injection and data leakage tests before go-live on any customer channel.
- Audit trail: inputs, model version, output, reviewer and decision for every Tier 3 use.

## Discovery questions

1. Are you APRA-regulated, an AFS or credit licensee, or neither? (Decides AU-13 to AU-16.)
2. Which AI tools touch customer data today, including ones staff use without approval?
3. Which decisions about customers (credit, onboarding, complaints, hardship) does any system
   influence, even as a score or a draft? (ADM map.)
4. Is any AI vendor already on your material service provider register? Has its exit plan been
   tested?
5. How would a customer challenge an outcome that a system contributed to today?
6. Who on the board has had AI risk briefing, and when?
7. Do you have AUSTRAC, ASIC reporting or statutory audit obligations that the workflow touches?
   `[from retired material]`
8. Any contractual data residency clauses that stop data leaving Australia? `[from retired material]`
