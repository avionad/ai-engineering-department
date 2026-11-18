# Verify live before naming

*v0.2.0, 2026-11-08. The rule: every model, region, deployment type, price, quota, certification
and assessment status in a client deliverable is checked on the vendor's own page on the day and
recorded with URL and date. URLs below come from the research files, harvested docs, and pages
opened live. Where no URL has been opened, the page is described and the URL is marked
`PENDING_VERIFICATION`: find it on the vendor's documentation site, record it here in the next
version, and never guess it.*

*v0.2.0 (2026-11-08): the Google Cloud block was replaced with the pages actually opened for the
`platforms.md` section 3 rewrite, and two new blocks added for self-hosting and for the Australian
government controls that on-premises builds depend on. A "Checked 2026-11-08" column now says
whether each page was opened and what it gave, including two pages that would not load
(the Google Cloud IRAP page, and cyber.gov.au).*

## 1. What to record for every fact

| Field | Example of the shape (not a real value) |
|---|---|
| Fact | "Model X available on `au.*` inference profile" |
| Vendor page URL | full URL |
| Date and time checked | 2026-11-08 14:05 AEDT |
| Checked by | operator |
| Account-specific? | Yes: quotas and model access can differ per account; check in the client's account console too |
| Screenshot or export | stored with the decision record |
| Re-check due | 60 days, or before any client deliverable after that (conventions s3) |

## 2. Pages to check

### AWS

| Fact | Where | URL |
|---|---|---|
| IRAP scope and services at PROTECTED | AWS IRAP compliance page | https://aws.amazon.com/compliance/irap/ |
| 2026 Phase 1a IRAP report (AgentCore added) | AWS Security blog; report in AWS Artifact | https://aws.amazon.com/blogs/security/2026-phase-1a-irap-report-is-now-available-on-aws-artifact-for-australian-customers/ |
| Guardrails available in Sydney | AWS What's New | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-guardrails-sydney |
| Which models are on `au.*` cross-region inference profiles | Bedrock User Guide, cross-region inference / supported models by Region pages, and the Bedrock console in the client's account | `PENDING_VERIFICATION` (research used a secondary source: https://sjramblings.io/keeping-ai-workloads-sovereign-on-aws/ **[secondary]**) |
| Bedrock pricing in Sydney/Melbourne | Bedrock pricing page | `PENDING_VERIFICATION` |
| Knowledge Bases ACL features | Bedrock Knowledge Bases docs | `PENDING_VERIFICATION` |
| Custom Model Import region support | Bedrock docs | `PENDING_VERIFICATION` |
| SageMaker GPU instance availability and quotas | Service Quotas in the client's account (harvested planner shows the CLI query) | account-specific |

### Microsoft Azure

| Fact | Where | URL |
|---|---|---|
| IRAP assessment of Azure Australian regions, per service | Microsoft compliance offerings | https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-australia-irap |
| Model continuity for Standard deployments in Australia East | Tech Community thread cited by research | https://techcommunity.microsoft.com/discussions/azure-ai-foundry-discussions/open-ai-model-continuity-plan-for-standard-deployments-in-australia-east/4485447 |
| Which models are available in Australia East, per deployment type (Standard, Data Zone, Global) | Azure OpenAI / AI Foundry model and region availability docs | `PENDING_VERIFICATION` |
| Data processing location per deployment type | Azure OpenAI deployment types docs | `PENDING_VERIFICATION` |
| Document-level access in Azure AI Search | Microsoft Learn | https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview |
| Query-time ACL enforcement | Microsoft Learn (linked from harvested sample) | https://learn.microsoft.com/azure/search/search-query-access-control-rbac-enforcement |
| Security trimming with filters (older pattern) | Microsoft Learn (linked from harvested sample) | https://learn.microsoft.com/azure/search/search-security-trimming-for-azure-search |
| AI Search tier limits | Microsoft Learn (linked from harvested sample) | https://learn.microsoft.com/azure/search/search-limits-quotas-capacity |
| Azure pricing | Azure pricing pages / calculator | `PENDING_VERIFICATION` |
| AVM AI/ML landing zone module | GitHub | https://github.com/Azure/terraform-azurerm-avm-ptn-aiml-landing-zone |
| Foundry baseline reference | GitHub | https://github.com/Azure-Samples/microsoft-foundry-baseline |
| AI hub gateway accelerator | GitHub | https://github.com/Azure-Samples/ai-hub-gateway-solution-accelerator |

### Google Cloud

*Every URL in this block was opened on 2026-11-08 for the platforms.md section 3 rewrite, except
the two marked as failed. Check the same pages.*

| Fact | Where | URL | Checked 2026-11-08 |
|---|---|---|---|
| Vertex AI generative AI data residency: which models have ML processing per Australian region, and the `global` endpoint having no residency guarantee | Google Cloud docs | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency | Yes. Only `australia-southeast1` appeared in the ML-processing table; Melbourne did not. Read the Australia rows and record the exact model IDs: two reads of the page returned slightly different model lists |
| Vertex AI regions in Australia; the "stores and processes your data only in the region you specify, except data labeling and preview features" statement; no global location for platform resources | Google Cloud docs | https://docs.cloud.google.com/vertex-ai/docs/general/locations | Yes |
| CMEK support per Vertex resource, and the resourceless Gemini API limitation (`us` and `eu` multi-regions only; Memory Bank and Sessions on the global endpoint unsupported) | Google Cloud docs | https://docs.cloud.google.com/vertex-ai/docs/general/cmek | Yes |
| VPC Service Controls support and limits (no request and response logging inside a perimeter; URL context live fetching disabled; Model Garden one-click public endpoints unsupported) | Google Cloud docs | https://docs.cloud.google.com/vertex-ai/docs/general/vpc-service-controls | Yes |
| Vertex AI Search data source access control: sources, identity providers, `acl_info`, and that it cannot be toggled after data store creation | Google Cloud docs | https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control | Yes |
| Provisioned Throughput definition and that it is bought per model per location | Google Cloud docs | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview | Yes. No prices recorded, by rule |
| Assured Workloads control packages: exact names "Australia Data Boundary" and "Australia Data Boundary and Support", and the five-country support-personnel restriction | Google Cloud docs | https://docs.cloud.google.com/assured-workloads/docs/control-packages | Yes. The page names neither IRAP nor the Hosting Certification Framework, so any such claim is `PENDING_VERIFICATION` |
| Whether Vertex AI is in scope for the two Australia control packages | Google Cloud docs | https://docs.cloud.google.com/assured-workloads/docs/supported-products | Partly: Vertex AI is listed as supported, but the Australia columns were truncated when read. `PENDING_VERIFICATION` |
| Vertex AI on Google Distributed Cloud air-gapped: services available on-premises | Google Cloud docs | https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/vertex-ai-overview | Yes. Gemini specifically on GDC air-gapped and in preview on GDC connected is **[secondary]** |
| Vertex AI IRAP status and per-service scope | Google Cloud compliance page | https://cloud.google.com/security/compliance/irap | **Failed**: the page returned truncated content on two attempts. Only a search extract was available, saying Google Cloud and Workspace were found "strongly aligned" with OFFICIAL and PROTECTED ISM controls **[secondary]**, with no per-service scope list. Still `PENDING_VERIFICATION` |
| Sovereign options context | IBRS analysis cited by research | https://ibrs.com.au/practices/strategy-transformation/vendoriq-google-leans-into-sovereign-ai/ | Not re-opened; research-era **[secondary]** |
| Regional availability and machine types for self-deployed Model Garden open models | Google Cloud docs | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models | Opened, but the page does not state regions or machine types. `PENDING_VERIFICATION` per model |

**Naming drift to expect.** Google's own documentation now brands Vertex AI as "Gemini Enterprise
Agent Platform" on these pages while the client's console and procurement papers may still say
"Vertex AI". Record both names.

### Self-hosting: serving stacks and our own VPS

| Fact | Where | URL | Checked 2026-11-08 |
|---|---|---|---|
| vLLM self-description, OpenAI-compatible API server plus Anthropic Messages API and gRPC, hardware support, quantisation formats | vLLM docs | https://docs.vllm.ai/en/latest/ | Yes |
| SGLang self-description, Hugging Face and OpenAI API compatibility, hardware support, production-scale claim | SGLang docs | https://docs.sglang.io/ | Yes. `docs.sglang.ai` 301-redirects here |
| Text Generation Inference archive status (archived read-only 21 March 2026, maintenance mode, Hugging Face points to vLLM, SGLang, llama.cpp and MLX) | GitHub | https://github.com/huggingface/text-generation-inference | Yes. Not for new builds |
| Model licence, context length and hardware requirements per open-weight model | The model's own card on its vendor or Hugging Face page | per model | Required per engagement. Never assume open weights are commercially licensed |
| Hosting provider data-centre locations, and where your own VPS instances actually sit | Provider API or console; the provider's own data-centre list is the source, not a marketing page | per provider | Required before citing any self-hosted box as Australian |
| Australian GPU VPS availability, GPU class and quota | The chosen provider, in writing | `PENDING_VERIFICATION` per provider | Usually a new procurement; verify GPU class and quota in writing |

### On-premises: Australian government controls

| Fact | Where | URL | Checked 2026-11-08 |
|---|---|---|---|
| Essential Eight mitigation strategies, maturity levels and target level | ASD ACSC. Held in the register as AU-23 (checked 2026-11-08) | https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-maturity-model | **Failed**: cyber.gov.au did not respond to automated fetches. Cite register AU-23 for the framework and read this page before stating strategy names, level numbering or a target level |
| ISM current release and the AI-specific controls added since December 2025 (general-purpose AI usage policy, source and integrity of models, weights and training data, fine-grained access control, content filtering, distinct AI agent identities, board accountability) | ASD ACSC ISM guidelines | https://www.cyber.gov.au/ism/latest | **Failed**: three automated fetches timed out. The release at the time of checking was the September 2026 ISM. **Control identifiers and wording are `PENDING_VERIFICATION`** and must be read from the ISM guidelines before appearing in a client deliverable |
| ISM and IRAP conclusions for a specific client environment | The client's own IRAP assessor | not a DDD output | By rule: DDD identifies controls, the client's assessor concludes |

### Anthropic

| Fact | Where | URL |
|---|---|---|
| Pricing, prompt caching rates | Anthropic pricing docs | https://platform.claude.com/docs/en/about-claude/pricing |
| Batch processing discount and window | Anthropic batch docs | https://platform.claude.com/docs/en/build-with-claude/batch-processing.md |
| Inference and storage location | Secondary sources only in research | https://www.futureability.com/claude-data-residency-australia **[secondary]**, https://www.nbh.co/learn/claude-queensland-data-centre-does-it-matter-to-you/ **[secondary]**; primary page `PENDING_VERIFICATION` |
| Certifications (SOC 2, ISO 42001) | Anthropic trust documentation, verified with the issuer | `PENDING_VERIFICATION` |
| Data usage and training terms per product | Commercial terms for the product tier | `PENDING_VERIFICATION` |

### OpenAI direct

Not researched. Residency, retention, training terms and certifications: all `PENDING_VERIFICATION`.

### Sovereignty and regulation

| Fact | URL |
|---|---|
| CLOUD Act exposure of onshore processing | https://aivy.com.au/resources/ai-data-residency-australia-cloud-act/ **[secondary]** |
| APRA AI letter (supplier dependence, exit and substitution) | https://www.apra.gov.au/news-and-publications/apra-letter-industry-artificial-intelligence-ai |
| ACSC careful adoption of agentic AI services | https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services |
| OAIC guidance on commercially available AI products | https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products |

## 3. Research snapshot items that most often go stale

1. Claude models on Bedrock `au.*` (research cites an April 2026 list plus newer models reported
   from a secondary source).
2. Model availability in Azure Australia East per deployment type, and retirement dates.
3. Vertex AI models processed in Sydney or Melbourne.
4. Anthropic and OpenAI residency offerings (a Queensland data centre lease from 2027 has been
   reported; no residency commitment announced as at the research date).
5. Every price.
6. Which Gemini models have ML processing in `australia-southeast1` (the table moved between the
   research date and 2026-11-08, and two reads on the same day returned slightly different lists).
7. Whether CMEK has reached Australian Gemini inference (as at 2026-11-08 it had not: `us` and `eu`
   multi-regions only for resourceless APIs).
8. Whether Vertex AI is in scope for the Assured Workloads Australia control packages, and the
   IRAP position for Vertex AI.
9. Google's product naming for Vertex AI in its own docs ("Gemini Enterprise Agent Platform" as at
   2026-11-08).
10. Open-weight serving stacks: which are maintained and which are archived (TGI went to
    maintenance mode and was archived on 21 March 2026), and each model's licence terms.
11. Where your own hosts actually sit: provider data-centre list, checked live.
12. The ISM release and its AI control identifiers, and the Essential Eight maturity model wording.
