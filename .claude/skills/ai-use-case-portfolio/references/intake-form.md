# Staff idea intake form

*v0.1.0, 2026-11-08. The practice's own design. Build it in the client's own form tool (Microsoft Forms,
Google Forms, their intranet or service desk) so the data stays in their tenancy. Questions are
written for any member of staff, not for IT.*

## Design rules

- **Ask about the work, not about AI.** Staff know their tasks; they do not know which technique
  fits. The portfolio owner decides whether it is rules-based automation, AI, or neither.
- **No dollar estimates from staff.** Ask for frequency and time; the value comes later from the
  process owner with real volumes and the loaded cost finance supplies.
- **Flag sensitive data early.** The data question routes the idea to a provisional risk tier.
- **Short.** Ten questions, most multiple choice. Long forms collect fewer ideas.

## Questions

| # | Question | Type | Feeds |
|---|---|---|---|
| 1 | What task or process do you want help with? Describe it as you would to a new colleague. | Long text | Name, pattern match (P1-P11) |
| 2 | Which team does this, and who is the best person to talk to about it? | Short text | Owner candidate |
| 3 | How often does it happen? (several times a day / daily / weekly / monthly / a few times a year) | Choice | Volume |
| 4 | Roughly how long does it take each time? (under 5 min / 5-15 / 15-60 / 1-4 hours / longer) | Choice | Time per item |
| 5 | How many people do this task? | Number | Volume |
| 6 | What goes wrong today? (errors, delays, rework, things missed, customer complaints, none) | Multi-choice + text | Error cost, risk reduction |
| 7 | Which systems or documents are involved? (email, spreadsheets, CRM, ERP, finance system, PDFs or scans, phone calls, other) | Multi-choice + text | Feasibility (integration) |
| 8 | Does it involve any of these? (customer or staff personal details, health information, financial details, decisions about a person such as hiring, credit, claims or eligibility, none of these) | Multi-choice | Provisional risk tier, ADM screen |
| 9 | Would the result go to a customer or member of the public, or stay inside the business? | Choice | Tier (customer-facing) |
| 10 | Is there anything else we should know (deadlines, workarounds, tools you already tried)? | Long text | Notes, shadow AI discovery |

Question 10 often surfaces shadow AI ("I already paste these into a chatbot"). Treat that as
discovery, not discipline, and pass it to `ai-governance-program`'s shadow AI method.

## Triage by the portfolio owner (weekly or fortnightly)

1. De-duplicate and merge similar ideas; credit every submitter.
2. Map to a solution pattern (`../../ai-discovery-scoping/references/solution-patterns.md`) or
   mark "not an AI problem" (process fix, training, existing feature) with the reason.
3. Set a provisional tier from questions 8 and 9: any decision about a person, health or
   financial detail suggests tier 3 for screening; personal data or customer-facing suggests 2.
4. Book a 20-minute call with the process owner to get real volumes and the current-cost inputs.
5. Add the register row with status `idea`, or `qualified` once value inputs and feasibility are in.
6. Tell the submitter what happened, including a no with the reason. Silence kills intake.
