# AI risk register: Customer service agent with order lookup and capped refunds

Client: Sample Outdoor Retail Pty Ltd (fictional) | Date: 2026-11-08 | Project risk tier: 3

This assessment identifies regulatory considerations for review by your legal adviser. It is not legal advice.

Inherent ratings: Critical 0, High 8, Moderate 13, Low 0, not assessed 0.

**Tier minimum controls not yet evidenced:** eval baseline, impact assessment, adm disclosure, human review, red-team, monitoring, incident plan.

**Risks needing more treatment:** R-15, R-17, R-07, R-21.

**Risks with no owner:** R-21.

| ID | Risk | Category | L | I | Inherent | Controls | Owner | Residual | Treatment |
|---|---|---|---|---|---|---|---|---|---|
| R-04 | Prompt injection (direct or indirect) changes system behaviour | security | 4 | 4 | High (16) | Input filtering; Tool allow-list; Output checks | IT lead | Moderate | modify; adequate on count (check quality) |
| R-16 | Rogue actions: agent takes unintended actions with real effect | security | 3 | 5 | High (15) | Refund cap $100; Human approval above cap; Kill switch | Operations director | Low | modify; adequate on count (check quality) |
| R-03 | Information security: model or integration widens attack surface | security | 3 | 4 | High (12) | Pen test before go-live; SSO | IT lead | Moderate | modify; adequate on count (check quality) |
| R-08 | Data privacy: leakage or unauthorised use or disclosure of personal information | privacy | 3 | 4 | High (12) | PII redaction in logs; No-training contract term | Privacy officer | Moderate | modify; adequate on count (check quality) |
| R-10 | Personal information entered into public consumer AI tools (shadow AI) | privacy | 4 | 3 | High (12) | Sanctioned tool; AUP | Operations director | Moderate | modify; adequate on count (check quality) |
| R-11 | Misleading statements or promises by a customer-facing AI | legal | 4 | 3 | High (12) | Policy-only answers; Human escalation | CX manager | Moderate | modify; adequate on count (check quality) |
| R-15 | Permission leak: retrieval returns documents the user may not see | privacy | 3 | 4 | High (12) | Customer-scoped lookups only | IT lead | Low | modify; more treatment needed |
| R-17 | Agent goal hijack via retrieved or tool content | security | 3 | 4 | High (12) | Untrusted content isolation | IT lead | Moderate | modify; more treatment needed |
| R-01 | Confabulation: confidently stated but false output relied on | safety | 3 | 3 | Moderate (9) | Grounding in policy docs; Answer citations | CX manager | Moderate | retain; adequate on count (check quality) |
| R-05 | Insecure model output passed to downstream systems or users | security | 3 | 3 | Moderate (9) | Output encoding | IT lead | Low | modify; adequate on count (check quality) |
| R-06 | Value chain: third-party model change, deprecation or opaque components | third-party | 3 | 3 | Moderate (9) | Pinned model version | IT lead | Moderate | modify; adequate on count (check quality) |
| R-09 | Excessive data handling during inference (retention, logging, vendor reuse) | privacy | 3 | 3 | Moderate (9) | 30-day log retention | Privacy officer | Low | modify; adequate on count (check quality) |
| R-13 | Unbounded consumption or denial of wallet from public traffic | operational | 3 | 3 | Moderate (9) | Rate limit; Spend cap | IT lead | Low | retain; adequate on count (check quality) |
| R-07 | Supplier concentration with no tested exit or substitution plan | third-party | 2 | 4 | Moderate (8) | none | Operations director | Not assessed | modify; more treatment needed |
| R-14 | Retrieval or vector store poisoning | security | 2 | 4 | Moderate (8) | Document integrity checks | IT lead | Low | modify; adequate on count (check quality) |
| R-18 | Identity and privilege abuse: over-scoped or shared agent credentials | security | 2 | 4 | Moderate (8) | Scoped short-lived credentials; Separate service account | IT lead | Low | retain; adequate on count (check quality) |
| R-20 | Tool source provenance: untrusted tool or MCP server | security | 2 | 4 | Moderate (8) | Approved tool list | IT lead | Low | modify; adequate on count (check quality) |
| R-02 | Human-AI configuration: automation bias or over-reliance by staff | operational | 3 | 2 | Moderate (6) | Staff training | CX manager | Low | modify; adequate on count (check quality) |
| R-12 | Harmful, hateful or abusive content shown to the public | safety | 2 | 3 | Moderate (6) | Content filter | CX manager | Low | modify; adequate on count (check quality) |
| R-19 | Runaway agent tool loops and cascading failures | operational | 2 | 3 | Moderate (6) | Step limit; Spend cap | IT lead | Low | retain; adequate on count (check quality) |
| R-21 | Memory and context poisoning across sessions | security | 2 | 3 | Moderate (6) | none | UNASSIGNED | Not assessed | modify; more treatment needed |

Sources per risk are in the CSV `source` column. Ratings use a 5x5 heuristic (1-4 Low, 5-9 Moderate, 10-16 High, 17-25 Critical) calibrated to the client's risk appetite.
