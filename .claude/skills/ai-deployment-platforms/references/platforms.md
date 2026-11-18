# Platform detail

*v0.2.0, 2026-11-08. Sources: research B2, B4, B6 (`ai-dept-web-research-2026-11-08.md`), GitHub
research area 5 (`ai-dept-github-research-2026-11-08.md`), harvested Azure sample docs and
huggingface/skills SageMaker skills. Every fact here carries its research date and must be
re-verified live before a client design relies on it (`verify-live.md`). Model names are
deliberately omitted.*

*v0.2.0 (2026-11-08): sections 3 (Google Cloud), 6 (self-managed VPS) and 7 (on-premises GPU)
rewritten to the depth of sections 1 and 2, after a review found the founder had named four
deployment options and only two were treated properly. Every factual claim added in those three
sections was verified live on 2026-11-08 against the vendor's own documentation, with the URL
inline; the URLs are also recorded in `verify-live.md` so the next person checks the same pages.
Two corrections fell out of the checks: DDD's own VPS instances are not in Australia (section 6),
and Text Generation Inference is archived upstream (section 7). Sections 1, 2, 4, 5 and 8 are
unchanged from v0.1.0 and still carry the research date, not a live check.*

## 1. AWS Bedrock

**Regions (research B4):** Sydney `ap-southeast-2`, Melbourne `ap-southeast-4`; Auckland
`ap-southeast-6` also listed.

**Residency mechanism.** Geographic cross-region inference profiles with the `au.` prefix route
requests only between Sydney and Melbourne. A `global.` profile routes anywhere. Research found
some Claude models available only via `global.*` at a point in time, and newer models reported on
the AU profile from a secondary source. So: confirm the exact model ID is available on an `au.*`
profile in the account on the day, and pin the inference profile ID in configuration so nobody
switches to `global.*` by accident.

**Assurance.** Bedrock (excluding Marketplace) is in scope for IRAP PROTECTED; the 2026 Phase 1a
IRAP report added Bedrock AgentCore (research cites 167 services at PROTECTED). The report is
available through AWS Artifact. IRAP scope is a statement about the service, not about the
client's configuration: the client's own security assessment still applies.

**Components relevant to our patterns.**

| Component | Use | Research status |
|---|---|---|
| Bedrock Guardrails | Input and output filtering, denied topics, sensitive information filters | Available in Sydney (June 2026 announcement) |
| Automated Reasoning checks | Policy-based verification of outputs | Added in Sydney June 2026 |
| Knowledge Bases | Managed RAG | Metadata filtering and connector ACL ingestion for some sources; specifics `PENDING_VERIFICATION` |
| AgentCore | Agent runtime and tooling | In the 2026 IRAP Phase 1a report; feature set to verify |
| Custom Model Import | Serve imported open-weight weights behind the Bedrock API | Per harvested HF planner: supported base families, weights only; Australian region availability `PENDING_VERIFICATION` |
| SageMaker endpoints | Self-managed model hosting with autoscaling and alarms | Method in `ai-model-customisation/references/tools/sagemaker-hosting.md`; GPU quota per region per account |

**Reference repos (GitHub research area 5):** `aws-samples/generative-ai-use-cases` (MIT-0,
deployable business app on Bedrock, a good "show the client" asset), `aws-samples/amazon-bedrock-samples`
(MIT-0), `awslabs/generative-ai-cdk-constructs` (Apache-2.0), `aws-samples/sample-genai-on-eks-starter-kit`
(MIT-0, self-hosted stack on EKS), `aws-ia/terraform-aws-eks-blueprints` (Apache-2.0).
`aws-samples/bedrock-access-gateway` is archived: use LiteLLM instead.

**Watch for:** model availability per profile; quotas per region; Marketplace models sit outside
the IRAP scope statement; logs and knowledge base stores must also be in Sydney or Melbourne.

## 2. Microsoft Azure (Azure OpenAI / AI Foundry)

**Region:** Australia East (research B4).

**Deployment types (research B4).** A **Standard (regional)** deployment in Australia East
processes in-region. **Data Zone** and **Global** deployments may process elsewhere. The
deployment type is chosen per model deployment, so a design must name it and the build must be
checked against it. Model availability in Australia East lags US regions; plan for model
retirement (Tech Community continuity thread cited in the research).

**Assurance.** Azure Australian regions are IRAP assessed to PROTECTED; check service by service
on Microsoft's IRAP offering page.

**Components.**

| Component | Use | Status |
|---|---|---|
| Azure AI Search | Hybrid retrieval with document-level security: security filters against Entra principals, native ACL/RBAC scope ingestion for ADLS Gen2 and similar sources, Purview sensitivity-label enforcement | Verified in research B2; harvested sample shows the built-in query-time enforcement pattern (`ai-rag-engineering`) |
| Azure AI Foundry / Azure OpenAI | Model deployments | Region and deployment-type availability per model: verify |
| API Management as an AI gateway | Chargeback, quotas, central keys across business units | `Azure-Samples/ai-hub-gateway-solution-accelerator` (MIT) |

**Landing zone.** `Azure/terraform-azurerm-avm-ptn-aiml-landing-zone` (MIT) is the Azure Verified
Module for an AI/ML landing zone in Terraform, the best Terraform landing-zone module found
(GitHub research area 5). `Azure-Samples/microsoft-foundry-baseline` (MIT) is the reference
implementation for the network-isolated Foundry chat baseline. The older
`Azure/azure-openai-landing-zone` is superseded by the AVM module. Use the AVM module as the
starting point for L and XL clients on Azure; pin its version; review every default against the
security baseline.

**Production notes from the harvested sample (`productionizing.md`):** restrict the app to
authenticated users, deploy inside a virtual network with a private DNS zone for internal use,
consider API Management in front, size search and app tiers for real load, load-test.

## 3. Google Cloud (Vertex AI)

**What it is, and when it fits.** Google's managed platform for Gemini models, embeddings, Vector
Search, self-deployed open-weight models and an agent runtime. It fits a client whose identity,
warehouse and suite are already Google (Workspace, BigQuery, Cloud IAM) and whose documents already
sit in Cloud Storage, BigQuery or Drive. It is the weakest of the three hyperscalers on Australian
generative AI residency, so for a Google-centric client with C3 or above the honest answer is often
hybrid: keep the data and retrieval on Google Cloud, put inference where residency holds.

**Regions, and what the residency actually gives.** Vertex AI runs in `australia-southeast1`
(Sydney) and `australia-southeast2` (Melbourne), and that page states Google "stores and processes
your data only in the region that you specify for all features of Agent Platform except for data
labeling tasks and any feature in experimental or preview launch status", and that the platform
"doesn't support a global location" for its own resources (checked 2026-11-08:
https://docs.cloud.google.com/vertex-ai/docs/general/locations). Generative AI inference is a
separate question, governed by the endpoint: requests to a `global` endpoint "may be processed in
any Google Cloud location around the world, and therefore don't provide any data residency
guarantees", while data at rest stays in the selected location whichever endpoint is called
(checked 2026-11-08:
https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency). So storage in
Sydney plus a `global` endpoint is **not** Australian processing, and a client will hear it as if it
were. On the day, that page's ML-processing table listed only `australia-southeast1`, not Melbourne,
and only a handful of models against it (two reads returned Gemini 3.5 Flash and Gemini 2.5 Flash
128k, one also a text embedding model). Do not carry those names forward: read the Australia rows
and record the exact IDs with the date. These pages now brand Vertex AI as "Gemini Enterprise Agent
Platform", so Google's docs and the client's console may use different names; name both in the ADR.

**Components that must also be in-region:** the model endpoint (regional, never `global`), the
embedding model, Vector Search indexes, the search data store, the Cloud Storage or BigQuery source
behind retrieval, the document parser (Document AI has its own region list), the agent runtime, any
session or memory store, caches, and Cloud Logging sinks.

**Identity and network.** Cloud IAM with one service account per application; Workforce Identity
Federation for the client's own identity provider. Permission-aware retrieval is real here: access
control for Vertex AI Search data stores covers "Cloud Storage, BigQuery, Google Drive, and all
third-party data sources", works with Google Identity or federation (Entra ID, Okta, Ping), and
Google uses the identity provider to decide whether the user may see each result; ACLs arrive as an
`acl_info` metadata field for Cloud Storage and a required-schema column for BigQuery (checked
2026-11-08: https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control).
VPC Service Controls supports Vertex AI, including generative AI, Vector Search, online and batch
inference, custom training and the agent runtime, and combines with Private Service Connect for
Google APIs (checked 2026-11-08:
https://docs.cloud.google.com/vertex-ai/docs/general/vpc-service-controls).

**Assurance (weaker than AWS and Azure, and the gap is ours to disclose).** Google publishes
Assured Workloads control packages "Australia Data Boundary" (free tier) and "Australia Data
Boundary and Support" (premium, which also limits support personnel to the United States, Canada,
Australia, New Zealand and the United Kingdom) (verified 2026-11-08:
https://docs.cloud.google.com/assured-workloads/docs/control-packages). Whether Vertex AI is in
scope for those two Australia packages is `PENDING_VERIFICATION`: Vertex AI is in the supported
products list but the Australia columns were truncated when we read it
(https://docs.cloud.google.com/assured-workloads/docs/supported-products). **Vertex AI IRAP scope
is `PENDING_VERIFICATION`**: the Google Cloud IRAP page would not render on 2026-11-08 (truncated
twice), and the only statement we saw, through a search extract, is that an assessor found Google
Cloud and Workspace "strongly aligned" with OFFICIAL and PROTECTED ISM controls **[secondary]**,
which is a platform alignment claim, not the per-service scope list AWS and Microsoft publish
(https://cloud.google.com/security/compliance/irap). Any "Assured Workloads Australia meets IRAP"
claim is also `PENDING_VERIFICATION`: the control-packages page names neither IRAP nor the Hosting
Certification Framework.

**Google Distributed Cloud, for sovereign needs.** Vertex AI runs on GDC in an air-gapped
configuration inside the client's own data centre, with Generative AI, Online Prediction, OCR,
Speech-to-Text, Translation and Workbench among the listed services, "to help meet your data
sovereignty and compliance requirements" (checked 2026-11-08:
https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/vertex-ai-overview).
Reports that Gemini itself is on GDC air-gapped, and in preview on GDC connected, are
**[secondary]** (vendor coverage and IBRS). This is the route for a client wanting Google models
with no cloud egress. It is a capital project with Google hardware and a Google contract, not a
configuration change: get Australian availability, the minimum footprint and the model list
confirmed by Google in writing before it enters a proposal.

**Operational burden, and who carries it.** Google patches and scales the models and search
service; the client's cloud team owns IAM, VPC-SC perimeters, budgets and quotas; DDD owns the
application, prompts, eval set and index. Two parts cost DDD more here than on the other clouds:
producing and maintaining the `acl_info` metadata for access-controlled data stores, and tracking
which Gemini models are still processed in Sydney as the table moves. On GDC the client's
infrastructure team carries the platform and DDD should not take uptime responsibility for it.

**Exit and portability.** Model calls behind our own gateway port to Bedrock or Azure with prompt
work only. The costly parts to leave are Vector Search indexes, access-controlled data stores (not
reconfigurable, so a move is a rebuild), grounding and agent-runtime configuration, and retrieval
bound to BigQuery. Keep source documents and the ACL mapping in Cloud Storage or BigQuery as the
system of record so the index is always rebuildable, and keep prompts and evals in the engagement
repo, never only in the console.

**Cost drivers** (no prices here; price from the vendor page at quote time with the date): tokens
per model tier; embedding volume and re-index frequency; Vector Search index size and serving
nodes; data store and query volume; Provisioned Throughput, which Google describes as "a fixed-cost,
fixed-term subscription available in several term-lengths that reserves throughput", bought per
model per location (checked 2026-11-08:
https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview); GPU or
TPU hours for any self-deployed Model Garden model including idle time; Cloud Logging ingestion and
retention; egress; the Assured Workloads premium tier; support plan. GDC is dominated by hardware,
licensing and site costs, quoted by Google.

**Traps.**

| # | Trap | Why it bites |
|---|---|---|
| 1 | `global` endpoint is the convenient default | It is the one with no residency guarantee. Pin the regional endpoint and test that a silent `global` fallback cannot happen |
| 2 | Preview features sit outside the residency statement | The locations page excludes experimental and preview features by name. If a flow needs one, the residency claim does not hold for that flow. Say so |
| 3 | Customer-managed keys do not reach Australian Gemini inference | Vertex supports CMEK across datasets, models, endpoints, training, Vector Search and the agent runtime, but for resourceless (request-based) Gemini APIs the documented support is the Gemini Live API and Interactions API in the `us` and `eu` multi-regions only, and Memory Bank and Sessions on the global endpoint are unsupported (checked 2026-11-08: https://docs.cloud.google.com/vertex-ai/docs/general/cmek). Matrix condition K5 asks for CMEK "where supported" at C4: here the answer for the inference leg is likely no |
| 4 | VPC Service Controls costs you logging | "Request and response logging isn't available with VPC Service Controls", and URL context live fetching is disabled in a perimeter. That is in direct tension with baseline control B6. Decide deliberately and record it |
| 5 | Access control cannot be retrofitted to a data store | "You must select this setting during data store creation. You can't turn this setting on or off for an existing data store." Getting it wrong means a rebuild and re-index |
| 6 | Model Garden one-click public endpoints are unsupported inside a perimeter | Use a private endpoint. Regional availability and machine types for self-deployed Model Garden models are `PENDING_VERIFICATION` per model |
| 7 | Melbourne is not a generative AI residency region on our evidence | Vertex AI exists in `australia-southeast2`, but the ML-processing table did not list it. Do not design two-region Australian failover for Gemini without verifying it |

**Reference repos:** `GoogleCloudPlatform/generative-ai` (Apache-2.0), `GoogleCloudPlatform/terraform-genai-rag`
(Apache-2.0). `agent-starter-pack` and `ai-on-gke` are archived.

**Fit.** Google-centric clients whose data classes allow processing where the needed model runs, or
hybrid designs that keep sensitive flows on another platform.

## 4. Anthropic direct (API, Claude Enterprise)

Research B4 **[secondary]**: global or US-only inference with US storage as at October 2026; an
Anthropic Queensland data centre lease from 2027 has been reported, with no residency commitment
announced. Certifications (SOC 2, ISO 42001): `PENDING_VERIFICATION`. Fit: low-sensitivity data where
onshore processing is not required. For Claude with Australian residency the researched route is
Bedrock `au.*`.

Cost levers on Anthropic's own pricing pages (research B6): Batch API 50% off within a 24-hour
window; prompt caching reads at 10% of the base input rate, 5-minute and 1-hour cache durations,
stacking with batch. Verify on the pricing page at quote time; Bedrock pricing and caching support
are separate and must be checked on AWS's pages.

## 5. OpenAI direct

Not covered by the research: residency, data-handling and certification facts are
`PENDING_VERIFICATION`. Until verified, treat like Anthropic direct (low-sensitivity data only). For
OpenAI models with Australian processing, the researched route is an Azure Standard deployment in
Australia East.

## 6. Self-managed VPS in an Australian data centre

**What it is, and when it fits.** A virtual machine we rent from a hosting provider, in a data
centre whose location we choose, running an open-weight model behind our own serving stack, or
running the workflow tooling (n8n and similar) that surrounds an AI system. It fits three cases and
no others: (a) a small open-weight model doing a narrow, high-volume, low-sensitivity task where
per-token API cost is the problem; (b) workflow and integration tooling that needs to live
somewhere, with model calls going out to a hyperscaler; (c) a client who will not sign with a
hyperscaler and whose data class still permits a provider-assessed host. It is the wrong answer
whenever the client needs vendor assurance, high availability, or a frontier model.

**Australian residency, and what it actually gives.** Full control of the location, and nothing
else. "Australian data centre" is a claim about one component. It holds only if the model weights,
the serving process, the vector store, the logs, the backups and the workflow tool are all on hosts
in Australia, and it fails the moment the application calls an offshore API for embeddings, parsing
or a fallback model. Get the data-centre address and the legal entity operating it from the
provider in writing, not from a marketing page: a provider's "AU region" can be resold capacity.

**Your own VPS pattern: verify it before citing it.** A real lesson from building this practice:
check your provider's data-centre list live through its API before claiming any hosting location.
Several popular VPS providers publish no Australian data centre at all, and an instance you assume
is onshore may not be. Two consequences: **never cite your own VPS as evidence of an Australian
hosting pattern without a live check**, and an Australian GPU VPS is usually a new procurement with
its own cost and lead time, not an extension of what you already run. An offshore general-purpose
VPS is fine as a demonstration host for non-client data, and nothing above C1 should go near it.

**Components and the stack.** Serving: vLLM, which describes itself as "a fast and easy-to-use
library for LLM inference and serving" and exposes an "OpenAI-compatible API server, plus Anthropic
Messages API and gRPC support" across NVIDIA and AMD GPUs and x86, ARM and PowerPC CPUs, with
FP8, INT8, INT4, GPTQ and AWQ quantisation among others (checked 2026-11-08:
https://docs.vllm.ai/en/latest/). SGLang is the alternative, "a high-performance serving framework
for large language and multimodal models", Hugging Face and OpenAI API compatible, and it states it
"powers large-scale production deployments, generating trillions of tokens each day across more
than 400,000 GPUs worldwide" (checked 2026-11-08: https://docs.sglang.io/; note that
`docs.sglang.ai` issues a 301 to `docs.sglang.io`). Either gives an OpenAI-shaped endpoint, which
is what makes the exit plan cheap. Model names, sizes and licences are deliberately not listed in
this skill: read the model's own card for the licence, the context length and the hardware it needs
on the day, and record it (`verify-live.md`).

**Identity and network controls.** No identity platform comes with a VPS, so we build the minimum:
the model server listens on localhost or a private interface only, never a public `0.0.0.0`; an
authenticating reverse proxy with TLS in front; per-application API keys issued at the proxy and
held in a secrets manager; admin access by SSH key over VPN or a zero-trust connector, no password login, no
root login, firewall default-deny. Client staff do not get accounts on the box; they reach the
application, which reaches the model. Full control list: `security-baseline.md` s3.

**Assurance position: we have none, and that is the headline.** A hosting provider is not IRAP
assessed unless it says so and shows the report, and most do not. There is no vendor attestation to
inherit, no SOC 2 covering our configuration, no shared-responsibility model doing work for us. The
client is assessing DDD, not a hyperscaler. Say that plainly in the decision record: "this option
carries no third-party assurance; the controls are the ones DDD implements and the client audits."
Any provider certification goes in the record only after it is verified with the issuer, with the
date (matrix condition K7).

**Operational burden, and who carries it.** DDD, and it is continuous: operating system and
dependency patching, kernel reboots, model server upgrades, certificate renewal, disk and GPU
monitoring, log rotation, backup verification with tested restores, and being the person who gets
called when inference stops at 7pm. There is no managed autoscaling and no multi-zone failover
unless we build and pay for it, so a single VPS is a single point of failure and should be
described to the client as one. This burden is a priced line item in the `run-ongoing` bucket, or
the client accepts it in writing and runs the host themselves. Do not sell a VPS deployment with no
run line: that is how an unpatched model server ends up on the public internet two years later.

**Exit and portability.** The best feature of this option. Weights, prompts, the vector store and
the eval set are all files we hold, and the OpenAI-compatible endpoint means the application can be
repointed at Bedrock, Azure or another host by changing a base URL and a key. Keep the whole host
reproducible (container images or a configuration script in the engagement repo) so it can be
rebuilt on another provider in a day, and keep backups somewhere that is not the same provider.

**Cost drivers** (no prices here): GPU class and count, and whether the instance runs always-on or
is stopped between batches; vCPU, RAM and disk for a CPU-only or workflow host; egress; snapshot and
backup storage; a second host if availability matters; and DDD's run hours, which on this option
usually exceed the hosting cost. A GPU VPS kept always-on for low volume is almost always dearer
than per-token API pricing: run that comparison with the client's own volumes before recommending
it.

**Traps.**

| # | Trap | Why it bites |
|---|---|---|
| 1 | "Australian" provider with no verified data-centre location | Resold or offshore capacity destroys the residency claim that justified the whole option. Get it in writing |
| 2 | Public inference port | A model server bound to `0.0.0.0` with no auth is an open API on someone else's bill, and a data leak. Private interface plus authenticating proxy, always |
| 3 | No GPU where one was assumed | General-purpose VPS plans have no GPU (DDD's own two do not). Confirm GPU availability and quota with the provider before scoping |
| 4 | Offshore calls inside an "onshore" design | Embeddings, document parsing, OCR or a fallback model quietly going to an offshore API breaks the claim. Audit every outbound call |
| 5 | Model supply chain | Weights pulled unpinned, or `trust-remote-code` on an unreviewed repository, is arbitrary code execution. Pin by revision or checksum |
| 6 | Licence assumed to be permissive | Open weights are not automatically commercially usable, and some carry acceptable-use terms. Read the licence on the model card per engagement |
| 7 | Patching with no named owner | The most common failure of this option, and it surfaces as an incident, not a ticket. Name the owner and the schedule in the record |

## 7. On-premises GPU (client-owned)

**What it is, and when it fits.** The client buys or leases GPU servers, puts them in their own
data centre or co-location rack, and serves open-weight models on their own network. Nothing leaves
the client's infrastructure. It fits a small number of real cases: C5 data (government
PROTECTED-level handling, legal professional privilege, defence-adjacent), a client whose own policy
says model inference must stay on their infrastructure, high steady-state volume where amortised
hardware beats per-token pricing, and air-gapped or poor-connectivity sites. It does not fit a
client who wants a frontier model, who has no infrastructure team, or who is hoping to save money on
low volume. Google Distributed Cloud (section 3) is the variant where the hardware is on-premises but
the platform is Google's.

**Residency, and what it actually gives.** Total sovereignty for the inference leg, and this is the
only option where the CLOUD Act caveat in the SKILL does not apply to the model call. It is still
only a claim about the components that are actually on-premises. Keep the whole flow local: weights,
serving process, embedding model, vector store, document parser, logs, traces and backups. A single
offshore call for OCR, a managed observability SaaS, or a frontier-model fallback for "hard
questions" collapses the claim, and on-premises builds are exactly where those creep in.

**Serving stack.** vLLM for production and SGLang as the alternative, both verified above in section
6. **Text Generation Inference is archived upstream and is not for new builds**: the repository is
archived and read-only, archived 21 March 2026, stating "text-generation-inference is now in
maintenance mode. Going forward, we will accept pull requests for minor bug fixes, documentation
improvements and lightweight maintenance tasks", and Hugging Face now points users to vLLM, SGLang,
llama.cpp and MLX (checked 2026-11-08:
https://github.com/huggingface/text-generation-inference). Flag that archive status whenever TGI
comes up, including where `ai-discovery-scoping/references/solution-patterns.md` still lists it as an
option. Ollama is a development and evaluation convenience, not a production serving layer. For
clusters: KServe and KubeRay (Apache-2.0); NVIDIA GenerativeAIExamples (Apache-2.0) for NIM-based
reference workflows. As with the VPS option, both vLLM and SGLang expose an OpenAI-compatible
endpoint, which is what keeps the exit plan cheap.

**Identity and network controls.** The client's own: their directory for user identity, their
network segmentation to put the GPU hosts in a restricted zone, their jump hosts and privileged
access management for admin access, their TLS and certificate authority. DDD's job is to specify
what the AI system needs (a service identity per application, per-application keys at the gateway,
no direct user access to the model port, egress rules that permit nothing by default) and to let the
client's security team implement it in their own controls. Do not stand up a parallel identity
system beside the client's.

**Assurance, and what the client inherits.** There is no vendor attestation at all here, and that is
the point: the client's own control framework is the assurance. For a client following ASD's
Essential Eight, the GPU hosts and the model server are in scope like any other application, so
application control, patching applications and operating systems, restricting administrative
privileges, multi-factor authentication and backups all apply to them (register AU-23, checked
2026-11-08; the Essential Eight maturity model page is the source for the current wording and the
maturity levels, and the client sets the target level, not DDD). For Commonwealth entities and their
suppliers the ISM applies: the current release at the time of checking is the September 2026 ISM on
cyber.gov.au, which has added AI-specific controls since December 2025 covering a general-purpose AI
usage policy, verifying the source and integrity of models, weights and training data, fine-grained
access control for AI applications, content filtering, distinct identities for AI agents and board
accountability. **The exact control identifiers and their current wording are
`PENDING_VERIFICATION`**: cyber.gov.au did not respond to three automated fetches on 2026-11-08, and
the control list above came from a search summary mixing cyber.gov.au PDFs with secondary
commentary. Read the ISM guidelines on cyber.gov.au and record the control IDs before any of this
reaches a client deliverable, and route the ISM and IRAP conclusions themselves to the client's own
security assessor, not to us.

**Operational burden, and who carries it.** The heaviest of any option, and it is the client's, not
DDD's. Hardware procurement with long lead times, rack space, power and cooling, GPU driver and
CUDA-stack upgrades (the most common source of breakage), model server upgrades, capacity planning
for concurrency, monitoring, spares and a hardware failure plan, and someone who can debug a model
that has stopped loading. The honest MLOps reality for an Australian SMB: most clients in the S and
M size bands do not have this skill in-house and will not hire it, and DDD does not sell 24/7
infrastructure support. So the decision record names the person or vendor who owns the hosts, or the
recommendation is not on-premises. Where the client wants on-premises sovereignty without the skill,
Google Distributed Cloud or a managed sovereign provider is the more honest recommendation than an
unsupported GPU box.

**Capex and the money shape.** This is a capital purchase on the client's balance sheet (or a
lease), with a depreciation schedule, a refresh cycle, and power as an ongoing operating cost. It
changes who approves the project: a finance or board decision, not a monthly tool spend, which
usually lengthens the sales cycle and should be flagged to `ai-proposal-pricing` early. Hardware is
quoted by the client's supplier, never by us.

**Exit and portability.** Strong on the software side and weak on the capital side. Weights, prompts,
vector store and eval set are files the client holds; the OpenAI-compatible endpoint means the
application can be repointed to a cloud model by changing a base URL and a key, so a failed
on-premises build is recoverable. The hardware is the sunk part: it cannot be handed back. Say that
in the decision record, and prove the fallback path works (route a test workload to the cloud
alternative once, in staging) rather than asserting it.

**Cost drivers** (no prices here, and hardware prices come from the client's supplier): GPU model,
count and memory; server, network and rack; power and cooling; vendor support contracts; spares and
refresh cycle; the client's engineering time; storage for weights, documents and the vector store;
backup and disaster recovery; and DDD's build and tuning hours. Utilisation decides whether this
option is sane: a box at low utilisation is the most expensive way to run inference, and the
break-even calculation uses the client's own measured volumes, never a vendor's.

**Traps.**

| # | Trap | Why it bites |
|---|---|---|
| 1 | TGI chosen because it is familiar | Archived upstream 21 March 2026 and in maintenance mode. Use vLLM or SGLang for new builds |
| 2 | Offshore leakage in an "air-gapped" design | OCR, observability SaaS, telemetry in a serving framework, or a frontier-model fallback. Audit every outbound call and turn framework telemetry off deliberately |
| 3 | GPU memory sized for the model but not the context and concurrency | Works in the demo, fails under real load. Size against measured concurrency and context length, then load-test |
| 4 | No one owns the CUDA and driver stack | A routine upgrade stops inference and there is no vendor to call. Name the owner before go-live |
| 5 | Open weights assumed to be commercially licensed | Read the licence and the acceptable-use terms per model per engagement |
| 6 | Quality expectation set by a frontier model | A small open-weight model on a narrow task can match; on open-ended work it will not. Set the expectation with an eval baseline before the hardware is bought, not after |
| 7 | Essential Eight and ISM treated as inherited | Nothing is inherited on-premises. Every control is the client's to implement and evidence, and the ISM control IDs are `PENDING_VERIFICATION` here |
| 8 | Single site, no failover | Hardware failure is an outage with a hardware lead time. Agree the degraded mode (cloud fallback, or the manual process) in advance |

**Fits** defence and defence-adjacent work, health records, legal privilege, and clients whose own
policy requires it.

## 8. Hybrid

Route each request by data class: sensitive classes to onshore Bedrock or self-hosted, public data
to any approved frontier API, through a gateway with a data-classification gate (research B4,
recommended for 500+ staff). Gateways: LiteLLM (MIT outside `enterprise/`; some SSO and admin
features sit in `enterprise/`, which is on the department's do-not-harvest list), Azure AI hub
gateway accelerator (MIT). SkyPilot (Apache-2.0) helps run occasional GPU jobs (for example a
fine-tuning run) across clouds, subject to the same residency rules.
