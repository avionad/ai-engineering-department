# ai-model-customisation

Decides whether to customise at all using the ladder prompt, RAG, fine-tune (LoRA/QLoRA), distil, and never pretrain for our clients; enforces the eval-first gate (no tuning plan without a baseline eval showing prompting plus RAG fall short); selects the method from the data shape; prepares training data with an OAIC-aligned privacy impact assessment; selects open-weight models licence first (Apache/MIT vs custom licences such as Llama's); plans hosting with vLLM, SGLang, llama.cpp or Ollama; and sets retraining cadence and drift monitoring. Written for non-technical owners and engineers. Costs as drivers only, never prices.

**When to use:** Use when a client asks for a custom, fine-tuned, private or open-source AI model, or when prompting and retrieval are not meeting a measured target and someone proposes training.

**Trigger phrases:** fine-tune a model, custom AI model, train our own AI, private LLM, open-source model, open-weight model, LoRA, QLoRA, distillation, should we fine-tune, prompt vs RAG vs fine-tune, which open model, model licence, Llama licence, Qwen, Gemma, DeepSeek, self-host a model, vLLM, Ollama, llama.cpp, SGLa...

## How SKILL.md is organised

- Department relationships
- Plain English: should you customise? (for owners)
- The ladder and the gate
- Protocol
- Method selection in one table
- Open-weight model selection (summary)
- Training data and privacy (summary)
- Hosting and operations (summary)
- Cost drivers (never prices)
- Effort drivers mapped to buckets
- Size bands
- Outputs
- Do not
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/eval-first-gate.md` | **The eval-first gate.** v0.1.0, 2026-11-08. Adapted from wshobson/agents `plugins/llm-finetuning/skills/eval-harness-first/SKILL.md`. |
| `references/hosting-and-operations.md` | **Hosting a custom model, monitoring, retraining and drift.** v0.1.0, 2026-11-08. Sources: research B4 and B6, GitHub research areas 4 and 5, harvested wshobson. |
| `references/method-selection.md` | **Method selection: off-ramps first, then the data shape.** v0.1.0, 2026-11-08. Adapted from wshobson/agents. |
| `references/open-weight-model-selection.md` | **Open-weight model selection: licence first.** v0.1.0, 2026-11-08. Sources: research B3 (`ai-dept-web-research-2026-11-08.md`), client FAQ Q10,. |
| `references/training-data-and-privacy.md` | **Training data preparation and privacy.** v0.1.0, 2026-11-08. Privacy rows from `../../_shared/regulatory-register.md` (AU-6, AU-12, EU-1,. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-model-customisation.** v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and pinned. |

## Templates

| File | What it holds |
|---|---|
| `templates/customisation-go-no-go.md` | **Model customisation go / no-go: {project}.** Template v0.1.0 (ai-model-customisation), 2026-11-08. Save as. |

*Skill version 0.1.0. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
