# Seven dimensions and scoring rubric

*v0.1.0, 2026-11-08. Level descriptors adapted from OneWave-AI `ai-readiness-assessment`
(MIT; six dimensions, 1-5 levels) and reorganised into DDD's seven dimensions; governance scored
against the National AI Centre's Guidance for AI Adoption six practices and the APP 1.7 ADM duty
(research file A1). See `vendored-provenance.md`.*

Rules for every score:
- Score 1 to 5, half-points allowed when a client clearly sits between two levels.
- Every score cites evidence (a document seen, a system observed, an interview line). No evidence
  means the score is marked unevidenced and the gate cannot be Go.
- Score conservatively. A 2 that is true helps the client more than a 3 that flatters.
- Record confidence (high, medium, low) and what would raise it.
- Score the organisation as it is today, not as it plans to be.

Machine keys (used by `scripts/readiness_score.py`) are shown in brackets.

---

## 1. Strategy and leadership [`strategy_leadership`]

Is there a reason, an owner and a way to measure value?

| Level | Descriptor |
|---|---|
| 1 | No stated reason for AI beyond curiosity or pressure. No executive owner. No budget. Nobody can name a business problem it should solve. |
| 2 | Leadership interested; one or two ideas; no named owner, no success measures, no budget committed. ROI expectations unclear or unrealistic. |
| 3 | Named executive sponsor; two or more prioritised problems tied to business goals; a pilot budget; success measures defined for at least one use case. |
| 4 | AI goals in the business plan; portfolio of use cases with value and risk scoring; budget covers run costs and change, not just build; value tracked after go-live. |
| 5 | AI is a standing board or executive agenda item; benefits tracked against baselines for every use case; funding protected over multiple years; decisions to stop failed pilots are made and recorded. |

## 2. Data [`data`]

Can the organisation produce clean, accessible, appropriately classified inputs?

| Level | Descriptor |
|---|---|
| 1 | Key data in spreadsheets, inboxes and personal drives; duplicates and conflicts common; nobody owns quality; paper processes remain. |
| 2 | Core data in SaaS systems or databases; no ownership or quality checks; joining data across systems is manual; reports often disputed. |
| 3 | Systems of record for key entities (customers, products, transactions); owners named; basic quality checks; trusted regular reporting; samples can be produced for a pilot within days. |
| 4 | Automated and monitored pipelines; quality measured; master data practices; personal and sensitive data classified and handled to the classification; history accessible. |
| 5 | Near real-time pipelines with lineage; self-service access within permissions; automated quality remediation; data treated as an asset with an executive owner. |

## 3. Technology and infrastructure [`technology_infrastructure`]

Can AI connect to the systems that matter, safely?

| Level | Descriptor |
|---|---|
| 1 | Core systems old, without APIs or exports; no cloud presence; no test environments; vendor lock-in with no export. |
| 2 | Mix of legacy and SaaS; some APIs; no sandbox; integrations are manual or ad hoc scripts; no single identity provider. |
| 3 | Cloud or hybrid; APIs on core systems; a test or sandbox environment exists or can be arranged; single sign-on in place; monitoring and logging exist. |
| 4 | Integration layer or workflow platform in use; infrastructure as code or managed platforms; enterprise AI tenancy available in a suitable region; service accounts with scoped permissions. |
| 5 | Platform for building and running AI (model gateway, evaluation and tracing, model routing); data and model in a chosen region by design; automated deployment with rollback. |

## 4. People and skills [`people_skills`]

Do people have the skills, the capacity and the willingness? (Culture is scored here.)

| Level | Descriptor |
|---|---|
| 1 | No technical capability in house or at a trusted partner; low digital confidence; open resistance; fear of job loss unaddressed. |
| 2 | Small IT or MSP focused on support; some confident spreadsheet users; awareness of AI is superficial; past rollouts were painful. |
| 3 | At least one capable internal owner per pilot area; staff open to new tools; leadership talks openly about how roles will change; some staff already experimenting. |
| 4 | Role-based AI training in place; champions network; cross-functional teams; change management practised; staff can raise concerns safely. |
| 5 | Organisation-wide AI literacy including the board; champions sustain communities of practice; AI skills in role descriptions and onboarding; structured feedback from users to builders. |

## 5. Process [`process`]

Are the processes understood well enough to automate?

| Level | Descriptor |
|---|---|
| 1 | Processes live in people's heads; outcomes vary by who does the work; critical key-person dependencies; nothing measured. |
| 2 | Some written procedures, outdated or scattered; inconsistent execution; onboarding by shadowing; no volume or time data. |
| 3 | Core processes documented with owners; mostly consistent; volumes and handling times known or easily sampled; common exceptions known. |
| 4 | Process KPIs tracked; exception handling documented; workflow tools enforce steps; improvement practised. |
| 5 | Processes mapped with decision logic, inputs and outputs per step; exceptions catalogued; business rules configurable; designed with automation in mind. |

## 6. Governance and risk [`governance_risk`]

Scored against the six practices of the Guidance for AI Adoption (National AI Centre, October
2025; voluntary) plus the APP 1.7-1.9 automated decision-making disclosure duty (in force from
10 December 2026 for APP entities). Rate each practice 0 (absent), 1 (partial) or 2 (in place)
in the input file; the script reports them beside the dimension score.

| Practice key | Practice (NAIC) | "In place" looks like |
|---|---|---|
| `accountability` | 1. Decide who is accountable | Named accountable executive for AI; roles for approving use cases |
| `impacts` | 2. Understand impacts and plan accordingly | Use cases screened for impact on people before build; impact assessment for higher-risk uses |
| `risk_management` | 3. Measure and manage risks | AI risk register; risk tiering per use case; vendor due diligence |
| `information_sharing` | 4. Share essential information | AI register; staff and customers told where AI is used; privacy policy current |
| `test_monitor` | 5. Test and monitor | Evaluation before go-live; monitoring after; incidents logged |
| `human_control` | 6. Maintain human control | Human oversight designed per use case; ability to override or stop |

ADM check (record in the input `adm` block): does the organisation use any computer program that
makes, or does something substantially and directly related to, decisions that could reasonably
be expected to significantly affect individuals' rights or interests, using their personal
information? If yes or unknown: has an inventory been done, and does the privacy policy disclose
the kinds of personal information used and the kinds of decisions? Human review does not remove
the duty where the program's output materially influences the decision (Allens and OAIC, research
file A1). This assessment identifies the consideration; the client's legal adviser confirms it.

| Level | Descriptor |
|---|---|
| 1 | No AI policy; no idea which AI tools are in use; no accountable person; ADM exposure unknown. (Practices mostly 0.) |
| 2 | Informal rules or a draft policy; some awareness of shadow AI; no register; ADM not yet assessed. |
| 3 | Acceptable use policy published; accountable executive named; AI register started; use cases screened; ADM inventory under way or done. (Most practices at least 1, accountability 2.) |
| 4 | Risk register and tiering in use; impact assessments for higher-risk uses; evaluation and monitoring standard; privacy policy discloses ADM; incident process. (Most practices 2.) |
| 5 | AI management system aligned to ISO/IEC 42001 (readiness, not certification by DDD); AI council operating; regular review of register and risks; board oversight; all six practices at 2. |

## 7. Security and privacy [`security_privacy`]

Can AI be used without leaking data or widening the attack surface?

| Level | Descriptor |
|---|---|
| 1 | Staff paste business or personal data into public AI tools; no MFA on key systems; no data handling rules; no breach process. |
| 2 | MFA on some systems; informal rules on AI tools; no approved AI tool, so shadow AI is the default; privacy policy not reviewed for AI. |
| 3 | Approved AI tools with business terms (no training on client data) for confidential data; tiered tool rule (unvetted tools for public data only); MFA and SSO on core systems; notifiable data breach process known. |
| 4 | Data classification applied and mapped to tool tiers; DLP or sensitivity labels; logging of AI use within privacy limits; privacy impact assessments for new AI uses; AI vendor due diligence (residency, sub-processors, exit). |
| 5 | AI-specific threat modelling (OWASP LLM and Agentic Top 10) and red-teaming for built systems; permission-leak testing on retrieval; Essential Eight maturity target met; regular review of AI vendor terms. |

---

## Overall result

The script computes an unweighted mean (equal weights by default; weights can be set in the input
if the engagement agrees them up front and records why). The mean is context only. The gate is
decided by the rules in `gates.md`, not by the average: one score of 1 blocks a Go however good the
others are.
