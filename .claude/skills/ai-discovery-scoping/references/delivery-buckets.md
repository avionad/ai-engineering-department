# Delivery buckets and cost shapes

*v0.1.0, 2026-11-08. Pattern borrowed from `odoo-discovery-scoping` (every item in exactly one
bucket because each bucket costs differently). Slugs must match `ai-proposal-pricing`'s
`estimate.py` exactly; it rejects anything else.*

| Slug | Bucket | Typical items | Cost shape | What makes it bigger |
|---|---|---|---|---|
| `config-saas` | Configuration and SaaS setup | Set up an off-the-shelf AI tool, voice platform, enterprise copilot tenancy, prompts and settings, SSO hookup on a SaaS product | Mostly fixed, hours to a few days per tool; low variance | Number of tenants or teams, policy settings, client IT turnaround |
| `integration-workflow` | Integration and workflow | n8n or similar workflows, API connections to CRM/ERP/email, document extraction into a system of record, notifications | Per connector and per document type; medium variance driven by the client's systems | No API, old system versions, many document formats, write access approvals, error handling and retries |
| `rag-knowledge` | Retrieval and knowledge | Ingestion of company documents, chunking, embeddings, retrieval tuning, permission-aware filtering, source citations | Scales with number of sources and permission complexity; high variance at M+ | Permission models (SharePoint, Drive, Confluence), ACL sync and revocation latency, scanned PDFs, document volume, residency of the vector store |
| `custom-agent-app` | Custom agent or application | Agent with tools, custom UI, voice agent logic, back-office agent with approvals, orchestration code | Effort-driven, the widest variance; quote after design | Number of tools and write actions, approval flows, multi-step state, UI requirements, concurrency |
| `model-customisation` | Model customisation | Fine-tuning (LoRA/QLoRA), distillation, open-weight model selection and hosting setup, training data preparation | Front-loaded data preparation plus compute; high variance; needs a baseline eval first | Labelled data availability, licence review, GPU hosting, retraining cadence |
| `governance-compliance` | Governance and compliance | Risk tier screen, impact assessment, ADM (APP 1.7) mapping, privacy check, eval baseline, red-team, policy and register entries, model card | Scales with risk tier: light at tier 1, substantial at tier 3 | Regulated sector, decisions about people, number of jurisdictions, client legal review cycles |
| `change-training` | Change and training | User training, admin handover, runbooks, champions sessions, communications, documentation | Scales with users and sites | Number of user groups, union or consultation steps, multiple locations, low digital confidence |
| `discovery-measurement` | Paid discovery and measurement | Paid discovery or readiness work quoted before a build, pilot baseline measurement, before/after benefit measurement, success-criteria tracking | Fixed and short; low variance | Number of stakeholders and sites, data access delays, how many measures the client wants tracked |
| `run-ongoing` | Ongoing run | Monitoring, monthly eval loop, prompt and retrieval tuning, model version migrations, support hours, cost reviews | Recurring monthly; fenced (never "unlimited") | Volume growth, model retirements, number of automations in scope |

## Placement rules

- One line, one bucket. If a line seems to span two, split it into two lines.
- Eval baselines and red-team go in `governance-compliance`, not inside the build line, so they
  cannot be quietly dropped.
- Data clean-up goes in `integration-workflow` (if it is pipeline work) or its own line in the
  bucket it serves; never hidden inside a build estimate.
- Platform and token costs are not hours. They go in the run-cost sheet for
  `ai-proposal-pricing` with a vendor source URL and date checked, not in this CSV.
- Project management overhead is applied by the estimator; do not add a PM line unless the
  client asked for dedicated PM.
