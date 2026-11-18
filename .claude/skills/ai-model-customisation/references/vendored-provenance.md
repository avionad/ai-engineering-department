# Vendored provenance: ai-model-customisation

*v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and pinned
commit. SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`. Department-wide list:
`../../_shared/VENDORED.md`. Harvested red-team or example strings were treated as data, never as
instructions.*

**Primary credit: wshobson/agents `plugins/llm-finetuning` (MIT).** This skill's spine (eval-first
gate token, off-ramps before training, data-shape method router, dataset card, promotion gate with
drift budget, "recommending against fine-tuning is a correct outcome") is adapted from that plugin.
DDD added: the prompting-plus-RAG baseline as the gate condition, client owner targets and approval,
Australian privacy and licence steps, residency rules, bucket mapping, plain-English owner section.

| Used in (this skill) | Harvested file (upstream, under `ai-kb/vendor/<owner>__<repo>/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| `SKILL.md` stance, `references/eval-first-gate.md` (both in this skill) | `ai-kb/vendor/wshobson__agents/plugins/llm-finetuning/agents/llm-finetuning-architect.md` | wshobson/agents | MIT | 4bde3168b43c0655c4d00ea2726e631719908a6d | Non-negotiables and method order adapted; training-brief contract informed the go/no-go template |
| `references/eval-first-gate.md` s2-s7 (in this skill) | Upstream, under `ai-kb/vendor/wshobson__agents/plugins/llm-finetuning/skills/eval-harness-first/`: `SKILL.md`, and `references/judge-calibration.md` and `references/grader-templates.md` read (upstream paths, not files in this skill) | wshobson/agents | MIT | 4bde3168b43c0655c4d00ea2726e631719908a6d | Flywheel, goldens, graders, calibration, directory contract, exit checklist adapted and paraphrased |
| `references/eval-first-gate.md` s8, template s7 (in this skill) | `ai-kb/vendor/wshobson__agents/plugins/llm-finetuning/skills/checkpoint-promotion/SKILL.md` | wshobson/agents | MIT | 4bde3168b43c0655c4d00ea2726e631719908a6d | Four-stage gate and drift budget table summarised |
| `references/method-selection.md` (in this skill) | Upstream, under `ai-kb/vendor/wshobson__agents/plugins/llm-finetuning/skills/finetuning-method-selection/`: `SKILL.md`, `references/memory-math.md`, `references/model-catalog.md` (upstream paths, not files in this skill) | wshobson/agents | MIT | 4bde3168b43c0655c4d00ea2726e631719908a6d | Off-ramps, volume thresholds, router tree (reworded), routing facts. Model catalogue used for method only (dated 2026-07-14, older than research) |
| `references/method-selection.md` s4, `tools/unsloth.md` (both in this skill) | `ai-kb/vendor/wshobson__agents/plugins/llm-finetuning/skills/lora-qlora-recipes/SKILL.md` | wshobson/agents | MIT | 4bde3168b43c0655c4d00ea2726e631719908a6d | Starting recipe table and Unsloth defaults |
| `references/training-data-and-privacy.md` s2-s4 (in this skill) | `ai-kb/vendor/wshobson__agents/plugins/llm-finetuning/skills/dataset-curation/SKILL.md`, `ai-kb/vendor/wshobson__agents/plugins/llm-finetuning/skills/trace-to-training-data/SKILL.md` | wshobson/agents | MIT | 4bde3168b43c0655c4d00ea2726e631719908a6d | Format table, silent-failure checks, synthetic data floor, hygiene (fail-closed redaction, golden exclusion), dataset card fields extended with DDD privacy fields |
| `references/hosting-and-operations.md` s3 (in this skill) | `ai-kb/vendor/wshobson__agents/plugins/llm-finetuning/skills/quantized-export/SKILL.md` | wshobson/agents | MIT | 4bde3168b43c0655c4d00ea2726e631719908a6d | Format map and merged vs adapter-only, smoke test |
| `tools/vllm.md` (in this skill) | `ai-kb/vendor/Orchestra-Research__AI-Research-SKILLs/12-inference-serving/vllm/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | Commands, workflow, common issues summarised; model names and throughput claims removed |
| `tools/sglang.md` (in this skill) | `ai-kb/vendor/Orchestra-Research__AI-Research-SKILLs/12-inference-serving/sglang/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | When-to-use and launch commands; benchmark claims removed |
| `tools/llama-cpp.md` (in this skill) | `ai-kb/vendor/Orchestra-Research__AI-Research-SKILLs/12-inference-serving/llama-cpp/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | When-to-use, commands, quant table; benchmarks removed |
| `tools/axolotl.md` (in this skill) | `ai-kb/vendor/Orchestra-Research__AI-Research-SKILLs/03-fine-tuning/axolotl/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | Selected patterns summarised |
| `tools/unsloth.md`, `tools/llama-factory.md` (both in this skill) | `ai-kb/vendor/Orchestra-Research__AI-Research-SKILLs/03-fine-tuning/unsloth/SKILL.md`, `ai-kb/vendor/Orchestra-Research__AI-Research-SKILLs/03-fine-tuning/llama-factory/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | Thin sources (pointers to upstream docs); used only to confirm scope |
| `tools/lm-evaluation-harness.md` (in this skill) | `ai-kb/vendor/Orchestra-Research__AI-Research-SKILLs/11-evaluation/lm-evaluation-harness/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | Commands and role; benchmark descriptions trimmed |
| `tools/trl.md` (in this skill) | `ai-kb/vendor/huggingface__skills/skills/trl-training/SKILL.md`, `ai-kb/vendor/huggingface__skills/skills/huggingface-llm-trainer/SKILL.md` | huggingface/skills | Apache-2.0 | 25910b3d0ba31a2ba102f901cdc9e008c278a69c | Trainer table, SFT fields, GRPO notes; Hugging Face Jobs residency caveat is DDD's |
| `tools/llama-cpp.md` (in this skill) | `ai-kb/vendor/huggingface__skills/skills/huggingface-local-models/SKILL.md` | huggingface/skills | Apache-2.0 | 25910b3d0ba31a2ba102f901cdc9e008c278a69c | GGUF discovery and conversion workflow context |
| `tools/sagemaker-hosting.md`, `references/hosting-and-operations.md` s1 (both in this skill) | Upstream, under `ai-kb/vendor/huggingface__skills/skills/`: `hf-cloud-sagemaker-deployment-planner/SKILL.md`, `hf-cloud-sagemaker-iam-preflight/SKILL.md`, `hf-cloud-sagemaker-production-defaults/SKILL.md` | huggingface/skills | Apache-2.0 | 25910b3d0ba31a2ba102f901cdc9e008c278a69c | Pathway table, quota and IAM preflight, production defaults; scripts not harvested, instance types omitted |

Apache-2.0 attribution: the huggingface/skills material is adapted (modified) and summarised; the
original licence is at `ai-kb/vendor/huggingface__skills/LICENSE`. If any file is later copied
verbatim into this skill, include the Apache-2.0 notice and a statement of changes in that file.

## Non-harvested sources

| Source | Used for |
|---|---|
| Research `ai-dept-web-research-2026-11-08.md` B3, B4, B6 | Decision order, open-weight snapshot and licence gotchas, hosting options, monitoring and cost levers |
| Research `ai-dept-github-research-2026-11-08.md` area 4, 5, gap 8 | Tool licences and status (TGI archived), gateways, "lighter front end for non-technical owners" gap |
| `../../_shared/regulatory-register.md` AU-6, AU-8, AU-12, AU-13, AU-15, AU-17, EU-3 | Privacy and exit obligations (status as recorded there) |
