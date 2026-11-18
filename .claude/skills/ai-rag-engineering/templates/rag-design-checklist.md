# RAG design checklist: {project}

*Template v0.1.0 (ai-rag-engineering), 2026-11-08. Fill during stage 3 (Design) with the
`ai-architect` agent. Save as `{client}/created/docs/strategy/rag-design-{project}-{YYYY-MM-DD}.md`
or paste into the solution design. Every "PENDING" item is resolved or listed as an open question
before the quote. Platform facts (models, regions, tiers) carry a source URL and date checked.*

## 0. Gate and context

- [ ] Risk tier assigned by `ai-compliance-risk`: ____ (no build before this)
- [ ] Size band: S / M / L / XL. Industry pack read: ____
- [ ] Decision-maker and content owner(s) named
- [ ] Ten real user questions collected (attach)
- [ ] Success measure agreed in the client's terms (for example minutes to find an answer, tickets deflected)

## 1. Buy-first check

- [ ] Client suite: Microsoft 365 / Google Workspace / other: ____
- [ ] Native assistant tested or ruled out, with a one-line reason: ____
- [ ] SaaS-embedded AI search considered for single-source cases: ____
- [ ] Decision: buy / build / hybrid, recorded as an ADR

## 2. Sources

| Source | System and version | Docs (approx.) | % scanned | Owner | Connector type | ACLs capturable? | Deletes captured? | Sync schedule |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

- [ ] In-scope and excluded locations listed (personal drives, archives, HR case files)
- [ ] Current-version rule agreed
- [ ] Parser tested on a 50-100 document sample per source; failure rate recorded: ____

## 3. Access control

- [ ] Access model: A open / B partitioned / C document-level. Justification: ____
- [ ] If A: client owner confirms in writing every user may see every document
- [ ] Identity provider: ____; nested groups: yes / no; guests: yes / no
- [ ] Binding: early / late / hybrid (ADR)
- [ ] Group expansion approach (ADR)
- [ ] Principal IDs stored are directory object IDs, not names or emails
- [ ] Deny-by-default on missing ACL; "everyone" only by explicit marker from source
- [ ] Ingestion fails closed on unreadable permissions
- [ ] Revocation latency target per data class: ____ (agreed by ____ on ____)
- [ ] Deletion and permission-removal sync designed and scheduled
- [ ] Caches, history, memory, logs, suggestions all identity-aware (leak paths table)
- [ ] Audit log fields defined
- [ ] Over-sharing review of in-scope sites scheduled (owner: ____)
- [ ] Tenancy separation needed (L/XL): yes / no

## 4. Privacy and redaction

- [ ] Data classes present: public / internal / confidential / personal / sensitive (health, TFN)
- [ ] Redaction decision per flow (index, prompts, logs) recorded
- [ ] Presidio AU recognisers registered explicitly; custom recognisers listed: ____
- [ ] Redaction test sample and recall target: ____
- [ ] APP considerations passed to `ai-compliance-risk` (collection, use, disclosure, ADM if answers feed decisions about people)

## 5. Platform and residency

- [ ] Platform chosen via `ai-deployment-platforms` (decision record link): ____
- [ ] Model region: ____ ; embedding endpoint region: ____ ; index region: ____ ; logs region: ____ ; OCR/parser region: ____ (all must match the residency claim)
- [ ] Each model, region and tier verified live (URL + date): ____
- [ ] Encryption at rest and key management per data class
- [ ] Private networking / SSO / no-training terms per the security baseline

## 6. Pipeline

- [ ] Chunking: structure-aware; size and overlap starting point: ____; tuned against golden set
- [ ] Chunks never span documents with different ACLs
- [ ] Metadata schema implemented (minimum fields in `references/ingestion-and-connectors.md`)
- [ ] Embedding model: ____ (version pinned, verified live); re-embedding plan
- [ ] Hybrid retrieval: yes; reranker: ____; top-k tuned
- [ ] Freshness filters: ____
- [ ] Citation format and link behaviour; abstain behaviour
- [ ] Retrieved text treated as untrusted (injection handling); assistant has no unnecessary tools
- [ ] AI disclosure and human handoff (customer-facing only)

## 7. Evaluation (handed to ai-evals-security-testing)

- [ ] Golden set: size ____, real questions ____%, owner ____, version ____
- [ ] Metrics and targets agreed: recall@k ____, faithfulness ____, citation match ____, abstain ____, latency ____
- [ ] LLM-judge calibrated against human labels (or N/A)
- [ ] Permission-leak test plan drafted from template, cases added for source-specific features
- [ ] Regression triggers listed

## 8. Operations

- [ ] Sync monitoring and alerting (lag vs revocation target)
- [ ] Feedback capture (thumbs plus reason) and monthly review owner
- [ ] Model and embedding version pinning and migration plan
- [ ] Runbook and admin handover

## 9. Effort and handover

- [ ] Effort drivers placed in bucket slugs (SKILL.md table) and sent to `ai-proposal-pricing`
- [ ] Run-cost inputs (queries per month, corpus size, re-index frequency) with vendor URLs and dates
- [ ] Threats sent to `ai-compliance-risk` (LLM01:2026, LLM02:2026, LLM09:2026 at minimum)
- [ ] Build spec ready for `ai-engineer` (sandbox only)
- [ ] Open questions: ____
