# ai-deployment-platforms

Compares AWS Bedrock (au.* cross-region inference between Sydney and Melbourne, Guardrails, Knowledge Bases, AgentCore, IRAP), Azure (Australia East, Standard vs Data Zone vs Global deployments, AI Search, the AVM AI/ML landing zone Terraform module), Google Cloud Vertex AI (Australian regions with real limits: see the skill's platform reference), Anthropic and OpenAI direct (residency limits), self-managed Australian VPS, on-prem GPU (vLLM, Ollama) and hybrid routing by data class. Provides a data-class-to-platform matrix, sovereignty notes (onshore does not remove CLOUD Act exposure), a security baseline per platform, an exit plan per APRA expectations, a decision record template, and a verify-live rule for every model, region and price.

**When to use:** Use when an AI solution needs a hosting platform chosen, compared or set up, or a client asks where their data will be processed.

**Trigger phrases:** which AI platform, where will our data be processed, data residency AI, Australian data residency, AWS Bedrock Sydney, Bedrock au profile, Azure OpenAI Australia East, Data Zone deployment, Vertex AI Australia, self-host AI, on-prem LLM, private AI server, VPS for AI, hybrid AI routing, IRAP AI, CLO...

## How SKILL.md is organised

- The verify-live rule (read before naming anything)
- Department relationships
- Protocol
- The options at a glance (research B4, checked 2026-11-08, re-verify)
- Decision flow
- Comparison method
- Hybrid routing (L and XL)
- Size bands
- Cost drivers (never prices in this skill)
- Outputs
- Do not
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/data-class-matrix.md` | **Data class to platform matrix.** v0.1.0, 2026-11-08. House default positions, built from research B2 and B4, the client FAQ and the. |
| `references/platforms.md` | **Platform detail.** v0.2.0, 2026-11-08. Sources: research B2, B4, B6 (`ai-dept-web-research-2026-11-08.md`), GitHub. |
| `references/security-baseline.md` | **Security baseline per platform.** v0.1.0, 2026-11-08. Sources: research B4, B5 and the ACSC agentic AI guidance it cites (register. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-deployment-platforms.** v0.1.0, 2026-11-08. Harvested files this skill read or adapted, with repo, licence and pinned commit. |
| `references/verify-live.md` | **Verify live before naming.** v0.2.0, 2026-11-08. The rule: every model, region, deployment type, price, quota, certification. |

## Templates

| File | What it holds |
|---|---|
| `templates/platform-decision-record.md` | **Platform decision record: {project}.** Template v0.1.0 (ai-deployment-platforms), 2026-11-08. ADR format (context, options, decision,. |

*Skill version 0.1.0. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
