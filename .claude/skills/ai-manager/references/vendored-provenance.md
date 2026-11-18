# Vendored provenance -- ai-manager

*What this skill's orchestration discipline was adapted from. Licences and the department-wide
table: `../../_shared/VENDORED.md`. Harvest manifest with full SHAs:
`ai-kb/vendor/_harvest-manifest-2026-11-08.json`.*

| Upstream file (upstream, under `ai-kb/vendor/<owner>__<repo>/`) | Repo and licence | Pinned commit | What we took | What we did not take |
|---|---|---|---|---|
| `skills/subagent-driven-development/SKILL.md` | obra/superpowers, MIT | 22f0b463e7a5e579904dd6211a520321035526f7 | One specialist per task with a clean brief; review what comes back before passing it on; decide rather than stall | Its code-review two-stage flow and developer-workflow framing: this is a consulting lifecycle, not a dev loop |
| `skills/writing-plans/SKILL.md` | obra/superpowers, MIT | same | Writing the step list before working it, and re-checking it before declaring done | Its plan file format (we use the engagement state file) |
| `skills/dispatching-parallel-agents/SKILL.md` | obra/superpowers, MIT | same | Parallel only for independent work; name the inputs and the output file in the brief | Its concurrency level (DDD's cap is two, per the practice owner) |
| `skills/verification-before-completion/SKILL.md` | obra/superpowers, MIT | same | Verify at the layer of the claim before reporting done | Nothing material |
| `categories/09-meta-orchestration/multi-agent-coordinator.md` | VoltAgent/awesome-claude-code-subagents, MIT | ed74d115b7fb7026a22a4f816a8e3250f425e3b4 | Agents coordinate through shared files and the orchestrator, never directly; no invented metrics | Its agent taxonomy and its performance targets, which are unsourced |

Everything else in `ai-manager` is DDD's own: the engagement lifecycle and its gates, the routing
table, the size bands and risk tiers (in `_shared/`), and the things-to-raise-unprompted list.
