# Hosting a custom model, monitoring, retraining and drift

*v0.1.0, 2026-11-08. Sources: research B4 and B6, GitHub research areas 4 and 5, harvested wshobson
`quantized-export` and `checkpoint-promotion` (MIT), Orchestra-Research serving cards (MIT),
huggingface/skills SageMaker planner and production defaults (Apache-2.0). Platform and region
choice is made in `ai-deployment-platforms`; this file covers what is specific to a model we
customised.*

## 1. Where a custom model can run

| Option | Fits | Residency note |
|---|---|---|
| Self-managed GPU VPS in an Australian data centre | Small models, low to moderate volume, sovereignty | Full control of location; the provider is not IRAP-assessed unless it says so (research B4) |
| On-premises GPU server | Defence, health records, legal privilege, total sovereignty | Client's own controls (ISM, Essential Eight); high capex and MLOps skill needed |
| Managed endpoint on AWS (SageMaker real-time, scale-to-zero or async endpoint) | AWS clients wanting managed scaling and alarms | Choose an Australian region; GPU instance types and quotas in that region `PENDING_VERIFICATION` per account |
| Bedrock Custom Model Import | AWS clients wanting the Bedrock API for imported weights | Per the harvested planner: supported base families and weights only, no custom inference logic. Availability in Sydney or Melbourne `PENDING_VERIFICATION` |
| Azure or Google custom model hosting | Clients on those clouds | Region and model support `PENDING_VERIFICATION`; check before design |

A hybrid design (research B4) can route a narrow high-volume task to the tuned small model and
everything else to a hosted frontier model, through a gateway (LiteLLM, MIT outside its `enterprise/`
folder; Azure AI hub gateway accelerator, MIT) that also tracks cost and enforces quotas.

## 2. Serving stack choice

| Situation | Default | Card |
|---|---|---|
| NVIDIA GPUs, multi-user production API, OpenAI-compatible endpoint | vLLM | `tools/vllm.md` |
| Structured JSON output, agents with repeated system prompts and tools | SGLang | `tools/sglang.md` |
| CPU-only, Apple Silicon, AMD/Intel GPUs, single box, edge | llama.cpp (GGUF) | `tools/llama-cpp.md` |
| Developer laptops, demos, small on-prem single user | Ollama | `tools/ollama.md` |
| Managed AWS endpoint | SageMaker via the harvested planner method | `tools/sagemaker-hosting.md` |

Text Generation Inference is archived (GitHub research area 4): not for new builds.

## 3. Export format (from wshobson `quantized-export`)

- Pick the format by target hardware: FP8 on recent datacentre GPUs that support it; AWQ 4-bit on
  older GPUs (GPTQ treated as superseded for new exports); GGUF (Q4_K_M from an importance matrix)
  for llama.cpp and edge use.
- **Merged vs adapter-only** is a separate decision. Merged folds the adapter into the base weights
  (bigger, portable). Adapter-only is small but must be served with the exact same base model
  revision; a mismatched base silently changes outputs. Record the base revision in the model card.
- **Smoke test** every export before serving: load, generate on a fixed prompt set, compare with
  the pre-export checkpoint on a slice of the eval harness. A quantised export is a new model for
  eval purposes.

## 4. Security baseline for self-hosted serving

- Never expose the inference port to the internet. The harvested examples bind servers to all
  interfaces for convenience (`--host 0.0.0.0`); in our builds the server listens on a private
  interface or localhost behind an authenticating reverse proxy or gateway, with TLS.
- Authentication per calling application (scoped keys from Doppler), rate limits and spend or
  token caps at the gateway.
- `--trust-remote-code` (seen in the vLLM card for custom architectures) runs code from the model
  repository: only for repositories reviewed and pinned to a commit.
- Pin model files by revision or checksum; scan downloaded artefacts; keep weights in encrypted
  storage with access logging (weights trained on client data hold client data).
- Patch the serving stack on a schedule; it is internet-facing software even when private.
- Logs of prompts and outputs follow the data class of the inputs (`ai-deployment-platforms`
  security baseline).

## 5. Monitoring in production (research B6)

| Signal | Why |
|---|---|
| Golden set and drift suite re-run on a schedule and on every change | Catches regressions and capability drift |
| Input distribution shift (topics, lengths, languages, new document types) | The world the model was tuned on has moved |
| Output quality sampling with human review | Catches failures graders miss |
| User feedback (thumbs plus reason) | Cheapest continuous signal; feeds error analysis |
| Cost and latency per task, GPU utilisation | Hosting economics; the reason distillation was chosen |
| Safety incident log | Required for tier 2 and above |

## 6. Retraining cadence and triggers

Retraining is not on a fixed clock by default. Agree triggers with the client owner and write them
in the model card:

- Golden or drift results fall below the agreed threshold.
- A new failure bucket appears in error analysis that prompting cannot fix.
- The process changed (new forms, products, policies the model formats or classifies).
- A better base model clears the target at lower cost on the same harness.
- A base model or dependency reaches end of support. Hosted providers retire model versions on a
  schedule (research B6); self-hosted weights do not retire, but their serving stack and hardware do.

Every retrain repeats the gates: dataset card, eval-first comparison, promotion gate, client owner
approval. Keep the previous promoted checkpoint ready for rollback until the new one has passed its
canary period.

## 7. Ownership and exit

The client owns the training data, goldens, graders, dataset and model cards, and (subject to the
base licence) the adapter or merged weights. Store them in accounts the client owns. Document how
to rebuild the model from the dataset and config, and how to fall back to the hosted+prompt
baseline if the custom model is retired (FAQ Q12; APRA-regulated clients see register AU-13, AU-15
on exit and substitution plans).
