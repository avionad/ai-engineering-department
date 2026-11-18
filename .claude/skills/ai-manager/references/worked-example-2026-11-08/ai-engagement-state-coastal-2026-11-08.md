# AI engagement state -- Coastal Health Partners (FICTIONAL DRY RUN)

*Owned by ai-manager. Dry run 2026-11-08. Would live at `prospects/coastal-health-partners/created/docs/strategy/ai-engagement-state.md`; written to scratchpad per test instructions.*

## Facts

| | |
|---|---|
| Industry | Healthcare (allied health) -> `_shared/industry-packs/healthcare.md` |
| Size band (S/M/L/XL) | XL (520 staff, 14 clinics) |
| Jurisdictions (users, data) | AU, Queensland (assumed: no NSW workers, no EU/NZ users; to confirm) |
| Decision-maker | PENDING: CIO wrote the brief; accountable executive and budget holder not named |
| Billing entity | (example) |
| Problem in the client's words | "an internal assistant so clinicians and admin can ask questions over our policies, procedures and some de-identified clinical guidelines (about 6,000 documents across SharePoint and a legacy file share; HR and board documents restricted). Data must stay in Australia." Plus "automate referral letter intake into our practice management system". "Some staff are worried about AI. We want a plan for rolling this out properly." |

## Stage

| Stage | Status | Exit gate met? | Evidence (file) | Date |
|---|---|---|---|---|
| 0 Intake | Done except decision-maker | Partly (decision-maker PENDING) | this file | 2026-11-08 |
| 1 Discover | Not started; paid discovery proposed | No: no client numbers (hours, volumes), no readiness Go/Wait | scope CSV (draft) | |
| 2 Govern (risk tier: PROVISIONAL assistant T2, referral T3) | Provisional prep only | No: answers assumed, not confirmed with project owner | ai-risk-screen-coastal-2026-11-08.md | 2026-11-08 |
| 3 Design | PROVISIONAL outline for call prep | No | ai-solution-design-outline-coastal-2026-11-08.md | 2026-11-08 |
| 4 Quote | INTERNAL DRAFT only | No (unconfirmed hours 83%; Aditya approval not sought) | quote-breakdown-coastal-2026-11-08.md | 2026-11-08 |
| 5-8 | Not started | | | |

## Use cases

| Use case | Value (client numbers) | Feasibility | Risk tier | Status |
|---|---|---|---|---|
| Staff knowledge assistant (policies, procedures, de-identified clinical guidelines) | PENDING (time-to-answer baseline) | 3/5 provisional (permissions on legacy share unknown) | 2 PROVISIONAL (3 if used for patient-specific clinical decisions) | Provisional pilot |
| Referral letter intake into PMS | PENDING (volume, minutes per referral) | 2/5 provisional (PMS unnamed, API unknown) | 3 PROVISIONAL | Discovery only |

## Decisions

- 2026-11-08: Pilot boundary proposed: policies and procedures on 2-4 SharePoint sites, about 50 users; clinical guidelines and legacy file share deferred until the screening floor F5 (regulated activity)/TGA question is answered and ACL mapping proven.
- 2026-11-08: Referral intake not quoted for build; discovery assesses PMS feasibility first.

## Open questions (owner, due)

- Accountable executive and program owner (CIO, before discovery starts)
- Will clinicians use the assistant to decide care for a specific patient? (Clinical governance lead)
- Does referral intake set urgency, priority or routing? (Admin lead)
- PMS name, API, test tenant (CIO / PMS vendor)
- Is on-prem AD synced to Entra ID; how are file share ACLs structured? (IT)
- Any NSW-based workers, EAs or union coverage requiring consultation? (HR)
- Copilot licences or trial available? (CIO)

## Next action

- Aditya reviews the internal draft; decide whether to propose discovery-only ($18,600 + GST draft) or discovery plus pilot ($60,700 + GST draft). Owner: Aditya.

## Agent notes

### ai-architect
Played by ai-manager in dry run (agents not spawned). Outline only.

### ai-compliance-officer
Played by ai-manager. PROVISIONAL screens, every answer assumed.
