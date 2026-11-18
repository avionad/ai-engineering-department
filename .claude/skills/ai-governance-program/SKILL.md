---
name: ai-governance-program
description: Use when an organisation needs an AI policy, acceptable use policy, AI council or AI register written, or AI governance set up or improved across the whole business rather than one project. Builds the organisation-level program for this AI automation department, sized from 5 to 500+ staff. Covers AI policy and acceptable use policy, governance charter (owner plus reviewer up to a cross-functional AI council), AI register including shadow AI discovery, ISO/IEC 42001 readiness gap (readiness only, the practice cannot certify), AI literacy plan by role including the board, AI incident response playbook, transparency statement and model card, and ADM-ready privacy policy wording for the legal adviser. Every artefact maps to the Guidance for AI Adoption six practices and cross-maps to ISO 42001 and NIST AI RMF. Australia first; not legal advice.
when_to_use: ai governance, ai policy, acceptable use policy ai, ai aup, ai governance charter, ai council, ai committee terms of reference, ai register, ai inventory, shadow ai, unapproved ai tools, iso 42001, iso 42001 readiness, aims gap analysis, ai literacy training, board ai training, ai incident response, ai incident playbook, ai transparency statement, model card, system card, privacy policy adm wording, guidance for ai adoption, six practices, nist ai rmf alignment, responsible ai program
trigger: ai governance, ai policy, acceptable use policy ai, ai aup, ai governance charter, ai council, ai committee terms of reference, ai register, ai inventory, shadow ai, unapproved ai tools, iso 42001, iso 42001 readiness, aims gap analysis, ai literacy training, board ai training, ai incident response, ai incident playbook, ai transparency statement, model card, system card, privacy policy adm wording, guidance for ai adoption, six practices, nist ai rmf alignment, responsible ai program
version: 0.1.0
---

<!-- Changelog: 2026-11-08 (v0.1.0) -- Phase 1 build per ai-automation blueprint. -->

Read `../_shared/engagement-conventions.md` first (lifecycle, gates, tiers, size bands, legal framing).

# AI Governance Program (organisation level)

You set up the standing machinery that lets an organisation use AI safely at scale: who is
accountable, what the rules are, what AI exists, how staff learn, and what happens when it goes
wrong. The per-project counterpart is `ai-compliance-risk` (screening, obligations, ADM check,
risk register, impact assessment, threat model, vendor DD, sign-off), which this program's
council and register depend on.

## Department relationships

- **Invoked by** `ai-manager` at stage 2 (Govern), or as a standalone engagement (governance
  program, ADM transparency sprint, ISO 42001 readiness).
- **Works with** `ai-compliance-risk` (run by the `ai-compliance-officer` agent): it supplies
  the per-system screens, risk registers and ADM inventory that this program's register and
  council consume. Org-level gaps it finds come back here.
- **Inputs from** `ai-discovery-scoping` (organisation, size band, systems, decision-makers) and
  `ai-readiness-assessment` (the governance dimension score tells you where to start).
- **Hands to** `ai-proposal-pricing` (scope by size band) and Phase 2 `ai-enterprise-rollout` for
  500+ staff change management.

## Where the practice adds value (be honest about this)

The National AI Centre gives basic templates away free (AI policy guide and template, AI register
template, AI screening tool; register row AU-4). Clients should not pay the practice to re-type them. The practice's
value is: **tailoring** to the client's size, tools, data and sector; **ADM mapping** for the
binding APP 1.7 duty from 10 December 2026 (AU-8), which the voluntary frameworks do not cover;
**alignment** so one set of artefacts satisfies the six practices, ISO 42001 readiness and NIST AI
RMF at once; and the **shadow AI discovery** that makes the register true. Every template here is
written to go beyond the generic version in at least one of those four ways.

## Spine: the six practices (AU-4, voluntary)

1 Decide who is accountable. 2 Understand impacts and plan accordingly. 3 Measure and manage
risks. 4 Share essential information. 5 Test and monitor. 6 Maintain human control.

Full artefact-to-framework table: `references/framework-crosswalk.md`.

| Artefact | Template | Practices | ISO/IEC 42001 clause | NIST AI RMF |
|---|---|---|---|---|
| AI policy + acceptable use policy | `templates/ai-policy-and-aup.md` | 1, 3, 6 | 5, 7 | Govern |
| Governance charter / council ToR | `templates/governance-charter.md` | 1 | 5, 9 | Govern |
| AI register incl. shadow AI | `templates/ai-register-template.md`, `references/shadow-ai-discovery.md` | 1, 3, 4 | 4 | Govern, Map |
| ISO 42001 readiness gap | `templates/iso42001-readiness-gap.md`, `scripts/iso42001_readiness_gap.py` | 1-6 | 4-10 | all |
| AI literacy plan incl. board | `templates/literacy-training-plan.md` | 1, 6 | 7 | Govern |
| AI incident response playbook | `templates/incident-response-playbook.md` | 5, 6 | 10 | Manage |
| Transparency statement, model/system card | `templates/transparency-statement-and-model-card.md` | 4, 5 | 7 | Map, Measure |
| ADM privacy policy wording guide | `templates/adm-privacy-policy-wording-guide.md` | 2, 4 | 4, 7 | Govern |

Clause-level ISO references only. Sub-clause numbers in the crosswalk come from a harvested source
and are flagged unverified; **Annex A control IDs are never cited** (harvested sources disagree).

## Playbook

**1. Baseline (week 1).** From discovery and readiness: size band, sector pack, existing policies,
who decides, which AI is known. Pull the governance dimension score. Note whether the client is
APRA-regulated (AU-13 to AU-15), an AFS/credit licensee (AU-16), a Commonwealth agency (AU-17),
or has NSW workers (AU-21): each changes priorities.

**2. Accountability first (practice 1).** Name the accountable executive and pick the charter
structure by size band. Approve one or two sanctioned AI tools at the same time so staff have a
legal alternative before discovery starts (research B1 step 1).

**3. Discover and register (practices 1, 3, 4).** Run the shadow AI method (survey, SaaS and
expense review, browser extensions and in-app AI features, network or CASB where available) and
seed the register. Discovery, not discipline. Any personal data found in public consumer tools
triggers the immediate actions in the method (incl. an NDB assessment with the privacy officer).

**4. Screen what you found.** Every register entry gets a tier via `ai-compliance-risk` mode (a);
every entry with all three ADM limbs goes into the ADM inventory (mode c).

**5. Policy and AUP.** Tailor by size band. Legal commitments section reviewed by the client's
legal adviser.

**6. ADM disclosure (deadline 10 Dec 2026).** Use the wording guide to draft the privacy policy
section from the ADM inventory, marked DRAFT for legal review. Where a process change (e.g. remove
an auto-reject) is better than disclosure, say so.

**7. Literacy.** Role matrix: all staff, managers, power users, builders, privacy/risk/legal,
executive, board (APRA's letter flags board AI literacy, AU-15; DTA mandates staff training for
agencies, AU-17).

**8. Incident playbook.** Integrated with the client's cyber incident and NDB processes, with
AI-specific types (wrong output, data exposure via AI, agent misfire, unfair decision, attack,
deepfake, vendor incident).

**9. Transparency.** Public transparency statement (mandatory for Commonwealth agencies, AU-17;
good practice for everyone; EU Art 50 if EU-facing, EU-1) and a system card per Tier 2+ system.

**10. ISO 42001 readiness (L and XL, or when a customer contract asks).** Evidence inventory, run
the script, review Annex A against the client's own copy of the standard, roadmap. Say plainly:
The practice prepares; only ISO/IEC 42006 certification bodies certify (INT-4).

**11. Operate.** Council cadence, quarterly management review, register review, policy review.
The monthly improvement loop for systems is Phase 3 (`ai-optimisation-llmops`).

## Size bands

| Band | Minimum program | Typical duration |
|---|---|---|
| S | Combined 2-page policy + AUP, owner + reviewer, single-sheet register, one all-staff session, incident one-pager, ADM check | Days, not weeks |
| M | Policy + AUP, working group charter, full register + survey discovery, role training, playbook, transparency statement, ADM wording | A few weeks |
| L | All of M + AI council, procurement-linked vendor DD, CASB/SSE discovery where available, ISO 42001 readiness if asked | One to two months |
| XL | All of L + board-level charter and appetite, champions network, LMS training, system cards for every Tier 2+ system, ISO 42001 readiness roadmap, DTA-format register export for government clients | Program over a quarter or more |

Durations are indicative for scoping conversations only; effort and price come from
`ai-proposal-pricing` (CFO-gated), never from this skill.

## Output conventions

- Client files in `created/docs/security/`, named `{purpose}-{YYYY-MM-DD}.{ext}` (R5).
- Every client-facing compliance artefact carries: **"This assessment identifies regulatory
  considerations for review by your legal adviser. It is not legal advice."**
- Status words every time: In force / Commenced later / Supervisory expectation / Proposed /
  Voluntary. The six practices, ISO 42001 and NIST AI RMF are **voluntary**: write "recommended",
  never "required", unless a binding rule (e.g. DTA policy for an agency) makes it so.
- Facts only from `../_shared/regulatory-register.md`, the industry packs, or a primary source just
  read; otherwise `PENDING_VERIFICATION`, kept out of the client document.
- Client-facing text passes a client-facing tone review; R2 verifier for anything with more than 3
  numbers (e.g. survey results, readiness percentages).
- Log the action to your own engagement activity log.

## Do not

- Do not sell the free government templates as the practice work.
- Do not claim the practice can certify ISO 42001, or predict an auditor's findings.
- Do not install monitoring on client systems for shadow AI discovery without written approval
  and a surveillance-law check.
- Do not write final privacy policy wording as if approved: it is a draft for the legal adviser.
- Do not quote IBM, Gartner or other statistics without source and year (research file has them).

## Known gaps (v0.1.0)

- NAIC templates (policy, register, screening tool) could not be downloaded on 2026-11-08; field
  alignment of the register and policy to them is `PENDING_VERIFICATION`.
- Guidance for AI Adoption Foundations 2026 revision content is `PENDING_VERIFICATION` (AU-4).
- No sector-specific governance variants yet beyond the industry packs; finance (APRA) is the
  first candidate.

Provenance and licences: `references/vendored-provenance.md`.
