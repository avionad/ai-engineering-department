# ai-solution-architecture

The method skill the ai-architect agent follows for DDD's ai-automation department: requirement restatement, the cheapest-rung ladder (SaaS or configuration, no-code workflow, prompt plus tools, RAG, custom agent or app, model customisation), architecture views (context, container, data flow with trust boundaries and personal-data paths, sequence) in Mermaid, ADRs, build vs buy over total cost of ownership with sourced prices only, a non-functional requirements checklist (security, privacy, residency, availability, latency, cost, observability, exit), integration design (system of record per entity, sync direction, error handling), effort drivers for ai-proposal-pricing, and plain-English answers to end-customer technical questions.

**When to use:** Use when an AI or automation project needs a solution design before quote or build, or when a client's IT team asks how it will work.

**Trigger phrases:** design the solution, solution architecture, ai architecture, how should we build this, draw the architecture, architecture diagram, data flow diagram, trust boundaries, sequence diagram, which platform, build vs buy ai, buy or build, prompt vs rag vs fine-tune, adr, architecture decision record, non...

## How SKILL.md is organised

- Department relationships
- Method
- Output
- Rules
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/architecture-views.md` | **Architecture views and Mermaid conventions.** v0.1.0, 2026-11-08. DDD conventions. The four views follow the common context, container,. |
| `references/build-vs-buy.md` | **Build vs buy.** v0.1.0, 2026-11-08. Approach adapted from the upstream `chief-ai-officer-advisor` skill, whose. |
| `references/customer-technical-questions.md` | **Answering end-customer technical questions.** v0.1.0, 2026-11-08. DDD method. Standing answers live in `../../_shared/client-faq.md`; this file. |
| `references/integration-design.md` | **Integration design.** v0.1.0, 2026-11-08. DDD method. Pairs with `ai-agents-automation/references/agent-controls.md`. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-solution-architecture.** v0.1.0, 2026-11-08. SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`. |

## Templates

| File | What it holds |
|---|---|
| `templates/adr-template.md` | **ADR-{nnn}: {decision in a few words}.** What forces the decision: the requirement, constraints (residency, budget, skills, existing. |
| `templates/nfr-checklist.md` | **Non-functional requirements checklist.**. |
| `templates/solution-design-template.md` | **AI solution design: {use case}, {Client}.** Prepared by Design Data Dynamics, {date}. Version {n}. Engagement stage 3 (Design). Risk tier. |

*Skill version 0.1.0. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
