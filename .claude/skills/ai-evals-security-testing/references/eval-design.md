# Eval design: golden set, test types, thresholds, baseline, regression

*v0.1.0, 2026-11-08. Method step 2 of `ai-evals-security-testing`. Sources: research B6 (evals
first, golden sets, regression on every prompt or model change, LLM-as-judge calibrated against
human labels); Azure-Samples evaluation guide (MIT, ground truth review and hidden rate limiting);
`../../ai-model-customisation/references/eval-first-gate.md` (judge calibration protocol). RAG
metrics are owned by `../../ai-rag-engineering/references/retrieval-and-evaluation.md` s6 and are
not repeated here.*

## 1. The golden set

A golden set is a versioned list of inputs with the expected behaviour, built from the client's
real work. It is the single reference every later change is measured against.

**Where items come from (in this order):**

1. Real examples the client gives us with permission: the discovery examples, helpdesk tickets,
   emails, forms, documents, call notes. Record the permission (who, date) in the test plan.
2. Edge cases the subject-matter owner names ("the ones that trip new staff up").
3. Failures found in production by the monthly loop (`ai-optimisation-llmops` adds them).
4. Synthetic items to fill coverage gaps only. The Azure sample generates synthetic questions and
   then has a human remove unrealistic ones; follow that rule: no synthetic item enters the set
   without human review, and synthetic items never outnumber real ones in a category.

**Masking.** Any item holding personal or confidential information is masked before it leaves
the client's environment or enters a tool not covered by the data-handling agreement. Use
Presidio with the Australian recognisers per
`../../ai-rag-engineering/references/pii-redaction-presidio.md` (AU_ABN, AU_ACN, AU_TFN,
AU_MEDICARE plus names, emails, phones) and consistent pseudonyms so the item still makes sense.
Masking is checked by a human on a sample before the set is used.

**Each item carries** (columns in `templates/golden-set-template.csv`): `test_id`, `category`,
`pattern`, `input`, `context_or_fixture`, `expected_behaviour`, `expected_answer_or_fields`,
`expected_sources`, `must_not`, `grader` (deterministic / llm-judge / human), `source` (real /
edge / production-failure / synthetic), `masked` (yes/no), `owner`, `added_on`, `set_version`.

**Coverage.** Every intent the system serves, every user role, every source system, unanswerable
or out-of-scope requests, and each High threat from the threat model. DDD v0.1 starting point
(uncalibrated, not an industry figure): at least 10 items per category before a baseline is
called, more where the risk tier is higher. Agree the final size with the client and record it.

**Held-out portion.** If prompts will be tuned against the set (including DSPy or GEPA in the
monthly loop), keep a held-out portion that is never used for tuning; report scores on it.

**Versioning.** The set lives in the engagement repo `evals/` and changes only by adding or
retiring items with a reason. Results always cite the set version.

## 2. Test types per pattern

| Pattern | What to measure | Typical grader |
|---|---|---|
| **RAG / knowledge assistant** | Retrieval recall at k, context precision, faithfulness, citation correctness, abstain correctness, permission leak (see `ai-rag-engineering` s6 and the permission-leak plan) | Deterministic for retrieval and citation match; calibrated judge or human for faithfulness |
| **Extraction / document processing** | Field-level accuracy per field (exact or normalised match), missing-field rate, wrong-field rate, format validity, handling of unreadable input (flag, never guess) | Deterministic against labelled fields |
| **Classification / triage / routing** | Accuracy per class, confusion between classes that matter (the costly mistakes), escalation of low-confidence cases | Deterministic |
| **Agents and automations** | Task success end to end, tool-use correctness (right tool, right arguments, right order), approval gates trigger where required, no forbidden tool calls, stops at caps, recovers or escalates on tool error | Trajectory checks plus outcome checks in a sandbox |
| **Chat / customer-facing** | Answer correctness on in-scope questions, refusal of out-of-scope and harmful requests, escalation to a human when the policy says so (complaints, vulnerability signals, legal or medical questions), AI disclosure where required, tone and format | Mix: deterministic for escalation triggers, calibrated judge for correctness and tone |
| **Generation (drafts, summaries)** | Factual consistency with the source, required elements present, prohibited content absent, length and format | Calibrated judge plus deterministic checks |

Prefer binary pass/fail per item over 1 to 5 scales (easier to calibrate and apply consistently,
per the eval-first gate). Use a score column only where a graded metric is genuinely needed.

## 3. Graders and judge calibration

- Deterministic graders first (exact match, normalised match, regex, schema, allow-list, tool-call
  assertions). They are cheap, repeatable and do not drift.
- An LLM judge may gate a metric only after calibration against human labels on a sample from
  this client's set, per `../../ai-model-customisation/references/eval-first-gate.md` s5. Pin the
  judge model version; recalibrate when it changes.
- The judge runs in a tool covered by the data-handling agreement, like the system itself.

## 4. Thresholds (set with the client, recorded)

There is no industry pass mark for "a good chatbot". Thresholds are a business decision made
with the client's accountable owner, per metric or category, informed by:

- what the current manual process achieves (from discovery, the client's own numbers);
- the cost of each kind of mistake (a wrong refund vs a slow answer);
- the risk tier and the human review design (a human checking every output tolerates more);
- the baseline itself (a first run tells you what is realistic for this build).

Record each threshold in the test plan and in `thresholds.json` with `agreed_by`, `agreed_on`
and a one-line reason. Some categories are **blocking**: any single failure fails the run
regardless of pass rate. Permission leak, PII leakage and agent approval-gate bypass are always
blocking (DDD rule, derived from the permission-leak plan and conventions s2 least agency).

`scripts/eval_compare.py` refuses to return PASS when `agreed_by` or `agreed_on` is missing.

## 5. Baseline

The baseline is the first full run that the client accepts as the reference. Record with it:
golden-set version, model ID and version (pinned), prompt version, retrieval index version,
guardrail config version, judge model and calibration date, run date, environment, and cost of
the run. The baseline CSV goes to `evals/results/{date}/` and its summary into the build notes
(`ai-engineer` output) and the test report.

Run the baseline more than once if graders or the model are non-deterministic and report the
spread; a single run can mislead.

**Latency caution (Azure sample):** SDK retries on HTTP 429 can hide throttling, so latency
comparisons are only valid when the logs for the run show no rate-limit retries. Note this in the
report when latency is a metric.

## 6. Regression rule

- Re-run the suite on **every** change to prompt, model or version, retrieval settings, index,
  guardrails, tools or workflow, and monthly in the retainer.
- **Regression** = an item that passed at the reference run and fails now. A regression blocks
  the change until fixed, or until the client's owner accepts it in writing with a reason
  (recorded in the change set).
- **New failure** = a new item that fails. It does not block on its own unless its category is
  blocking or the category falls below threshold; it becomes a finding.
- **Coverage drop** = items in the reference run missing from the current run. Treated as a
  condition: explain or restore.
- When the client accepts a new reference (after an approved change), the new run becomes the
  baseline and the previous one is kept, never overwritten.

## 7. Result CSV contract (for `eval_compare.py`)

Columns: `test_id`, `category`, `passed` (true/false, also accepts yes/no, 1/0, pass/fail),
`score` (optional, 0 to 1). Extra columns are ignored. One row per test. promptfoo results can be
exported and reshaped to this contract with a short script in the engagement repo.
