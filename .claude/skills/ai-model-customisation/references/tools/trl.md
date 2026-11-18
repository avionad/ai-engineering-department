# Tool card: TRL (Hugging Face post-training library)

*Adapted 2026-11-08 from huggingface/skills `skills/trl-training/SKILL.md` and
`skills/huggingface-llm-trainer/SKILL.md` (Apache-2.0, commit 25910b3d0ba31a2ba102f901cdc9e008c278a69c).
TRL itself: Apache-2.0 (GitHub research area 4). Example model and dataset IDs replaced with
placeholders. Check the API against the TRL docs for the pinned version.*

## Trainers (from the source)

| Trainer | Dataset shape | Use |
|---|---|---|
| `SFTTrainer` | `messages` or prompt/completion | Supervised fine-tuning |
| `DPOTrainer` | prompt, chosen, rejected | Preference optimisation |
| `KTOTrainer` | prompt, completion, boolean label | Unpaired feedback |
| `GRPOTrainer` | prompt only plus reward function(s) | Verifiable-reward reinforcement learning |
| `DistillationTrainer` | prompt only plus a teacher model | On-policy distillation |
| `RewardTrainer` | prompt, chosen, rejected | Trains a reward model |

Each pairs with a config class extending `transformers.TrainingArguments`. LoRA is passed as
`peft_config=LoraConfig(...)`. The chat template is applied automatically for conversational data;
the source says never to apply it yourself.

## SFT fields that matter (from the source)

```python
SFTConfig(
    max_length=1024,           # truncation length
    packing=True,              # fewer pad tokens; then inspect packed sequences (training-data file s3)
    assistant_only_loss=True,  # loss on assistant turns only
)
```

## GRPO notes (from the source)

- Reward functions receive prompts, completions and extra dataset columns as keyword arguments and
  return one float per completion.
- Generation is usually the bottleneck; the source describes using vLLM for generation (colocated or
  as a separate server).
- wshobson's rule applies: inspect the reward function against 50-100 sampled outputs before
  training, and only use RL once the model already succeeds sometimes.

## House rules

- The huggingface-llm-trainer skill runs training on Hugging Face Jobs infrastructure. Its
  processing region is unverified (`PENDING_VERIFICATION`): do not send client personal or
  confidential data there. Run TRL inside the approved environment instead.
- Never push client datasets or tuned weights to the public Hub; the trainer skill's "save to Hub"
  defaults must be switched to private storage in the approved environment.
