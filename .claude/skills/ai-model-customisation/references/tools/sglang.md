# Tool card: SGLang (structured output and agent-style serving)

*Adapted 2026-11-08 from Orchestra-Research/AI-Research-SKILLs `12-inference-serving/sglang/SKILL.md`
(MIT, commit 773a52944ba4747a18bd4ae9ade53fff041adcbc). SGLang itself: Apache-2.0 (GitHub research area
4, "high-throughput serving alternative"). Speed and adoption figures in the source omitted; check
commands against the SGLang docs for the pinned version.*

## When to use (per the source)

- Structured outputs constrained by JSON schema, regex or grammar (extraction into a system of
  record, pattern P1).
- Agent workloads with repeated prefixes (long system prompts, tool definitions) and multi-turn
  conversations, where its prefix cache (RadixAttention) helps.
- Use vLLM instead for plain text generation or when the most widely tested production server is
  preferred.

## Core commands (orientation)

```bash
pip install "sglang[all]"                          # pin the version

python -m sglang.launch_server \
  --model-path <model-id-or-local-path> \
  --port 30000                                     # prefix cache on by default per the source

python -m sglang.launch_server --model-path <model> --tp 4 --port 30000   # tensor parallel
```

It exposes an OpenAI-compatible API, so the same gateway and client code can sit in front of vLLM or
SGLang.

## DDD rules

- Same security baseline as vLLM: private binding, authenticating proxy, TLS, pinned revisions.
- Validate structured output against the schema in the application as well; constrained decoding
  reduces format failures but does not check business rules.
