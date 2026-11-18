# Security baseline per platform

*v0.1.0, 2026-11-08. Sources: research B4, B5 and the ACSC agentic AI guidance it cites (register
AU-23), engagement conventions s2 (least agency, Doppler), harvested Azure sample
`productionizing.md` and `login_and_acl.md`, harvested huggingface/skills SageMaker IAM and
production-defaults skills. Service and feature names are the general mechanism each cloud offers;
confirm the current feature for the specific AI service and region before relying on it (some AI
services lag the platform on private networking or customer-managed keys).*

## 1. Baseline controls (every platform, every engagement)

| # | Control | Minimum |
|---|---|---|
| B1 | Identity and SSO | Users sign in through the client's identity provider; MFA; no shared accounts; service identities per application with least privilege |
| B2 | No-training and retention terms | Business or enterprise tier whose terms exclude training on client data, verified for the exact product (FAQ Q3); retention and abuse-monitoring settings recorded |
| B3 | Secrets | Credentials and keys only in a secrets manager (e.g. Doppler) or the client's own vault; never in code, files, chat or documents |
| B4 | Network | Confidential and above (C2+): private connectivity to model, search and storage endpoints; no public inference ports on self-hosted servers |
| B5 | Encryption | At rest and in transit everywhere; customer-managed keys for C4 and above where the service supports them |
| B6 | Logging and audit | Central logs in the same Australian region; who called which model with what data class; access to prompt and output logs restricted to an approved admin role; retention per client policy |
| B7 | Guardrails | Input and output checks appropriate to the tier (prompt injection, sensitive information, denied topics); guardrails run in the approved region |
| B8 | Least agency (agents) | Allow-listed tools, scoped short-lived credentials, human approval for irreversible or external actions, spend and rate caps, kill switch, full action log (conventions s2; research B5; ACSC agentic guidance) |
| B9 | Model and version pinning | Exact model IDs, inference profiles or deployments pinned; retirement dates tracked; changes trigger eval re-runs |
| B10 | Cost controls | Budgets and alerts; per-application quotas at the gateway |
| B11 | Environments | Separate sandbox, staging and production; the practice builds in sandbox or staging only (conventions s2) |
| B12 | Incident readiness | Who is notified, how a key is revoked, how the kill switch is pulled, vendor incident notification terms (vendor due diligence gate) |

## 2. Per-platform mapping

| Control | AWS (Bedrock, SageMaker) | Azure (AI Foundry / OpenAI, AI Search) | Google Cloud (Vertex AI) | Vendor direct (Anthropic, OpenAI) |
|---|---|---|---|---|
| B1 SSO and service identity | Federate the client's identity provider into AWS; IAM roles per application; for SageMaker, reuse a validated execution role and scope it to the model bucket, container pulls and logs, never a full-access managed policy (harvested IAM preflight) | Entra ID for users; managed identities for services; the RAG pattern uses on-behalf-of flow so queries run as the user (harvested `login_and_acl.md`) | Google Cloud IAM with the client's identity provider; service accounts per application | Enterprise SSO where the product offers it (`PENDING_VERIFICATION` per product); API keys per application held in Doppler |
| B4 Network | VPC endpoints / private connectivity to Bedrock and other services where offered; SageMaker endpoints in a VPC (the harvested defaults do not set VPC config: we require it for C2+) | Deploy inside a virtual network with private endpoints and a private DNS zone for internal apps; API Management in front (harvested `productionizing.md`); the Foundry baseline and AVM landing zone are network-isolated starting points | Private connectivity options for Vertex endpoints `PENDING_VERIFICATION` | Public internet endpoints; restrict egress to the vendor's API domains from our servers |
| B5 Keys | AWS KMS customer-managed keys where the service supports them; the harvested SageMaker defaults do not set a KMS key: we require one for C4+ | Azure Key Vault customer-managed keys where supported | Cloud KMS customer-managed keys where supported | Vendor-managed; check enterprise options |
| B6 Logging | CloudTrail for API activity; CloudWatch logs, metrics and alarms (harvested defaults enable alarms; alarms need a notification target); model invocation logging stored in an Australian region with restricted access | Azure Monitor / Application Insights in an Australian region; the harvested evaluation doc shows querying dependency logs for throttling | Cloud Logging in an Australian region | Our own gateway logs in Australia; vendor console logs are offshore |
| B7 Guardrails | Bedrock Guardrails (available in Sydney per research); Automated Reasoning checks (Sydney, June 2026) | Platform content filtering and Prompt Shields-type controls `PENDING_VERIFICATION` for current names and region | Platform safety settings `PENDING_VERIFICATION` | Our own input and output checks in the application or gateway |
| B9 Pinning | Pin `au.*` inference profile and model IDs; never fall back to `global.*` silently | Pin deployment name, model version and **deployment type (Standard)**; track retirement notices | Pin model version and **regional** endpoint, never `global` for C2+ | Pin model IDs; track deprecation notices |
| Assurance evidence | IRAP report via AWS Artifact (Bedrock excluding Marketplace at PROTECTED; AgentCore added 2026 Phase 1a) | Microsoft IRAP offering page, service by service | `PENDING_VERIFICATION` | `PENDING_VERIFICATION` |

## 3. Self-managed VPS and on-premises

| Control | Minimum |
|---|---|
| Host hardening | Minimal OS, automatic security updates or a named patch owner and schedule, SSH keys only, no root login, firewall default-deny |
| Inference exposure | Model servers (vLLM, SGLang, llama.cpp, Ollama) listen on localhost or a private interface; an authenticating reverse proxy with TLS in front; never `0.0.0.0` on a public interface |
| Access | VPN or zero-trust access for admins; per-application API keys at the proxy or gateway |
| Model supply chain | Weights downloaded from official or reviewed repositories, pinned by revision or checksum; `trust-remote-code` only for reviewed, pinned repositories |
| Data | Encrypted disks; backups in Australia, tested restores; logs with restricted access |
| Monitoring | Uptime, GPU and disk alerts; security logs retained |
| Ownership | The client accepts the operations burden in writing (data-class matrix C8) or buys it as `run-ongoing` |
| Essential Eight | For on-premises in clients that follow it, align host controls with the client's Essential Eight maturity target (register AU-23) |

## 4. Evidence pack for sign-off

`ai-compliance-officer` checks at stage 6: screenshots or exported configuration showing region and
deployment type per model, network isolation, key configuration, logging location and access,
guardrail configuration, no-training terms (document and date), pinned versions, budgets, and the
exit plan. Missing evidence for a tier's mandatory controls blocks sign-off
(`ai-compliance-risk/templates/compliance-signoff-checklist.md`).
