<!-- Audience: client (accountable owner, legal adviser, affected-stakeholder reps).
Save as created/docs/security/ai-impact-assessment-{project-slug}-{YYYY-MM-DD}.md
Mandatory for Tier 3 (conventions s6). Re-run on material change. -->

# AI impact assessment: {Project name}

> This assessment identifies regulatory considerations for review by your legal adviser. It is
> not legal advice.

**Alignment note.** This template is aligned in structure to ISO/IEC 42005:2025, AI system impact
assessment (register INT-3: published May 2025, voluntary, covers when and how to assess across
the lifecycle and how to document it, for any size of organisation). The practice has not verified the
standard's clause numbering against the purchased text, so **no ISO 42005 clause numbers are
cited**; the sections below are described generically. It also borrows question themes from the
Government of Canada AIA (MIT, see `references/vendored-provenance.md`) and, for Commonwealth
agencies, should be read alongside the DTA AI impact assessment tool (AU-17).

| Field | Value |
|---|---|
| Client / system owner | |
| Assessment lead (the practice) | |
| Version / date | v1 / {YYYY-MM-DD} |
| Risk tier and screen date | |
| Lifecycle stage at assessment | Design / Build / Pre-go-live / In operation |
| Next review trigger | {material change, model change, annual, incident} |

## 1. Scope and timing
Why an assessment now; what is in and out of scope (system boundary, versions, integrations);
which lifecycle stage; what triggers a reassessment.

## 2. System description
Purpose and intended use; explicitly out-of-scope or prohibited uses; who uses it; how it works
at a level an affected person could follow; model(s), provider, hosting region; human role at
each step (human does / approves each / samples / autonomous within limits).

## 3. Data
Personal and sensitive information used (kinds, sources, who collected it); training or
fine-tuning data and its provenance; retention; cross-border flows; data quality and
representativeness for the people affected.

## 4. Affected stakeholders
Direct users; people the outputs are about (including those who never interact with it);
vulnerable groups; staff whose roles change. How each was consulted, or why not.

## 5. Impact analysis
For each stakeholder group, the plausible benefits and harms across: rights and freedoms;
equality and non-discrimination; privacy and autonomy; health, safety and wellbeing; economic
interests; access to services. For each harm: likelihood, severity, reversibility, duration
(same scales as the screening questionnaire I1 to I6), and whether it falls unevenly on a group.

## 6. Legal and regulatory considerations
Pull from the applicable-obligations document (mode b): ADM status (mode c result), sector rules,
EU applicability. Status words as per conventions s4.

## 7. Measures
Controls that prevent or reduce each harm: human review design, contestability path, bias
testing, transparency to affected people, fallback process, monitoring thresholds, incident plan.
Cross-reference risk register IDs.

## 8. Residual impact and decision
Residual harms after measures; who accepts them; go / go with conditions / do not proceed.

| Role | Name | Decision | Date |
|---|---|---|---|
| Client accountable owner | | | |
| Client privacy officer or legal adviser (reviewed) | | | |
| The practice assessment lead | | | |

## 9. Monitoring and review
What is monitored, by whom, how often; what result reopens this assessment; where the record is
kept (client AI register entry ID).
