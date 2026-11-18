# Mode (f) Threat model: OWASP LLM, OWASP Agentic, MITRE ATLAS

*v0.1.0, 2026-11-08. Use with `ai-architect`'s data-flow and trust-boundary diagram. Output:
`threat-model-{project-slug}-{YYYY-MM-DD}.md` in the client's `created/docs/security/`.*


> **Agentic name warning (2026-11-08).** The ASI01-ASI10 names below came from the DDD research
> file, not from an OWASP page. An internal review found OWASP's own press release naming ASI01
> "Agent Behavior Hijacking" where we have "Agent Goal Hijack", and a second-source variant for
> ASI04. The ten names are therefore `PENDING_VERIFICATION`: cite the ID in client work and verify
> the name against the OWASP document before printing it.

## Licensing rule

> **Edition warning (verified 2026-11-08).** OWASP released a **2026** edition of the Top 10 for
> LLM Applications (announced 1 September 2026, https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/), together with a new Agent Control
> Standard. The LLM01-LLM10 mapping below is the **2025** edition and the 2026 ranking changed.
> The 2026 ID list could not be retrieved from a primary OWASP source on 2026-11-08, so the
> mapping below is `PENDING_VERIFICATION`: use it for internal structure, and re-verify every ID
> against the 2026 document before it appears in a client deliverable or a sign-off. Also add the
> Agent Control Standard when obtaining it.


OWASP Top 10 lists are **CC BY-SA 4.0** (https://creativecommons.org/licenses/by-sa/4.0/). We cite **IDs only** (LLM01:2026, ASI01) and write our own test
descriptions. Never paste OWASP descriptions, examples or mitigations into a DDD file or a client
deliverable; link to the source instead:
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/ (register INT-9)
- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/ (register INT-10)

MITRE ATLAS is Apache-2.0 (register INT-11).

## Step 1. Draw the architecture and mark trust boundaries

Mermaid flowchart with: users (internal, external), channels, model endpoint (provider and
region), retrieval stores, tools and their credentials, memory, logs, external content sources,
and every place untrusted text enters a prompt. Mark each boundary B1, B2 ... Untrusted content
(emails, web pages, uploaded files, retrieved documents, tool results) is the main injection path.

## Step 2. Walk the checklists per component

### OWASP LLM Top 10 2025 (IDs only; names as listed in the research file)

| ID | Short name | DDD question for this architecture |
|---|---|---|
| LLM01:2026 | Prompt Injection | Where does untrusted text enter a prompt, and what can the model do afterwards? |
| LLM02:2026 | Sensitive Information Disclosure | Can any user get data they are not entitled to through the model or its logs? |
| LLM04:2026 | Supply Chain | Which models, packages, plugins and datasets are third party, pinned and scanned? |
| LLM05:2026 | Data and Model Poisoning | Can anyone influence training, fine-tuning or retrieval content? |
| LLM10:2026 | Improper Output Handling | Is model output ever executed, rendered as HTML, or passed to another system unchecked? |
| LLM03:2026 | Excessive Agency | What can the system do without a human, with what permissions? |
| LLM08:2026 | System Prompt Leakage | Would leaking the system prompt expose secrets or logic that matters? |
| LLM09:2026 | Vector and Embedding Weaknesses | Is retrieval filtered by the querying user's permissions at query time? |
| LLM07:2026 | Misinformation | What happens when the answer is confidently wrong? |
| LLM06:2026 | Unbounded Consumption | What caps cost, rate and loop depth? |

### OWASP Agentic Top 10 2026 (only if the system plans, uses tools or acts)

| ID | Short name | DDD question |
|---|---|---|
| ASI01 | Agent Goal Hijack | Can retrieved or tool content redirect the agent's objective? |
| ASI02 | Tool Misuse and Exploitation | Is every tool allow-listed, parameter-validated and least-privilege? |
| ASI03 | Identity and Privilege Abuse | Does each agent have its own scoped, short-lived credential? |
| ASI04 | Agentic Supply Chain Vulnerabilities | Who publishes each tool or MCP server, and is it pinned? |
| ASI05 | Unexpected Code Execution | Is any generated code executed, and in what sandbox? |
| ASI06 | Memory and Context Poisoning | Can one session or user poison what another sees later? |
| ASI07 | Insecure Inter-Agent Communication | Are agent-to-agent messages authenticated and logged? |
| ASI08 | Cascading Failures | Does one agent's bad output propagate unchecked through others? |
| ASI09 | Human-Agent Trust Exploitation | Could the agent persuade a human approver to approve something harmful? |
| ASI10 | Rogue Agents | Can you detect and stop an agent acting outside its mandate (kill switch)? |

Unifying principle from OWASP's agentic list, and conventions section 2: **least agency**.

## Step 3. Map relevant MITRE ATLAS techniques

**Data provenance.** The harvested `mitre-atlas/atlas-data` snapshot (commit
f56c1468731d6428e5bf875263b4643b46d67437) contained only a symlink file pointing to
`v6/ATLAS-2026.10.yaml`; the `v6/` folder IS harvested: `~/ai-kb/vendor/mitre-atlas__atlas-data/dist/v6/ATLAS-2026.10.yaml` (sha256 ac41ee9f...142d, verified 2026-11-08). The names below were read on
2026-11-08 from that same file fetched at the **same pinned commit** from GitHub
(`dist/v6/ATLAS-2026.10.yaml`, collection version 2026.10, modified 2026-10-28; sha256
ac41ee9f99a47084ba5fdfc77ae83a28687e12390240fffeb37df7914ffe142d). No re-harvest needed.

**ATLAS version caution.** CoSAI pins its ATLAS mappings to v5.0.1. At 2026.10 some of those IDs
no longer exist (AML.T0019, which CoSAI maps to Data Poisoning, is absent). Cite techniques from
the table below, not from CoSAI's mapping column, and state "ATLAS 2026.10".

ATLAS 2026.10 tactics (16): AI Model Access (AML.TA0000), AI Attack Adaptation (TA0001),
Reconnaissance (TA0002), Resource Development (TA0003), Initial Access (TA0004), Execution
(TA0005), Persistence (TA0006), Defense Evasion (TA0007), Discovery (TA0008), Collection
(TA0009), Exfiltration (TA0010), Impact (TA0011), Privilege Escalation (TA0012), Credential
Access (TA0013), Command and Control (TA0014), Lateral Movement (TA0015).

Techniques most relevant to DDD architectures:

| Architecture element | ATLAS technique (2026.10) |
|---|---|
| Any LLM with user input | AML.T0051 LLM Prompt Injection (.000 Direct, .001 Indirect); AML.T0054 LLM Jailbreak |
| Public API or chat | AML.T0024 Exfiltration via AI Inference API; AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting; AML.T0049 Exploit Public-Facing Application |
| RAG | AML.T0070 RAG Poisoning; AML.T0071 False RAG Entry Injection; AML.T0066 Retrieval Content Crafting; AML.T0064 Gather RAG-Indexed Targets; AML.T0082 RAG Credential Harvesting |
| Agents and tools | AML.T0053 AI Agent Tool Invocation; AML.T0086 Exfiltration via AI Agent Tool Invocation; AML.T0101 Data Destruction via AI Agent Tool Invocation; AML.T0080 AI Agent Context Poisoning (.000 Memory); AML.T0081 Modify AI Agent Configuration; AML.T0083 Credentials from AI Agent Configuration; AML.T0098 AI Agent Tool Credential Harvesting; AML.T0110 AI Agent Tool Poisoning; AML.T0034.002 Agentic Resource Consumption |
| Credentials and identity | AML.T0012 Valid Accounts; AML.T0055 Unsecured Credentials |
| Supply chain | AML.T0010 Supply Chain Compromise (.001 Software, .002 Data Repository, .003 Model Repository, .004 Container Registry, .005 AI Agent Tool) |
| Training or fine-tuning | AML.T0020 Training Data Poisoning; AML.T0059 Erode Dataset Integrity; AML.T0018 Manipulate AI Model |
| Classifiers and vision | AML.T0015 Evade AI Model; AML.T0043 Craft Adversarial Data |
| Hallucination abuse | AML.T0062 Discover LLM Hallucinations; AML.T0060 Publish Hallucinated Entities |
| Social engineering | AML.T0052 Phishing (.001 Deepfake-Assisted Phishing); AML.T0088 Generate Deepfakes |
| Harm outcome | AML.T0048 External Harms |

Relevant ATLAS mitigations (2026.10): AML.M0020 Generative AI Guardrails; AML.M0024 AI Telemetry
Logging and Monitoring; AML.M0026 Manage AI Agent Service Access; AML.M0028 Enforce Access
Controls for AI Agent Tools; AML.M0029 Human In-the-Loop for AI Agent Actions; AML.M0030 Restrict
AI Agent Tool Invocation on Untrusted Data; AML.M0031 Memory Hardening; AML.M0033 Input and Output
Validation for AI Agent Components; AML.M0035 AI Red Team; AML.M0036 Limit AI Workload Resource
Consumption; AML.M0004 Limit AI Service Query Volume and Rate; AML.M0023 Maintain an AI Bill of
Materials; AML.M0025 Maintain AI Dataset Provenance; AML.M0018 User Training.

## Step 4. Australian controls overlay

- ACSC "Careful adoption of agentic AI services" (May 2026, AU-23) is the Australian reference for
  agent designs. Map agent service accounts to Essential Eight controls (application control,
  patching, restricting admin privileges, MFA, backups); this mapping is DDD interpretation.
- APRA-regulated clients: APRA's AI letter names prompt injection, data leakage and agent misuse
  (AU-15). The threat model is assurance evidence.

## Step 5. Output

| Threat ID | Component / boundary | OWASP ID(s) | ATLAS ID(s) | Scenario (our words) | Likelihood | Impact | Control | Test to prove it (handed to `ai-security-tester`) | Owner |
|---|---|---|---|---|---|---|---|---|---|

Every High threat gets a named test in the Phase 3 eval suite before go-live. Threats feed the
risk register (mode d) as risks with the same IDs cross-referenced.
