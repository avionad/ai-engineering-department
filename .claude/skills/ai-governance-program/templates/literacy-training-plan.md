<!-- Audience: client executive and HR/L&D. Save as
created/docs/security/ai-literacy-plan-{client}-{YYYY-MM-DD}.md -->

# AI literacy training plan (by role, incl. board)

*v0.1.0, 2026-11-08. Practices 1 and 6 (AU-4); ISO/IEC 42001 Clause 7 (competence, awareness);
NIST Govern. Why now: APRA's AI letter (30 Apr 2026, AU-15) found boards lack AI literacy; the DTA
policy (AU-17) makes staff responsible-AI training mandatory for Commonwealth agencies within 12
months (due around 15 Dec 2026); the EU literacy duty was softened by the Omnibus to Commission
and member states "support and facilitate" (EU-2) but is still expected of EU-facing clients.
Research B1 step 6: role-based training for all staff, power users, developers (OWASP) and the
board.*

## Role matrix

| Audience | Outcome | Content | Format and length | When | Evidence |
|---|---|---|---|---|---|
| All staff | Use approved tools safely; know the never-list; report issues | What AI is and is not; the AUP never-list; checking outputs; confabulation examples from their own work; how to report; why reporting early is safe | 45-60 min live or recorded + 5-question check | On start; refresh annually | Completion + AUP acknowledgement |
| Managers and decision-makers | Know when a decision is ADM and what human review really means | APP 1.7 three-limb test in plain language; automation bias; designing review steps; contestability | 60 min workshop with their own processes | Within first quarter of the program | Attendance; one ADM item each brought for the register |
| Power users and use-case owners | Write good prompts, evaluate output, own a register entry | Prompting and grounding; evaluation basics; data classes; register and screening duties | Half day | Before they own a system | Register entry created |
| Builders (internal devs, admins, integrators) | Build to least agency and test for known weaknesses | OWASP LLM01-LLM10 and ASI01-ASI10 (by ID, our own material); scoped credentials; logging; eval baselines; permission-aware retrieval | 1 day + lab | Before first build | Lab completion; threat model on first project |
| Privacy, risk, legal | Run screens, impact assessments, vendor DD | Register walk-through; the tier model; mode (a)-(h) of `ai-compliance-risk` | Half day | Program start | First screen co-run with DDD |
| Executive team | Set direction, appetite and accountability | Value cases from their discovery numbers; the risk tiers; accountability; what good looks like at 6 and 12 months | 90 min | Program start | Charter approved |
| Board (M where relevant; L and XL; any APRA-regulated client) | Oversee AI risk with informed challenge | AI risk appetite; questions to ask management; the client's register and top risks; supplier concentration and exit plans (APRA area); cyber exposure from AI (prompt injection, data leakage, agent misuse); regulatory horizon from the register (in force vs proposed) | 60-90 min session + one-page question card | Annually and on major change | Board minutes; appetite statement |

## Size band scaling

- **S:** one 60-minute all-staff session run by DDD, AUP signed, owner gets a 30-minute decision-
  maker briefing. No separate board.
- **M:** all staff + managers + power users; executive briefing; board if one exists.
- **L:** full matrix; champions in each department deliver refreshers.
- **XL:** full matrix through the LMS; champions network; board session annually; completion
  reported to the council monthly.

## Measures

Completion by role; AUP acknowledgements; register entries created by trained owners; number of
issues reported (rising early is healthy); pre and post quiz on the never-list.
