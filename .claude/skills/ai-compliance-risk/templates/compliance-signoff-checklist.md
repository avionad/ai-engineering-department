<!-- Audience: internal (ai-compliance-officer) and client accountable owner. Save as
created/docs/security/compliance-signoff-{project-slug}-{YYYY-MM-DD}.md -->

# Compliance sign-off checklist (pre-go-live)

*v0.1.0, 2026-11-08. Mode (h). Stage 6 exit gate in `engagement-conventions.md`: no go-live
without an eval baseline and this sign-off. Run by the `ai-compliance-officer` agent; the client's
accountable owner gives the go-live approval at stage 7, not DDD.*

**Project:** {name} | **Client:** {client} | **Tier:** {1-4} | **Date:** {YYYY-MM-DD}

Mark each item Done (with evidence path), N/A (with reason), or Open. **Any Open item in the
tier's column blocks sign-off.**

| # | Item | T1 | T2 | T3 | Evidence |
|---|---|---|---|---|---|
| 1 | Risk tier screen on file and still accurate (no material change since) | x | x | x | |
| 2 | Entry in the client's AI register (owner, purpose, data, vendor, tier) | x | x | x | |
| 3 | Acceptable use policy covers this system and users have it | x | x | x | |
| 4 | Applicable obligations document done; every In force / Commenced-later item has an owner | x | x | x | |
| 5 | No `PENDING_VERIFICATION` item relied on in any client-facing statement | x | x | x | |
| 6 | Privacy check done (PIA where required); data kinds and flows documented | | x | x | |
| 7 | Vendor due diligence done for every AI vendor touching client data; gates passed or accepted in writing | | x | x | |
| 8 | Data processed only in tools covered by the engagement's data-handling agreement; no client PI in public consumer AI tools | x | x | x | |
| 9 | Access control: SSO/RBAC; least privilege; access review owner | | x | x | |
| 10 | Logging: inputs, outputs, actions, model version, reviewer; retention set | | x | x | |
| 11 | Eval baseline run and results filed (accuracy, groundedness, refusals, format) | | x | x | |
| 12 | Risk register complete; no High or Critical risk without owner and treatment; residual accepted by the right person | | x | x | |
| 13 | Credentials in a secrets manager only; none in code, config files, chat or documents | x | x | x | |
| 14 | ADM check done; if in scope, privacy policy disclosure live (or live by 10 Dec 2026 and tracked) | | x | x | |
| 15 | AI impact assessment signed off | | | x | |
| 16 | Human review designed and tested (who, when, information shown, override recorded) | | | x | |
| 17 | Contestability path for affected people exists and is described to them | | | x | |
| 18 | Threat model done; red-team and security tests passed (prompt injection, data leakage, permission leak, agent privilege) | | | x | |
| 19 | Least agency for agents: scoped short-lived credentials, allow-listed tools, human approval for irreversible actions, kill switch tested, spend and rate caps | | (if agent) | x | |
| 20 | Monitoring live: owner, metrics, thresholds, review cadence | | | x | |
| 21 | Incident plan covers this system; contacts and NDB assessment path confirmed | | | x | |
| 22 | Transparency: users told they are dealing with AI where relevant; system or model card filed | | x | x | |
| 23 | Industry pack controls applied (list each) | | x | x | |
| 24 | Non-automated fallback if the system is unavailable | | | x | |
| 25 | Tier 4: confirm the system was not built | | | | |

## Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| DDD compliance (ai-compliance-officer run, reviewed by the practice owner) | | Ready / Not ready | |
| Client accountable owner (go-live approval, stage 7) | | Approve / Reject | |

Open items and conditions: {list}

*This checklist identifies regulatory considerations for review by your legal adviser. It is
not legal advice.*
