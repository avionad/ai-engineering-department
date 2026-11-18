# Tool card: LLaMA-Factory (web UI fine-tuning)

*Adapted 2026-11-08 from Orchestra-Research/AI-Research-SKILLs `03-fine-tuning/llama-factory/SKILL.md`
(MIT, commit 773a52944ba4747a18bd4ae9ade53fff041adcbc; thin, points to upstream docs) and GitHub
research area 4 (LlamaFactory: Apache-2.0, "100+ models, web UI; good for client-operated tuning").*

## When to use

- A client's own engineers will operate retraining after handover and want a web UI rather than
  scripts.
- Quick comparison of several base models with the same dataset.

## DDD rules

- The web UI must not be exposed beyond the private network; it can start jobs and read datasets.
- Handover includes the exact config exported from the UI, the dataset card and the eval harness,
  so a retrain can be compared with the promoted model.
- Read the upstream docs at the pinned version; this card is a pointer, not a manual.
