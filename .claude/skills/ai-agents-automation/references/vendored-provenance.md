# Vendored provenance: ai-agents-automation

*v0.1.0, 2026-11-08. SHAs from `~/ai-kb/vendor/_harvest-manifest-2026-11-08.json`.
Department-wide list: `../../_shared/VENDORED.md`.*

| Used in (this skill) | Source file (upstream, under `~/ai-kb/vendor/<owner>__<repo>/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| `references/agent-controls.md` section 3 (failure handling: recoverable vs fatal, idempotent re-runnable steps, leave state consistent on abort) | `categories/09-meta-orchestration/multi-agent-coordinator.md` | VoltAgent/awesome-claude-code-subagents | MIT | ed74d115b7fb7026a22a4f816a8e3250f425e3b4 | **Ideas adapted**, rewritten for business automations; no text copied |
| Build options named in `references/voice-agents.md` | pipecat-ai/pipecat (not harvested, nothing copied) | pipecat-ai/pipecat | **BSD-2-Clause, verified live 2026-11-08** from the repo LICENSE file, https://github.com/pipecat-ai/pipecat/blob/main/LICENSE (SPDX `BSD-2-Clause` returned by https://api.github.com/repos/pipecat-ai/pipecat/license) | n/a (not harvested, no commit pinned) | Named as an option only; no code or text used |
| Build options named in `references/voice-agents.md` | livekit/agents (not harvested, nothing copied) | livekit/agents | **Apache-2.0, verified live 2026-11-08** from the repo LICENSE file, https://github.com/livekit/agents/blob/main/LICENSE (SPDX `Apache-2.0` returned by https://api.github.com/repos/livekit/agents/license) | n/a (not harvested, no commit pinned) | Named as an option only; no code or text used |

## Cited by ID only (CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/, nothing copied)

- OWASP Top 10 for LLM Applications 2025 (LLM01 to LLM10)
- OWASP Top 10 for Agentic Applications 2026 (ASI01 to ASI10)

ID-to-name pairs are taken from `ai-compliance-risk/references/threat-model.md`, which took them
from the Internal web research file, not from OWASP pages.

## Non-harvested sources

| Source | Used for |
|---|---|
| Internal web research 2026-11-08, sections B1 and B5 | HITL tiers, least-agency control list, ADM note on human approval, Gartner agentic cancellation prediction |
| `DDD Clients/Projects/ai-receptionist/CLAUDE.md` (DDD's own build, verified 2026-08-13) | Hosted-platform option, SIP import, call-loop rule, platform-neutral prompt and knowledge base |
| `n8n/n8n-architect` (live DDD skill) | Hand-off target; its assess-mode signals informed `process-selection.md` section 1 |
