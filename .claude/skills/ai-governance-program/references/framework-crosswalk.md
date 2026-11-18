# Framework crosswalk: artefacts to the six practices, ISO/IEC 42001 and NIST AI RMF

*v0.1.0, 2026-11-08. The organising spine of `ai-governance-program`. Every artefact we deliver
maps to one or more of the National AI Centre's six practices first (Australian baseline), then
to ISO/IEC 42001 and NIST AI RMF for clients who need international alignment.*

## Sources and confidence

| Framework | Status (register) | What is verified here | What is not |
|---|---|---|---|
| Guidance for AI Adoption, 6 practices (NAIC, Oct 2025) | Voluntary (AU-4) | Practice names, from the research file | Content of the 2026 Foundations revision (`PENDING_VERIFICATION`); template field lists (site timed out 2026-11-08) |
| ISO/IEC 42001:2023 | Voluntary, certifiable (INT-1) | Annex SL management-system structure (Clauses 4 to 10, Plan-Do-Check-Act, Annex A controls) per the research and harvested sources | Sub-clause numbers come from the harvested alirezarezvani reference (MIT) and are **not verified against the purchased standard**; shown in brackets with that caveat. **Annex A control IDs are not cited**: two harvested sources number them differently |
| NIST AI RMF 1.0 | Voluntary (INT-5) | Four functions Govern, Map, Measure, Manage (research). Category numbers (GOVERN 1 to 6, MAP 1 to 5, MEASURE 1 to 4, MANAGE 1 to 4) from the harvested Sushegaad NIST AI RMF skill (MIT, author's "last verified 2026-10-03") | Subcategory numbers not cited; revision status `PENDING_VERIFICATION` |

## The six practices (AU-4)

1. Decide who is accountable
2. Understand impacts and plan accordingly
3. Measure and manage risks
4. Share essential information
5. Test and monitor
6. Maintain human control

## Crosswalk

| DDD artefact | Template / skill | GfAA practice(s) | ISO/IEC 42001 clause (sub-clause per harvested source, unverified) | NIST AI RMF function (category per harvested source) |
|---|---|---|---|---|
| AI policy | `templates/ai-policy-and-aup.md` | 1, 6 | Clause 5 Leadership (5.2 AI policy) | Govern (GOVERN 1) |
| Acceptable use policy | `templates/ai-policy-and-aup.md` | 1, 3, 6 | Clause 5; Clause 7 Support (7.3 awareness) | Govern (GOVERN 1, GOVERN 5) |
| Governance charter, RACI, council terms of reference | `templates/governance-charter.md` | 1 | Clause 5 (5.1, 5.3); Clause 9 (9.3 management review) | Govern (GOVERN 2, 3, 4) |
| AI register incl. shadow AI | `templates/ai-register-template.md`, `references/shadow-ai-discovery.md` | 1, 3, 4 | Clause 4 Context (4.3 scope) | Govern (GOVERN 1), Map (MAP 1) |
| Risk screening and risk register (per system) | `ai-compliance-risk` modes a, d | 3 | Clause 6 Planning (6.1.2, 6.1.3) | Map (MAP 4, MAP 5), Manage (MANAGE 1) |
| AI impact assessment | `ai-compliance-risk` mode e | 2 | Clause 6 (6.1.4); Clause 8 Operation (8.2) | Map (MAP 1, MAP 3, MAP 5) |
| Vendor due diligence | `ai-compliance-risk` mode g | 3 | Clause 8 (8.4 third-party relationships) | Govern (GOVERN 6), Map |
| ADM inventory and privacy policy wording | `ai-compliance-risk` mode c, `templates/adm-privacy-policy-wording-guide.md` | 2, 4 | Clause 4 (4.1 context: legal requirements); Clause 7 (7.4 communication) | Govern (GOVERN 6) |
| ISO/IEC 42001 readiness gap | `scripts/iso42001_readiness_gap.py`, `templates/iso42001-readiness-gap.md` | 1 to 6 | Clauses 4 to 10 | All four |
| AI literacy training plan (incl. board) | `templates/literacy-training-plan.md` | 1, 6 | Clause 7 (7.2 competence, 7.3 awareness) | Govern (GOVERN 2, GOVERN 4) |
| AI incident response playbook and incident log | `templates/incident-response-playbook.md` | 5, 6 | Clause 10 Improvement (10.2 nonconformity and corrective action) | Manage (MANAGE 3, MANAGE 4) |
| Transparency statement | `templates/transparency-statement-and-model-card.md` | 4 | Clause 7 (7.4 communication) | Govern, Map (MAP 2) |
| Model or system card | `templates/transparency-statement-and-model-card.md` | 4, 5 | Clause 7 (7.5 documented information) | Map (MAP 2), Measure (MEASURE 2) |
| Monitoring and eval cadence | `ai-evals-security-testing`, `ai-optimisation-llmops`; charter section | 5 | Clause 9 Performance evaluation (9.1) | Measure (MEASURE 3, MEASURE 4) |
| Human review design and kill switch | `ai-compliance-risk` sign-off items 16, 19 | 6 | Clause 8 (8.1 operational control) | Manage (MANAGE 2) |
| Compliance sign-off before go-live | `ai-compliance-risk` mode h | 3, 5, 6 | Clause 8 (8.1) | Manage (MANAGE 1, MANAGE 2) |

## Australian obligations the crosswalk does not cover

The six practices, ISO 42001 and NIST AI RMF are all voluntary. Binding Australian rules sit
beside them, not inside them: APP 1.7 ADM disclosure (AU-8, from 10 Dec 2026), the Privacy Act
(AU-6), CPS 230 and CPS 234 for APRA-regulated entities (AU-13, AU-14), the DTA policy for
Commonwealth agencies (AU-17), and sector rules in the industry packs. A governance program that
scores well on the crosswalk can still breach APP 1.7. Always run `ai-compliance-risk` mode (c).

## Optional mapping for DTA-covered agencies (AU-17)

| DTA requirement | DDD artefact |
|---|---|
| Accountable officials | Governance charter (accountable executive) |
| AI transparency statement | Transparency statement template |
| Internal AI use-case register, shared with DTA every 6 months | AI register (export the agency's required fields; field list `PENDING_VERIFICATION`) |
| AI impact assessment for in-scope use cases | `ai-compliance-risk` mode e as input to the DTA tool |
| Mandatory staff training | Literacy training plan |
