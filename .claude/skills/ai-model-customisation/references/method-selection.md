# Method selection: off-ramps first, then the data shape

*v0.1.0, 2026-11-08. Adapted from wshobson/agents
`plugins/llm-finetuning/skills/finetuning-method-selection/SKILL.md` and `lora-qlora-recipes/SKILL.md`
(MIT). Decision order also matches research B3 (prompt, RAG or tools, fine-tune, distil; fine-tuning
does not reliably add fresh facts; practitioner consensus, secondary source). Hyperparameter
defaults are pointers for engineers; they are recipes from the harvested source, to be validated on
the client's eval harness.*

## 1. Off-ramps (check every time, before any training talk)

| Signal | Route | Why |
|---|---|---|
| The gap is facts that change (prices, policies, stock, people, news) | RAG (`ai-rag-engineering`) | A tuned model bakes in a snapshot that goes stale; retrieval stays current and cites sources |
| The desired behaviour is still being worked out, or differs per request | Prompt engineering | Fine-tuning locks in a behaviour; do not lock in one that has not settled |
| The model already does it with good instructions, but cost or speed is the issue at volume | Prompt caching, batch processing, routing to a smaller hosted model first; distillation only if those fall short | Cheaper levers first (research B6 cost levers) |
| Small domain corpus | RAG | wshobson's sizing: under roughly 10MB of domain text, RAG only; 10MB to 500MB, RAG plus fine-tune; above that, continued pretraining enters, which we treat as out of normal scope |

## 2. Data-shape router

```
New FACTS?     changing        -> RAG
               stable + huge   -> continued pretraining (guidance only, needs the practice owner's approval)
New BEHAVIOUR? still shifting  -> prompt engineering
               stable, and you have:
                 demonstrations (input -> ideal output)   -> SFT with LoRA / QLoRA
                 paired better/worse answers              -> DPO family
                 unpaired thumbs up / down                -> KTO
                 an automatic pass/fail check             -> GRPO with verifiable rewards
                                                             (only once the model succeeds sometimes;
                                                              otherwise SFT first)
COST / LATENCY at volume, big model already good          -> distillation to a smaller model
BEFORE ANY OF THIS: the eval harness and baselines exist (eval-first-gate.md)
```

### Worked examples in client terms

- "Draft replies that follow our support macros exactly." Stable behaviour, demonstrations exist in
  past tickets: SFT, after checking that a prompt with the macros plus retrieval misses the target.
- "Know this month's price list." Changing facts: RAG, no training.
- "Extract 40 fields from delivery dockets into our ERP." Usually prompting with a schema plus
  validation rules (pattern P1). Fine-tune only if the eval shows a persistent format or accuracy
  gap at high volume, and a small tuned model would cut cost.
- "Our reviewers thumbs-up or thumbs-down drafts." Unpaired feedback: KTO, not DPO.
- "Classify 200,000 support emails a month; the big model is accurate but expensive." Distillation
  candidate: label with the big model (check its terms on output use), train a small model, compare
  on the same harness.

## 3. Key routing facts (from the harvested source)

- Data quality and model scale matter far more than the choice between preference-loss variants:
  spend effort on the data shape and size, not on picking a DPO variant.
- Preference methods suit taste (tone, style); verifiable-reward methods suit checkable skills
  (schemas, code, calculations).
- Reinforcement methods sharpen an existing capability; they do not teach one from zero.

## 4. LoRA and QLoRA starting recipe (for engineers)

From wshobson `lora-qlora-recipes` ("LoRA Without Regret" convention as cited there):

| Setting | Starting point |
|---|---|
| Target modules | All linear layers (attention and MLP), not attention only |
| Alpha | 2 x rank |
| Rank | 16-32 general default; 1-32 for RL adapters; higher only if held-out eval shows underfitting |
| Learning rate | About 10x the full fine-tune rate; 2e-4 a common QLoRA start |
| Effective batch size | Under 32 |
| QLoRA vs LoRA | QLoRA when memory is the constraint; LoRA otherwise; full fine-tune rarely |

Memory feasibility is estimated as weights + optimiser state + gradients + activations for the
chosen precision and method (worked worksheets in the harvested upstream file
`ai-kb/vendor/wshobson__agents/plugins/llm-finetuning/skills/finetuning-method-selection/references/memory-math.md`,
not a file in this skill). Confirm GPU
availability in the approved region before promising a size class.

## 5. Distillation

Teacher (large model that already meets the target) labels a dataset; the student (small open-weight
model) is fine-tuned on it; both are compared on the same harness. Rules:

- Keep a share of real, non-teacher data in the training mix (wshobson's dataset rules keep at least
  25% real data as a collapse guard).
- Check the teacher vendor's terms on using outputs to train other models (`PENDING_VERIFICATION`
  per vendor) and record the check.
- Student must clear the same targets; a cheaper model that misses the target is not a saving.

## 6. Continued pretraining and pretraining

Continued pretraining on a very large stable domain corpus is guidance-only here and needs the practice owner's
approval as a scope exception. Pretraining a model from scratch is out of scope for every DDD
client: the data, compute and expertise required are outside any engagement we sell.
