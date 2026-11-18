# Discovery question bank

*v0.1.0, 2026-11-08. Pick from this; never read it out. Questions marked **[MUST]** are the 12
asked in every engagement, whatever the size or industry. Everything else is chosen in pre-call
prep against the hypothesis list.*

How to use the answers:
- Write numbers exactly as the client said them, with units and who said it ("Ben: 10-15 min plus
  a phone call per lookup, several a day"). A range is fine. A guess by us is not.
- If the client does not know a number, write `PENDING` and add "who can tell us" to the
  follow-up list. Do not fill the gap with a benchmark.
- Answers in the risk and compliance section go straight to the `ai-compliance-risk` screen.

---

## 1. Business goal and pain

1. **[MUST]** What problem are you trying to solve, in your own words? What made you look at this
   now?
2. **[MUST]** If this works, what changes for the business in 12 months? How would you measure it?
   (This becomes the success measure in the scope.)
3. Which of these matters most: hours back, fewer errors, faster response to customers, more
   revenue, lower risk, or something else?
4. What have you already tried (tools, pilots, staff using ChatGPT on their own)? What happened?
   (Failed pilots are signal; find out why before proposing the same thing.)
5. What happens if you do nothing for a year?
6. Is this one person's pain or a team's? How many people feel it?

## 2. Current process walkthrough (per candidate use case)

Ask for a screen-share or a walk-through of a real example.

7. **[MUST]** Walk me through the last time this happened, step by step. Who does it, in which
   system, and what do they do with the result?
8. **[MUST]** How often does it happen (per day, week, month) and how long does each one take?
9. What does an error cost? How often do errors happen, and who catches them?
10. Who does the work (role, not name) and roughly what is their loaded hourly cost? (If they will
    not share wages, ask for the role; the CFO step can work from a client-confirmed figure later.
    Never assume one.)
11. Which systems are touched along the way? Any copy-paste between systems?
12. What are the exceptions? What does a hard case look like, and how often do they come up?
13. Is the process written down anywhere? Does everyone do it the same way?
14. What is the turnaround expectation (customer, regulator, internal SLA)?

## 3. Data

15. **[MUST]** Where does the information this process needs live today (systems, shared drives,
    email, paper)? Can you send us five to ten real examples?
16. How consistent is it? Same supplier formats, same templates, or every one different?
17. Does it contain personal information? Sensitive information (health, financial, criminal
    record, biometrics, children's data)?
18. Who owns the data and who is allowed to see which parts of it?
19. Are there any rules about where the data must be stored or processed (Australia only,
    contract terms with your customers, government security classification)?
20. How far back does the history go, and do you need the AI to use historical records?
21. Has any of this data already been put into public AI tools by staff? (Shadow AI; OAIC best
    practice is not to enter personal information into publicly available generative AI tools.)

## 4. Systems and integrations

22. **[MUST]** What are your core systems: CRM, ERP or accounting, email and documents (Microsoft
    365 or Google Workspace), phones, line-of-business apps? Which version or plan?
23. Do those systems have an API or export we could use? Who administers them (internal IT,
    an MSP, the vendor)?
24. Can we get a test or sandbox environment? (the practice builds in sandbox or staging only.)
25. Do you already run any automation (Power Automate, Zapier, n8n, scripts, macros)?
26. Is there a system of record the output must land in (for example purchase orders in the ERP)?

## 5. People and change

27. **[MUST]** Who would own this internally and drive it after we hand over? (An owner, not a
    sponsor who will "support" it. No owner, no pilot.)
28. Who will use it day to day? How comfortable are they with new tools?
29. Is anyone worried about what AI means for their job? How has leadership talked about it?
30. Who are the likely champions, the people already experimenting?
31. Who needs to approve the change (union, works council, HR, the board)?
32. How have past technology rollouts gone here?

## 6. Risk and compliance (feeds the `ai-compliance-risk` screen)

33. **[MUST]** Will the system make, or materially shape, decisions about people: hiring,
    credit, pricing, claims, entitlements, access to services, discipline? (APP 1.7 ADM
    disclosure applies from 10 December 2026 where a program makes or does something
    substantially and directly related to a decision that could significantly affect an
    individual's rights or interests, using their personal information. Human review does not
    remove the duty if the output materially influences the decision. Source: research file A1,
    OAIC guidance 30 Sep 2026.)
34. Are you regulated by APRA, ASIC, TGA, AHPRA or another sector regulator? Are you a supplier to
    government?
35. **[MUST]** Where are the people whose data this touches: customers, candidates, staff? Any outside Australia (NZ, EU, UK, US)? (NZ: Privacy Act 2020 incl. IPP 3A applies, register NZ-2. EU: the EU AI Act may apply to output used in the EU. Others: PENDING_VERIFICATION, flag to the legal adviser.)
36. Will it talk to customers or the public directly (chat, phone, email)?
37. Will it record calls or meetings? (Consent and listening-device laws vary by state and
    are not yet in the register: PENDING_VERIFICATION, flag to the client's legal adviser.)
38. Do you have an AI policy, acceptable use policy or AI register today?
39. What is the worst thing that could happen if the AI got it wrong? Who would be harmed?
40. What would you not want it to do without a person approving first?

## 7. Technical constraints

41. Cloud preference or mandate: AWS, Azure, Google Cloud, Australian VPS, on-premises? Existing
    enterprise agreements?
42. Security requirements: SSO (Entra ID, Google, Okta), MFA, Essential Eight maturity target,
    ISO 27001 or SOC 2 expectations of suppliers, IRAP for government work?
43. Any security questionnaire or vendor onboarding we must complete before access?
44. Data residency: must processing stay in Australia? (Determines platform: see
    `solution-patterns.md` deployment notes and `../../_shared/client-faq.md`.)
45. Any tools banned by policy (for example certain model origins for government or critical
    infrastructure clients)?
46. Expected volumes: documents per month, conversations per day, users. (Drives run cost.)

## 8. Commercial

47. **[MUST]** Who makes the decision and who signs? Anyone else who can say no?
48. **[MUST]** Is there a budget range or a figure you need to stay under? (Ask for a range; do
    not offer one. Pricing is set later by `ai-proposal-pricing`.)
49. **[MUST]** When do you need the first result, and is there a hard date behind it (end of
    financial year, a regulator deadline, a busy season)?
50. How will you judge whether this was worth it after three months?
51. Would you rather pay for a short paid discovery or pilot first, or a fixed price for the full
    build?
52. Who pays the ongoing platform and usage costs, and from which budget?

---

## Size-band variants

The band changes who you ask and how, not just how many questions.

| Band | Who is in the room | How to ask | Extra questions |
|---|---|---|---|
| S (1-19) | Owner, maybe one key staff member | One conversation; owner answers most areas. Keep it to the 12 must-asks plus process detail. Ask to see the work. | "Who covers this when you are away?" "What SaaS tools are you already paying for?" |
| M (20-199) | Owner or GM, department heads, the person who runs IT (often an MSP) | Workshop with department heads; short follow-up with IT/MSP. | SSO in place? Which department goes first and why? Is there an AI policy? |
| L (200-499) | Executive sponsor, department heads, IT, risk or compliance, procurement | Separate interviews per function before the workshop. Expect a vendor due-diligence questionnaire. | Data classification scheme? AI council or steering group? Procurement thresholds and panel rules? Change-management capability? |
| XL (500+) | Executive sponsor, CIO/CTO, CISO, privacy officer, legal, procurement, HR, business owners, often internal audit | Multi-session discovery. Security and procurement run in parallel with business discovery, not after it. | DLP and sensitivity labels? Existing enterprise AI tenancy (Copilot, Bedrock, Azure OpenAI)? Permission model of the document stores (SharePoint, Drive, Confluence)? Board AI literacy? ISO 42001 or 27001 alignment? Shadow AI inventory? Model risk policy? |

XL warning signs to record: no named accountable executive; security not yet engaged; "IT will
sort out access later". Each one means discovery is not finished.

## Industry-specific questions

Each industry pack at `../../_shared/industry-packs/<industry>.md` carries its own questions
(regulator, high-risk use cases, sector obligations). Read the pack in pre-call prep and add its
top questions to the call sheet. Industries planned in the blueprint: finance, insurance, health,
legal, education, government, retail, recruitment/HR, manufacturing, real estate, professional
services, not-for-profit. If the pack is missing, use the industry matrix in the research file
and flag the gap to `ai-manager`.

## Follow-up list format

Every unanswered must-ask and every `PENDING` number becomes a line:

| # | Question | Why it matters | Who can answer | Due |
|---|---|---|---|---|
