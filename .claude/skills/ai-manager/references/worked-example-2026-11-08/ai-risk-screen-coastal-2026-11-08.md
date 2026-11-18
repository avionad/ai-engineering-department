# PROVISIONAL risk screens and obligations -- Coastal Health Partners (FICTIONAL DRY RUN)

*Internal prep. Every answer is `assumed`; tiers are PROVISIONAL (screening-questionnaire.md). This assessment identifies regulatory considerations for review by your legal adviser. It is not legal advice.*

## Screen 1: staff knowledge assistant

```
Project: knowledge-assistant | Size band: XL | Industry pack: healthcare | Jurisdictions: AU (Qld)
Stop questions: all No (assumed)
Floors triggered: F6 (HR and board documents in corpus; staff PI possible) -> Tier 2.
  F5 (regulated activity: clinical care) = OPEN: if clinicians use guideline answers to decide care
  for a specific patient, F5 = Yes -> Tier 3 and a TGA (AU-18) check.
  ADM limbs: F1 N, F2 N, F3 N (no decision about an individual) -> APP 1.7 not triggered by this system.
  F4 N (read-only), F7 N (internal), F8 N.
Impact score: 25 / 54 (46%) -> Tier 2  (I1 3, I2 2, I3 2, I4 3, I5 3, I6 1, I7 0, I8 0, I9 0,
  I10 0, I11 3, I12 2, I13 2 read, I14 3, I15 0, I16 1). Two points below the Tier 3 band.
FINAL TIER: 2 PROVISIONAL (confidential and possibly personal data behind access control, human uses
  output; becomes 3 if the use extends to patient-specific clinical decision support).
Mitigation readiness: M1 N (no accountable owner named), M2 N, M3 ?, M4 Planned, M5 Planned, M6 Planned, M7-M12 n/a at T2
Screened by: ai-manager (dry run), no client present, 2026-11-08. Re-screen trigger: clinical guidelines added, patient data in prompts, new user group.
```

Note: the healthcare pack lists "internal policy and procedure assistant" as typical Tier 1. That does not hold here: the corpus holds restricted HR and board documents (F6) and clinical guidelines.

## Screen 2: referral letter intake into the PMS

```
Project: referral-intake | Size band: XL | Industry pack: healthcare | Jurisdictions: AU (Qld)
Stop questions: all No (assumed)
Floors triggered: F6 Y (health information = sensitive, AU-6) -> T2; F5 assumed Y (part of the clinical
  care pathway) -> T3; F4 depends on design (writes to the patient record; design keeps a human approval
  per write, so N by design, but the use is what is tiered).
  ADM limbs: F1 assumed Y if it sets urgency, priority, routing or clinician allocation; F2 Y (access to
  health care); F3 Y (patient PI and health information) -> APP 1.7-1.9 disclosure from 10 Dec 2026 if F1 holds.
Impact score: 30 / 54 (56%) -> Tier 3  (I1 3, I2 2, I3 2, I4 3, I5 3, I6 2, I7 0, I8 2, I9 0,
  I10 0, I11 3, I12 2, I13 4 write, I14 3, I15 0, I16 1).
FINAL TIER: 3 PROVISIONAL (health information written into the patient record by software, likely
  shaping who is seen and when; the score alone reaches Tier 3 even if F1 turns out No).
Mitigation readiness: all Planned/unknown. Tier 3 adds impact assessment, ADM disclosure, human review design, red-team, monitoring, incident plan.
```

ADM check (mode c, provisional): System = referral intake automation; decision type = referral acceptance and triage priority; limbs Y/Y/Y if it scores or sets priority; classification = "program does a thing substantially and directly related"; PI kinds = patient identity, contact, Medicare number, referrer, clinical reason; current privacy policy coverage = unknown; action = inventory the existing PMS's own automated features too (vendor-embedded ADM counts).

## Top obligations (register + healthcare pack), ranked per mode (b) step 5

| # | Obligation | Row | Status | Applies to | Why it matters here |
|---|---|---|---|---|---|
| 1 | Privacy Act and APPs, health information as sensitive information; APP 8 cross-border; APP 11 security; NDB | AU-6 | In force | Both | Health service providers are APP entities regardless of turnover; the "data stays in Australia" requirement maps to APP 8 and the residency design |
| 2 | Statutory tort for serious invasions of privacy | AU-7 | In force (10 Jun 2025) | Both (assistant: HR and board leak path) | A permission leak of HR records is the realistic exposure |
| 3 | TGA software as a medical device | AU-18 | In force | Assistant if patient-specific; referral if it triages clinically | Keep both outside diagnosis or treatment suggestion unless ARTG-included |
| 4 | ADM transparency, APP 1.7-1.9 | AU-8 | Commenced later (10 Dec 2026) | Referral intake (if it prioritises); whole-org inventory | 32 days from today; offer the ADM transparency sprint |
| 5 | AHPRA guidance on AI in healthcare | AU-19 | Voluntary (professional guidance) | Both | Practitioner remains responsible for anything used in care |
| 6 | OAIC guidance on commercially available AI products | AU-11 | Voluntary (guidance on binding law) | Both; shadow AI | No health information in public GenAI tools; due diligence on the platform |
| 7 | Guidance for AI Adoption (six practices) | AU-4 | Voluntary | Program | Accountability, testing, human control: frame for the rollout |
| 8 | ACSC AI guidance and Essential Eight | AU-23 | Voluntary for this client | Platform | Security baseline reference |
| -- | Queensland health records and surveillance law | Overlay, no row | Named in research, not row-verified | Both | Question for legal adviser |
| -- | Workforce consultation, enterprise agreements | No row | PENDING_VERIFICATION | Rollout | Staff concern raised by the CIO; HR and legal adviser to confirm |
| n/a | AU-21 NSW digital work systems | AU-21 | Commenced later (duties not commenced) | Only if NSW workers | Confirm no NSW staff |
| n/a | AU-22 ACL | AU-22 | In force | Not for internal tools | No consumer-facing output |
| n/a | EU-1/2/3 | | | No EU users (assumed) | |

Flags: professional indemnity cover for AI governance advice is PENDING_VERIFICATION (raise with the practice owner). All rows checked 2026-11-08, within the 60-day window.
