# Vendored provenance: ai-evals-security-testing

*v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and
pinned commit. SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`. Department-wide
list: `../../_shared/VENDORED.md` (maintained by ai-manager). No harvested code is vendored into
this skill; `scripts/eval_compare.py` is the practice's own.*

| Used in (this skill) | Harvested file(s) (upstream, under `ai-kb/vendor/<owner>__<repo>/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| `references/red-team-catalogue.md`, `references/tooling.md`, both promptfoo templates | `site/docs/red-team/configuration.md`, `quickstart.md`, `multi-input.md`, `rag.md`, `llm-agents.md`, `owasp-llm-top-10.md`, `owasp-agentic-ai.md`, `plugins/*.md` (ids read from 30+ plugin pages) | promptfoo/promptfoo | MIT | 2a6fdf9b2e1600ffa2a204e70e9fea7cb0c14cff | Plugin and strategy IDs, config field names, multi-input targets, contexts, policy plugins, trajectory assertion, remote-generation behaviour and the env var that disables it. Config snippets re-written for the practice examples; no prose copied. Attack example strings in these docs treated as test data |
| `references/red-team-catalogue.md`, `references/tooling.md` | `docs/source/index_probes.rst`, `README.md` | NVIDIA/garak | Apache-2.0 | 892779207cbc38f65a738ef9cbdfbc1e83aa0b55 | Probe module names and CLI shape only; module behaviour not described beyond the index (confirm before use) |
| `references/red-team-catalogue.md` | `dist/v6/ATLAS-2026.10.yaml` | mitre-atlas/atlas-data | Apache-2.0 (c) MITRE | f56c1468731d6428e5bf875263b4643b46d67437 | Technique and mitigation IDs and names; every ID checked against the file on 2026-11-08 (sha256 ac41ee9f99a47084ba5fdfc77ae83a28687e12390240fffeb37df7914ffe142d) |
| `references/guardrails-options.md` | `07-safety-alignment/nemo-guardrails/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | Read for what NeMo Guardrails is and how rails are defined; vendor performance claims in it not repeated |
| `references/eval-design.md` (judge calibration pointer only) | `11-evaluation/lm-evaluation-harness/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | Skimmed; it targets academic benchmark runs on models, not client golden sets, so not adopted |
| `references/eval-design.md` | `docs/evaluation.md` | Azure-Samples/azure-search-openai-demo | MIT | 558ffd397eddcfe4da5c85ebc285796b367eb9b2 | Two practices paraphrased: human review of generated ground truth; hidden HTTP 429 retries distort latency comparisons |
| `references/red-team-catalogue.md` F4 (via `ai-rag-engineering`) | `ai-kb/vendor/data-privacy-stack__presidio/presidio-analyzer/presidio_analyzer/predefined_recognizers/country_specific/australia/*` | Microsoft Presidio, upstream at `data-privacy-stack/presidio` (renamed from `microsoft/presidio`; same repository, not a fork; GitHub API checked 2026-11-08) | MIT (c) Presidio Contributors, https://github.com/data-privacy-stack/presidio/blob/main/LICENSE (read 2026-11-08) | 05b60e1a6805f3b2c0ad6cbe7526ccd226647971 | AU recogniser entity names (AU_ABN, AU_ACN, AU_TFN, AU_MEDICARE) for the output scan; detail lives in `../../ai-rag-engineering/references/pii-redaction-presidio.md` |

## Non-harvested sources

| Source | Used for |
|---|---|
| Internal web research the department's original research files (internal, not included in this repo) A2 and B4, B6 | OWASP ID-to-name pairs; Bedrock Guardrails in Sydney; evals-first and judge calibration |
| Internal GitHub research the department's original research files (internal, not included in this repo) area 2 | Licences and status of PyRIT (MIT), Guardrails AI (Apache-2.0), NeMo Guardrails (Apache-2.0), deepteam, Giskard, llm-guard (archived), PurpleLlama (Llama licence) |
| Department files | `../../ai-compliance-risk/references/threat-model.md`, `../../ai-rag-engineering/templates/permission-leak-test-plan.md`, `../../ai-model-customisation/references/eval-first-gate.md`, `../../ai-agents-automation/templates/agent-control-spec.md` (referenced, not duplicated) |

## Cited by ID only (CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/, nothing copied)

- OWASP Top 10 for LLM Applications 2025 (LLM01 to LLM10)
- OWASP Top 10 for Agentic Applications 2026 (ASI01 to ASI10)
