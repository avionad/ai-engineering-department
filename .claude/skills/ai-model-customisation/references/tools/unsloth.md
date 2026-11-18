# Tool card: Unsloth (fast single-GPU LoRA / QLoRA)

*Adapted 2026-11-08 from wshobson/agents `plugins/llm-finetuning/skills/lora-qlora-recipes/SKILL.md`
(MIT, commit 4bde3168b43c0655c4d00ea2726e631719908a6d) and Orchestra-Research/AI-Research-SKILLs
`03-fine-tuning/unsloth/SKILL.md` (MIT, commit 773a52944ba4747a18bd4ae9ade53fff041adcbc; thin, points
to upstream docs). Unsloth itself: Apache-2.0 (GitHub research area 4, "default for SMB fine-tunes").
Speed and memory-saving percentages in the sources omitted.*

## When to use

- LoRA or QLoRA supervised fine-tuning on a single GPU; the wshobson plugin treats it as the
  default fast path.
- Exception noted by wshobson: for conversational SFT that needs assistant-only loss on a `messages`
  dataset, its compiled trainer had no messages-shaped path in the version they tested; plain TRL is
  the default for that combination (see `trl.md`). Re-check on the version installed.

## Defaults wshobson explains (on the PEFT model call)

| Setting | Value | Reason given |
|---|---|---|
| `lora_dropout` | 0 | Optimised kernel path assumes zero dropout |
| `bias` | "none" | Negligible gain at these ranks |
| `use_gradient_checkpointing` | "unsloth" | Its own checkpointing variant, saves memory |
| `optim` | "adamw_8bit" | Cuts optimiser memory |
| `random_state` | fixed | Reproducibility |
| Target modules, alpha, rank, learning rate | See `../method-selection.md` s4 | |

## House rules

- Train inside the approved environment for the data class; never in a notebook service that has
  not been verified for residency.
- Dataset card and the eval-first baseline exist before the first run.
- Read the upstream Unsloth docs at the pinned version; this card is a pointer, not a manual.
