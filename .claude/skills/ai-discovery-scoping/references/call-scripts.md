# Call scripts, workshop agenda and stakeholder interview guides

*v0.1.0, 2026-11-08. Timings are guides. Australian English, plain language, no jargon the client
has not used first.*

## 1. First call (30 minutes)

Goal: qualify. Leave knowing whether there is a real problem, an owner, a decision-maker, a rough
size, and whether the next step is a discovery workshop, a readiness assessment or a polite no.

| Min | Section | What to do |
|---|---|---|
| 0-3 | Open | Thank them, confirm time, say the aim: "understand what you are trying to fix and whether we are the right people to help. No pitch today." Ask permission to take notes or record (record only with consent). |
| 3-10 | Their problem | Must-asks 1 and 2. Let them talk. Note their exact words. |
| 10-18 | One real example | Must-asks 7 and 8 on the most painful process. Ask for numbers: how often, how long, who. Ask for a screen-share if possible. |
| 18-23 | Data and systems | Must-asks 15 and 22. "Could you send five to ten real examples after the call?" |
| 23-27 | Owner, decision, timing, budget | Must-asks 27, 47, 48, 49. Ask for a budget range; do not offer one. |
| 27-30 | Close | Say what you heard in two sentences. Propose the next step: workshop (clear problem), readiness assessment (no clear starting point), or no fit. Confirm who will send what by when. |

Red flags to note: nobody owns it; "the board wants AI" with no problem; insistence on full
autonomy for decisions about people; data they cannot share even as samples; a deadline that
cannot fit a pilot.

Do not on a first call: quote, name a price range, promise a capability, or name a model.

## 2. Discovery workshop (90 minutes)

Goal: map the process, collect the numbers, rank the candidates, and agree the pilot shortlist.
Attendees: owner plus the people who do the work. For L/XL add IT and risk (or run them as
separate interviews first).

| Min | Section | What to do |
|---|---|---|
| 0-5 | Frame | Goal, agenda, ground rules: "we want the messy reality, not the policy manual." |
| 5-15 | Goals and success | Restate the success measure from the first call; get agreement on how it will be measured. |
| 15-50 | Process walk-throughs | Two or three candidate processes, about 12 minutes each. For each: steps, systems, volume, time per item, error rate and cost, exceptions, who. Draw it live (whiteboard or Mermaid). |
| 50-65 | Data and access | Where the inputs live, quality, personal information, who may see what, residency rules, sample availability. |
| 65-75 | Risk and boundaries | Must-ask 33, plus 36, 39 and 40: what the AI must never do alone, who could be harmed. |
| 75-85 | Rank | Quick value/feasibility/risk read on each candidate with the group (scoring template). Agree a pilot shortlist of one or two. |
| 85-90 | Close | Follow-up list (owner, due date), samples to send, next step (design brief and scope within an agreed number of business days). |

After the workshop: discovery notes within 24 hours, follow-up list sent, scoring sheet updated.

## 3. Stakeholder interview guides (M, L, XL)

30-45 minutes each, one function at a time. Same opening every time: purpose, confidentiality of
individual comments, permission to take notes. Close every interview with: "What would make this
fail?" and "Who else should we talk to?"

### Executive sponsor / CEO / GM
- What business outcome justifies this investment? How will you know in 6 and 12 months?
- What are you prepared to stop or change to make it work?
- Who is accountable for AI decisions today? (NAIC practice 1: decide who is accountable.)
- How do you want to talk to staff about AI and jobs?
- What risk would you not accept?

### Operations / department heads
- Which tasks consume the most time in your team? Volumes and time per item.
- Where do errors or rework happen, and what do they cost?
- What would you do with the hours if they came back?
- Who in your team is already experimenting? Who would resist?

### Finance
- Where is the manual effort in AP, AR, reconciliations, reporting?
- What is the loaded cost of the roles involved (or who can confirm it)?
- How do you evaluate payback on technology spend? Budget cycle and approval thresholds?

### IT / CIO / MSP
- Core systems, versions, APIs, admin access, sandbox availability.
- Identity: SSO provider, MFA, group structure, provisioning (SCIM).
- Cloud agreements and preferred platform; data residency constraints.
- Existing AI tools licensed (enterprise tenancy or consumer accounts)?
- Change control process for integrations; who approves service accounts and scopes?

### Security / CISO
- Security requirements for suppliers (questionnaire, ISO 27001, SOC 2, IRAP).
- Essential Eight maturity target; logging and SIEM; DLP and sensitivity labels.
- Shadow AI: do you know which AI tools staff use? Any incidents?
- Position on agents with write access: approval, kill switch, spend caps.

### Privacy officer / legal / risk
- Is there a privacy impact assessment process? When is one required?
- Current privacy policy: does it describe automated decisions? (APP 1.7 from 10 Dec 2026.)
- Sector obligations (APRA CPS 230/234, ASIC, TGA, anti-discrimination, surveillance laws).
- Contract terms with customers that restrict data use or location.
- Who signs off AI use cases today?

### HR / people
- Workforce impact concerns; consultation obligations (unions, enterprise agreements).
- Training capacity; onboarding; champions programme appetite.
- Any HR use cases (screening, rostering, performance)? These are high-risk by default
  (anti-discrimination, ADM, NSW digital work systems duties once commenced).

### Procurement (L/XL)
- Panel or tender rules, thresholds, vendor onboarding timeline.
- Contract templates; liability, insurance and IP requirements.
- Evaluation criteria for AI suppliers.

### Front-line users
- Show me how you do it today. What slows you down?
- What would you never trust a machine to do?
- How would you want to check the AI's work?

## 4. Interview log

| Date | Function | Person (role) | Key numbers | Pains | Risks raised | Follow-ups |
|---|---|---|---|---|---|---|
