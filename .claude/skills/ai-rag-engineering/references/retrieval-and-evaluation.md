# Embeddings, vector store, retrieval, citations and evaluation

*v0.1.0, 2026-11-08. Sources: research B2 and B6, GitHub research areas 3 and 4, harvested
`~/ai-kb/vendor/Azure-Samples__azure-search-openai-demo/docs/evaluation.md` and `data_ingestion.md` (MIT). No model,
store tier, price or benchmark figure is named here on purpose: they change monthly and must be
verified live (conventions s3).*

## 1. Embeddings

Choose on these criteria, recorded in an ADR:

| Criterion | Question |
|---|---|
| Residency | Is the embedding endpoint available in the same Australian region as the model and index? (Embedding calls send document text to the endpoint) |
| Language and domain | Does the corpus include non-English content, code, legal or clinical language? Test on the golden set |
| Dimensions and size | Larger vectors cost more storage and query time; check the store's maximum dimensions |
| Lock-in | Changing the embedding model means re-embedding the whole corpus: plan and price it as a migration (run-ongoing) |
| Licence (self-hosted embeddings) | Open-weight embedding models carry licences like any model; check the model card (see `ai-model-customisation` licence-first rule) |

Pin the embedding model version. Store the model identifier with every vector so a mixed index can
be detected.

## 2. Vector store and index

| Option class | Fits | Notes |
|---|---|---|
| Cloud search service with vector + keyword + security filter fields (for example Azure AI Search) | M to XL on that cloud | Research B2 verified document-level security for Azure AI Search; choose the AU region matching the model |
| Cloud-native knowledge base service (for example Bedrock Knowledge Bases) | AWS-centric clients | ACL features `PENDING_VERIFICATION`; check which underlying stores are available in Sydney or Melbourne |
| Postgres with a vector extension, or a self-hosted vector database | Self-hosted, VPS, on-prem, or where the client already runs Postgres | Full residency control; we own filtering correctness, backups and patching |
| Embedded or file-based stores | Prototypes and S-band single-user tools only | No multi-user access control |

Residency rule: the store, keyword index, logs and caches sit in the same Australian region as the
model (research B2). Encryption at rest with client-managed keys where the data class requires it
(see `ai-deployment-platforms/references/security-baseline.md`).

## 3. Retrieval

- **Hybrid by default**: keyword (exact terms, codes, names, policy numbers) plus vector
  (meaning). Pure vector search misses exact identifiers users type.
- **Security filter inside every query** (access model B or C), before ranking.
- **Rerank** the merged candidates with a reranker (cloud semantic ranker or a cross-encoder),
  then pass the top few to the model. Tune top-k against retrieval recall and answer quality on
  the golden set, not by default.
- **Freshness filters**: current version only, effective date, document status, where the
  metadata supports it.
- **Query rewriting** for conversational follow-ups ("what about part-timers?" becomes a
  self-contained query) before retrieval.
- **Graph RAG** (microsoft/graphrag, LightRAG, both MIT per GitHub research) only for global
  questions across a corpus ("what themes recur in our incident reports?"); it is not the default
  and needs its own permission design because graph summaries mix documents.

## 4. Generation and citations

- Answer only from retrieved chunks; cite each claim with source title, section and page, linking
  to the source the user can open.
- **Abstain**: when retrieval returns nothing relevant, say so and point to a human or the source
  system. Abstain correctness is measured (section 6).
- **Retrieved text is untrusted input.** Documents can contain instructions (indirect prompt
  injection, OWASP LLM01:2026; goal hijack via retrieved content in the Agentic Top 10, research B5).
  Delimit retrieved content, instruct the model to treat it as data, give the assistant no tools it
  does not need, and include injection documents in the test corpus.
- Show "last updated" dates for cited documents when policy currency matters.
- Customer-facing assistants: AI disclosure and handoff per pattern P3.

## 5. Logging

Per request: audit fields from `permission-aware-retrieval.md` section 8, plus latency per stage,
tokens, retrieval scores, the answer, citations, and user feedback (thumbs plus reason). Logs sit in
the same region, under restricted access. These traces feed the monthly improvement loop
(run-ongoing; Phase 3 `ai-optimisation-llmops`).

## 6. Evaluation (specified here, executed by ai-evals-security-testing)

### 6.1 Golden Q&A set

- Source: real questions from users (discovery's ten examples, then helpdesk tickets, emails, intranet
  searches), each with the correct answer and the source document(s), checked by a named subject-matter
  owner.
- Size: grow with risk and audience. The Azure sample suggests generating at least 200 synthetic
  questions and then removing unrealistic ones by hand; we treat synthetic generation as a top-up for
  coverage, never a replacement for real questions. The golden-set rules are owned by
  `../../ai-evals-security-testing/references/eval-design.md` (minimum items per category, human
  review of every synthetic item, synthetic never outnumbering real): follow that file, this section
  only adds the retrieval-specific question types.
- Coverage dimensions: each source, each user role, question types (lookup, how-to, comparison,
  "which version applies"), unanswerable questions, multilingual if relevant.
- Versioned like code; never used for prompt tuning without a held-out portion.

### 6.2 Metrics

| Metric | What it tells you |
|---|---|
| Retrieval recall at k | The right source appears in the top k results |
| Context precision | How much of what was retrieved was relevant |
| Faithfulness / groundedness | Every claim in the answer is supported by the cited chunks |
| Citation match | Cited sources match the golden sources |
| Answer relevance / correctness | Answers the question correctly (judge or human) |
| Abstain correctness | Says "I don't know" for unanswerable questions, and only then |
| Latency and cost per answer | Production fitness, from logs |

Tools from GitHub research: ragas (Apache-2.0, last push Feb 2026, check activity), deepeval
(Apache-2.0), promptfoo (MIT, harvested), inspect_ai (MIT, UK AISI, credible for government
clients). LLM-as-judge metrics need calibration against human labels before they gate anything
(research B6; `ai-model-customisation/references/eval-first-gate.md` covers the calibration protocol).
The Azure sample notes its groundedness evaluator is not reliable for multimodal answers that use
images: prefer relevance and citation match there.

### 6.3 Targets

Targets are agreed with the client owner per metric and recorded in the design. Do not quote a
target or an achieved figure from a vendor, a demo or another client. Report the client's own eval
results with the golden set version and date.

### 6.4 Permission-leak suite

`templates/permission-leak-test-plan.md`. Any leak blocks go-live.

### 6.5 Regression

Re-run the golden set and the leak suite on every change to prompts, model or model version,
embedding model, chunking, reranker, connector code or ACL mapping. Check runs were not distorted
by throttling (the Azure sample's hidden-429 check) before comparing latency.
