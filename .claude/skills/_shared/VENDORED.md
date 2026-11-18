# Vendored and adapted open-source material -- ai-automation department

*Harvested 2026-11-08 into `ai-kb/vendor/` at pinned commits (manifest:
`ai-kb/vendor/_harvest-manifest-2026-11-08.json`). Downloaded as raw text via the GitHub API;
nothing cloned, installed or executed during harvest. The file counts in the tables below were
counted from disk on 2026-11-08 and reconciled against the manifest; they sum to 692.*

## Security scan (re-run and re-counted from disk, 2026-11-08)

**Scope: 692 files across 17 repo folders** in `ai-kb/vendor/` (693 counting the harvest
manifest itself). The earlier "547 files" figure was the Phase 1 scope only; the Phase 2/3 harvest
added six repos (promptfoo, garak, Presidio, azure-search-openai-demo, huggingface/skills,
Orchestra-Research) and the mitre-atlas v6 re-harvest added two files.

All 692 files are UTF-8 readable and **none contains hidden or bidirectional unicode** (zero-width
space / non-joiner / joiner, LTR and RTL marks, bidi overrides and isolates, word joiner, BOM,
soft hyphen, invisible maths operators): zero hits. Injection-phrase hits were all topical:
documents about LLM security discussing "system prompt", and deliberate attack examples inside the
promptfoo and garak red-team documentation, which are test data. None was an instruction addressed
to an agent.

**Python files: the 8 scripts the practice runs, and 23 upstream files we never execute.**

| | Where they live | Count | Imports | Do we run them |
|---|---|---|---|---|
| The practice scripts we run | in the department itself, not in the vendor folder | 8 | stdlib only: `argparse`, `calendar`, `collections`, `csv`, `datetime`, `json`, `math`, `os`, `re`, `sys`, `typing`. No network, no `subprocess`, nothing to install | Yes |
| Upstream reference files | `ai-kb/vendor/` | 23 | 18 (all under `alirezarezvani__claude-skills/`) import stdlib only: `argparse`, `json`, `sys`, `textwrap`, `typing`. The other 5 are upstream Presidio recogniser modules under `data-privacy-stack__presidio/presidio-analyzer/.../country_specific/australia/`: four import `presidio_analyzer` and `__init__.py` relative-imports those four, so they cannot run without Presidio installed | **No, never** |

The 8 the practice scripts are `_shared/check_freshness.py` plus one each in `ai-proposal-pricing`,
`ai-compliance-risk`, `ai-readiness-assessment`, `ai-governance-program`,
`ai-evals-security-testing`, `ai-optimisation-llmops` and `ai-use-case-portfolio`
(`engagement-conventions.md` s6b lists them with their exit codes). The Presidio recognisers are
reference material for entity names and detection approach only; a client build installs Presidio
from its published package, never from these files. Vendored code is not executed on this box
without a quarantine review (`ai-kb/README.md`).

## Phase 1 harvest

| Repo | Licence | Pinned commit | Files | What we use | Used by |
|---|---|---|---|---|---|
| wshobson/agents | MIT | 4bde3168b43c0655c4d00ea2726e631719908a6d | 33 (`plugins/llm-finetuning/`) | Fine-tuning architect, method selection, eval-first rule | ai-model-customisation (Phase 2), ai-architect interim |
| alirezarezvani/claude-skills | MIT | 8f082544116fc0d014188e521ca40304cdfc86b0 | 54 | iso42001-specialist (risk register builder, AIMS gap analyser), eu-ai-act-specialist, aims-audit, chief-ai-officer-advisor (build vs buy, cost economics), llm-cost-optimizer | ai-compliance-risk, ai-governance-program, ai-discovery-scoping, ai-optimisation-llmops (Phase 3) |
| obra/superpowers | MIT | 22f0b463e7a5e579904dd6211a520321035526f7 | 15 | subagent-driven-development, writing-plans, dispatching-parallel-agents, verification-before-completion | ai-manager orchestration discipline |
| Sushegaad/Claude-Skills-Governance-Risk-and-Compliance | MIT | 5a9afcfce98efa4d64f75bead5e544ee06c38154 | 407 | ISO 42001 / NIST AI RMF / EU AI Act skills, with-vs-without-skill eval method | ai-compliance-risk, ai-governance-program, department eval method |
| cosai-oasis/secure-ai-tooling | Apache-2.0 | 622605a13fafaa2784acbdbe3f8d23ee22da4be7 | 11 (`risk-map/yaml/`) | Risk, control, component and framework mappings | ai-compliance-risk risk register seed |
| mitre-atlas/atlas-data | Apache-2.0 | f56c1468731d6428e5bf875263b4643b46d67437 | 4 on disk after the v6 re-harvest: `LICENSE`, `dist/ATLAS-latest.yaml` (a 20-byte pointer stub), `dist/v6/ATLAS-2026.10.yaml`, `dist/v6/ATLAS-latest.yaml` | The v6 file's techniques and mitigations (the top-level `dist/ATLAS-latest.yaml` stub is unusable) | ai-compliance-risk threat model |
| canada-ca/aia-eia-js | MIT | b62573389db4946b4d70b7fa62c4ca8d9990dba3 | 2 | Scored algorithmic impact questionnaire structure | ai-compliance-risk screening + impact assessment |
| anthropics/financial-services | Apache-2.0 | 60565064557ca77b12f62aa7877f365d111c129d | 2 | ai-readiness gate method (Go/Wait, ranked actions) | ai-readiness-assessment |
| OneWave-AI/claude-skills | MIT | b2267d9171af4f56848d82992381b20b89b44056 | 5 | ai-readiness-assessment rubric | ai-readiness-assessment |
| github/ai-adoption-playbook | CC BY 4.0 (attribution required) | 95c00131a3a88bf5c7df737b6676d2038e821fcf | 13 (main playbook, 7 `pillar_docs/`, LICENSE, README, 3 `.github/` files) | Adoption playbook structure | ai-readiness-assessment, ai-enterprise-rollout (Phase 2) |
| VoltAgent/awesome-claude-code-subagents | MIT | ed74d115b7fb7026a22a4f816a8e3250f425e3b4 | 2 | multi-agent-coordinator honesty and coordination rules | ai-manager |

## Phase 2/3 harvest (fetched 2026-11-08, included in the scan above)

| Repo | Licence | Pinned commit | Files | What we use | Used by |
|---|---|---|---|---|---|
| promptfoo/promptfoo | MIT | 2a6fdf9b2e1600ffa2a204e70e9fea7cb0c14cff | 97 (`site/docs/red-team/`) | Red-team plugin and strategy catalogue, config patterns | ai-evals-security-testing |
| NVIDIA/garak | Apache-2.0 | 892779207cbc38f65a738ef9cbdfbc1e83aa0b55 | 4 | Probe taxonomy | ai-evals-security-testing |
| Microsoft Presidio, now at `data-privacy-stack/presidio` (see the naming note below) | MIT (c) Presidio Contributors | 05b60e1a6805f3b2c0ad6cbe7526ccd226647971 | 6 | Australian recognisers (ABN, ACN, Medicare, TFN) | ai-rag-engineering, ai-evals-security-testing |
| Azure-Samples/azure-search-openai-demo | MIT | 558ffd397eddcfe4da5c85ebc285796b367eb9b2 | 5 (`docs/`) | Permission-aware retrieval (login and ACL), ingestion, productionising, evaluation | ai-rag-engineering |
| huggingface/skills | Apache-2.0 | 25910b3d0ba31a2ba102f901cdc9e008c278a69c | 21 | SageMaker deployment planner, IAM preflight, LLM trainer, TRL | ai-deployment-platforms, ai-model-customisation |
| Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | 11 | vLLM, SGLang, llama.cpp, Unsloth, Axolotl, LLaMA-Factory, lm-eval-harness, NeMo Guardrails, DSPy, Phoenix how-tos (Phoenix itself is Elastic Licence 2.0: client self-host only) | ai-model-customisation, ai-deployment-platforms, ai-evals-security-testing, ai-optimisation-llmops |
| mitre-atlas/atlas-data `dist/v6/ATLAS-2026.10.yaml` | Apache-2.0 | f56c1468731d6428e5bf875263b4643b46d67437 | the re-harvest added 2 files to the mitre-atlas folder (counted in its row above), of which this is the usable one (sha256 ac41ee9f99a47084ba5fdfc77ae83a28687e12390240fffeb37df7914ffe142d) | Current ATLAS techniques (the top-level v6 pointer file alone was empty) | ai-compliance-risk, ai-evals-security-testing |

## Presidio naming (verified live 2026-11-08)

Presidio is **Microsoft's** open-source PII detection and anonymisation framework. The repository
has been renamed from `microsoft/presidio` to `data-privacy-stack/presidio`: it is the **same
repository** (GitHub repository ID 132129752) and GitHub serves the old path as a permanent
redirect, so `data-privacy-stack/presidio` is upstream and **not a fork of** `microsoft/presidio`.
Checked this session against `https://api.github.com/repos/microsoft/presidio` (HTTP 301 to
`https://api.github.com/repositories/132129752`, which resolves to `data-privacy-stack/presidio`)
and `https://api.github.com/repos/data-privacy-stack/presidio` (`"fork": false`, no parent, no
source). Licence MIT (c) Presidio Contributors, read from the repo LICENSE file,
https://github.com/data-privacy-stack/presidio/blob/main/LICENSE.

We harvested from `ai-kb/vendor/data-privacy-stack__presidio/` at the pinned SHA above (SHA
unchanged). Asked whose PII library the practice uses, the correct answer is "Microsoft's Presidio, now
maintained in the `data-privacy-stack` organisation". Nothing was copied from it, so there is no
licence exposure either way.

## github/ai-adoption-playbook `pillar_docs/` (reconciled 2026-11-08)

All 13 files are on disk, **including `pillar_docs/`**: `advocates.md`,
`communities_of_practice.md`, `dri.md`, `exec_support.md`, `policies_and_guardrails.md`,
`right_fit_tooling.md`, `training.md`. So `pillar_docs/` **was harvested**. It was **not mined**
for v0.1.0: every adapted passage in the department traces to the main `github_ai_playbook.md`,
which itself covers the advocates network, communities of practice, the DRI role and the two-tier
tool policy in full. A v0.2 pass should mine the deep-dives for the champions and training
sections. `ai-readiness-assessment` and `ai-enterprise-rollout` provenance files now say the same.

## Cite-only and do-not-harvest

**Cite-only (not copied):** OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic
Applications (CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/) -- IDs and names only.

**Do not harvest** (licence): Onyx / LiteLLM / Langfuse `ee/` folders, Arize Phoenix (Elastic
Licence 2.0, confirmed from the repo LICENSE file 2026-11-08,
https://github.com/Arize-ai/phoenix/blob/main/LICENSE), PurpleLlama (Llama licence), Open WebUI
(branding clause), Dify (modified Apache), n8n core (Sustainable Use), borghei/Claude-Skills
(Commons Clause), any NC/ND or unlicensed repo.

Also used: github/ai-adoption-playbook main playbook (CC BY 4.0, attribution and change notice in
`ai-enterprise-rollout/references/vendored-provenance.md`) and VoltAgent
multi-agent-coordinator failure-handling ideas (MIT) in `ai-agents-automation`.

Each skill that adapts material also lists the specific files in its own
`references/vendored-provenance.md`.
