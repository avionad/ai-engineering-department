# Vendored provenance: ai-rag-engineering

*v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and
pinned commit. SHAs from `~/ai-kb/vendor/_harvest-manifest-2026-11-08.json`. Department-wide list:
`../../_shared/VENDORED.md` (maintained by ai-manager; these repos were on its "Phase 2/3 harvest
list" and are now harvested).*

| Used in (this skill) | Harvested file (upstream, under `~/ai-kb/vendor/<owner>__<repo>/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| `references/permission-aware-retrieval.md` s3, s6, s7, s9; `templates/permission-leak-test-plan.md` P1 | `docs/login_and_acl.md` | Azure-Samples/azure-search-openai-demo | MIT | 558ffd397eddcfe4da5c85ebc285796b367eb9b2 | **Design facts summarised in our own words**: two-app Entra setup with on-behalf-of flow, user/group ID permission fields, query-time token header, explicit `["all"]` for global access (deny-by-default), ADLS Gen2 ACL extraction and its no-inheritance caveat, three-way verification (no token / user token / elevated read). No code copied |
| `references/ingestion-and-connectors.md` s2, s3, s4, s7 | `docs/data_ingestion.md`, `docs/productionizing.md` | Azure-Samples/azure-search-openai-demo | MIT | 558ffd397eddcfe4da5c85ebc285796b367eb9b2 | Format table, layout-parser vs local-parser trade-off, tables-as-HTML, ~1,000-character sentence-aware chunks with 10% overlap as a starting point, MD5 change detection, production hardening notes. Paraphrased |
| `references/retrieval-and-evaluation.md` s6 | `docs/evaluation.md` | Azure-Samples/azure-search-openai-demo | MIT | 558ffd397eddcfe4da5c85ebc285796b367eb9b2 | Synthetic ground truth then human pruning, run diffing, hidden HTTP 429 check, multimodal groundedness caveat. Paraphrased |
| `references/pii-redaction-presidio.md` s2 | `~/ai-kb/vendor/data-privacy-stack__presidio/presidio-analyzer/presidio_analyzer/predefined_recognizers/country_specific/australia/au_abn_recognizer.py`, `au_acn_recognizer.py`, `au_tfn_recognizer.py`, `au_medicare_recognizer.py`, `__init__.py` | Microsoft Presidio, upstream at `data-privacy-stack/presidio` (renamed from `microsoft/presidio`; same repository ID 132129752, old path permanently redirects, not a fork; GitHub API checked 2026-11-08) | MIT (c) Presidio Contributors, https://github.com/data-privacy-stack/presidio/blob/main/LICENSE (read 2026-11-08) | 05b60e1a6805f3b2c0ad6cbe7526ccd226647971 | **Read only, never executed.** Entity names, detection approach (regex, context words, checksum) described. Code not copied; builds install Presidio from its published package |
| Eval-calibration cross-reference | `plugins/llm-finetuning/skills/eval-harness-first/` | wshobson/agents | MIT | 4bde3168b43c0655c4d00ea2726e631719908a6d | Judge calibration rule referenced via `ai-model-customisation` (see that skill's provenance) |

## Described, never copied (licence)

| Project | Licence | What we describe |
|---|---|---|
| onyx-dot-app/onyx `backend/ee/onyx/external_permissions/` | Onyx Enterprise Licence (`ee/`) | The design idea of separate per-connector document-permission sync and group sync jobs, from GitHub research area 3. Not harvested, not read beyond the research summary, not copied |
| open-webui/open-webui | Open WebUI Licence (branding clause) | Presence of SCIM, OAuth and access-control modules, as a front-end option. Not harvested |

## Non-harvested sources

| Source | Used for |
|---|---|
| Research file `ai-dept-web-research-2026-11-08.md` B2, B5, B6 | Query-time identity principle, Azure AI Search capabilities (Microsoft Learn link there), delivery checklist, OWASP LLM02:2026/LLM09:2026 mapping, eval-first and regression |
| Research file `ai-dept-github-research-2026-11-08.md` area 3, gap 4 | Framework and front-end options with licences, Onyx approach, permissive tiny repos |
| OWASP Top 10 for LLM Applications 2025, Agentic Top 10 | IDs only (CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/), names from the research file |
