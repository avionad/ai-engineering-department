# Worked example: one engagement end to end (FICTIONAL CLIENT)

**Every file in this folder is a dry run against an invented client. "Coastal Health Partners" does
not exist. No number here is an approved DDD price, and no figure came from a real client.** The
folder exists because the department had no committed example of a full engagement, so nobody could
see what good output looks like before doing it for the first time.

The run was produced on 2026-11-08 by a session that had never seen the department, following
`ai-manager/SKILL.md` as written. The friction it hit was then fixed in the skills, so this example
shows the department working after those fixes, not before.

## The fictional brief

A Queensland allied health group, 520 staff across 14 clinics, on Microsoft 365 with some AWS. They
want a staff assistant over about 6,000 policy and procedure documents (HR and board documents
restricted), referral letter intake into their practice management system, data kept in Australia,
and a plan for rolling it out with staff who are nervous about AI.

## The artefacts, in the order the lifecycle produces them

| Stage | File | What to look at |
|---|---|---|
| 0 Intake | `ai-engagement-state-coastal-2026-11-08.md` | The four facts, size band XL, and an honest "decision-maker unknown" that keeps the gate open |
| 2 Govern | `ai-risk-screen-coastal-2026-11-08.md` | Two use cases screened separately: assistant tier 2, referral intake tier 3, each with its reason. Note the ADM analysis on the referral intake and that every answer is labelled provisional because the client was not in the room |
| 2 Govern | `ai-risk-register-assistant-2026-11-08.md` and `.csv`, plus `project-assistant-coastal.json` and `seeded-assistant-coastal-2026-11-08.json` | The seed-then-score flow of `ai_risk_register.py`, including the tier 3 controls it reports as missing |
| 3 Design | `ai-solution-design-outline-coastal-2026-11-08.md` | The buy-first check, the platform recommendation with its residency reasoning, permission-aware retrieval, and a data-flow diagram with trust boundaries |
| 4 Quote | `scope-discovery-only-coastal-2026-11-08.csv` and `scope-discovery-pilot-coastal-2026-11-08.csv` | Scope lines in the nine buckets with `confirmed=no` on hours that rest on unconfirmed facts |
| 4 Quote | `quote-breakdown-*.md` and `quote-*.json` | Both quotes stamped INTERNAL DRAFT because most hours are unconfirmed, and the discovery-only quote priced as a fixed fee |
| 4 Quote | `verify_quote-coastal-2026-11-08.py` | The R2 verifier that recomputed every figure independently. Run it from inside this folder: `python3 verify_quote-coastal-2026-11-08.py .` (12 of 12 PASS, re-run 2026-11-08) |
| 4 Rollout | `ai-rollout-verify-run-coastal-2026-11-08.md` | Phases and the first 90 days, with the 10 December ADM inventory inside the window |

## What to copy from it, and what not to

Copy: the shape of each artefact, the provisional labelling, the per-use-case screening, the
verifier, and the habit of writing PENDING where the client has not given a number.

Do not copy: any hours, any fee, any tier. Those were invented for a client that does not exist.
Run the real discovery and the real screen.
