# Risk catalogue for mode (d) risk register

*v0.1.0, 2026-11-08. Seed lists for the per-project register. `scripts/ai_risk_register.py seed`
picks from these automatically by architecture flag; this file is the human-readable version and
the place to look up a risk's source. Licences and SHAs: `vendored-provenance.md`.*

## 1. NIST AI 600-1 Generative AI Profile: the 12 risks

Verified against the primary PDF (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf, section
2) on 2026-11-08. NIST AI 600-1 is **voluntary** (register INT-6). Names are NIST's; the
"when it applies" column is DDD guidance.

| # | NIST risk | When it usually applies to a DDD project |
|---|---|---|
| 1 | CBRN Information or Capabilities | Rare for business automation; consider only for open-ended public chat on frontier models |
| 2 | Confabulation | Every GenAI system |
| 3 | Dangerous, Violent, or Hateful Content | Public or customer-facing open chat |
| 4 | Data Privacy | Any personal information in prompts, retrieval, logs or training |
| 5 | Environmental Impacts | Large training or high-volume inference; usually noted, rarely rated High |
| 6 | Harmful Bias or Homogenization | Any output that ranks, scores or describes people |
| 7 | Human-AI Configuration | Every system a person relies on (automation bias, over-reliance) |
| 8 | Information Integrity | Generated content published externally |
| 9 | Information Security | Every system (integrations widen the attack surface) |
| 10 | Intellectual Property | Generated text, images or code used externally |
| 11 | Obscene, Degrading, and/or Abusive Content | Public-facing generation, image generation |
| 12 | Value Chain and Component Integration | Any third-party model, API, plugin or dataset |

## 2. CoSAI risk map (36 risks)

From `cosai-oasis/secure-ai-tooling` `risk-map/yaml/risks.yaml` (Apache-2.0, commit
622605a13fafaa2784acbdbe3f8d23ee22da4be7). IDs, titles, categories and mappings are CoSAI's.
OWASP mappings are CoSAI's own (IDs only). CoSAI pins ATLAS IDs to ATLAS v5.0.1; check them in
`threat-model.md` before citing. Short descriptions are DDD paraphrase.

| CoSAI ID | Title | CoSAI category | OWASP LLM (CoSAI map) | DDD flag |
|---|---|---|---|---|
| riskDataPoisoning | Data Poisoning | Supply chain and development | LLM05:2026 | fine_tune |
| riskUnauthorizedTrainingData | Unauthorized Training Data | Supply chain and development | - | fine_tune |
| riskModelSourceTampering | Model Source Tampering | Supply chain and development | LLM04:2026 | self_hosted |
| riskExcessiveDataHandling | Excessive Data Handling | Supply chain and development | LLM02:2026 | fine_tune |
| riskExcessiveDataHandlingDuringInference | Excessive Data Handling During Inference | Runtime data security | LLM02:2026 | personal_data |
| riskModelExfiltration | Model Exfiltration | Deployment and infrastructure | - | self_hosted |
| riskModelDeploymentTampering | Model Deployment Tampering | Deployment and infrastructure | LLM04:2026, LLM01:2026 | self_hosted |
| riskDenialOfMLService | Denial of ML Service | Runtime input security | LLM06:2026 | customer_facing |
| riskModelReverseEngineering | Model Reverse Engineering | Deployment and infrastructure | - | (custom models) |
| riskInsecureIntegratedComponent | Insecure Integrated Component | Deployment and infrastructure | LLM04:2026, LLM03:2026 | agent |
| riskPromptInjection | Prompt Injection | Runtime input security | LLM01:2026 | genai |
| riskModelEvasion | Model Evasion | Runtime input security | LLM01:2026 | (classifiers) |
| riskSensitiveDataDisclosure | Sensitive Data Disclosure | Runtime data security | LLM02:2026, LLM08:2026 | personal_data |
| riskInferredSensitiveData | Inferred Sensitive Data | Runtime data security | LLM02:2026, LLM07:2026 | decisions_about_people |
| riskInsecureModelOutput | Insecure Model Output | Runtime output security | LLM10:2026, LLM07:2026 | genai |
| riskRogueActions | Rogue Actions | Runtime output security | LLM03:2026 | agent |
| riskAcceleratorAndSystemSideChannels | Accelerator and System Side-channels | Deployment and infrastructure | - | (on-prem GPU) |
| riskEconomicDenialOfWallet | Economic Denial of Wallet | Runtime input security | - | customer_facing |
| riskFederatedDistributedTrainingPrivacy | Federated/Distributed Training Privacy | Supply chain and development | - | (rare) |
| riskAdapterPEFTInjection | Adapter/PEFT Injection | Deployment and infrastructure | - | fine_tune |
| riskToolRegistryTampering | Tool Registry Tampering | Deployment and infrastructure | LLM03:2026 | agent |
| riskOrchestratorRouteHijacking | Orchestrator/Route Hijack | Runtime output security | - | (model routers) |
| riskEvaluationBenchmarkManipulation | Evaluation/Benchmark Manipulation | Runtime data security | - | (evals) |
| riskCovertChannelsInModelOutputs | Covert Channels in Model Outputs | Runtime output security | - | (rare) |
| riskMaliciousLoaderDeserialization | Malicious Loader/Deserialization | Supply chain and development | - | self_hosted |
| riskToolSourceProvenance | Tool Source Provenance | Supply chain and development | LLM04:2026, LLM03:2026 | agent |
| riskPromptResponseCachePoisoning | Prompt/Response Cache Poisoning | Runtime data security | - | (caching) |
| riskRetrievalVectorStorePoisoning | Retrieval/Vector Store Poisoning | Runtime output security | - | rag |
| riskAgentDelegationChainOpacity | Agent Delegation Chain Opacity | Deployment and infrastructure | - | agent (multi-agent) |
| riskStaleAgentIdentityBinding | Stale Agent Identity Binding | Deployment and infrastructure | - | agent |
| riskMCPTransportHijacking | MCP Transport Hijacking | Deployment and infrastructure | - | agent (MCP) |
| riskShadowAndUnknownAgents | Shadow and Unknown Agents | Deployment and infrastructure | - | shadow_agents |
| riskRunawayAgentToolLoops | Runaway Agent Tool Loops | Runtime input security | LLM06:2026 | agent |
| riskAgenticDelegationConfusedDeputy | Agentic Delegation Confused Deputy | Deployment and infrastructure | LLM03:2026 | agent |
| riskCrossTenantCredentialPropagation | Cross-Tenant Credential Propagation | Deployment and infrastructure | LLM03:2026 | agent (multi-tenant) |
| riskZombieShadowMCPServers | Zombie / Shadow MCP Servers | Deployment and infrastructure | LLM04:2026 | agent (MCP) |

CoSAI also lists 37 controls (e.g. Agent Permissions, Agent Execution Bounds, Input Validation
and Sanitization, Output Validation and Sanitization, Red Teaming, Incident Response Management,
Risk Governance). Use their titles as control names in the register where they fit; their own
NIST AI RMF mappings (e.g. Agent Inventory Management to GOVERN-1.6 and MAP-3.4) are CoSAI's.

## 3. Australian legal and governance risks (DDD, from the register)

The two catalogues above are security and harm lenses. Australian projects also carry these,
which the seed script adds by flag:

| Risk | Flag | Register |
|---|---|---|
| ADM disclosure missing from privacy policy from 10 Dec 2026 | adm | AU-8 |
| Personal information entered into public consumer AI tools | personal_data | AU-11 |
| Supplier concentration, no tested exit or substitution plan | third_party_model | AU-15, AU-13 |
| No contestability for affected people | decisions_about_people | AU-16, AU-24 |
| Misleading statements or promises by a customer-facing AI | customer_facing | AU-22 |
| Training or fine-tuning on customer data beyond the collection purpose | fine_tune | AU-12 |
| Recording without consent (scribes, call tools) | (add manually) | AU-19, AU-7 |
| Solely automated rejection of candidates | (add manually, recruitment) | AU-24 |
| Sector rules from the industry pack | (add manually) | pack's governing-rules table |

## Register columns (match the script)

`id, title, category, source, likelihood (1-5), impact (1-5), inherent score and rating, controls,
owner, residual likelihood, residual impact, residual rating, treatment option, treatment adequacy`.
Category is one of security, privacy, fairness, safety, legal, operational, third-party.

Likelihood and impact are the consultant's judgement with the client, recorded with a one-line
reason in the working notes. Never leave a High or Critical risk without an owner.
