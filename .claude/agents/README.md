# Agents: the specialist roles

Five role-gated subagents the skills delegate to. Each holds a hard guardrail that does not move.

| Agent | Does | Hard guardrail |
|---|---|---|
| `ai-architect.md` | Designs the solution: architecture views in Mermaid, data flows with trust boundaries, platform choice with Australian data-residency reasoning, build vs buy, ADRs; answers client technical questions in plain English | Output is a design, never a build or production change |
| `ai-engineer.md` | Builds approved designs in sandbox or staging: RAG pipelines, agents and automations, integrations, PII redaction, eval harnesses, runbooks | Never touches client production; deployment is a separate, client-approved step |
| `ai-compliance-officer.md` | Runs the compliance and risk review: risk tier, applicable obligations with status, ADM check, risk register, impact assessment, threat model, go-live sign-off | Read-only on client systems; never gives legal advice |
| `ai-security-tester.md` | Pre-launch and post-change testing: golden-set evals, red-teaming mapped to OWASP LLM Top 10 and MITRE ATLAS, RAG permission-leak tests, guardrail checks | Tests only systems you built or are authorised in writing to test; never production without written approval |
| `ai-optimiser.md` | The monthly improvement loop on live systems: reads traces, evals, cost and usage, samples failures, proposes the next change set with expected effect | Proposes changes, never deploys them |

Each agent file carries its own reading list (which skills and references it loads), its method, and its output contract. Claude Code picks these up automatically as project agents.
