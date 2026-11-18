# Tool card: lm-evaluation-harness (general capability drift suite)

*Adapted 2026-11-08 from Orchestra-Research/AI-Research-SKILLs
`11-evaluation/lm-evaluation-harness/SKILL.md` (MIT, commit 773a52944ba4747a18bd4ae9ade53fff041adcbc).
lm-evaluation-harness itself: MIT (EleutherAI; GitHub research area 4, "benchmark baselines before and
after tuning"). Check task names and flags against the harness docs at the pinned version.*

## Role in our gate

It supplies the **frozen general-capability part of the drift suite** (wshobson's promotion gate
compares the checkpoint with the base-model baseline on standard benchmarks plus domain-adjacent
items). It does **not** replace the client's golden set: academic benchmarks say nothing about
whether the model drafts the client's letters correctly.

## Core commands (orientation)

```bash
pip install lm-eval                                # pin the version
lm_eval --tasks list                               # available tasks

lm_eval --model hf \
  --model_args pretrained=<local-checkpoint-path>,dtype=bfloat16 \
  --tasks <frozen task list from eval/drift-suite.yaml> \
  --device cuda:0 --batch_size auto
```

The source also shows running the harness through vLLM for speed and tracking checkpoints during
training.

## House rules

- Freeze the task list and harness version in `eval/drift-suite.yaml`; never change it between the
  baseline and the checkpoint run.
- Prefer log-probability scoring for multiple-choice tasks (wshobson grader note).
- Report results with the harness version, task versions and date; more than 3 numbers in a client
  report needs an R2 verifier.
