# Industry pack: aged care and NDIS (disability services)

*v0.1.0, 2026-11-08. Residential aged care, home care and home support providers, and registered
and unregistered NDIS providers. Added after a review found the Sydney SMB market DDD sells into
includes a large aged care and disability services segment with no pack. Rules point at
`../regulatory-register.md`.*

> **Read this before any client conversation in this sector.** This is a regulated,
> vulnerable-persons sector and **our register does not cover its sector rules**. The Aged Care
> Quality Standards, the NDIS Practice Standards and Code of Conduct, worker screening, and
> reportable incident obligations (aged care SIRS and NDIS reportable incidents) are **not in
> `../regulatory-register.md`** and DDD holds **no verified position** on any of them. They are
> marked `PENDING_VERIFICATION` throughout this pack. Identify them as questions, send them to the
> client's legal adviser and to the provider's own quality and compliance function, and never state
> one as a requirement, a threshold or a deadline. Do not fill the gap from memory. If a client
> conversation turns on one of these, stop and verify first, or say plainly that DDD has not
> verified it.

Three things set the floor here, and they are higher than in any other pack:

1. **Health and disability information is sensitive information** under the Privacy Act (AU-6), and
   aged care and disability providers are generally health service providers, which is one of the
   nine small-business categories AU-6 covers regardless of turnover. Confirm with the client's
   legal adviser, but assume coverage.
2. **Participants and residents are vulnerable people**, so screening floor F8 applies to almost
   every use case (`../../ai-compliance-risk/references/screening-questionnaire.md`), and where the
   use also affects their rights or interests it is Tier 3.
3. **Many cannot consent for themselves.** Substitute decision-makers, guardians, nominees and
   enduring powers of attorney are in the consent path, which makes "we told the client" an
   insufficient answer for recording tools and for AI use in care documentation.

Conservative default: in this sector, when a use case sits on the line, put it in the higher tier
and say why. The README's narrowing rule still applies (scoping a staff assistant to reference use
can lower the tier), but only with the scope boundary recorded and the refusal proven in testing.

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Rostering and shift-fill administration (matching available workers to open shifts for a coordinator to approve) `[DDD addition]` | 2, and 3 where the allocation itself materially affects workers' hours or earnings | Worker personal information; algorithmic allocation of work engages AU-21 in NSW. A coordinator approves every roster |
| 2 | Progress note and shift-report drafting from a support worker's own dictation `[DDD addition]` | 3 | Sensitive health and disability information entering the care record, about a vulnerable person; these records are evidence in incident and complaint investigations. Recording consent path is `PENDING_VERIFICATION` per state |
| 3 | Care plan or support plan drafting for a qualified person to review `[DDD addition]` | 3 | Shapes the care a specific person receives. Clinical or allied health content can also engage TGA device rules (AU-18) and AHPRA duties (AU-19) |
| 4 | Policy, procedure and practice-guidance assistant for staff, scoped to reference use `[DDD addition]` | 1 where the corpus is public or non-confidential internal documents only; 2 once it holds confidential, HR or board material (floor F6) | Becomes 3 the moment a worker uses an answer to decide care or supports for a named participant. Scope that out explicitly and prove the refusal in `../../ai-evals-security-testing` |
| 5 | Family, participant and referrer enquiry handling and information requests `[DDD addition]` | 2 | Personal information and public-facing output (floors F6, F7). It must not assess eligibility, suitability, priority or clinical questions |
| 6 | Claim and invoice preparation support for NDIS claiming or aged care subsidy claiming `[DDD addition]` | 2 where a person checks and submits every claim; 3 where it determines what is claimable | Claiming against a government programme carries integrity and overpayment consequences. It never submits, and it never decides claimability |
| 7 | Incident report drafting and triage `[DDD addition]` | 3 | Reportable incident obligations carry statutory timeframes. A wrong severity classification or a delay is a regulatory breach, not a service annoyance. Obligations are `PENDING_VERIFICATION` |
| 8 | Recruitment and onboarding administration (document collection, interview scheduling, compliance-document chasing) `[DDD addition]` | 2 for scheduling and document chasing; 3 if it screens, ranks or filters candidates | Worker screening clearances are statutory checks and are never automated or inferred by a model. Status of those checks is `PENDING_VERIFICATION` |

## Key risks

- **Vulnerable persons, and consent that may not be the person's own.** Substitute decision-makers
  in the consent path for any recording, transcription or AI-assisted documentation.
- **Sensitive information leakage.** Health and disability information in consumer AI tools, or
  processed offshore without an APP 8 analysis. The default expectation is onshore processing.
- **Hallucinated content in a care record.** A fabricated observation, medication reference or
  behaviour note in a progress note is clinical misinformation that later readers act on, and it is
  discoverable in an investigation.
- **Incident mis-triage.** Software that sorts, de-prioritises or delays an incident that should
  have been reported.
- **Scope creep from reference to decision.** A policy assistant quietly becoming the way workers
  decide supports for a named participant.
- **Workforce surveillance and algorithmic rostering** of a low-paid, high-turnover workforce.
- **Claiming integrity.** AI-prepared claims that nobody verified, against a programme with
  overpayment recovery and fraud consequences.
- **Reputational and regulatory asymmetry.** In this sector a single bad outcome for one person is a
  regulatory event. Pilot scope should reflect that.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| Privacy Act and the APPs, sensitive information | AU-6 | In force | Higher bar for collection, use and disclosure; cross-border disclosure under APP 8; assume the provider is an APP entity as a health service provider and confirm with their legal adviser |
| ADM disclosure, APP 1.7 to 1.9 | AU-8 | Commenced later (from 10 Dec 2026) | Strong candidate here: eligibility, priority, service allocation, roster allocation and candidate screening can all meet the three limbs. Human review does not by itself exempt it. Run the ADM check in `../../ai-compliance-risk` |
| OAIC guidance on commercially available AI products | AU-11 | Voluntary, on binding law | No participant or resident information in public GenAI tools |
| OAIC guidance on developing and training GenAI models | AU-12 | Voluntary, on binding law | Participant data is not training data; APP 3 and APP 6 limits |
| Statutory tort for serious invasions of privacy | AU-7 | In force (from 10 Jun 2025) | Relevant to recording, monitoring and data-linkage in people's homes and rooms |
| AHPRA guidance on AI in healthcare | AU-19 | Voluntary, professional guidance | Applies to registered practitioners the provider employs (nurses, allied health): the practitioner remains responsible, and informed consent matters for recording tools |
| TGA medical device regulation, software as a medical device | AU-18 | In force | Engages if a tool suggests diagnoses or treatment. Confirm with the vendor whether the product is ARTG-included, or why it says it is not a device |
| NSW WHS Amendment (Digital Work Systems) Act 2026 | AU-21 | Commenced later | Algorithmic rostering, workload and monitoring for NSW care workers |
| Australian Consumer Law | AU-22 | In force | Statements made to families and participants by a chatbot are the provider's statements |
| AHRC AI and recruitment compliance checklist | AU-24 | Voluntary, on binding anti-discrimination law | Disclose AI use in hiring; no candidate removed solely by an automated decision |
| ASD ACSC guidance and Essential Eight | AU-23 | Voluntary for most | Agent credentials and access control |
| Guidance for AI Adoption | AU-4 | Voluntary | Governance baseline |
| State health records Acts, and surveillance and listening-device Acts | Overlay | Named in the research (healthcare), no register row | Legal adviser confirms per state, especially for any recording in a home or a resident's room |
| **Aged Care Quality Standards and the aged care legislative framework** | **No register row** | `PENDING_VERIFICATION` | Not verified by DDD. Route to the client's legal adviser and their quality and compliance function |
| **NDIS Practice Standards, the NDIS Code of Conduct and registration conditions** | **No register row** | `PENDING_VERIFICATION` | Not verified by DDD. Route to the client's legal adviser and their quality and compliance function |
| **Worker screening (NDIS worker screening checks, aged care police and screening requirements)** | **No register row** | `PENDING_VERIFICATION` | Not verified by DDD. Treat screening as a statutory check that is never automated or inferred |
| **Reportable incident obligations (aged care Serious Incident Response Scheme; NDIS reportable incidents) and their timeframes** | **No register row** | `PENDING_VERIFICATION` | Not verified by DDD, including every timeframe. Never state a reporting deadline. Any AI touching incidents is designed around the provider's own documented process |

## Controls

- **Nothing enters a care record without a named qualified person reviewing it**, with the review
  recorded and the AI-drafted original retained, so an investigator can see what was changed.
- **Consent workflow before any recording or transcription**, covering substitute decision-makers,
  the right to decline with no effect on care, and how consent is evidenced. The legal basis is
  confirmed per state by the client's adviser before the tool is switched on.
- **Onshore processing and no vendor training on participant or resident data**, confirmed in the
  contract, not in a sales deck (data-class matrix C4 conditions).
- **Incidents stay with people.** No AI classification of incident severity or reportability, and
  no AI step that can delay a report. Drafting support only, inside the provider's own process.
- **Hard scope boundary on staff assistants:** refuse participant-specific care, clinical,
  behavioural, medication and eligibility questions, with the refusal in the golden set and proven
  in testing before go-live, and a re-screen the moment the scope expands.
- **No claim submission and no claimability decisions.** Draft, human verifies, human submits.
- **Roster and allocation transparency:** workers can see why they were offered a shift, a
  coordinator approves, and the client takes a position on worker consultation (and on AU-21 where
  NSW workers are involved).
- **Access control that matches the care team.** Support workers see the participants they support,
  not the whole client base; permission-aware retrieval, not a shared index
  (`../../ai-rag-engineering`).
- **Vulnerable-persons review in the impact assessment**, including who is harmed if the system is
  wrong and who would notice first.

## Discovery questions

1. Which client management system do you use (aged care or NDIS), and which AI features are already
   switched on inside it?
2. Who are your participants or residents, and for how many of them does someone else hold decision
   making authority? How is that recorded today?
3. Does anything record or transcribe conversations with participants, residents, families or staff,
   and how is consent captured and evidenced?
4. Walk me through how a progress note is written today, who reads it afterwards, and what happens
   to it in an incident or complaint investigation.
5. What is your incident reporting process, who classifies severity, and what are your own
   documented timeframes? (DDD does not hold the regulatory timeframes: your adviser confirms them.)
6. Who prepares your claims, what is the error and rejection rate today, and who checks a claim
   before it is submitted?
7. How are rosters built and shifts filled now, how many hours a week does that take, and which
   states are your workers in?
8. Where is participant and resident data processed and stored, and does any vendor use it to train
   models?
