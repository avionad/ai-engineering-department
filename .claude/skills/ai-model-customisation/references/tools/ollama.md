# Tool card: Ollama (developer and small single-box serving)

*v0.1.0, 2026-11-08. **No harvested source for Ollama.** Facts here come only from GitHub research
area 4 (Ollama: MIT licence, "SMB and on-prem single box serving") and research B4 ("Ollama for
dev"). Commands are intentionally not given: read the Ollama docs at the version being installed.*

## When to use

- Developer laptops and demos.
- A small on-prem or VPS box serving a small model to a handful of users where vLLM's operational
  weight is not justified.
- Not for multi-user production APIs at M+ scale: use vLLM.

## House rules

- Bind to localhost or a private interface; put an authenticating proxy with TLS in front if any
  other machine calls it.
- Pull models only from reviewed sources; record the exact model tag and digest in the model card.
- Treat it as part of the evaluated system: a model served through Ollama is re-run on the eval
  slice like any other export.
- Gap: a harvested Ollama card is on the Phase 3 harvest wish list.
