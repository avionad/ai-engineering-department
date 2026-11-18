# Rollout headline, go-live tests and run loop -- Coastal Health Partners (FICTIONAL DRY RUN)

*PROVISIONAL. Durations are planning defaults from ai-enterprise-rollout, not commitments.*

## 1. Rollout headline (XL, four phases)

| Phase | Window (default) | Exit gate (from ai-enterprise-rollout) |
|---|---|---|
| Get ready | Weeks 0-6 | Accountable exec and program owner named; AUP with tool tiers published; sanctioned tool live with SSO and no-training terms in contract; permission hygiene check on reachable stores; shadow AI baseline; ADM inventory started; consultation plan agreed with HR (and unions if applicable) |
| Onboard and engage | Weeks 4-10 | Pilot groups trained before access; champions in every pilot clinic; adoption baseline; support channel |
| Deliver impact | Weeks 6-12+ | One redesigned workflow per pilot function with measured baseline and first planned-vs-actual |
| Extend and optimise | Q2 onward | Waves by clinic on evidence; referral intake admitted through its own Tier 3 screen; board report |

Tool tiers: A (sensitive-approved: the onshore assistant platform), B (enterprise-approved: M365 tenancy features under business terms), C (public tools: public data only, no health information, AU-11).

## 2. First 90 days

| Weeks | Workstream | Activity | Done when |
|---|---|---|---|
| 1-2 | Governance | Sponsor, program owner, AI council confirmed; RACI signed | Signed |
| 1-4 | Policy | AUP with tool tiers (ai-governance-program), legal review | Published |
| 1-6 | Discovery (paid) | Interviews, workshops, baselines, source and permission inventory, PMS feasibility, Copilot comparison | Discovery report accepted |
| 1-6 | Compliance | Confirm tiers, obligations, ADM inventory; **ADM disclosure by 10 Dec 2026** if any in-scope system | Council reviewed |
| 2-6 | People | Comms pack that answers staff concerns honestly (what changes, what does not, how roles are supported); consultation plan with HR; champion call | Agreed |
| 4-10 | Pilot build | Sandbox build of assistant on 2-4 SharePoint sites, about 50 users | Evals and leak suite pass |
| 8-10 | Verify | Test report + compliance sign-off; client owner approves go-live in writing | Approved |
| 10-12 | Pilot live | Training before access; adoption and time-to-answer measured vs baseline | First scorecard |
| 12 | Review | Scale, fix or stop; decide referral intake build and clinical guidelines | Decisions recorded |

## 3. Must pass before go-live (assistant, Tier 2)

Thresholds are set with the client's owner and recorded; none are House defaults. Blank threshold = no PASS.

| Area | Tests | Source in skills |
|---|---|---|
| Functional evals | Golden set of 100+ real questions checked by a clinic SME: retrieval recall at k, context precision, faithfulness, citation match, answer correctness, abstain correctness, latency and cost per answer | rag retrieval-and-evaluation s6; eval-design |
| Permission leak | Full plan P1-P22, with P9/P10 timed against the agreed revocation target, P16-P19 cache/history/side-channel/log leaks, P20 app identity. **Any leak = Critical = FAIL** | permission-leak-test-plan |
| Red-team F1 | Direct prompt injection (LLM01:2026) | red-team-catalogue |
| Red-team F2 | Indirect injection via documents (LLM01:2026, LLM09:2026; P14 canary doc) | |
| Red-team F3 | System prompt and data leakage (LLM08:2026, LLM02:2026) | |
| Red-team F4 | PII leakage incl. Presidio AU scan of outputs (LLM02:2026) | |
| Red-team F10 | Misinformation (LLM07:2026): hallucinated clinical statements, overreliance, source attribution. Added because answers may inform care | |
| Red-team F7 | Unbounded consumption (LLM06:2026): rate and length caps | |
| Refusal and escalation | Declines patient-specific diagnosis or treatment questions (TGA boundary) and points to the guideline owner | tier 2 scope |
| Verdict | FAIL if any Critical/High open, any regression unaccepted, any category under threshold | evals SKILL s6 |

Referral intake (Tier 3, later): adds full red-team across the catalogue, multi-turn attacks, agent control proofs (approval gate on every PMS write cannot be bypassed by letter content, kill switch, caps, tool allow-list), every High threat in its threat model tested, impact assessment and ADM disclosure in place. XL note from the skill: consider an independent tester for Tier 3 because the practice built it.

## 4. Monthly optimisation loop (what it tracks)

| Measure | Against |
|---|---|
| Eval pass rates by category (faithfulness, citation match, abstain), via eval_compare.py | Baseline and last month; a regression blocks |
| Override and feedback signals: thumbs-down with reason, "no answer" rate, escalations | Last month |
| Cost per answer, per active user and total (cost_trend.py on supplied cost_aud only) | Last month; flag threshold set per client |
| Latency, volume, failure rate | Last month, volume swings flagged as context |
| Permission sync lag and deletion lag vs revocation target | Agreed target (run-ongoing) |
| Retrieval hit rate and source freshness (superseded policies) | Drift watch |
| Pinned model and embedding versions vs vendor retirement dates in Australia East | Deprecation watch |
| Time to answer vs the discovery baseline (sampled) | Client's own baseline minutes |

One change set per month (prompt, retrieval tuning, routing, caching, golden-set growth, workflow step removal), built in staging, re-tested, client-approved. Material change (clinical guidelines added, new user group, new model or region) goes back to ai-compliance-risk for a re-screen. Trace store: Langfuse self-hosted in the same Australian region (features PENDING_VERIFICATION). Retainer draft: [figure removed] per month (one system, one change set, 11.3 h/month quoted).
