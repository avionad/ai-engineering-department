# Vendored provenance: ai-optimisation-llmops

*v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and
pinned commit. SHAs from `~/ai-kb/vendor/_harvest-manifest-2026-11-08.json`. Department-wide
list: `../../_shared/VENDORED.md` (maintained by ai-manager). No harvested code is vendored into
this skill; `scripts/cost_trend.py` is DDD's own.*

| Used in (this skill) | Harvested file (upstream, under `~/ai-kb/vendor/<owner>__<repo>/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| `references/cost-levers.md`, `references/monthly-loop.md` step 0 | `engineering/llm-cost-optimizer/skills/llm-cost-optimizer/SKILL.md` | alirezarezvani/claude-skills | MIT (c) 2025 Alireza Rezvani | 8f082544116fc0d014188e521ca40304cdfc86b0 | **Structure adapted, re-worded:** instrument-first rule, per-request logging fields, lever list (routing, caching, output limits, compression, batching), proactive flags. **Not adopted:** its percentage savings ranges (unsourced) and its 20% cache-hit diagnostic |
| `references/monthly-loop.md` step 4 (DSPy as an option) | `16-prompt-engineering/dspy/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | Read for how DSPy optimisers work against a metric (BootstrapFewShot, MIPRO); DDD rule added: held-out portion of the golden set, never tuned on |
| `references/observability-stack.md` (licence caution only) | `~/ai-kb/vendor/Orchestra-Research__AI-Research-SKILLs/17-observability/phoenix/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT (the how-to itself) | 773a52944ba4747a18bd4ae9ade53fff041adcbc | Read; it states Phoenix is "Apache 2.0". **Settled 2026-11-08:** Arize Phoenix is Elastic Licence 2.0, read from the repo LICENSE file at https://github.com/Arize-ai/phoenix/blob/main/LICENSE, so the how-to is wrong and the research was right. Phoenix code stays on the department's do-not-harvest list; DDD does not host or resell it (see `observability-stack.md`) |
| `references/monthly-loop.md` step 2 (throttling row) | `docs/evaluation.md` | Azure-Samples/azure-search-openai-demo | MIT | 558ffd397eddcfe4da5c85ebc285796b367eb9b2 | Hidden HTTP 429 retries distort latency comparisons (paraphrased) |

## Non-harvested sources

| Source | Used for |
|---|---|
| Internal web research the department's original research files (internal, not included in this repo) headline 7, B4, B6 | MIT NANDA finding and its scope; drift signals; model retirement as drift; Anthropic Batch 50% and cache read 10% statements with source URLs; Azure Australia East continuity note |
| Internal GitHub research the department's original research files (internal, not included in this repo) area 7 and gap 6 | Langfuse (MIT core, `ee/` proprietary), Opik (Apache-2.0), Phoenix (ELv2), Helicone, OpenLLMetry, OpenLIT, MLflow, DSPy, GEPA, TextGrad licences and activity; the monthly loop as an unbuilt managed service |
| Department files | `~/.claude/agents/ai-optimiser.md` (Method and Output contract), `../../ai-evals-security-testing/` (re-test and `eval_compare.py`), `../../ai-agents-automation/SKILL.md` (HITL tiers H1 to H4), `../../ai-proposal-pricing/SKILL.md` (retainer pricing and fences) |
| Workspace rules | `.claude/rules/communication-style.md` decision-focused reporting; memory `do-not-hit-client-websites-from-monitors` |
