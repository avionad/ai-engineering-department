<!-- Audience: client. Save as {client}/created/docs/strategy/ai-rollout-raci-{YYYY-MM-DD}.md.
R = responsible (does it), A = accountable (one per row, signs off), C = consulted, I = informed.
Exactly one A per row. DDD is never A for a client decision. Adjust columns to the client's
actual roles. -->

# AI rollout RACI: {Client}

| Activity | Accountable exec | Program owner | AI council | Function leads | IT / security | Privacy / legal | HR | Champions | DDD |
|---|---|---|---|---|---|---|---|---|---|
| Set AI strategy and risk appetite | A | R | C | C | C | C | C | I | C |
| Approve tool tiers and AUP | I | R | A | C | C | C | C | I | C |
| Configure SSO, RBAC, provisioning, logging | I | C | I | I | A/R | C | I | I | C |
| Permission hygiene and labels | I | C | I | C | A/R | C | I | I | C |
| DLP policies | I | C | C | I | A/R | C | I | I | C |
| Shadow AI discovery | I | A | C | C | R | C | C | C | R |
| AI register upkeep | I | A | C | R | C | C | I | I | C |
| Use-case intake and ranking | I | A | C | R | C | C | I | R | R |
| Risk tier screen per use case | I | C | A | C | C | R | I | I | R |
| Impact assessment (tier 3) | I | C | A | R | C | R | C | I | R |
| Workflow redesign in a function | I | C | I | A | C | C | C | R | R |
| Build automations and agents (sandbox) | I | C | I | C | C | I | I | I | R (client A: function lead) |
| Go-live approval per system | I | C | C | A | C | C | I | I | C |
| Consultation with staff and unions | C | C | I | C | I | C | A/R | I | I |
| Training delivery | I | A | I | C | C | C | C | R | R |
| Communications | A | R | C | C | I | C | C | R | C |
| Adoption and value measurement | I | A | I | R | C | I | I | C | R |
| Incident response | I | R | A | C | R | R | C | I | C |
| Board reporting | A | R | C | C | C | C | I | I | C |

Notes:
- "A/R" means the same role is accountable and does the work.
- Build row: DDD is responsible for the build; the client's function lead is accountable for
  accepting it. Go-live is always approved by the client (conventions stage 7).

---

*Adapted, with changes, from "How to build an AI-powered workforce: GitHub's playbook", GitHub,
licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Changes: re-sequenced for DDD's
engagement stages, Australian regulatory obligations added, DDD measurement and RACI added.*
