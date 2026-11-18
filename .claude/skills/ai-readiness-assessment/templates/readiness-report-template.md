Audience: client ({Client} leadership). Passes a client-facing tone review before it ships.

# AI readiness assessment: {Client}

*{Month YYYY}. Prepared by {your practice}. File as
`{client}/reports/adhoc-report/ai-readiness-assessment-{YYYY-MM-DD}.md` and render to .html and
.pdf with `tools/report-renderer/render_report.py`. Every number in this report traces to the
scorecard input or the client's own figures; R2 verifier in `scripts/verifiers/`.*

## 1. Summary

Two or three sentences: the result (Go / Go with conditions / Wait), the single biggest reason,
and the first thing to do. Then:

| | |
|---|---|
| Result | {Go / Go with conditions / Wait} |
| Recommended first use case | {name, or "none yet: see section 5"} |
| Most urgent action | {action and why it is urgent} |
| Assessment scope | {who we spoke to, what we reviewed, dates} |

## 2. Scorecard

Paste the scorecard table from `readiness_score.py`. Under it, one sentence per dimension that
explains the score in the client's terms, citing what we saw or were told. Name low-confidence
scores and what would firm them up.

## 3. Governance and compliance position

- Six practices of the Guidance for AI Adoption (voluntary guidance from the National AI Centre,
  October 2025): status table from the scorecard, with one line each on what exists today.
- Automated decision-making disclosure (Privacy Act APP 1.7 to 1.9, in force from 10 December
  2026 for organisations covered by the Privacy Act): exposure, what has been done, what remains.
- Sector obligations, if any (from `_shared/regulatory-register.md`; each with its status: in
  force, commencing later, proposed or voluntary).

> This assessment identifies regulatory considerations for review by your legal adviser. It is
> not legal advice.

## 4. Top risks

Rank by business impact, not by dimension order. Three to five risks, each with: what we
observed, why it matters, what to do. A tracking or evidence gap is described as a gap, not as
poor performance.

| # | Risk | What we observed | Why it matters | Action |
|---|---|---|---|---|
| 1 | | | | |

## 5. Recommended first use cases

From the use-case gate. For each Go candidate: the problem, the value in the client's own numbers
(or "to be measured during discovery" where a figure is still missing), the owner, the risk tier,
and the next step (discovery and scoping). For Wait candidates: what would unblock them. Include
the "not doing now" list with reasons.

## 6. 90-day action plan

The ranked plan from the scorecard (P1 prerequisites, P2 foundations, P3 first use cases), each
with an owner on the client side, a target month and what "done" looks like. P4 items listed as
"after 90 days".

| # | Action | Owner | Target | Done looks like |
|---|---|---|---|---|
| 1 | | | | |

## 7. Method

Seven dimensions scored 1 to 5 against a published rubric, with evidence recorded for each score;
Go/Wait gates for the organisation and for each use case. Size band {S/M/L/XL} method: {what we
did}. Rubric adapted from open-source work credited in the appendix.

## Appendix

- A. Evidence register (item, dimension, seen or stated, date)
- B. People interviewed (roles)
- C. Credits: rubric adapted from OneWave AI's ai-readiness-assessment (MIT licence); gate method
  adapted from Anthropic's financial-services ai-readiness skill (Apache 2.0); adoption practices
  from "How to build an AI-powered workforce: GitHub's playbook" (CC BY 4.0).
