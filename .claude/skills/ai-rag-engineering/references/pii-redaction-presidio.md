# PII redaction with Presidio (Australian recognisers)

*v0.1.0, 2026-11-08. Source: **Microsoft Presidio**, upstream at `data-privacy-stack/presidio`
(MIT (c) Presidio Contributors). The project was renamed from `microsoft/presidio` to
`data-privacy-stack/presidio`: same repository, GitHub repository ID 132129752, old path serves a
permanent redirect, not a fork (verified against the GitHub API 2026-11-08; detail in
`../../_shared/VENDORED.md`). Harvested files under
`~/ai-kb/vendor/data-privacy-stack__presidio/presidio-analyzer/presidio_analyzer/predefined_recognizers/country_specific/australia/`.
Pinned SHA in `vendored-provenance.md`. We read the recogniser code; we do not vendor it into this
skill and we never execute it.*

## 1. Decide what redaction is for (before choosing a tool)

Redaction is a control chosen per data flow, recorded in the design and the risk register. It is
not automatically right for every corpus: redacting a TFN from a payroll procedure is sensible;
redacting client names from the client files the assistant exists to search breaks the use case.

| Flow | Typical decision |
|---|---|
| Documents into the index | Redact identifiers nobody needs to search by (TFN, Medicare number, bank details). Keep what the use case needs, protected by access control instead |
| User prompts before they reach the model | Detect and warn or mask identifiers when the model or logs sit under weaker controls than the source |
| Logs and eval traces | Mask by default; restricted admin access for unmasked logs if kept at all |
| Training or fine-tuning data | See `ai-model-customisation`; privacy impact assessment first (register AU-12) |
| Answers shown to users | Normally no redaction (the user is entitled to the source); rely on access control |

Redaction does not replace permission-aware retrieval, and access control does not replace
redaction where the downstream service (model, logs, third-party processor) is less trusted than
the source. Record which control covers which risk.

## 2. Australian recognisers in the harvest

| Recogniser class | Entity | Detection approach (from the code) |
|---|---|---|
| `AuAbnRecognizer` | `AU_ABN` | Regex for the 11-digit ABN (spaced and unspaced patterns, low base scores), context words ("australian business number", "abn"), modulus 89 checksum validation |
| `AuAcnRecognizer` | `AU_ACN` | Regex, context words, weighted checksum (weights 8 to 1) |
| `AuTfnRecognizer` | `AU_TFN` | Regex, context words, weighted checksum (nine weights) |
| `AuMedicareRecognizer` | `AU_MEDICARE` | Regex, context words, weighted checksum |

Practical notes:

- Base pattern scores are deliberately low (the ABN unspaced pattern scores very low on its own);
  confidence rises with context words and checksum validation. Set the score threshold from a test
  on the client's documents, not from defaults.
- Spaces and dashes are normalised before checksum checks (replacement pairs in the code).
- **Whether these recognisers load by default in the installed Presidio version is
  `PENDING_VERIFICATION`.** Register them explicitly in the analyzer's recogniser registry and
  assert in a unit test that each one fires on a known valid test value.
- An ABN or ACN identifies a business and is usually public; a TFN or Medicare number identifies a
  person and is sensitive. Default policy: redact TFN and Medicare, keep ABN and ACN unless the
  client says otherwise.

## 3. Gaps to cover with custom recognisers or rules

Not in the harvested AU set (verify against the installed version before building duplicates):
driver licence numbers (formats differ by state), passport numbers, Centrelink customer reference
numbers, BSB and account numbers, Individual Healthcare Identifiers, Australian phone numbers and
addresses in local formats, employee and patient IDs specific to the client. Presidio's general
recognisers (names, emails, phone numbers, credit cards) cover some of these generically; test
recall on a labelled sample of the client's real documents.

## 4. Where redaction runs

- In the ingestion pipeline, inside the same approved Australian environment as the index, before
  embedding (so the vector store never holds the raw value).
- Keep a reversible mapping only if a business need exists, stored separately under stricter access;
  otherwise use irreversible replacement (`<AU_TFN>`).
- Log entity type counts per document (`redaction_applied`, counts), never the values.

## 5. Testing redaction

Part of the eval baseline (`governance-compliance` bucket):

1. Build a labelled sample: 50+ real document excerpts with known identifiers, plus valid synthetic
   values that pass the checksums, plus near-misses (11-digit numbers that are not ABNs).
2. Measure recall (identifiers caught) and precision (false redactions) per entity type.
3. Recall target for TFN and Medicare agreed with the client owner and recorded; misses are logged
   as findings for `ai-compliance-risk`.
4. Re-run when Presidio is upgraded or recognisers change.
