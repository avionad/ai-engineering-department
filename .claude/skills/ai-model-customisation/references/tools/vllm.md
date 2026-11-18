# Tool card: vLLM (production serving on NVIDIA GPUs)

*Adapted 2026-11-08 from Orchestra-Research/AI-Research-SKILLs `12-inference-serving/vllm/SKILL.md`
(MIT, commit 773a52944ba4747a18bd4ae9ade53fff041adcbc). vLLM itself: Apache-2.0 (GitHub research area
4, "default production serving"). Commands summarised for orientation; check flags against the vLLM
docs for the pinned version before use. Model names replaced with placeholders; throughput claims in
the source omitted.*

## When to use

- Multi-user production API with an OpenAI-compatible endpoint, on NVIDIA GPUs (also supports AMD
  ROCm, Intel GPUs and TPUs per the source).
- Serving a merged fine-tuned model or a quantised export (AWQ, GPTQ, FP8).
- Use llama.cpp instead for CPU or single-user edge; SGLang when structured output and prefix reuse
  dominate.

## Core commands (orientation)

```bash
pip install vllm                                   # pin the version in requirements

# OpenAI-compatible server
vllm serve <model-id-or-local-path> \
  --gpu-memory-utilization 0.9 \
  --max-model-len <context> \
  --enable-prefix-caching \
  --port 8000                                      # bind privately; see security below

# Larger models across GPUs (power-of-two GPU counts per the source)
vllm serve <model> --tensor-parallel-size 4 --quantization awq
```

Offline batch inference uses the Python `LLM` and `SamplingParams` classes; useful for running the
eval harness and for distillation labelling.

## Operating checklist (from the source's production workflow)

1. Configure for model size (memory utilisation, max context, quantisation, tensor parallelism).
2. Load-test with representative prompts before go-live (the source uses locust).
3. Enable metrics (Prometheus endpoint) and watch time to first token, running requests and KV cache
   usage.
4. Deploy in a container for consistency.
5. Verify latency and throughput against the targets agreed in the design, not generic numbers.

## Common issues (from the source)

| Symptom | First things to try |
|---|---|
| Out of memory on load | Lower `--gpu-memory-utilization` or `--max-model-len`; use a quantised export |
| Slow first token | `--enable-prefix-caching`; `--enable-chunked-prefill` for long prompts |
| Custom architecture not found | `--trust-remote-code`, **only for reviewed repositories pinned to a commit** |
| Low throughput | Raise `--max-num-seqs`; check GPU utilisation |

## DDD rules

- Never expose the port publicly; private interface or localhost behind an authenticating proxy
  with TLS (`../hosting-and-operations.md` s4). The source's examples bind to `0.0.0.0` for
  convenience.
- Pin model revision; smoke-test against the eval slice after every model or version change.
