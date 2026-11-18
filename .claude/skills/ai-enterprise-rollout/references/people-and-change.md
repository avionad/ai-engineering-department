# People and change: champions, training, communications, consultation

*v0.1.0, 2026-11-08. Champions, communities of practice, executive messaging and learning paths
adapted from GitHub's AI adoption playbook (CC BY 4.0, see `vendored-provenance.md`). Regulatory
points from `../../_shared/regulatory-register.md`. Nothing here is employment or WHS legal advice.*

## 1. Champions network

GitHub's playbook model, adapted:

- **Recruit by asking for volunteers.** A company-wide call surfaces intrinsically motivated
  people; formal nomination is usually unnecessary. Aim for coverage: at least one champion in
  every pilot team and every site.
- **What champions do**: local go-to help; find and showcase real use cases from their own team;
  act as the feedback channel to the program; help shape and co-lead training.
- **What the program gives them**: their own channel and regular champion-led check-ins; a direct
  line to the program owner or sponsor; "train the trainer" coaching; early access to new tools
  and training material; recognition (agree with HR how champion time is recognised).
- **Communities of practice**: a general "how do I" community, function-specific communities as
  needed (finance, operations, sales), each with a charter and a leader (often a champion).

## 2. Role-based training

Training paths come from `ai-governance-program/templates/literacy-training-plan.md` (roles: all
staff, managers, power users, builders, privacy/risk/legal, executive, board). This skill adds
sequencing for the rollout:

| Audience | Before access | First 30 days | Ongoing |
|---|---|---|---|
| All staff | AUP and tool tiers, what data goes where, how to report a problem | Hands-on with two or three tasks from their own job | Short refreshers when tools change |
| Managers | As above plus how to redesign team workflows and lead the conversation about role change | Identify team use cases with champions | Coaching through champions |
| Power users and champions | As above plus advanced use and prompt patterns for their function | Co-lead team sessions | Community of practice |
| Builders (anyone making automations or agents) | OWASP LLM and Agentic risks by ID, the agent control spec, the tiered screen | Supervised first build | Review of each new build |
| Privacy, risk, legal | ADM duty (register AU-8), screening, incident playbook | Council participation | Quarterly |
| Executive and board | Oversight duties, risk appetite, what to ask, how benefits and incidents are reported | Board briefing | Annual refresher; APRA's AI letter flags board AI literacy for regulated entities (AU-15) |

GitHub's playbook advice to curate excellent external content rather than build training that
dates quickly applies here; DDD builds only the client-specific parts (their tools, their data
rules, their workflows).

## 3. Communications plan

| When | Message | From | Channel |
|---|---|---|---|
| Launch | Why we are doing this, what tools are approved, what data goes where, what support exists, what happens next | Accountable executive | All-staff message and meeting |
| Before each wave | Who is in, when, training dates, where to get help | Program owner | Email, intranet |
| Monthly | What is working (real examples from champions), what changed, what we are fixing | Program owner, champions | Community channel, newsletter |
| On incidents | What happened, what we changed (as appropriate) | Program owner with council | As per incident playbook |
| Quarterly | Results against the scorecard, decisions taken | Accountable executive | All-staff, board |

**Be honest about role change.** GitHub's playbook: don't say "your job is safe"; say "this is how
our jobs will change, and this is how we will support you". If the client intends any headcount
change, that is a consultation matter (section 4) before it is a communications matter.

## 4. Consultation, WHS and workplace considerations (identify, do not advise)

Carry the disclaimer: "This assessment identifies regulatory considerations for review by your
legal adviser. It is not legal advice."

| Consideration | Status (register) | What to raise with the client's HR and legal advisers |
|---|---|---|
| NSW WHS Amendment (Digital Work Systems) Act 2026 | AU-21: commenced later. Passed, assent 18 Feb 2026; duties await proclamation after SafeWork NSW guidelines. Check the register row for the latest status before stating it | Defines digital work systems (algorithm, AI, automation, online platform); new PCBU duty that workers' health and safety is not put at risk by them (workload, metrics, monitoring, discrimination); union entry right to inspect systems. Relevant to NSW workers even before commencement as direction of travel |
| WHS consultation duties generally | No register row: PENDING_VERIFICATION | Whether introducing AI into work processes triggers consultation with workers and health and safety representatives |
| Enterprise agreements and modern awards (consultation terms) | No register row: PENDING_VERIFICATION | Whether major workplace change terms apply to the rollout or to any role change |
| Fair Work Act general protections; state workplace surveillance Acts | Named overlays without a row (register "sector overlays" table) | Monitoring of staff AI use, logging of prompts, any productivity measurement at individual level |
| Privacy Act and APPs | AU-6, in force | Staff personal information in prompts and logs; employee records exemption applicability is for the legal adviser |
| ADM disclosure | AU-8, from 10 Dec 2026 | Any AI that influences decisions about staff or candidates |
| Anti-discrimination; AHRC recruitment checklist | AU-24, voluntary on binding law | HR use cases (screening, performance) |

Design choices that reduce exposure and are good practice anyway: measure adoption and benefits
at team or use-case level, not individual surveillance; tell staff what is logged and why;
involve staff and representatives in workflow redesign; keep humans deciding on matters about
people.

## 5. Resistance and stalls (what to look for)

- Licences assigned, low use: no defined use case or no training. Fix the use case first.
- High use, no measured benefit: workflow not redesigned; AI bolted onto the old process.
- One team racing ahead, others not: champion coverage gap.
- Quiet return to public tools: sanctioned tool not good enough for a common task; find out which.
