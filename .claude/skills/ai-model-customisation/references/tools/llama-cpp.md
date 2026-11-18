# Tool card: llama.cpp (CPU, Apple Silicon, non-NVIDIA, edge)

*Adapted 2026-11-08 from Orchestra-Research/AI-Research-SKILLs `12-inference-serving/llama-cpp/SKILL.md`
(MIT, commit 773a52944ba4747a18bd4ae9ade53fff041adcbc) and huggingface/skills
`skills/huggingface-local-models/SKILL.md` (Apache-2.0, commit 25910b3d0ba31a2ba102f901cdc9e008c278a69c).
llama.cpp itself: MIT. Build flags and binary names change between releases: check the README at the
pinned version. Benchmark tables in the source omitted.*

## When to use

- CPU-only servers, Apple Silicon, AMD or Intel GPUs, edge devices; simple single-box deployments.
- Running a GGUF export of a fine-tuned model locally (from wshobson `quantized-export`: GGUF Q4_K_M
  from an importance matrix is the edge format).
- Not for high-concurrency GPU serving: use vLLM.

## Core commands (orientation)

```bash
# Build from source with the accelerator flag for the hardware (Metal, CUDA, ROCm), or install a package
# Run a local GGUF file
./llama-cli -m models/<model>.gguf -p "test prompt" -n 256

# OpenAI-compatible server (bind privately in our builds)
./llama-server -m models/<model>.gguf --port 8080 -ngl <layers-to-offload-to-gpu>

# Convert a Hugging Face checkpoint when no GGUF exists (script in the llama.cpp repo)
python convert_hf_to_gguf.py <local-model-dir>
```

## Quantisation choice (from the source)

| Format | Use |
|---|---|
| Q4_K_M | Recommended default balance |
| Q5_K_M, Q6_K, Q8_0 | Higher quality, more memory |
| Q3_K_M, Q4_K_S | Very large models that must fit in memory |
| Q2_K | Testing only |

Any quantised export is re-evaluated on the eval slice before use.

## House rules

- The huggingface-local-models skill pulls GGUFs from the public Hub: download only from the
  official or a reviewed repository, pin the exact file, record its checksum.
- Never put client-tuned GGUFs on a public hub.
