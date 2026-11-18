# AI Automation department -- engagement conventions

*Every skill and agent in the `ai-automation` department reads this first. Owner: ai-manager.
v0.1.0, 2026-11-08. Blueprint: the department's original research files (internal, not included in this repo).*

## 1. What DDD sells here

AI automation across the whole business (CRM, data, voice, finance, operations, knowledge), with
compliance and risk management built in, for organisations from 5 to 500+ staff in any industry.
Marketing is one use case among many, never the frame (memory
`ddd-is-an-ai-automation-practice-not-a-marketing-agency`). Payoff language is hours removed,
manual steps eliminated, systems connected and risk controlled.

## 2. Engagement lifecycle and hard gates

| Stage | Skill(s) | Exit gate (must be true before the next stage) |
|---|---|---|
| 0. Intake | `ai-manager` | Client, industry, size band, decision-maker and the problem in their words recorded |
| 1. Discover | `ai-discovery-scoping`, `ai-readiness-assessment` | Discovery notes with the client's own numbers (hours, volumes, error costs); readiness Go/Wait |
| 2. Govern | `ai-compliance-risk`, `ai-governance-program` | Risk tier assigned; applicable obligations listed; ADM (APP 1.7) check done |
| 3. Design | `ai-architect` agent following `ai-solution-architecture` | Architecture + data-flow diagram, platform choice with residency, build-vs-buy, ADR |
| 4. Quote | `ai-proposal-pricing` | Effort model + package price, owner-approved, R2 verifier PASS |
| 5. Build | `ai-engineer` agent with `ai-rag-engineering`, `ai-agents-automation`, `ai-model-customisation`, `ai-deployment-platforms` | Built in sandbox/staging only; never on client production |
| 6. Verify | `ai-evals-security-testing` (`ai-security-tester` agent) | Baseline eval + security tests passed; compliance sign-off by `ai-compliance-officer` |
| 7. Go-live | `ai-manager` | Human approval from the client's accountable owner, recorded |
| 8. Run | `ai-optimisation-llmops` (`ai-optimiser` agent), `ai-use-case-portfolio` benefits tracking | Monthly improvement loop, reported in business terms |

**Non-negotiables:**
- No build before a risk tier exists. No go-live without an eval baseline and a compliance sign-off.
- No client personal or confidential data in public consumer AI tools (OAIC guidance). Client data
  is processed only in tools covered by the engagement's data-handling agreement.
- Credentials only in a secrets manager.
  Never in files, chat or client documents.
- Least agency for every agent we build: scoped credentials, human approval for irreversible
  actions, kill switch, spend cap, logging.
- Telco-referred clients: Telco ICT billing and branding rules apply, not DDD's.

## 3. Ground truth order (R1)

1. The client's own documents, systems and statements (discovery notes, data samples).
2. `_shared/regulatory-register.md` and `_shared/industry-packs/` -- each row carries a source URL
   and a `date checked`. A row older than 60 days is re-verified before it appears in a
   client deliverable.
3. Live primary sources (legislation.gov.au, oaic.gov.au, industry.gov.au, apra.gov.au,
   asic.gov.au, iso.org, nist.gov, eur-lex, owasp.org, vendor docs).
4. Research files in the department's original research files (internal, not included in this repo).

Training data is never a source for a regulation, a date, a model name, a price or a region.
Anything unverified is written `PENDING_VERIFICATION` and does not go to a client.

## 4. Legal framing (DDD is not a law firm)

- Compliance outputs identify obligations, risks and controls. They do not give legal advice.
- Every client-facing compliance deliverable carries: "This assessment identifies regulatory
  considerations for review by your legal adviser. It is not legal advice."
- Distinguish **in force**, **commenced on a later date**, **proposed** and **voluntary** in every
  statement about a rule. Never call voluntary guidance a requirement.
- Professional indemnity cover for AI governance advice is PENDING_VERIFICATION with DDD's insurer;
  until confirmed, ai-manager flags it on any compliance-led engagement.

## 5. Size bands (they change the method, not just the volume)

| Band | Staff | Typical shape |
|---|---|---|
| S | 1-19 | Owner decides; one or two automations; SaaS tools; light governance (policy + register) |
| M | 20-199 | Department heads involved; several use cases; SSO likely; formal policy + risk register |
| L | 200-499 | IT and risk functions; procurement and vendor due diligence; RBAC; AI council |
| XL | 500+ | Enterprise rollout: data classification, DLP, permission-aware RAG, change management, board literacy, ISO 42001 alignment |

## 5a. Verify your own infrastructure claims

Never cite your own hosting as evidence of a hosting-location pattern without a live check of the
provider's data-centre list (via its API, not a marketing page). Lessons baked into this department:

- "We self-host in Australia" must never be said or implied to a client unless verified live.
- An Australian VPS, and far more so an Australian GPU box, is typically a **new procurement** with
  its own cost, lead time and security work. Price it, do not assume it.
- If a client needs Australian processing now, the researched routes are AWS Bedrock `au.*` or
  Azure Australia East, not an unverified box of your own.

## 6. Risk tiers (assigned by `ai-compliance-risk`, used by every skill)

| Tier | Meaning | Examples | Minimum controls |
|---|---|---|---|
| 1 Low | Internal productivity, no personal data, human uses output | Drafting internal docs, summarising public info | Acceptable use policy, register entry |
| 2 Moderate | Personal or confidential data, or customer-facing, human in the loop | Support chatbot with handoff, internal RAG over HR docs | + privacy check, eval baseline, logging, access control |
| 3 High | Decisions that significantly affect people's rights or interests (ADM), regulated sector, or autonomous action | Credit, hiring screens, claims triage, clinical scribes, agents that spend money | + impact assessment, ADM disclosure, human review design, red-team, monitoring, incident plan |
| 4 Prohibited / stop | Unlawful or unacceptable use | Covert biometric surveillance, manipulation, uses banned under EU AI Act Art 5 where EU applies | Do not build; explain why |

## 6a. Finding severity (one scale, used by every skill and agent)

| Severity | Meaning | Effect |
|---|---|---|
| Critical | Likely unlawful, or would leak data, or breaks a hard gate | Stop. Nothing goes live until it is resolved |
| High | Must be fixed before go-live | Blocks the go-live gate |
| Medium | Fix on an agreed date after go-live | Recorded with owner and date |
| Low | Improvement, no deadline | Recorded |

Always-blocking regardless of count: a permission leak, a PII leak, or an approval-gate bypass.
Do not restate this scale in a skill; reference it.

## 6b. Department scripts (one table, so a wrapper can trust them)

All eight are stdlib-only, print to stdout by default, and write a file only when asked. Every one
accepts `--out` for its markdown output (some also keep an older alias).

| Script | Skill | Does | Exit codes |
|---|---|---|---|
| `check_freshness.py` | `_shared` | Age-checks every `date checked` claim | 0 fresh, 1 stale, 2 input error |
| `estimate.py` | ai-proposal-pricing | Scope CSV to effort, fee and retainer | 0 ok, 2 scope rejected (nothing priced) |
| `ai_risk_register.py` | ai-compliance-risk | `seed` starter risks, `build` scores them | 0 ok, 1 input error |
| `readiness_score.py` | ai-readiness-assessment | Scorecard and Go/Wait gate | 0 ok, 2 input error |
| `iso42001_readiness_gap.py` | ai-governance-program | ISO 42001 clause gap percentage | 0 ok |
| `eval_compare.py` | ai-evals-security-testing | Baseline vs current evals | 0 PASS, 1 PASS WITH CONDITIONS, 2 FAIL, 3 no verdict or input error |
| `cost_trend.py` | ai-optimisation-llmops | Cost per task and trend flags | 0 ok, 1 flag raised, 3 input error |
| `portfolio.py` | ai-use-case-portfolio | Ranked use-case portfolio | 0 ok, 1 with `--strict` and an error row |

A non-zero exit is a finding to read, not a crash. Nothing here needs installing.

## 7. Output conventions

- Client-facing text passes a client-facing tone review (audience tag, `voice_lint.py` zero FAIL).
- Diagrams in Mermaid (renders in Markdown, Docs and the report renderer).
- Engagement files live in the client's workspace: discovery and meeting notes in `meetings/`,
  designs and scopes in `created/docs/strategy/`, compliance outputs in `created/docs/security/`,
  reports in `reports/adhoc-report/`. Filenames `{purpose}-{YYYY-MM-DD}.{ext}` (R5).
- Every deliverable with more than 3 numbers gets an R2 verifier in `scripts/verifiers/`.
- Australian English, no em dashes, no hype.

## 8. Logging

Log the action to your own engagement activity log.
`[YYYY-MM-DD HH:MM] [CLAUDE_CODE:<operator>] ACTION | client | detail | outcome`.
