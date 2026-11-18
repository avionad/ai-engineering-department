---
name: ai-readiness-assessment
description: Use when a client or prospect wants to know whether they are ready for AI, does not know where to start, or leadership asks for an AI strategy starting point. DDD's paid front-door product. Scores seven dimensions 1-5 with evidence (strategy and leadership, data, technology and infrastructure, people and skills, process, governance and risk, security and privacy), scores governance against the Guidance for AI Adoption six practices and the APP 1.7 automated decision-making duty, applies Go/Wait gates to the organisation and each candidate use case, and produces a readiness report with a ranked 90-day plan plus a one-page executive summary. Scales from a 2-hour owner interview (S) to a multi-week assessment with data sampling (XL).
when_to_use: "AI readiness, are we ready for AI, AI readiness assessment, AI maturity, where do we start with AI, AI audit of our business, AI strategy starting point, readiness scorecard, AI gap analysis, should we invest in AI yet, AI health check, readiness report, Go or Wait on AI"
trigger: "AI readiness, are we ready for AI, AI readiness assessment, AI maturity, where do we start with AI, AI audit of our business, AI strategy starting point, readiness scorecard, AI gap analysis, should we invest in AI yet, AI health check, readiness report, Go or Wait on AI"
version: 0.1.0
---

<!-- Changelog: 2026-11-08 (v0.1.0) -- Phase 1 build per ai-automation blueprint. -->

Read `../_shared/engagement-conventions.md` first. Lifecycle stage 1 (Discover): this skill
produces the readiness Go/Wait that the stage exit gate requires.

# AI Readiness Assessment

The front-door product: a paid, evidence-based view of how ready an organisation is to use AI,
what blocks it, and where to start. The research found no credible open-source readiness method
for 20 to 500+ staff organisations tied to Australian obligations (GitHub research, gap 2); this
is DDD's own, built on credited open-source pieces (`references/vendored-provenance.md`).

## Rules

1. **Evidence or it does not count.** Every dimension score cites evidence, marked `seen`
   (document or system observed) or `stated` (interview only). An unevidenced dimension blocks a
   Go. Stated-only evidence caps confidence at medium (the script enforces this).
2. **Never inflate.** A 2 the client needs to hear beats a 3 that flatters. A score of 1 is a
   deal-breaker and the report says plainly that AI work in that area should wait.
3. **The gate decides, not the average.** The mean is context. Go/Wait follows `references/gates.md`.
4. **Client numbers only** for any value statement. No productivity multipliers; missing values
   are written as "to be measured" and carried into discovery.
5. **Legal framing.** Governance findings identify considerations for the client's legal adviser.
   Every client-facing output carries: "This assessment identifies regulatory considerations for
   review by your legal adviser. It is not legal advice." Voluntary guidance (the six practices)
   is never called a requirement; APP 1.7 is described as commencing 10 December 2026.
6. **Client data stays in approved tools** (conventions s2). Never paste client documents into
   public AI tools.
7. **No prices here.** The assessment's own fee and any build estimate come from
   `ai-proposal-pricing` (CFO-gated).

## Playbook

### Step 1. Scope the assessment by size band

Read `references/size-band-scaling.md`. Confirm the band at intake (conventions s5); it sets the
interviews, the evidence standard and the report depth.

| Band | Shape |
|---|---|
| S | One owner interview of about 2 hours, screen-share of 1-2 processes, light report |
| M | Owner, 3-5 department heads, IT/MSP; full report |
| L | All functions incl. risk, privacy, HR, procurement; staff pulse; per-function appendix |
| XL | Multi-week, all functions and business units, data sampling, log-based shadow AI evidence, readout deck |

Send the evidence request (`references/evidence-checklist.md`) before the interviews, trimmed to
the band.

### Step 2. Interview and collect evidence

Guides per function: `references/interview-guides.md`. Each question names the dimension it feeds.
Record every evidence item as you go in the input JSON (`templates/readiness-input-template.json`).
If the client also needs use cases found, borrow the process questions from
`../ai-discovery-scoping/references/question-bank.md` (sections 2 and 3).

Industry overlay: read `../_shared/industry-packs/<industry>.md` for sector obligations and
high-risk use cases; record any that apply under governance and risk.

### Step 3. Score the seven dimensions

Rubric with concrete descriptors per level: `references/dimensions-rubric.md`. Half-points
allowed. For governance and risk, also rate each of the six practices 0 (absent), 1 (partial) or
2 (in place), and complete the ADM block (exposure yes/no/unknown, inventory done, privacy policy
updated).

The seven dimensions follow the brief Aditya approved (2026-11-08). They differ slightly from the
research recommendation (B7), which had "culture and change" separate and security inside
technology: culture is scored inside people and skills, and security and privacy has its own
dimension because shadow AI and data leakage are the strongest governance findings in the research
(IBM 2026, research headline 8).

### Step 4. Gate the candidate use cases

For each candidate the client raises (or that the assessment surfaces), record: data ready, named
owner, can pilot in about 30 days, risk tier (provisional until `ai-compliance-risk` confirms),
compliance screen done, value figure with its source (client only) or null, time to value. Gate
rules: `references/gates.md`. Tier unassigned means Wait until screened; tier 4 means stop.

### Step 5. Run the scorer

```bash
python3 scripts/readiness_score.py input.json --out scorecard-YYYY-MM-DD.md --json scorecard-YYYY-MM-DD.json
```

It validates the input (rejects scores outside 1-5 or off the half-point grid, value figures
without a source, unexplained weights), then writes the scorecard, the governance table, the ADM
flag (with days to 10 December 2026, or "has applied since" after that date), the use-case gate,
and a ranked 90-day plan (P1 prerequisites, P2 foundations, P3 first use cases; P4 listed after 90
days). Exit 0 means scored; exit 2 means invalid input and nothing was scored. Keep the input JSON
in the client's `data/` folder: it is the R2 source of truth.

### Step 6. Write the outputs

- **Readiness report** (`templates/readiness-report-template.md`): summary, scorecard with a
  plain-English line per dimension, governance and compliance position, top risks ranked by
  business impact, recommended first use cases, 90-day plan with client owners, method, appendix
  with evidence register and credits. File in `{client}/reports/adhoc-report/` as
  `ai-readiness-assessment-{YYYY-MM-DD}.md`, render .html and .pdf with
  `tools/report-renderer/render_report.py` (R11).
- **Executive summary** (`templates/executive-summary-template.md`): one page for the owner,
  executive team or board.
- Both pass a client-facing tone review (audience tag, `voice_lint.py` zero FAIL). R2 verifier in
  the client's `scripts/verifiers/`, re-reading the input JSON and checking every score, count and
  date in the report.

### Step 7. Hand off

| Result | Next |
|---|---|
| Go or Go with conditions | `ai-discovery-scoping` for the recommended first use case (it reuses the evidence and interview notes) |
| Governance or security below 3 | `ai-governance-program` for policy, register, tool tiers, training |
| ADM exposure yes or unknown | `ai-compliance-risk` (ADM mapping); the ADM transparency sprint package in `ai-proposal-pricing` |
| Any tier 3 candidate | `ai-compliance-risk` screen before design |
| Wait | Fix the P1 items; offer a re-assessment of the blocked dimensions only |
| XL rollout | `ai-enterprise-rollout` |

Log the action to your own engagement activity log.
`[YYYY-MM-DD HH:MM] [CLAUDE_CODE:<operator>] READINESS | client | band, gate result | outcome`.

## Use in a sales conversation

The research gives three honest framing points (all with their caveats, research file B1 and
headlines): MIT NANDA 2025 found 95% of organisations got zero measurable return from GenAI
pilots, a pilot-to-P&L measure on a small sample, citing systems that do not learn as the cause;
McKinsey found workflow redesign has the biggest effect on EBIT impact; IBM 2026 found about two thirds of
breached organisations lacked AI governance policies. Use them to explain why readiness comes
first, quoted with their caveats, never as "95% of AI projects fail".

## Files

| File | Holds |
|---|---|
| `references/dimensions-rubric.md` | Seven dimensions, 1-5 descriptors, six-practice and ADM scoring |
| `references/gates.md` | Organisation and use-case Go/Wait rules, action ranking |
| `references/evidence-checklist.md` | Evidence to request per dimension |
| `references/interview-guides.md` | Interview questions per function, tagged by dimension |
| `references/size-band-scaling.md` | S to XL method differences |
| `references/vendored-provenance.md` | Credits for adapted MIT, Apache and CC BY material |
| `templates/readiness-input-template.json` | Input schema with a fictional sample |
| `templates/readiness-report-template.md` | Full client report |
| `templates/executive-summary-template.md` | One-page summary |
| `scripts/readiness_score.py` | Scorer and gate (stdlib only) |
