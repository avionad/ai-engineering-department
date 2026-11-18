# Tool card: Axolotl (YAML-configured, multi-GPU fine-tuning)

*Adapted 2026-11-08 from Orchestra-Research/AI-Research-SKILLs `03-fine-tuning/axolotl/SKILL.md`
(MIT, commit 773a52944ba4747a18bd4ae9ade53fff041adcbc). Axolotl itself: Apache-2.0 (GitHub research
area 4). The source is a set of doc excerpts; read the Axolotl docs at the pinned version before use.*

## When to use

- Multi-GPU runs, reproducible YAML configs kept in the engagement repo, many model families, and
  methods beyond SFT (DPO, KTO, ORPO, GRPO per the source's description).
- Prefer Unsloth or plain TRL for a single-GPU LoRA run.

## Patterns from the source worth knowing

- **FSDP configuration** lives in the YAML (version, parameter offload, state-dict type, wrap policy).
- **Context parallelism** must divide the GPU count and reduces the number of distinct batches per
  step (so the effective global batch shrinks); recompute the learning-rate schedule.
- **Compressed saving** (`save_compressed: true`) reduces disk use and stays compatible with vLLM per
  the source.
- **Check interconnect bandwidth** with NCCL tests before blaming the config for slow multi-GPU runs.

## DDD rules

- Config files are versioned with the dataset card and eval results so a run can be reproduced.
- Same data residency and eval-first rules as every training tool.
