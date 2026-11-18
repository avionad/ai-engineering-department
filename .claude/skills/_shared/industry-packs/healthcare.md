# Industry pack: healthcare

*v0.1.0, 2026-11-08. Clinics, allied health, hospitals, health tech. Rules point at
`../regulatory-register.md`.*

Health information is sensitive information under the Privacy Act (AU-6), so almost every
patient-facing use case starts at Tier 2 and clinical ones at Tier 3. Onshore hosting is the
default expectation (research matrix).

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Ambient clinical scribes | 3 | Recording consent; sensitive data; may be a medical device if it suggests diagnoses or treatments (AU-18) |
| 2 | Referral and discharge letter drafting | 3 | Clinical content; clinician must verify |
| 3 | Appointment and triage chat | 3 if it triages clinically; 2 if booking only | Triage affects access to care |
| 4 | Clinical coding and billing | 2 | Sensitive PI; financial accuracy; human review |
| 5 | Practice admin automation (reminders, intake forms) `[House addition]` | 2 | Patient PI; no clinical judgement |
| 6 | Internal policy and procedure assistant for staff `[House addition]` | 1 if public or non-confidential internal documents only; 2 once the corpus holds confidential, HR or board material (floor F6) | Becomes 3 if clinicians use answers to decide care for a specific patient (clinical-care floor); scope that out explicitly and test the refusal |
| 7 | Referral intake into the practice management system `[House addition]` | 3 | Health information written into the patient record; if it sets urgency, priority or routing it shapes access to care and meets the ADM limbs (AU-8) |

## Key risks

- A scribe or assistant crossing into software as a medical device by suggesting diagnoses or
  treatments: the TGA review found 8 of 12 scribes reviewed may be medical devices, none
  classified that way by their suppliers (AU-18, `[secondary]`).
- Recording consultations without consent: possible criminal exposure under surveillance and
  listening-device laws (AU-19).
- Health data leakage; offshore processing of sensitive information.
- Hallucinated clinical content reaching a patient record.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| TGA medical device regulation (SaMD incl. AI) | AU-18 | In force | Confirm with the vendor whether the tool is ARTG-included or claims it is not a device, and why |
| AHPRA AI guidance | AU-19 | Voluntary (professional guidance) | Practitioner remains responsible; informed consent for recording tools |
| Privacy Act, sensitive (health) information | AU-6 | In force | Higher bar for collection, use and disclosure; cross-border disclosure (APP 8) |
| ADM disclosure | AU-8 | Commenced later (10 Dec 2026) | Triage and eligibility decisions are candidates |
| State health records Acts; surveillance and listening-device Acts | Overlay | Named in research, no row | Legal adviser confirms per state |
| OAIC AI guidance | AU-11, AU-12 | Voluntary | No health information in public GenAI tools |

## Controls

- Written patient consent workflow before any recording; ability to decline and still be seen.
- Configure scribes to transcribe and summarise only; disable diagnosis or treatment suggestion
  features unless the product is ARTG-included for that purpose.
- Clinician verification step before anything enters the record; edits logged.
- Onshore hosting and no vendor training on patient data, confirmed in the contract.
- Incident path for a hallucinated clinical statement that reached a record.

## Discovery questions

1. Which clinical software (PMS, EMR) do you use, and which AI features are already switched on
   in it?
2. Do any tools record or transcribe consultations? How is patient consent captured today?
3. Does any tool suggest diagnoses, treatments, codes or triage categories?
4. Which states do you operate in? (Health records and surveillance laws differ.)
5. Where is patient data processed and stored, and does any vendor use it to train models?
6. Who verifies AI-drafted letters before they go out, and is that verification recorded?
7. Has any patient complained about, or asked about, AI use in their care?
