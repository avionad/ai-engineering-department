# Readiness interview guides per function

*v0.1.0, 2026-11-08. Each guide is 30-45 minutes (the S owner interview combines them into about
two hours). The dimension each question feeds is in brackets. Open every interview with purpose,
confidentiality of individual comments, and permission to take notes. Close with "What would make
AI fail here?" and "Who else should we speak to?" For use-case discovery questions, see
`../../ai-discovery-scoping/references/question-bank.md`.*

## Owner / CEO / executive sponsor
1. Why AI, why now? What problem would justify the spend? [strategy]
2. Who is accountable for AI decisions today? Who approves a new AI tool? [governance: accountability]
3. Is there a budget, and does it cover running costs and training, not just the build? [strategy]
4. How will you judge value at 6 and 12 months? [strategy]
5. How are you talking to staff about AI and their jobs? [people]
6. What AI use would you never accept in this business? [governance: impacts]
7. Do any of your systems make or shape decisions about customers or staff? [governance: ADM]

## Operations / department heads
1. Which tasks take the most time? Volumes and time per item, if known. [process]
2. Are these processes written down and done the same way by everyone? [process]
3. Where do errors and rework happen? [process, data]
4. Who in your team experiments with AI already, and with which tools? [people, security]
5. What data do you need that is hard to get? [data]

## Finance
1. Where is the manual effort in AP, AR, reconciliations and reporting? [process]
2. Do you trust the numbers in your reports? Where do disputes come from? [data]
3. How do you assess payback on technology? Approval thresholds? [strategy]
4. Is AI spend visible anywhere (subscriptions on cards, expense claims)? [security: shadow AI]

## IT / MSP
1. Core systems, versions, APIs, exports, sandbox availability. [technology]
2. Identity: SSO provider, MFA coverage, group structure. [technology, security]
3. Cloud agreements and regions; any residency requirements. [technology]
4. Which AI tools are licensed, and under what terms? [security]
5. Integration tooling and who maintains it. [technology]
6. Logging and monitoring; backups; change control. [technology]

## Security / CISO (M+ where the role exists)
1. Data classification scheme and how it is applied. [security, data]
2. DLP, sensitivity labels, SSE or CASB coverage. [security]
3. Known shadow AI use; any incidents involving AI tools. [security]
4. Supplier security requirements (ISO 27001, SOC 2, IRAP). [security]
5. Essential Eight maturity target; position on agents with write access. [security]

## Privacy officer / legal / risk
1. Privacy policy last reviewed when? Does it describe automated decisions? [governance: ADM]
2. Privacy impact assessment process; when is one triggered? [governance: impacts]
3. Risk register: are AI risks on it? Risk appetite for AI? [governance: risk_management]
4. Sector regulator expectations (for example APRA's AI letter of 30 April 2026 for APRA-regulated entities). [governance]
5. Contract terms with customers that restrict data use or location. [security, data]
6. Incident and breach process; does it cover AI? [governance: test_monitor]

## HR / people
1. Staff sentiment about AI; consultation obligations. [people]
2. Training capacity and current digital skills programmes. [people]
3. Any HR uses of automation (screening, rostering, performance)? These are ADM and anti-discrimination exposure. [governance]
4. Appetite for a champions network. [people]

## Front-line staff (small group, L/XL)
1. Which AI tools do you use, for what, with what data? (No blame; this is the shadow AI inventory.) [security]
2. What slows you down most? [process]
3. What would you want AI to do, and what would you never trust it with? [people, governance: human_control]
4. Have you had any training on AI? Would you want it? [people]
