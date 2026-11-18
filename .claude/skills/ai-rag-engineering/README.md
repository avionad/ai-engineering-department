# ai-rag-engineering

Covers the buy-first check (Microsoft 365 Copilot, Google Workspace assistants, vendor tools) before any custom build, ingestion from SharePoint/M365, Google Drive, Confluence and file shares, scanned PDFs and OCR, chunking and metadata, embeddings and vector store choice with Australian residency, hybrid retrieval and reranking, citations, permission-aware retrieval for M+ clients (query-time security trimming by the user's identity, ACL sync, revocation latency, deny-by-default, group expansion, audit), PII redaction with Presidio AU recognisers, and RAG evaluation including permission-leak tests.

**When to use:** Use when a client wants staff or customers to get answers from the company's own documents (policies, procedures, manuals, contracts, past work) and DDD must design, build or review the retrieval system.

**Trigger phrases:** company RAG, knowledge assistant, chat with our documents, search our SharePoint with AI, internal knowledge base AI, permission-aware retrieval, document level security AI, staff only see their documents, ACL sync, security trimming, vector database choice, embeddings, chunking, reranking, citation...

## How SKILL.md is organised

- Department relationships
- Ground truth (R1)
- Protocol
- Buy-first check (always before a custom build)
- Access models
- Pipeline at a glance
- Residency rule
- Size bands
- Evaluation (designed before build, run by ai-evals-security-testing)
- Effort drivers mapped to buckets
- Outputs
- Do not
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/ingestion-and-connectors.md` | **Ingestion, connectors, parsing and chunking.** v0.1.0, 2026-11-08. Sources: harvested `ai-kb/vendor/Azure-Samples__azure-search-openai-demo/docs/data_ingestion.md`. |
| `references/permission-aware-retrieval.md` | **Permission-aware retrieval (access model C).** v0.1.0, 2026-11-08. Sources: research B2 (`ai-dept-web-research-2026-11-08.md`), GitHub research. |
| `references/pii-redaction-presidio.md` | **PII redaction with Presidio (Australian recognisers).** v0.1.0, 2026-11-08. Source: **Microsoft Presidio**, upstream at `data-privacy-stack/presidio`. |
| `references/retrieval-and-evaluation.md` | **Embeddings, vector store, retrieval, citations and evaluation.** v0.1.0, 2026-11-08. Sources: research B2 and B6, GitHub research areas 3 and 4, harvested. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-rag-engineering.** v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and. |

## Templates

| File | What it holds |
|---|---|
| `templates/permission-leak-test-plan.md` | **Permission-leak test plan: {project}.** Template v0.1.0 (ai-rag-engineering), 2026-11-08. Save as. |
| `templates/rag-design-checklist.md` | **RAG design checklist: {project}.** Template v0.1.0 (ai-rag-engineering), 2026-11-08. Fill during stage 3 (Design) with the. |

*Skill version 0.1.0. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
