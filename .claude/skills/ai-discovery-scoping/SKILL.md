---
name: ai-discovery-scoping
description: Use when running discovery for an AI engagement and writing the scope of work -- preparing a first call, choosing the questions to ask, running a workshop or stakeholder interviews, qualifying and ranking candidate use cases, picking a pilot, matching a use case to a solution pattern, writing the solution design brief, or turning discovery answers into a scope of work with line items and three-point hours ready for ai-proposal-pricing to quote. Every value claim traces to the client's own numbers; missing numbers become follow-up questions, never estimates. Covers S to XL organisations in any industry.
when_to_use: "AI discovery, discovery call prep, first call with AI prospect, what questions should I ask, AI workshop agenda, stakeholder interviews for AI, qualify AI use cases, pick a pilot, AI solution design, solution design brief, scope the AI project, scope of work for AI, AI requirements, which AI pattern fits, RAG or automation, help me quote the AI project, AI wish list"
trigger: "AI discovery, discovery call prep, first call with AI prospect, what questions should I ask, AI workshop agenda, stakeholder interviews for AI, qualify AI use cases, pick a pilot, AI solution design, solution design brief, scope the AI project, scope of work for AI, AI requirements, which AI pattern fits, RAG or automation, help me quote the AI project, AI wish list"
version: 0.1.0
---

<!-- Changelog: 2026-11-08 (v0.1.0) -- Phase 1 build per ai-automation blueprint. -->

Read `../_shared/engagement-conventions.md` first. Lifecycle stage 1 (Discover). Hands off to
stage 2 (Govern), stage 3 (Design) and stage 4 (Quote).

# AI Discovery and Scoping

You help the practice owner turn "we want to use AI" into three things: a verified picture of the problem in
the client's own numbers, a solution design brief, and a scope of work that `ai-proposal-pricing`
can price without re-asking anything. The department brief was to "include discovery
phase help to ask the right questions and design the solution and help me quote the project"
(2026-11-08). This skill is that help.

## Four rules that override everything below

1. **Facts before promises.** Never say a capability will work before feasibility is checked
   against the client's data, systems and risk tier. "That is likely possible, we would confirm
   it on a sample of your documents" is the correct register.
2. **Value comes from the client's numbers only.** Hours, volumes, error rates, wage cost,
   revenue at stake: from the client's mouth or documents, with the note line it came from. No
   productivity multipliers from vendors, research or vendored skills (the Anthropic
   `ai-readiness` source suggests "assume 30-50%"; we deliberately do not carry that over). If a
   number is missing, write `PENDING` in the field and add the question to the follow-up list.
3. **Every scope line lands in exactly one delivery bucket** (`references/delivery-buckets.md`),
   because each bucket has a different cost shape and the estimator rejects anything else.
4. **No the practice prices here.** This skill produces hours and assumptions. Fees come only from
   `ai-proposal-pricing`, which is CFO-gated and owner-approved.

## Playbook

### Step 1. Pre-call prep (15-30 minutes, before any first call)

Fill `templates/pre-call-prep-template.md`:

- **Who they are.** Website, LinkedIn headcount, locations, what they sell, who their customers
  are. Assign a provisional size band (S 1-19, M 20-199, L 200-499, XL 500+, conventions s5).
  The band changes who must be in the room and how you ask, not just the volume.
- **Industry pack.** Read `../_shared/industry-packs/<industry>.md` (list the folder to find the
  file name). It holds high-ROI use cases, key risks and regulators for that industry. If no pack
  exists yet, use the industry matrix in
  the department's original research files (internal, not included in this repo) (section "Industry x use
  case x key risk matrix") and note the gap.
- **Hypothesis list.** Three to six likely use cases, each with the solution pattern it would map
  to (`references/solution-patterns.md`) and the one question that would confirm or kill it.
  Hypotheses are for steering the call, never for the proposal.
- **Early risk flags.** Regulated sector? Decisions about people (hiring, credit, claims,
  entitlements, pricing)? Health or children's data? EU customers? Each one raises the likely
  risk tier and adds questions from the risk section of the question bank.
- **Pick the questions.** The 12 must-ask questions (marked in the bank) plus the five or six
  most relevant to the hypotheses. Do not take 60 questions into a 30-minute call.

### Step 2. First call (30 minutes) and discovery workshop (90 minutes)

Scripts and agendas: `references/call-scripts.md`. The first call qualifies (is there a real,
owned, measurable problem and a decision-maker?). The workshop maps the process and collects the
numbers. For M, L and XL, run stakeholder interviews per function before or after the workshop
(interview guides in the same file).

Questions: `references/question-bank.md`, organised by business goal and pain; current process;
data; systems and integrations; people and change; risk and compliance; technical constraints;
commercial. It carries size-band variants (XL needs IT, security, procurement and legal in the
conversation) and points to industry-specific questions in the packs.

Questions that earn their place in every engagement (house style, from the Odoo practice):

- "Show me the task you most hate doing." A screen-share beats a survey.
- "How long does that take, how often, and who does it?" Capture the time cost in their words.
  Matthew's Timber (2026-10-30): a sales lookup takes "10, 15 minutes and a phone call", and
  supplier delivery docket PDFs are keyed into purchase orders by hand. Those two sentences found
  both use cases.
- "What would you not want the AI to do on its own?" Matthew's Timber declined automated purchase
  orders because suppliers would get too many. That answer sets the human-in-the-loop tier.
- "What happens if you do nothing for a year?" Sizes urgency honestly.
- "Who else touches this?" Finds the roles the contact forgot.

Write the notes into `templates/discovery-notes-template.md` within 24 hours, file in the
client's `meetings/` folder as `{YYYY-MM-DD}-{who}-ai-discovery-notes.md` (R14).

### Step 3. Route if the client is not ready to scope

- Client cannot name a problem, or has ten ideas and no priority, or leadership wants "an AI
  strategy": hand to `ai-readiness-assessment` (paid front-door product). Discovery resumes with
  its recommended first use cases.
- Client is regulated, or a use case makes or shapes decisions about people: run the
  `ai-compliance-risk` screen before design (conventions gate 2). No build before a risk tier.

### Step 4. Qualify the candidate use cases and pick a pilot

Method and scoring template: `references/use-case-qualification.md` and
`templates/use-case-scoring-template.csv`. Each candidate gets:

- **Value** in the client's numbers (hours x loaded cost, revenue, risk reduction). PENDING where
  missing.
- **Feasibility** 1-5 (data ready, integration access, complexity).
- **Risk tier** from conventions s6 (provisional until `ai-compliance-risk` confirms).
- **Time to value** (weeks to the first measurable result).

Rank and pick the pilot with `references/use-case-qualification.md` (it is the single rule: value
first, then feasibility, time to value, and risk tier as the tie-breaker; a tier 3 pilot is allowed
but carries the full tier 3 governance lines in scope). A candidate whose value is PENDING can be
named the *provisional* pilot, stated as conditional on the client confirming the missing number.
It also needs an internal owner and must fit one team and one workflow. Gate questions
adapted from Anthropic's `ai-readiness` (Apache-2.0): is the data there, is there an owner, can it
pilot in about 30 days? Any no means Wait, with what would unblock it.

### Step 5. Match to a solution pattern

`references/solution-patterns.md` has eleven patterns (P11 covers scoring or ranking people), each with when it fits, a Mermaid
architecture, deployment options with Australian residency notes, typical risk tier, build
components, effort drivers and the questions clients ask. Pick one primary pattern per use case.
If two patterns combine (for example voice receptionist plus workflow automation), name both and
scope both.

For detailed architecture, trust boundaries, build-vs-buy and the ADR, delegate to the
`ai-architect` agent (read-only; it returns a design). Give it the discovery notes, the chosen
pattern, the provisional risk tier and the client's constraints (cloud preference, residency,
SSO).

### Step 6. Write the solution design brief

`templates/solution-design-brief-template.md`: problem in the client's words and numbers,
current vs future process, architecture diagram, data flow, platform choice with residency, risk
tier, human-in-the-loop design, assumptions, out of scope, open questions. File in
`created/docs/strategy/solution-design-brief-{use-case}-{YYYY-MM-DD}.md`.

### Step 7. Write the scope of work

`templates/scope-of-work-template.md` plus `templates/scope-line-items-template.csv`. The CSV is
the contract with `ai-proposal-pricing`. Columns, in this order:

`line_item,bucket,assumption,low,likely,high,dependencies,risk,confirmed`

- `bucket` is one of: `config-saas`, `integration-workflow`, `rag-knowledge`,
  `custom-agent-app`, `model-customisation`, `governance-compliance`, `change-training`,
  `run-ongoing` (monthly hours, priced as a retainer), `discovery-measurement` (paid discovery,
  pilot baselines, benefit measurement).
- `confirmed` is `yes` or `no` (optional; `no` = the hours rest on a fact the client has not
  confirmed).
- `low <= likely <= high`, in hours, numbers only.
- `assumption` says what must be true for the hours to hold ("client supplies 50 sample dockets
  covering all suppliers").
- `dependencies` names what blocks the line (API access, test environment, client SME time).
- `risk` is one short phrase on what would blow the estimate.

Completeness checks before handing over (these are where AI projects overrun):

- Tier 2 or higher: an eval baseline line exists.
- Tier 3: impact assessment, ADM disclosure and red-team lines exist (`governance-compliance`).
- Any personal data: a privacy check line exists.
- Integration and data-cleaning effort is itemised, not hidden inside the build line.
- Handover, documentation and training are itemised (`change-training`).
- Ongoing run cost has its own `run-ongoing` lines, separate from the build.

**Hours the client has not confirmed.** Hours are always numbers (the estimator rejects text).
Where an estimate rests on an unconfirmed fact, set the optional `confirmed` column to `no` and
say what is unconfirmed in `assumption`. The estimator then stamps the quote INTERNAL DRAFT,
reports the share of hours that are unconfirmed, and recommends paid discovery when that share
or the range is large. Value figures are different: those stay PENDING, never estimated.

The template CSV's rows are an illustrative docket-extraction example (structure only, hours are
placeholders): replace every row. Validate the CSV parses before handover (output to the
scratchpad; the fee it prints is an internal draft, not ours to share):

```bash
python3 ../ai-proposal-pricing/scripts/estimate.py scope.csv \
  --config ../ai-proposal-pricing/references/pricing-config.json --out <scratchpad>/check.md
```

File the CSV and the scope document together in `created/docs/strategy/` with the same date
stamp.

### Step 8. Hand off and log

- `ai-compliance-risk`: the screen, if not done. Its tier replaces your provisional tier.
- `ai-architect` agent: the detailed design, if the brief needs one.
- `ai-proposal-pricing`: the scope CSV, the risk tier, the size band, the deployment choice and
  the discovery notes (for the value case).
- Log: your engagement activity log,
  `[YYYY-MM-DD HH:MM] [CLAUDE_CODE:<operator>] DISCOVERY | client | detail | outcome`.
- Any document with more than three numbers gets an R2 verifier in the client's
  `scripts/verifiers/`.

## Pushback that is part of the service

- A use case with no owner is not a pilot, whatever its value.
- If the binding constraint is data (no clean list, no consistent documents), say a data clean-up
  is the first project.
- If the client asks for full autonomy on an irreversible action (payments, emails to customers,
  deletions, decisions about people), propose human approval first and explain least agency.
- If the client wants a custom or fine-tuned model, check the decision order first: prompt, then
  retrieval, then fine-tune, then distil (research B3). Most knowledge problems are retrieval
  problems.
- If the stated budget cannot fund the scope, name what comes out; never thin the scope silently.

## Files

| File | Holds |
|---|---|
| `references/question-bank.md` | Questions by area, 12 must-asks, size-band variants, industry pointers |
| `references/call-scripts.md` | 30-min first call, 90-min workshop, stakeholder interview guides |
| `references/use-case-qualification.md` | Scoring method, gates, pilot selection |
| `references/solution-patterns.md` | Eleven patterns (P1-P11) with architecture, deployment, risk, effort drivers |
| `references/delivery-buckets.md` | Nine buckets, cost shapes, what goes where |
| `references/vendored-provenance.md` | Licensed material adapted here |
| `templates/pre-call-prep-template.md` | Prospect research and hypothesis sheet |
| `templates/discovery-notes-template.md` | Notes structure with numbers and follow-ups |
| `templates/use-case-scoring-template.csv` | Scoring sheet |
| `templates/solution-design-brief-template.md` | Design brief |
| `templates/scope-of-work-template.md` | Scope document |
| `templates/scope-line-items-template.csv` | Line items consumed by `ai-proposal-pricing` |
