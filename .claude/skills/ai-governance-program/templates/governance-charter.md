<!-- Audience: client executive. Save as created/docs/security/ai-governance-charter-{client}-{YYYY-MM-DD}.md -->

# AI governance charter template (scaled by size band)

*v0.1.0, 2026-11-08. Practice 1 "Decide who is accountable" (AU-4); ISO/IEC 42001 Clause 5
(5.1, 5.3 per harvested source) and Clause 9 (9.3 management review); NIST Govern. Research B1
step 1: name an accountable executive and an AI council (risk, legal/privacy, security, HR,
business owners) in the first weeks. Gartner (26 May 2026, research B1): uniform governance
across all agents leads to failure, so govern by risk tier.*

## Pick the structure by size band

| Band | Structure | Members | Meets | Decides |
|---|---|---|---|---|
| S | **Owner + one reviewer** | Owner (accountable); one trusted reviewer (staff member, adviser, or DDD under engagement) | When a new tool or use case comes up; review quarterly | Owner approves all; reviewer checks Tier 2+ |
| M | **AI working group** | Accountable executive; operations; privacy/compliance lead; IT; one business owner per active use case | Monthly | Tier 1 by system owner; Tier 2 by working group; Tier 3 by accountable executive |
| L | **AI council** | Accountable executive (chair); risk; legal/privacy; security; HR; data; business owners | Monthly, plus out-of-cycle for Tier 3 | Tier 1 self-serve with register entry; Tier 2 by council delegate; Tier 3 by council; Tier 4 never |
| XL | **Cross-functional AI council reporting to the board risk committee**, plus system owners and a champions network | As L, plus internal audit (observer), change management, union or staff representative where relevant | Monthly; quarterly management review; board report quarterly | As L; board sets AI risk appetite (APRA AI letter expects an AI risk appetite for APRA-regulated entities, AU-15) |

---

**{Client} AI governance charter** | Version {n} | Approved {date} by {role}

### 1. Purpose
Ensure AI at {Client} is used safely, lawfully and for real business value, with clear
accountability and decisions proportionate to risk.

### 2. Authority
Established by {CEO / board}. The {council / working group / reviewer} may approve, condition or
stop AI use within this charter. Tier 4 uses are not approved under any circumstances.

### 3. Accountable executive
{Name, role}. Accountable for AI risk across the organisation; owns the AI policy; reports to
{CEO / board} {frequency}.

### 4. Membership and quorum
{Members by role}. Quorum: {n}, including the chair or delegate and the privacy lead for any
item involving personal information.

### 5. Responsibilities
- Maintain the AI register and confirm every system has an owner and a tier.
- Approve use cases at the tier thresholds above.
- Review impact assessments for Tier 3 systems.
- Track ADM disclosure readiness (APP 1.7, from 10 Dec 2026).
- Approve AI vendors after due diligence.
- Oversee incidents, lessons and corrective actions.
- Set and review the training plan, including board literacy (XL, and APRA-regulated at any size).
- Review the AI policy {annually / six-monthly}.

### 6. Decision rights (RACI)

| Activity | Accountable exec | Council / reviewer | System owner | Privacy lead | IT/security | All staff |
|---|---|---|---|---|---|---|
| AI policy | A | R | C | C | C | I |
| Register entry | I | A | R | C | C | - |
| Risk screen | I | A | R | C | C | - |
| Tier 3 approval | A | R | R | C | C | - |
| Vendor approval | I | A | R | C | R | - |
| Incident response | A | R | R | R | R | report |
| Go-live approval | A (Tier 3) | A (Tier 2) | R | C | C | - |

### 7. Lifecycle gates
Intake, screen, design, build in sandbox, verify (eval baseline, security tests, compliance
sign-off), go-live approval, operate and monitor, **decommission** (data deletion, register
updated). {Mirror the engagement lifecycle in `engagement-conventions.md` s2.}

### 8. Standing agenda
Register changes; new requests by tier; incidents and near misses; monitoring exceptions;
regulatory changes (from DDD's regulatory register); training status; actions.

### 9. Management review (quarterly)
Inputs: register, risk register changes, incidents, monitoring results, audit findings, objective
progress, regulatory changes. Outputs: decisions, resource changes, policy changes.

### 10. Review of this charter
{Annually}.
