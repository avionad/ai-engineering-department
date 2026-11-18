# Rollout phases, tool tiers and platform controls

*v0.1.0, 2026-11-08. Sources: Internal web research B1 (Microsoft adoption phases and playbook
emphasis, Microsoft CAF AI phases, Gartner tiered governance, IBM shadow AI figures); GitHub's
AI adoption playbook (CC BY 4.0, adapted, see `vendored-provenance.md`). Vendor feature names
are deliberately generic: verify each vendor's current capability before naming it to a client.*

## 1. Program structure

| Role | Who | Does |
|---|---|---|
| Accountable executive | C-level sponsor | Owns the outcome, budget and risk appetite; explains the "why" to staff; chairs or sponsors the AI council |
| Program owner (DRI) | Named full- or part-time lead | Runs the roadmap, change plan, tool intake, metrics and success stories. GitHub's playbook: "an enabler, not a gatekeeper" whose job is to scale others |
| AI council | Risk, legal/privacy, security, HR, business owners, IT | Approves tool tiers, high-risk use cases, policy changes; reviews incidents (charter from `ai-governance-program`) |
| Champions (advocates) | Volunteers in each team | Local help, use-case discovery, feedback, co-lead training |
| Function leads | Department heads | Own workflow redesign and benefits in their area |
| IT and security | Client IT | Identity, DLP, labels, logging, tool configuration |
| The practice | Consultancy | Method, design, build of automations, measurement, training content, reporting; recommends, never decides |

## 2. Sanctioned tool tiers by data class

Start from the client's data classification (public, internal, confidential, personal,
sensitive or regulated). If none exists, a simple four-class scheme is drafted with IT and the
privacy officer in Get ready.

GitHub's playbook model (two tiers): **Tier 1** fully vetted and approved tools, safe for
confidential company and customer data; **Tier 2** unvetted public and consumer tools, public
non-sensitive data only. "If a tool isn't on the fully vetted list, treat it as public and use
only public data."

The practice extension for L/XL (needed where sensitive or regulated data exists):

| Tool tier | Example of what sits here | Data classes allowed | Conditions |
|---|---|---|---|
| A: Sensitive-approved | Onshore private platform (for example a model on an Australian-region cloud deployment or self-hosted), specific approved applications | Up to sensitive or regulated | Residency confirmed, impact assessment where tier 3, access by role |
| B: Enterprise-approved | Enterprise assistant tenancy, approved SaaS with no-training terms | Up to confidential and personal (as the data-handling agreement permits) | SSO, logging, DLP where available, AUP training done |
| C: Public tools | Anything not on the approved list | Public only | No personal or confidential data (OAIC guidance, register AU-11) |

The AUP lists every tool by tier with the data allowed, in one easy-to-find place (GitHub
playbook). The council owns changes. A tool request process lets staff ask for a new tool; the
program owner runs it with IT, security and legal.

## 3. Identity and platform controls

| Control | Purpose | Notes |
|---|---|---|
| SSO | One identity, MFA enforced, conditional access | Every sanctioned AI tool; no local accounts |
| RBAC | Features and data by role | Map roles to tool tiers; admins separate |
| SCIM (or the vendor's provisioning equivalent) | Joiners get access, leavers lose it automatically | Confirm the vendor supports it; otherwise a documented manual process with a monthly reconciliation |
| Enterprise tenancy, no-training terms | Client data not used to train vendor models | Confirm in the contract, not the marketing page (vendor due diligence, `ai-compliance-risk` mode g) |
| Permission hygiene | Assistant inherits existing document permissions | Find "everyone" and over-shared sites before enabling access; fix or exclude |
| Sensitivity labels | Mark confidential and sensitive content | Labels applied before the assistant can reach the store, where the suite supports it |
| DLP | Stop sensitive data leaving approved tools | Policies for public-tool uploads and copy-paste where the suite or a CASB/SSE supports it |
| Logging | Prompts, outputs and admin actions retained for audit within privacy limits | Retention and access agreed with the privacy officer |
| Residency | Where prompts, outputs and indexes are stored and processed | Per the solution-patterns deployment table; re-verify per vendor |

Research B1 step 4 is the source for this set: "SSO and RBAC on every AI tool; enterprise tenancy
with no-training terms; DLP and sensitivity labels; permission-aware retrieval; logging of prompts
and outputs for audit within privacy limits."

## 4. Shadow AI replacement

The sales argument is real (IBM 2026 Cost of a Data Breach: incidents involving unapproved AI
rose from 20% to 43% of organisations; about two thirds of breached organisations had no AI governance
policies; quote with source and year). The method:

1. **Discover** with `ai-governance-program/references/shadow-ai-discovery.md` (survey, SaaS and
   expense review, browser extensions and in-app AI features, network or CASB where available,
   with written approval and a surveillance-law check before any monitoring).
2. **Group by use**: what were people trying to do (summarise, draft, translate, analyse a
   spreadsheet, code)?
3. **Provide the sanctioned alternative** for each common use, with training, before any block.
4. **Announce a transition date**; personal data found in public tools triggers the immediate
   actions in the governance method (including a notifiable data breach assessment with the
   privacy officer).
5. **Then block** the highest-risk public tools where the network allows, and keep measuring.

## 5. Phase activities (checklist)

**Get ready (weeks 0 to 6 for most L clients; research B1 step 1 says weeks 0 to 6 for "govern first, lightly")**
- Sponsor, program owner, council named; RACI agreed.
- AUP with tool tiers published; one or two sanctioned tools live (so shadow AI has a legal
  alternative).
- Identity and platform controls configured; permission hygiene check done.
- Shadow AI discovery run; baseline recorded.
- ADM inventory started; AI register seeded.
- Consultation plan agreed with HR; union notification where required (people-and-change s4).
- Measurement baseline designed (`measurement.md`).

**Onboard and engage**
- Pilot groups chosen by use case, not seniority; seats assigned intentionally.
- Champions recruited; their channel and leadership contact set up.
- Role-based training delivered before access; support channel open.
- Adoption baseline captured.

**Deliver impact**
- Per pilot function: two or three use cases redesigned end to end; baselines measured before.
- First planned-vs-actual results; stories shared through champions.
- Risk incidents and near misses reviewed by the council.

**Extend and optimise**
- Scale to further functions in waves on evidence.
- Agents admitted through the tiered screen; control specs for anything that acts.
- Retire unused seats and tools; refresh training as tools change.
- Quarterly management review and board report.

Microsoft CAF's AI adoption guidance uses Plan, Govern, Secure, Manage (research B1 step 5) and
suits Azure-centric clients as a cross-reference. AWS and Google equivalents are
PENDING_VERIFICATION.
