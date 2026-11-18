# Shadow AI discovery method

*v0.1.0, 2026-11-08. Feeds the AI register. Why it matters (research headline 8, IBM 2026 Cost of
a Data Breach): security incidents involving unapproved AI rose from 20% to 43% of organisations;
about two thirds of breached organisations had no AI governance policy (32% had one, down from 37%);
92% of organisations with AI-related
breaches lacked proper AI access controls. Cybernews (Aug 2025): 59% of US employees use
unapproved AI tools `[secondary]`. Quote these with their source and year, never rounded up.*

**Principle: discovery, not discipline.** The aim is a complete register and a sanctioned
alternative, not catching people. Say so in every communication, or people hide usage and the
register stays wrong. Pair discovery with approving one or two sanctioned tools (research B1
step 1) so there is a legal alternative on day one.

## Four lenses, scaled by size band

| Lens | What you look at | S | M | L | XL |
|---|---|---|---|---|---|
| 1 Survey | Anonymous staff survey (below) | 10-minute chat with the owner and each staff member | Survey | Survey + interviews per department | Survey + department champions |
| 2 SaaS and expense review | Card statements, expense claims, accounts payable, app marketplace installs, SSO app catalogue, OAuth grants to third-party apps in Microsoft 365 / Google Workspace | Owner reviews card statement with us | Finance export + admin console | Procurement + identity team | Identity + procurement + DLP reports |
| 3 Browser extensions and endpoint | Extension inventory via device management or a script; desktop AI apps; AI features switched on inside existing tools (CRM, helpdesk, office suite, meeting tools) | Check the main laptops together | Device management report if available | Device management report | Endpoint tooling report |
| 4 Network, CASB/SSE | Proxy, DNS, firewall, CASB or SSE logs for AI service domains; data-loss events | Usually not available: skip and say so | If a firewall or secure web gateway exists | CASB/SSE where deployed | CASB/SSE + DLP |

Lens 4 depends on what the client already runs. Never install monitoring on client systems as
part of discovery without written approval, and check surveillance law for the client's states
first (state workplace surveillance Acts, research A3; NSW DWS Act duties when commenced, AU-21).

**Vendor-embedded AI counts.** AI features inside approved software (ATS ranking, CRM scoring,
helpdesk auto-replies, meeting recorders) are part of the register and often the ADM candidates.

## Staff survey (anonymous, about 10 minutes)

1. Which AI tools have you used for work in the last three months? (List common ones plus
   "other", include browser extensions, phone apps and AI features inside work software.)
2. Personal or company account?
3. What do you use them for? (drafting, summarising, analysis, coding, images, meeting notes,
   customer replies, other)
4. Have you put any of these into an AI tool: customer or patient details, staff details,
   financial data, contracts, passwords or keys, internal strategy? (Yes / No / Not sure)
5. Roughly how much time does AI save you per week?
6. What would you use AI for if you had an approved tool?
7. Do you know whether we have an AI policy? Have you read it?
8. Anything about AI at work that worries you?

Report aggregated results only; minimum group size of five for any breakdown.

## Output

1. Register rows for every tool and feature found (`templates/ai-register-template.md`), tagged
   `discovery: survey / expense / extension / network`.
2. A one-page summary: tools found, how many staff, data types exposed, top three risks, the
   sanctioned-tool recommendation.
3. Immediate actions for any discovered use that puts personal or confidential data in public
   consumer tools (OAIC guidance, AU-11): stop, move to the sanctioned tool, check whether a
   notifiable data breach assessment is needed (Privacy Act NDB scheme, AU-6, with the client's
   privacy officer).
