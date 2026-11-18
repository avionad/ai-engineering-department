# Ingestion, connectors, parsing and chunking

*v0.1.0, 2026-11-08. Sources: harvested `ai-kb/vendor/Azure-Samples__azure-search-openai-demo/docs/data_ingestion.md`
and `productionizing.md` (MIT), research B2, GitHub research area 3. Product capabilities change:
confirm connector features, parser support and limits in the vendor's current docs at design time.*

## 1. Connector decision per source

For each source record: system and version, connector type, what it captures (content, ACLs,
deletions, metadata), sync schedule, throttling limits, and who at the client grants access.

| Connector type | When | Watch for |
|---|---|---|
| Platform-native connector or indexer (cloud search service pulls from the source) | Source and search service are in the same cloud and the connector captures ACLs | Whether ACLs and deletions are actually captured; region of any intermediate processing |
| Our own API-based sync job (scheduled, in the client's or DDD's AU environment) | Mixed sources, ACL capture the native connector lacks, or residency control | Rate limits, delta queries, retry and back-off, credential scope (read-only, least privilege) |
| Export drop (client exports to a storage location we index) | Source has no usable API; low-change archives | Permissions usually lost in export: access model A or B only unless ACLs are exported too |
| Third-party connector product | Many sources, client accepts the vendor | Vendor due diligence (`ai-compliance-risk` mode g); residency of the connector's processing |

Credentials for any connector live in Doppler (conventions s2), scoped read-only to the in-scope
sites or spaces, never tenant-wide admin unless the client's IT approves it in writing.

## 2. Sync design

- **Full load, then deltas.** Delta or change-feed APIs where the source has them; otherwise
  content hashing to skip unchanged files (the Azure sample stores an MD5 per file and skips files
  whose hash has not changed).
- **Three streams, three schedules**: content changes, permission changes, deletions. Permission
  and group sync run more often than content (see `permission-aware-retrieval.md` section 9,
  Onyx approach), because they drive revocation latency.
- **Deletions are first-class.** A document deleted or moved out of scope at the source is removed
  from the index within the agreed revocation target. Test it (permission-leak plan P9).
- **Scheduled indexing** with alerting on failure; a failed sync must not silently leave the index
  stale. Record last successful sync time per source in the audit log.
- **Ingestion fails closed**: unreadable permissions, password-protected or encrypted files are
  skipped and listed in an exceptions report, never indexed without an ACL.

## 3. Parsing and OCR

The Azure sample's format table is a useful baseline: PDF, HTML, DOCX, PPTX, XLSX, images (JPG,
PNG, BMP, TIFF, HEIF), TXT, JSON, CSV. It defaults to a layout-aware cloud parser (Azure Document
Intelligence) for PDFs, Office files and images, extracting text, tables and figures with layout,
and offers cheaper local parsers (PyPDF, BeautifulSoup) for simple documents.

| Content | Approach | Decision driver |
|---|---|---|
| Born-digital PDFs and Office files | Local text extraction is often enough | Cost; test on a sample |
| Scanned PDFs, faxes, photos of documents | OCR with a layout-aware parser | Scan quality, handwriting, volume; the parser's region (residency) |
| Table-heavy documents (price lists, schedules, rosters) | Layout parser that preserves tables; the Azure sample converts tables to HTML markup inside the chunk | Whether answers depend on table cells |
| Figures, diagrams | Optional: generate a text description per figure (multimodal) | Only if users ask about diagrams; adds model calls and cost |
| Spreadsheets used as databases | Often better served by a query tool (pattern P7) than by chunked text | Whether questions are lookups or aggregations |
| Email archives | Thread-aware parsing, attachment handling, sender/recipient metadata | Privacy: email holds the most personal information; redaction scope |

Run the parser on a **representative sample of 50-100 documents from each source** during
design, and count failures (unreadable, garbled tables, wrong reading order). The failure rate is
the main effort driver for the `rag-knowledge` bucket.

The OCR or layout service is a data processor: it must sit in an approved region for the data
class, under the engagement's data-handling agreement.

## 4. Chunking

- **Structure first.** Split on headings, sections, clauses, list items and table boundaries before
  falling back to size. Policies, contracts and manuals have structure: use it.
- **Size baseline.** The Azure sample uses a sentence-aware splitter of about 1,000 characters
  (roughly 400-500 English tokens per its docs) with 10% overlap between consecutive chunks. Treat
  that as a starting point, then tune against the golden set (retrieval recall), not by intuition.
- **Keep context with the chunk.** Prefix or store the document title, section path and page so a
  chunk read alone still makes sense ("Leave policy > Parental leave > Eligibility").
- **Tables**: keep a table (or a logical block of rows with the header row) in one chunk.
- **Do not split across permission boundaries.** A chunk inherits exactly one document's ACL; never
  merge text from documents with different permissions into one chunk.

## 5. Metadata schema (minimum)

| Field | Purpose |
|---|---|
| `chunk_id`, `doc_id`, `source_system`, `source_url` | Identity and citation link |
| `title`, `section_path`, `page` | Citation display and context |
| `acl_users`, `acl_groups` (directory object IDs), `acl_everyone` (explicit boolean) | Security filter (deny-by-default when empty) |
| `sensitivity_label` / `data_class` | Label-based filtering, routing, DLP alignment |
| `owner`, `last_modified`, `version`, `effective_date` | Freshness, "current version only" filters, answering "which policy applies" |
| `language` | Multilingual corpora |
| `content_hash`, `ingested_at`, `acl_synced_at` | Change detection and revocation audit |
| `tenant_id` (L/XL) | Tenancy separation |
| `redaction_applied` + entity counts | PII audit (no raw values) |

## 6. Document hygiene before ingestion

Most poor RAG answers come from the corpus, not the model: five versions of the same policy,
superseded procedures, personal copies. Agree with the client owner:

- Which sites or spaces are in scope, and which are excluded (personal drives, archives, HR case
  files unless that is the use case).
- How the current version is identified (approved library, "final" status, effective date).
- Who owns each source and signs off its content.

Clean-up pipeline work is priced in `integration-workflow`; the over-sharing review in
`governance-compliance` (SKILL.md effort table).

## 7. Production notes carried from the harvest (Azure-specific, re-check before use)

- The sample's default search tier and free semantic ranker allowance are for demos; size the
  search service tier, replicas and semantic ranker for real query volume (`productionizing.md`).
  Tier names and quotas: verify live.
- Restrict the app to authenticated users, deploy inside a virtual network with private DNS for
  internal use, consider an API gateway in front (`productionizing.md` "Additional security
  measures").
- Load-test for expected concurrent users before go-live, and check evaluation latency figures are
  not distorted by silent HTTP 429 retries (`evaluation.md`).
