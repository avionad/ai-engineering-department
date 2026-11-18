# ai-agents-automation

Chooses rules-based automation first and AI only where judgement or unstructured input needs it, designs agents under least agency (scoped credentials, tool allow-lists, human approval for irreversible, financial or customer-facing actions, spend caps, kill switch, logging, idempotency, retries and error queues) mapped to OWASP Agentic Top 10 IDs, designs human-in-the-loop, covers voice agent build and buy options with recording consent flagged, and hands workflow builds to n8n-architect and UI apps to product-builder. Ships the agent control spec and runbook templates.

**When to use:** Use when a DDD client wants a business process automated, or an AI agent, customer support agent or voice receptionist built, covering document intake, email triage, CRM automation, data enrichment and finance and back-office work, customer support agents or voice agents.

**Trigger phrases:** automate this process, ai agent for the business, build an agent, process automation, back-office automation, document intake automation, email triage, inbox automation, crm automation, data enrichment, invoice capture, accounts payable automation, reconciliation automation, quote generation automat...

## How SKILL.md is organised

- Department relationships
- Protocol
- Rules first, AI second
- Human-in-the-loop tiers (research B5)
- Least agency (non-negotiable for anything that acts)
- Voice agents
- Hand-offs
- Industry use cases
- Output conventions
- Do not
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/agent-controls.md` | **Agent and automation controls (least agency).** v0.1.0, 2026-11-08. Control set from the Internal web research B5 (OWASP Agentic Top 10 2026, ACSC. |
| `references/automation-patterns.md` | **Automation patterns.** v0.1.0, 2026-11-08. Deepens the solution patterns in. |
| `references/industry-use-case-library.md` | **Industry automation and agent use-case library.** v0.2.0, 2026-11-08. Built from the research industry matrix (`ai-dept-web-research-2026-11-08.md`). |
| `references/process-selection.md` | **Process selection: what to automate, and with what.** v0.1.0, 2026-11-08. DDD method. Builds on `ai-discovery-scoping/references/use-case-qualification.md`. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-agents-automation.** v0.1.0, 2026-11-08. SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`. |
| `references/voice-agents.md` | **Voice agents.** v0.1.0, 2026-11-08. Sources: solution pattern P4 in `ai-discovery-scoping`; GitHub research. |

## Templates

| File | What it holds |
|---|---|
| `templates/agent-control-spec.md` | **Agent control spec: {automation or agent name}.** What it does, in two sentences. What it must never do (explicit list). |
| `templates/automation-runbook.md` | **Runbook: {automation name}.** Version {n}, {date}. Built by Design Data Dynamics. Agent control spec: {link}. |

*Skill version 0.1.0. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
