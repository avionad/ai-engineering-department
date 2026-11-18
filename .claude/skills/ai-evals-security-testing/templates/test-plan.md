<!-- Audience: internal (ai-security-tester, ai-manager) and the client's technical owner.
Save as {client}/created/docs/security/ai-test-plan-{project-slug}-{YYYY-MM-DD}.md -->

# AI test plan: {system name}

*Template v0.1.0 (ai-evals-security-testing), 2026-11-08.*

**Client:** {client} | **System:** {name, version} | **Risk tier:** {1-3} | **Size band:** {S-XL}
**Plan author:** {name} | **Date:** {YYYY-MM-DD} | **Engagement state:** {path}

## 1. Authorisation (no test starts until every row is filled)

| Item | Value |
|---|---|
| Target system and components | |
| Environment (sandbox / staging / production) | |
| Production testing approved in writing by the client? (required if production) | Yes / No / N/A, evidence path |
| Test window (start, end, timezone AEST/AEDT) | |
| Test accounts and roles (test tenant or approved test accounts; never real staff accounts without written approval) | |
| Data used (synthetic / masked client examples / approved live data) | |
| Destructive tests allowed? (never against real data) | No / Sandbox only |
| Tools to be installed or run, and where | |
| Attacker and grader provider for promptfoo, and remote generation setting (see `references/tooling.md` s2) | |
| Paid API budget for the run and who approved it | |
| Authorised by (client name, role) and date | |
| Recorded in engagement state on | |
| Stop conditions (who to call, when to halt) | |

## 2. Scope

| Item | Detail |
|---|---|
| Pattern(s) | RAG / extraction / classification / agent / chat / generation |
| Entry points | chat UI, API, email inbox, document upload, scheduled job, tools |
| Untrusted content sources | retrieved docs, inbound email, CRM notes, web, tool results |
| User roles | |
| Data classes | public / internal / confidential / personal / sensitive |
| Tools and actions the system can take | (from the agent control spec) |
| Model, version, region | (pinned; from build notes) |
| Guardrails and versions | |
| Out of scope (and why) | |

## 3. Threat model rows to cover

| Threat ID | OWASP ID(s) | ATLAS ID(s) | Rating | Test ID(s) |
|---|---|---|---|---|
| | | | | |

Every High threat has at least one test ID.

## 4. Functional eval plan

| Item | Value |
|---|---|
| Golden set version and size per category | |
| Sources of items (real / edge / production failure / synthetic) and client permission (who, date) | |
| Masking method and human check (who, sample size) | |
| Held-out portion (if prompts will be tuned) | |
| Graders per category (deterministic / calibrated judge / human) | |
| Judge model, version, calibration date | |
| Runs per baseline (non-determinism) | |

## 5. Thresholds (agreed with the client, recorded)

| Category | Metric | Threshold | Blocking? | Agreed by | Agreed on | Reason |
|---|---|---|---|---|---|---|
| | pass rate | | Yes / No | | | |

Always blocking (DDD rule): permission leak, PII leakage, approval-gate bypass. Regressions block
(conventions and `references/eval-design.md` s6). Mirror this table in `thresholds.json`.

## 6. Security test plan

| Family | Planned? | Tools / plugins / strategies | Tests | Notes |
|---|---|---|---|---|
| F1 Direct injection | | | | |
| F2 Indirect injection | | | | |
| F3 System prompt and data leakage | | | | |
| F4 PII leakage (incl. Presidio output scan) | | | | |
| F5 Jailbreak | | | | |
| F6 Excessive agency (agents) | | | | |
| F7 Unbounded consumption | | | | |
| F8 Insecure output handling | | | | |
| F9 Supply chain and model (review) | | | | |
| F10 Misinformation | | | | |
| RAG permission-leak suite (`../ai-rag-engineering/templates/permission-leak-test-plan.md`) | | | | |
| Agent control proofs (approval gate, kill switch, caps, allow-list, credentials) | | | | |

## 7. Deliverables

- Results CSVs in `evals/results/{date}/`; compare output from `scripts/eval_compare.py`.
- Report from `templates/security-test-report.md`; R2 verifier for its numbers.

## 8. Sign-off of this plan

| Role | Name | Date |
|---|---|---|
| DDD tester | | |
| Client technical owner | | |

## Authorisation (both rows required before any attack family runs)

| What | Who gave it | Date | Evidence |
|---|---|---|---|
| Client authorisation for the target and window | | | |
| Provider position on adversarial testing (URL + date read; prior authorisation obtained where required) | | | |
