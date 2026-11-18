<!-- Audience: client (all staff for the AUP; executive for the policy). Save as
created/docs/security/ai-policy-{client}-{YYYY-MM-DD}.md and ai-acceptable-use-policy-{client}-{YYYY-MM-DD}.md -->

# AI policy and acceptable use policy template

*v0.1.0, 2026-11-08. Practices 1 and 6 (AU-4); ISO/IEC 42001 Clause 5 and 7; NIST Govern.
Start from the NAIC AI policy guide and template (free, AU-4) when the client wants the government
format; this template is what DDD adds on top: size-band tailoring, Australian legal hooks (APP 1.7,
OAIC guidance), the client's own tool list and data classes, and links to the register and incident
playbook. Do not charge for re-typing the free template; charge for the tailoring.*

## How to tailor by size band

| Section | S (1-19) | M (20-199) | L (200-499) | XL (500+) |
|---|---|---|---|---|
| Format | One combined 2-page policy + AUP | Policy (4 pages) + AUP (2 pages) | Policy + AUP + standards for build teams | Policy + AUP + standards + procedures; board-approved |
| Approver | Owner | CEO or GM | Executive committee | Board or board risk committee |
| Accountable role | Owner | Named executive | Accountable executive + AI council | Accountable executive + AI council + system owners |
| Data classes | Two: "public" and "everything else" | Three: public, internal, confidential/personal | Four: + sensitive/regulated | Client's existing classification scheme |
| Approved tools | Named list in the AUP | Named list + request form | Register-driven list + intake form | Register-driven, tiered by data class |
| Review | Annually | Annually | Six-monthly | Six-monthly + on regulatory change |

---

# Part A: AI policy

**{Client} AI policy** | Version {n} | Approved by {role} on {date} | Next review {date}

### 1. Purpose
Why {Client} uses AI, and the commitment to use it lawfully, safely, transparently and with
people in control.

### 2. Scope
All staff, contractors and volunteers; all AI systems, including AI features inside software
we buy, tools staff use on their own accounts for work, and systems we build. "AI system" means
{plain definition; note that rule-based automated decision tools are in scope for privacy
disclosure even if not "AI"}.

### 3. Principles
Accountability (every AI system has a named owner); human control (people make decisions that
significantly affect others); privacy and security; fairness; transparency; continual improvement.
{Keep to the client's words; tie each to one of the six practices.}

### 4. Roles
Accountable executive; AI council or reviewer (see governance charter); system owners; privacy
officer; all staff. {RACI in the charter.}

### 5. Risk-based approach
Every AI use is screened into a risk tier before it is built or bought (Tier 1 low to Tier 4
stop). Higher tiers need more controls before go-live, including impact assessment and human
review design for Tier 3. {Reference the client's register and screening process.}

### 6. Legal and regulatory commitments
- Privacy Act 1988 and the APPs. From 10 December 2026 our privacy policy will describe
  automated decisions that significantly affect people (APP 1.7 to 1.9). Human review does not
  remove that duty where a system's output materially influences the decision.
- No personal, sensitive or confidential information in public consumer AI tools (OAIC guidance).
- {Sector rules from the industry pack, each with its status: in force / commenced later /
  supervisory expectation / voluntary.}

### 7. Measurable objectives
{e.g. 100% of AI systems in the register; every Tier 3 system has an impact assessment before
go-live; all staff complete AI basics training within {n} days of starting; AI incidents reviewed
within {n} days.}

### 8. Incidents
How to report an AI incident; link to the incident playbook.

### 9. Review and exceptions
Who can grant an exception, how it is recorded, when the policy is reviewed.

---

# Part B: Acceptable use policy (one to two pages, plain language)

**Using AI at {Client}: the rules**

**You can** use these approved tools for work: {tool, account type, what data class allowed}.
To request a new tool, {form or person}.

**Never put these into any AI tool that is not approved for them:** customer, patient or student
details; staff details; passwords, keys or access tokens; {client-specific: contracts, pricing,
designs, legal advice, health information}. If you are not sure, ask {person}.

**Always**
- Check AI output before you use it. You are responsible for anything you send, publish or
  decide, whoever drafted it.
- Tell people when they are dealing with an AI system where it matters to them (e.g. a chatbot,
  an AI-drafted letter that a person has not reviewed).
- Keep a person in the loop for any decision about a customer, candidate, patient or staff member.
- Report mistakes, leaks or odd behaviour to {person} straight away. Reporting early is expected
  and will not be held against you.

**Do not**
- Use personal AI accounts for work data.
- Connect AI tools or browser extensions to work email, files or systems without approval.
- Use AI to monitor or assess colleagues without approval from {role}.
- Create images, audio or video of real people without their consent.
- {Client-specific bans, e.g. AI in affidavits for legal clients (AU-20); recording consultations
  without consent for health clients (AU-19).}

**Questions:** {contact}. I have read and understood this policy: {name, date}.

*Template note for the client: have your legal adviser review the legal commitments section. This
template identifies regulatory considerations; it is not legal advice.*
