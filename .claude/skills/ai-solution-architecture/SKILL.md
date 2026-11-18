---
name: ai-solution-architecture
description: "Use when an AI or automation project needs a solution design before quote or build, or when a client's IT team asks how it will work. The method skill the ai-architect agent follows for DDD's ai-automation department: requirement restatement, the cheapest-rung ladder (SaaS or configuration, no-code workflow, prompt plus tools, RAG, custom agent or app, model customisation), architecture views (context, container, data flow with trust boundaries and personal-data paths, sequence) in Mermaid, ADRs, build vs buy over total cost of ownership with sourced prices only, a non-functional requirements checklist (security, privacy, residency, availability, latency, cost, observability, exit), integration design (system of record per entity, sync direction, error handling), effort drivers for ai-proposal-pricing, and plain-English answers to end-customer technical questions."
when_to_use: "design the solution, solution architecture, ai architecture, how should we build this, draw the architecture, architecture diagram, data flow diagram, trust boundaries, sequence diagram, which platform, build vs buy ai, buy or build, prompt vs rag vs fine-tune, adr, architecture decision record, non-functional requirements, nfr checklist, integration design, system of record, sync direction, effort drivers for the quote, explain this to the client's it team, technical questions from the customer, solution design document"
trigger: "design the solution, solution architecture, ai architecture, how should we build this, draw the architecture, architecture diagram, data flow diagram, trust boundaries, sequence diagram, which platform, build vs buy ai, buy or build, prompt vs rag vs fine-tune, adr, architecture decision record, non-functional requirements, nfr checklist, integration design, system of record, sync direction, effort drivers for the quote, explain this to the client's it team, technical questions from the customer, solution design document"
version: 0.1.0
---

<!-- Changelog: 2026-11-08 (v0.1.0) -- Phase 2 build per ai-automation blueprint. -->

Read `../_shared/engagement-conventions.md` first.

# AI Solution Architecture (method)

The `ai-architect` agent (`.claude/agents/ai-architect.md`) holds the role, the rules and the
output contract. This skill holds the depth it works from. Stage 3 (Design) of the lifecycle:
the exit gate is an architecture and data-flow diagram, a platform choice with residency, a
build-vs-buy decision and at least one ADR. The output is a design, never a build.

## Department relationships

- **Followed by** the `ai-architect` agent; invoked through `ai-manager` after discovery and the
  risk tier exist.
- **Inputs**: discovery notes and the solution design brief (`ai-discovery-scoping`, starting
  pattern from `../ai-discovery-scoping/references/solution-patterns.md` there), the risk tier, obligations and threat
  model (`ai-compliance-risk`), readiness findings, the industry pack, `_shared/client-faq.md`.
- **Hands to**: `ai-proposal-pricing` (effort drivers by delivery bucket, run-cost inputs);
  `ai-compliance-officer` agent (risks, data flows and trust boundaries for the threat model);
  `ai-engineer` as the build spec; `ai-agents-automation` (agent control spec),
  `ai-rag-engineering`, `ai-model-customisation`, `ai-deployment-platforms` for
  specialist depth; `ai-evals-security-testing` for the
  eval and test plan; `ai-optimisation-llmops` for run and monitoring needs.
- **Live DDD skills it can hand to**: `product/app-stack-decision` (stack and hosting for an app
  with a UI), `product/documentation-and-adrs` (ADR conventions in a code repository),
  `product/product-builder` (any app build), `n8n/n8n-architect` (workflow builds).

## Method

### 1. Restate the requirement

One paragraph the client would recognise: the process, users and how many, volumes, data classes,
systems, success measure with its baseline, risk tier, size band, jurisdiction. Then list
**load-bearing unknowns** as open questions with who can answer them. Never fill a gap with an
assumption silently; an assumption that must stand is written as one, with the risk if wrong.

### 2. Climb the ladder, cheapest rung first

| Rung | What it is | Move up only when |
|---|---|---|
| 1 SaaS or configuration | A feature of a tool the client has or can buy (CRM automation, M365 or Google feature, a vertical SaaS) | It cannot meet a must-have requirement, residency or control need |
| 2 No-code or low-code workflow | n8n or the client's platform automation, rules plus one or two LLM steps | The path varies too much for a fixed flow, or volume or latency rules it out |
| 3 Prompt plus tools on a hosted model | Fixed prompt, structured output, a few scoped tools | It needs knowledge the prompt cannot carry |
| 4 RAG | Retrieval over company content, permission-aware for M+ | Retrieval plus prompting fails the baseline eval, or a UI or multi-step agent is required |
| 5 Custom agent or app | Code: agent with tools, custom UI, orchestration | A baseline eval shows prompting and RAG fall short on behaviour, format, cost or latency |
| 6 Model customisation | Fine-tune or distil an open-weight model | (top rung) |

Every rung above the first carries a one-line reason the rung below fails. This is the
agent's method step 2 and the research B3 decision order (prompt, RAG or tools, fine-tune,
distil). Fine-tuning does not reliably add fresh facts.

### 3. Build vs buy

Compare at most three options over the same period (DDD default three years) on total cost of
ownership and on the things money does not capture: residency, control, lock-in, exit path,
operational burden, time to value. Method and worksheet: `references/build-vs-buy.md` (approach
adapted from the alirezarezvani chief-ai-officer-advisor calculator, MIT, credited there). Every
unit price carries a vendor URL and date checked, or it is PENDING_VERIFICATION. No figures
from the harvested calculator are used.

### 4. Choose the platform with residency stated

Map each data class to where it may be processed and stored, using the deployment table in
`ai-discovery-scoping/references/solution-patterns.md` and re-verifying any model or region
claim live. Vector store, logs and caches sit in the same region as the model for a residency
claim to hold. State the CLOUD Act caveat for US-headquartered providers where relevant.

### 5. Draw the views

`references/architecture-views.md` has the four views and the Mermaid conventions:

1. **Context**: the system, its users and every external system, with regions.
2. **Container**: the deployable parts (workflow engine, model endpoint, vector store, app,
   database, queue) and how they talk.
3. **Data flow with trust boundaries**: where data crosses an organisational, network or vendor
   boundary, and every path personal data takes, including logs and backups.
4. **Sequence** for the key interaction (and the approval path for anything that acts).

### 6. Non-functional requirements

Walk `templates/nfr-checklist.md`: security, privacy, residency, availability, latency,
throughput, cost, observability, accessibility, maintainability, exit and portability. Each item
gets a target the client agrees, "not required", or an open question. Targets come from the
client, never from a template default.

### 7. Integration design

`references/integration-design.md`: system of record per entity, sync direction and frequency,
identifiers and matching, write permissions, error handling, idempotency, rate limits, and what
happens when each connected system is down.

### 8. Access control (M and above)

Identity provider and SSO; roles; how permissions reach retrieval (filter by the querying user's
identity, not the app's); sync and revocation latency; deny by default; audit logging. For XL,
data classification and DLP (coordinate with `ai-enterprise-rollout`).

### 9. Least agency for anything that acts

Tools, credential scope, approvals for irreversible, financial or customer-facing actions, caps,
kill switch, logs: summarised in the design, specified in full in the agent control spec
(`ai-agents-automation/templates/agent-control-spec.md`).

### 10. Record decisions

One ADR per significant choice (`templates/adr-template.md`): platform, rung, build vs buy,
retrieval approach, hosting, identity. In a code repository with an ADR convention, follow
`product/documentation-and-adrs` instead.

### 11. Extract effort drivers for the quote

For each design element, name the delivery bucket (the nine slugs in
`ai-discovery-scoping/references/delivery-buckets.md`, which `ai-proposal-pricing`'s estimator
accepts exactly) and the drivers that make it bigger: number of document types, systems without
APIs, write approvals, permission models, user groups, eval depth, consultation steps. List
run-cost inputs (volumes, tokens per task, hosting) for the run-cost sheet; unit prices stay with
`ai-proposal-pricing` and must be sourced. Never put hours or prices in the design.

### 12. Answer the client's technical questions

`references/customer-technical-questions.md`: plain English first, technical appendix for IT,
sources for every factual claim, the conventions disclaimer on anything regulatory.

## Output

`{client}/created/docs/strategy/ai-solution-design-{YYYY-MM-DD}.md` from
`templates/solution-design-template.md`, whose sections match the agent's output contract.
ADRs live in the design or, for long engagements, as separate `adr-{nnn}-{slug}-{YYYY-MM-DD}.md`
files in the same folder. Update the `ai-architect` section of the engagement state file.

## Rules

- Never name a model version, region, price or feature from memory: vendor page URL and date,
  or PENDING_VERIFICATION (agent rule; conventions s3).
- Recommend one option and say why; note the strongest alternative in one line.
- Plain English in the body; IT depth in appendices.
- No legal conclusions; regulatory points go to `ai-compliance-officer` with the disclaimer.
- If a file save is refused, stop and report it. Never write by another route.

## Known gaps (v0.1.0)

- No worked client design yet; first real engagement becomes the reference example.
- Build-vs-buy worksheet is manual (no script); a sourced-price calculator is a v0.2 candidate.

Provenance: `references/vendored-provenance.md`.
