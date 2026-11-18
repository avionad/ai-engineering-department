<!-- Audience: public / customers (transparency statement); client staff, auditors (system card).
Save as created/docs/security/ai-transparency-statement-{client}-{YYYY-MM-DD}.md and
system-card-{system}-{YYYY-MM-DD}.md -->

# Transparency statement and model or system card templates

*v0.1.0, 2026-11-08. Practice 4 "Share essential information" (AU-4); ISO/IEC 42001 Clause 7
(communication, documented information); NIST Map. The DTA policy requires agencies to publish an
AI transparency statement (AU-17). For EU-facing clients, EU AI Act Article 50 transparency has
applied since 2 Aug 2026 (EU-1); the legal adviser confirms what Article 50 requires for the
specific system. Neither template replaces the privacy policy's APP 1.7 ADM disclosure (AU-8):
that has to be in the privacy policy itself.*

---

## Part A: AI transparency statement (public, one page)

**How {Client} uses artificial intelligence** | Last updated {date}

**Why we use AI.** {One or two sentences in business terms: faster replies, fewer errors.}

**Where you might meet it.**

| Where | What the AI does | What a person does | How to reach a person |
|---|---|---|---|
| {Website chat} | {Answers questions from our published policies} | {Takes over on request or when the AI is unsure} | {Type "person" / phone number} |
| {Application processing} | {Checks forms are complete and flags missing items} | {Makes every decision} | {contact} |

**What we do not use AI for.** {e.g. We do not use AI to make final decisions about {x}.}

**Your information.** {Where it is processed, that vendors do not train on it (if contractually
true), link to the privacy policy section on automated decisions.}

**Keeping it safe and fair.** {Testing before launch, monitoring, human review, how we handle
mistakes. Keep claims to what is evidenced; the ACL applies to these statements (AU-22).}

**Questions or concerns.** {contact}. You can ask for a person to review any outcome that affects you.

**Accountable person.** {role}.

---

## Part B: model or system card (internal, per system, under document control)

| Section | Content |
|---|---|
| Identity | System name, register ID, version, owner, date |
| Intended use | Purpose; users; in-scope tasks; explicitly out-of-scope uses |
| Components | Model(s) and provider, version pinned, hosting region; retrieval sources; tools and permissions; prompts location (version-controlled) |
| Data | Inputs, personal information kinds, retention, training or fine-tuning data and provenance |
| Human role | Human-in-the-loop tier; who reviews what; override recorded where |
| Performance | Eval set description; baseline results (accuracy, groundedness, refusal correctness, format); date; known failure modes |
| Fairness | Groups tested; results; limits of testing |
| Security | Threat model link; red-team results summary; open risks |
| Limitations | What it gets wrong; conditions where it should not be used |
| Monitoring | Metrics, thresholds, owner, cadence; drift and model-retirement plan |
| Compliance links | Risk tier and screen; impact assessment; ADM status; vendor DD; sign-off |
| Change log | Every model, prompt, retrieval or permission change with date and eval result |

For bought products, ask the vendor for their model or system documentation (vendor DD question
25) and attach it; fill the rest from the client's configuration.
