# AI Engineering Department

A complete, self-contained AI consulting and engineering department for Claude Code: 15 skills,
5 specialist agents and a shared knowledge base covering the full lifecycle of an AI engagement,
from the first discovery call to a running, monitored, compliant system.

Built and used in production by Aditya Anand for AI automation consulting with Australian small
businesses through to 500+ staff enterprises. Shared as a working toolkit: open it in Claude Code and it works as-is.

## Quick start

1. Clone the repo and open the folder in Claude Code (`claude` in the repo directory).
2. Ask for the department: *"Act as the AI manager and run discovery for this client..."* or invoke
   any skill directly. Skills live in `.claude/skills/`, agents in `.claude/agents/`, and Claude
   Code picks both up automatically for this project.
3. Start with `.claude/skills/ai-manager/SKILL.md` -- the router that runs every engagement through
   lifecycle gates and calls the rest.

To make the department available in every project, copy `.claude/skills/*` into `~/.claude/skills/`
and `.claude/agents/*` into `~/.claude/agents/`.

## What is inside

Every skill folder, the shared knowledge base and the agents folder carry their own `README.md` describing what each file does.

### The engagement lifecycle (skills, in the order an engagement uses them)

| Stage | Skill | What it does |
|---|---|---|
| Route | `ai-manager` | Front door: pins client facts, places the engagement at a lifecycle stage, enforces exit gates, routes to everything below |
| Discover | `ai-discovery-scoping` | The right discovery questions, solution patterns, pre-call prep, scope-of-work templates |
| Assess | `ai-readiness-assessment` | Readiness scoring across data, systems, people and governance |
| Comply | `ai-compliance-risk` | Risk tiering, Australian regulatory obligations (incl. APP 1.7-1.9 automated decision-making disclosure), impact assessment, sign-off checklist |
| Govern | `ai-governance-program` | Ongoing governance: policies, registers, review cadence |
| Design | `ai-solution-architecture` | End-to-end architecture: flowcharts, data flows, trust boundaries, NFR checklist, integration design |
| Choose platform | `ai-deployment-platforms` | AWS Bedrock, Azure, Google Vertex, VPS, on-prem GPU; data-residency verification discipline; security baseline |
| Retrieve | `ai-rag-engineering` | RAG design incl. permission-aware retrieval |
| Customise | `ai-model-customisation` | Prompting vs RAG vs fine-tuning; open-weight model selection |
| Automate | `ai-agents-automation` | Agent and workflow design under least agency, control specs, runbooks |
| Roll out | `ai-enterprise-rollout` | Enterprise rollout: data classification, DLP, access, change management |
| Portfolio | `ai-use-case-portfolio` | Use-case libraries by industry, prioritisation |
| Test | `ai-evals-security-testing` | Golden-set evals, red-teaming mapped to OWASP LLM Top 10 (2026) and MITRE ATLAS, promptfoo templates |
| Improve | `ai-optimisation-llmops` | The monthly improvement loop: traces, drift, cost, change sets |

### Shared knowledge base (`.claude/skills/_shared/`)

Engagement conventions, a 40+ row Australian regulatory register, 12 industry packs, a client FAQ,
vendored-source provenance, and `check_freshness.py` -- a rot check that flags any reference file
whose facts are older than 60 days so stale claims never reach a client.

### Specialist agents (`.claude/agents/`)

| Agent | Role | Guardrail |
|---|---|---|
| `ai-architect` | Designs solutions, draws architectures, answers client technical questions | Output is a design, never a build |
| `ai-engineer` | Builds approved solutions in sandbox/staging | Never touches client production |
| `ai-compliance-officer` | Risk and compliance review of a design or project | Read-only on client systems; never legal advice |
| `ai-security-tester` | Evals and red-team testing before go-live | Only systems you built or are authorised in writing to test |
| `ai-optimiser` | Monthly optimisation loop on live systems | Proposes changes, never deploys them |

## Working principles baked in

- **Verify before asserting.** Platform capabilities, data-residency claims and regulatory facts
  carry a verification date and a live-check instruction; anything unverified is marked
  `PENDING_VERIFICATION` rather than guessed. Residency claims are checked against the provider's
  own API or documentation on the day, never a marketing page.
- **Gates, not vibes.** Engagements move through lifecycle stages with exit gates; nothing is
  quoted without discovery, nothing is built without a risk tier, nothing goes live without the
  security test report.
- **Least agency.** Agents and automations get the minimum tools, credentials and autonomy the job
  needs, with human approval where client-visible.
- **Australia-first compliance.** The register and packs centre Australian obligations (Privacy
  Act / APPs incl. the Dec 2026 ADM disclosure, industry rules), with international frameworks
  (ISO 42001, NIST AI RMF, EU AI Act) mapped alongside.

## Honest limitations

- References were verified around 8 November 2026; run
  `python3 .claude/skills/_shared/check_freshness.py` and re-verify anything it flags.
- Some register rows are deliberately `PENDING_VERIFICATION` (state-level rules beyond NSW, a few
  vendor certifications); the discipline is to verify at point of use, not to pretend completeness.
- Internal pricing/quoting machinery and original research documents were removed from this copy;
  pointers to them say so where they occur.

## Licence and provenance

(c) Aditya Anand. Shared publicly for evaluation and use in your own practice; not for resale or republication as a product.
Vendored third-party material is listed per skill in `references/vendored-provenance.md` files with
upstream repos and licences; all of it was adapted and rewritten rather than copied at length.
