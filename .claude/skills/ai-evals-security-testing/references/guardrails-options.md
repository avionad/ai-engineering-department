# Guardrails: build choices

*v0.1.0, 2026-11-08. Guardrails are controls chosen at design time (`ai-architect`) and built by
`ai-engineer`; this skill tests them. ATLAS names the class of control AML.M0020 Generative AI
Guardrails. Sources: GitHub research area 2 (licences, activity), web research B4 (Bedrock
Guardrails in Sydney), harvested Orchestra-Research `nemo-guardrails` how-to (MIT, commit
773a5294). Vendor claims about detection rates are not repeated here and never go to a client.*

## Principle

Guardrails reduce risk; they do not replace least agency, permission-aware retrieval or human
approval for irreversible actions. Put the hard controls in code first (allow-lists, scoped
credentials, schema validation, identity filters), then add guardrails for the fuzzy cases
(injection attempts, off-topic, harmful content, PII in free text).

## Options

| Option | Licence / type | What it is (our words) | Fits when | Watch |
|---|---|---|---|---|
| **Deterministic checks** (DDD's own code) | n/a | Input length limits, allow-listed tools and parameters, JSON schema validation of outputs, URL and domain allow-lists for links, encoding of rendered output | Always, first | Cheapest and most reliable; cover them in unit tests |
| **Presidio redaction** | MIT | PII detection and anonymisation on input, retrieved text, output and logs, with Australian recognisers | Any Tier 2+ system handling personal information | Register AU recognisers explicitly; tune score thresholds on client-like test data (see `../../ai-rag-engineering/references/pii-redaction-presidio.md`) |
| **NeMo Guardrails** | Apache-2.0 (per research, from LICENSE.md) | Programmable rails defined in a dialogue language (Colang): input rails, output rails, topic control, dialogue flows | Self-hosted or custom stacks wanting rails as code, versioned with the app | Adds model calls for some rails (latency and cost: measure); rails are themselves tested against the golden set so they do not block legitimate items |
| **Guardrails AI** | Apache-2.0 (per research) | Validators for structured output and content checks wrapped around model calls | Extraction and structured-output systems where output shape and field validity matter | Not harvested; check current validator list and licence of each hub validator before use (`PENDING_VERIFICATION`) |
| **Platform guardrails** (e.g. Amazon Bedrock Guardrails) | Managed service | Content filtering and related policies applied by the model platform | Client already on Bedrock for Australian residency (research B4: Guardrails available in Sydney; Automated Reasoning checks added in Sydney June 2026) | Feature list, pricing and per-region availability `PENDING_VERIFICATION` on the live AWS page at design time; Azure and Google equivalents not verified in research |
| **Llama Guard / Prompt Guard** (PurpleLlama) | Llama Community Licence | Classifier models for unsafe content and injection | Self-hosted stacks | Licence has use restrictions: reference only unless the client accepts the licence terms |
| **llm-guard** | MIT, archived | Scanner list | Do not adopt for new builds (research: archived) | Useful only as a checklist of scanner types |

## Selection rules

1. Residency and data handling first: a guardrail that sends text to a third-party service is a
   data flow and needs the same vendor due diligence as the model
   (`../../ai-compliance-risk/templates/vendor-due-diligence-questionnaire.md`).
2. Prefer the platform the system already runs on when it meets the need (one less vendor).
3. Prefer rails as code in the repo for anything Tier 3, so changes go through the eval suite.
4. Record the choice and its config version in the solution design and the test plan.

## How guardrails are tested

- Run the full golden set with guardrails on: **false blocks are failures** (a guardrail that
  refuses legitimate client questions fails the functional threshold).
- Run the red-team catalogue with guardrails on and, where safe in sandbox, off: the difference
  shows what the guardrail actually contributes.
- Re-test whenever the guardrail config, model or vendor version changes.
- Report what our tests measured; never a vendor's claimed rate.
