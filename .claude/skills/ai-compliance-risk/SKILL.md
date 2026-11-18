---
name: ai-compliance-risk
description: Use when any AI or automation project needs to know what rules apply and how risky it is. Project-level compliance and risk for DDD's ai-automation department, Australia first. Screens the project into a risk tier (1 Low to 4 Stop) with a scored questionnaire, lists applicable obligations with status and source from the regulatory register and industry pack, runs the APP 1.7-1.9 automated decision-making check (10 Dec 2026), builds a per-project risk register seeded from CoSAI and NIST AI 600-1, structures an AI impact assessment, threat-models against OWASP LLM and Agentic Top 10 and MITRE ATLAS, issues a vendor due diligence questionnaire, and runs the pre-go-live compliance sign-off. Identifies obligations for the client's legal adviser; never gives legal advice.
when_to_use: ai risk assessment, ai compliance check, what rules apply to this ai project, risk tier, ai screening, adm check, automated decision making disclosure, app 1.7, privacy policy adm, ai risk register, ai impact assessment, iso 42005, threat model ai, owasp llm, owasp agentic, mitre atlas, prompt injection risk, ai vendor due diligence, vendor questionnaire ai, cps 230 ai vendor, compliance sign-off, go-live sign-off ai, is this ai project high risk
trigger: ai risk assessment, ai compliance check, what rules apply to this ai project, risk tier, ai screening, adm check, automated decision making disclosure, app 1.7, privacy policy adm, ai risk register, ai impact assessment, iso 42005, threat model ai, owasp llm, owasp agentic, mitre atlas, prompt injection risk, ai vendor due diligence, vendor questionnaire ai, cps 230 ai vendor, compliance sign-off, go-live sign-off ai, is this ai project high risk
version: 0.1.1
---

<!-- Changelog: 2026-11-09 (v0.1.1) -- adm-check proposition 4 aligned to trap 4: the fact sheet
answers the vendor-software case, not the two-APP-entity agency/employer split, which stays
PENDING_VERIFICATION; risk-catalogue and threat-model OWASP IDs re-mapped to the 2026 edition. -->
<!-- Changelog: 2026-11-08 (v0.1.0) -- Phase 1 build per ai-automation blueprint. -->

Read `../_shared/engagement-conventions.md` first (lifecycle, gates, tiers, size bands, legal framing).

# AI Compliance and Risk (project level)

You work out, for one AI project, **what applies and how risky it is**, then prove the controls
exist before go-live. Compliance and risk management is the main focus of the department, and
this skill is its engine. The organisation-wide counterpart (policy, council, AI register, ISO
42001 readiness, training) is `ai-governance-program`.

## Department relationships

- **Invoked by** `ai-manager` at stage 2 (Govern) and stage 6 (Verify) of the lifecycle.
- **Run by** the `ai-compliance-officer` agent (read-only, reports findings ranked by severity).
- **Inputs from** `ai-discovery-scoping` (use case, data, users, systems, the client's numbers)
  and `ai-readiness-assessment` (governance maturity). Architecture and data-flow diagrams come
  from the `ai-architect` agent.
- **Hands to** `ai-governance-program` (org gaps found here, e.g. no AI register, no AUP),
  `ai-proposal-pricing` (tier drives scope and effort), and Phase 3 security testing (every High
  threat becomes a named test).

## Ground truth (R1)

1. The client's own documents and statements.
2. `../_shared/regulatory-register.md` (row IDs AU-1 ... UK-1) and `../_shared/industry-packs/`.
   Any row older than 60 days is re-verified before it appears in a client deliverable.
3. Live primary sources (conventions s3).

Never assert a regulation, clause, date, figure or status from memory. If it is not in the
register, a pack, or a primary source you have just read, write `PENDING_VERIFICATION` and keep it
out of the client document. Distinguish **In force / Commenced later / Supervisory expectation /
Proposed / Voluntary** every time. Never call voluntary guidance a requirement.

## Modes

Run (a) first on every project. Then (b) and (c) always; (d) for Tier 2 and above; (e) and (f)
for Tier 3; (g) whenever a third-party AI product touches client data; (h) before go-live.

| Mode | Does | Detail | Output file (client `created/docs/security/`) |
|---|---|---|---|
| a Screen | Assign the risk tier | `references/screening-questionnaire.md` | `ai-risk-screen-{project}-{date}.md` |
| b Applicable obligations | List every rule that applies, with status and source | Below + `templates/applicable-obligations-template.md` | `applicable-obligations-{project}-{date}.md` |
| c ADM check | APP 1.7-1.9 three-limb test and disclosure gap | `references/adm-check.md` | `adm-inventory-{client}-{date}.md` |
| d Risk register | Per-project register, scored | `references/risk-catalogue.md`, `scripts/ai_risk_register.py` | `ai-risk-register-{project}-{date}.csv` + `.md` |
| e Impact assessment | ISO/IEC 42005-aligned structure | `templates/impact-assessment-template.md` | `ai-impact-assessment-{project}-{date}.md` |
| f Threat model | OWASP LLM + Agentic IDs, ATLAS techniques | `references/threat-model.md` | `threat-model-{project}-{date}.md` |
| g Vendor due diligence | Questionnaire with gate questions | `templates/vendor-due-diligence-questionnaire.md` | `ai-vendor-dd-{vendor}-{date}.md` |
| h Sign-off | Pre-go-live checklist by tier | `templates/compliance-signoff-checklist.md` | `compliance-signoff-{project}-{date}.md` |

### (a) Screen

Stop questions (any Yes = Tier 4), then floor questions (the three ADM limbs together set Tier 3;
autonomous action and regulated activity set Tier 3; personal data, customer-facing and
vulnerable users set Tier 2), then a 16-item impact score out of 54 for everything else. Final
tier = highest of the three. Mitigation answers are recorded but **never lower the tier**:
controls reduce residual risk in the register, the tier says which controls are mandatory.
Bands are DDD v0.1 and uncalibrated: record every score so they can be tuned after five projects.

Tier 4 is not argued in the meeting. Record it, explain it plainly, offer a lawful alternative.

### (b) Applicable obligations

1. **Jurisdictions.** Australia always. EU only if the client has EU users, customers or output
   used in the EU (EU-1, EU-2, EU-3). NZ and UK briefly if the client operates there (NZ-2 Privacy Act 2020 incl. IPP 3A is binding law whenever NZ individuals are involved; NZ-1 and UK-1 are voluntary).
   Record who confirmed the jurisdictional facts.
2. **Walk the register top to bottom.** For each row decide: applies / does not apply (one-line
   reason) / cannot tell (question for the client). General rows that almost always apply to an
   Australian business: AU-6, AU-8 (if ADM), AU-11, AU-22, AU-4 (voluntary).
3. **Walk the industry pack** governing-rules table. Overlays without a register row are listed
   as "named in research, not row-verified" and go to the legal adviser as questions.
4. **Size band and entity type** change what applies: APRA-regulated (AU-13 to AU-15), AFS or
   credit licensee (AU-16), Commonwealth agency (AU-17), NSW workers (AU-21).
5. **Rank** in-force first, then commenced-later by nearest date, then supervisory expectations,
   then proposed (direction of travel), then voluntary (recommended).
6. **Unverifiable items** go in their own section and are not relied on.

### (c) ADM check

Three limbs, per system and per decision type: (1) a program makes the decision or does a thing
substantially and directly related to it; (2) the decision could reasonably be expected to
significantly affect an individual's rights or interests; (3) personal information is used. All
three = disclose in the privacy policy from **10 December 2026**: kinds of PI, kinds of decisions
made solely by the program, kinds where the program does a thing substantially and directly
related. **Human review does not exempt** a tool whose output materially influences the decision.
Spreadsheets and vendor features count. Penalty exposure is `PENDING_VERIFICATION`: do not quote
one. Wording is drafted for the legal adviser via `ai-governance-program`'s wording guide.

### (d) Risk register

```bash
# 1. Seed from architecture flags (genai, third_party_model, personal_data, adm,
#    decisions_about_people, customer_facing, generates_content, rag, agent,
#    fine_tune, self_hosted, shadow_agents)
python3 scripts/ai_risk_register.py seed project.json -o seeded.json
# 2. Score likelihood/impact 1-5, add controls, owner, residual with the client
# 3. Build
python3 scripts/ai_risk_register.py build seeded.json --csv out.csv --md out.md
```

The build flags: risks with no owner; risks whose control count is below what the rating needs;
and **tier-minimum controls not yet evidenced** (conventions s6). A Tier 3 project without ADM
satisfies "adm disclosure" by listing `ADM disclosure: not applicable (ADM check {date})` in
`project_controls`. Ratings: 1-4 Low, 5-9 Moderate, 10-16 High, 17-25 Critical (stop and escalate
to the client's accountable owner). Add the Australian rows from `risk-catalogue.md` section 3
and the industry pack's key risks by hand; the seed is a start, not the register.
Worked example: `scripts/samples/` (fictional retailer, Tier 3 refund agent, 21 risks).

### (e) Impact assessment

Mandatory for Tier 3. Nine sections: scope and timing, system description, data, affected
stakeholders, impact analysis, legal considerations, measures, residual impact and decision,
monitoring and review. Aligned in structure to ISO/IEC 42005:2025 (INT-3); **no clause numbers
cited** because the standard's text has not been verified. Commonwealth agencies use the DTA tool
(AU-17); the template supplies their inputs.

### (f) Threat model

Architecture diagram with trust boundaries from `ai-architect`, then walk LLM01-LLM10, ASI01-ASI10
(agents only) and the ATLAS 2026.10 technique table. **OWASP is CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/): IDs only, our
own words.** ATLAS IDs come from the 2026.10 table in the reference, not from CoSAI's v5.0.1 mapping
(some of those IDs no longer exist). Every High threat gets a named test before go-live.

### (g) Vendor due diligence

36 questions in 11 sections. Gate sections (residency, training on customer data, incident
notification, and exit and substitution for APRA-regulated or critical use) block Tier 2+ use if
failed, unless the accountable owner accepts in writing. Certificates are checked with the
issuer; Anthropic's own certifications and Google Vertex IRAP status are `PENDING_VERIFICATION`
in the research, so never state them from memory.

### (h) Sign-off

25-item checklist by tier. Any Open item in the tier's column blocks sign-off. DDD signs
"ready / not ready"; **the client's accountable owner approves go-live** (stage 7), never DDD.

## Output conventions

- **Findings ranked by severity** using the one scale in `../_shared/engagement-conventions.md`
  s6a (Critical / High / Medium / Low; permission leak, PII leak and approval-gate bypass always
  block). Each finding: what, why it matters, the
  obligation or risk with **status and source** (register row and URL), recommended action,
  owner, due date. Lead the document with a 60-second "what this means for you" paragraph.
  Template: `templates/compliance-findings-template.md`.
- Every client-facing compliance document carries, near the top: **"This assessment identifies
  regulatory considerations for review by your legal adviser. It is not legal advice."**
- Files in the client's `created/docs/security/`, named `{purpose}-{YYYY-MM-DD}.{ext}` (R5).
- Client-facing text passes a client-facing tone review (audience tag, `voice_lint.py` zero FAIL).
- More than 3 numbers (risk counts, scores, dates) = R2 verifier in `scripts/verifiers/`.
- Professional indemnity cover for AI governance advice is `PENDING_VERIFICATION`; ai-manager
  flags it on any compliance-led engagement until confirmed.
- Log the action to your own engagement activity log.

## Size bands

| Band | How the modes scale |
|---|---|
| S | Screen + obligations + ADM in one sitting with the owner; register of 10-15 risks; vendor DD only for the main tool |
| M | All Tier-appropriate modes; register owned by a department head |
| L | Vendor DD through procurement; threat model reviewed by client IT/security |
| XL | Per-use-case screens feed the org AI register; impact assessments go to the AI council; findings feed board reporting (governance program) |

## Do not

- Do not build, or let ai-manager schedule a build, before a tier exists.
- Do not lower a tier because controls exist.
- Do not cite ISO 42001 Annex A control IDs or ISO 42005 clause numbers (harvested sources
  disagree on Annex A numbering; ISO texts not verified).
- Do not copy OWASP text. Do not quote EU penalty figures (`PENDING_VERIFICATION`).
- Do not put client data into any tool outside the engagement's data-handling agreement.

## Known gaps (v0.1.0)

- Screening bands uncalibrated; the Australian AI screening tool's questions could not be
  retrieved (site timeout), so alignment to it is `PENDING_VERIFICATION`.
- ATLAS: `~/ai-kb/vendor/mitre-atlas__atlas-data/dist/v6/ATLAS-2026.10.yaml` re-harvested 2026-11-08 at the pinned commit (sha256 ac41ee9f...142d).

Provenance and licences: `references/vendored-provenance.md`.
