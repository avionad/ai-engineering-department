# The eval-first gate

*v0.1.0, 2026-11-08. Adapted from wshobson/agents `plugins/llm-finetuning/skills/eval-harness-first/SKILL.md`
and `agents/llm-finetuning-architect.md` (MIT, SHA in `vendored-provenance.md`). The structure (gate
token, flywheel, golden building, one grader per failure bucket, judge calibration, directory
contract, exit checklist) is theirs; the client-engagement framing, the prompting-plus-RAG baseline
and the practice's sign-off are ours. Numeric floors below are wshobson's working conventions, not research
findings: treat them as defaults to adjust with evidence.*

## 1. Why the gate exists

Without a measured baseline there is nothing to compare a tuned model against, nothing to catch
regressions, and no labelled data to train on. "The model seems better" is not a finding. For a
client engagement the gate also protects the client from paying for training that a better prompt
or retrieval would have made unnecessary.

**House rule:** the baseline is run on the **strongest practical non-customised option**, not just
the untuned open-weight base model: (a) a capable hosted model in the approved region with the best
prompt we can write, and (b) the same plus retrieval or tools where the gap is knowledge. Only if
both miss the client's agreed target does customisation proceed. Then the untuned open-weight base
model is also baselined, because that is what the checkpoint will be compared against.

## 2. The flywheel

1. Collect traces: real cases from the client's process (emails, tickets, documents, transcripts),
   or synthetic tasks where none exist yet.
2. Error analysis: read at least 100 traces, tag failures in plain words (open coding), then group
   the tags into 4 to 8 named failure buckets (axial coding). Single-surface tasks (for example
   strict schema extraction) may have 1 or 2 buckets with per-field sub-metrics.
3. One grader per bucket: deterministic first (regex, schema validation, execution, exact match),
   an LLM judge only for genuinely subjective criteria (tone, faithfulness, "which is better").
4. Prioritise buckets by frequency x severity x business value.
5. Labelled traces become training data, minus an explicit holdout: every golden ID is excluded
   from training by ID.
6. Train (only after the gate).
7. Re-run the **same** harness on the checkpoint, never a looser one.
8. Production drift re-opens error analysis.

## 3. Goldens

- From real traces where they exist; synthetic generation by enumerating dimensions (task type,
  difficulty, edge case, persona) and sampling the combinations, because free-form generated
  prompts cluster around the easy cases.
- Versioned like code (`eval/goldens.jsonl`), reviewed by a named client subject-matter owner,
  tagged per release, doubling as the regression suite.
- Personal information in goldens follows the same rules as training data
  (`training-data-and-privacy.md`).

## 4. Graders

- One per failure bucket, so a regression in one bucket cannot hide in a blended score.
- Binary pass/fail over 1-5 scales: easier to calibrate and apply consistently.
- For general capability checks prefer log-probability scoring over generate-and-extract where the
  harness supports it (generate-and-extract confuses format compliance with knowledge).

## 5. Judge calibration (only when a bucket uses an LLM judge)

- Label at least 100 items by hand; split into train, dev and a sealed test set reported once.
- Report true-positive and true-negative rates separately, not one accuracy figure (a judge that
  always says "pass" scores well on a skewed set).
- Pin the judge to a fixed model snapshot; recalibrate when the judge model changes, and quarterly.
- The judge comes from a different model family than the model under test.
- A judge that misses the agreed bar is advisory only: it flags items for human review and never
  gates a promotion.
- If no bucket uses a judge, write "N/A, all graders deterministic" rather than leaving it blank.

## 6. Directory contract (in the sandbox repo for the engagement)

```
eval/
  goldens.jsonl            labelled traces + synthetic goldens, versioned
  graders/                 one module per failure bucket
  drift-suite.yaml         frozen general-capability items + 200-500 domain-adjacent items
  baseline-<name>.json     gate tokens: one per baselined option (hosted+prompt, hosted+RAG, base model)
runs/
  <run-id>/results.json    per-run output, one per checkpoint
```

`eval/` persists across runs; run scripts never write into it. `runs/` is disposable.

## 7. Phase 0 exit checklist (all true, or a stated N/A)

1. At least 100 traces open-coded; 4 to 8 failure buckets (or the single-surface exception).
2. `eval/goldens.jsonl` committed, versioned and signed off by the client's subject-matter owner.
3. One grader per bucket, deterministic first.
4. Judges calibrated, or "N/A, all deterministic".
5. Drift suite frozen.
6. Baselines written for hosted+prompt, hosted+RAG (where relevant) and the untuned base model.
7. **Target agreed in writing with the client owner, and the baseline shows the non-customised
   options miss it.** (House addition.)

Missing any item: the gate is closed. Record it in the go/no-go template.

## 8. Promotion gate (after training)

Adapted from wshobson `checkpoint-promotion`. A checkpoint ships only after:

1. **Data-quality check**: training set de-duplicated, no golden leakage, label noise scanned.
2. **Held-out and drift suite** re-run and compared with the base-model baseline. wshobson's drift
   budget: 1 point or less is noise; 2 to 5 points means rerun with seed variation before deciding;
   more than 5 points is a hard fail regardless of task gains. Report the uncertainty (half-width)
   with every verdict; a margin smaller than it is "reject (uncertain)".
3. **Paired comparison** against the base model and against the hosted+prompt option on the same
   prompts (position-randomised if judged). A held-out win that loses the paired comparison does
   not ship.
4. **Canary** for production traffic: a small stratified share with automatic rollback.
5. **Client owner approval** of the comparison report (House addition; stage 7 rule).

Terminal verdict: PROMOTE or REJECT, with evidence and one top remediation on REJECT. Forgetting
mitigation (general-data replay, lower learning rate, fewer epochs, smaller rank) and the reasoning
behind the budget are in the harvested `checkpoint-promotion` references at the pinned SHA.
