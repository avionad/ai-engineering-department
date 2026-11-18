# Drift detection and model migration

*v0.1.0, 2026-11-08. Standing watches in `ai-optimisation-llmops`. Sources: web research B6
(drift signals; model retirement as a drift source; pin versions and plan migrations) and B4
(Azure Australia East model availability lags US regions, continuity planning needed when models
retire).*

## 1. Drift signals (check every cycle)

| Signal | What it means | Source | Watch for |
|---|---|---|---|
| Input distribution | The work the system receives has changed (new intents, products, policies, languages, longer inputs) | Traces: intent or category tags, input length, language | New clusters of requests the golden set does not cover |
| Output quality sample | Answers getting worse on real traffic even if the golden set passes | Monthly human review of a random sample plus the worst cases | Faithfulness or correctness falling on the sample |
| Feedback | Users unhappy or overriding more | Thumbs plus reason, overrides, edits | Override or negative feedback rate rising |
| Retrieval hit rate | Retrieval finding less, or the wrong things | Retrieval scores, empty results, citation clicks | More "no answer" or low-score retrievals |
| Cost and latency per task | System doing more work per task | `cost_trend.py`, traces | Tokens per task creeping up; latency rising |
| Safety incidents | Policy breaches, leaks, injections seen in production | Incident log, guardrail logs | Any occurrence: incident process, not just the monthly report |
| Source freshness | The documents or data the system relies on changed or went stale | Index build dates, source change logs | Index older than the agreed refresh interval |

## 2. Responding to drift

- **Coverage drift** (new kinds of input): add items to the golden set first, then decide if a
  change is needed.
- **Quality drift on the same inputs**: check the change log (vendor model update, our change,
  source documents) before touching prompts.
- **Content drift**: the client's content owner fixes or refreshes the source; re-index; re-run
  retrieval evals.
- **Tracking drift** (logs changed): fix logging before drawing conclusions.

## 3. Model deprecation and version migration watch

Models are retired on vendor schedules. A pinned version that is retired breaks the system or is
silently replaced, either of which invalidates the baseline.

**Every cycle:**

1. Keep a model inventory per system: provider, platform (Anthropic direct, Bedrock profile,
   Azure deployment, Vertex), model ID and version, region, judge models used in evals, embedding
   models used in retrieval.
2. Check each provider's deprecation or retirement page **live** and record: status, announced
   retirement date, recommended replacement, the URL and the date checked. Never record a date
   from memory.
3. For Australian residency, also check the replacement is available in the required region or
   inference profile (research B4: newer models can reach US regions first).
4. Flag in the report any retirement inside the planning horizon agreed with the client (DDD
   suggestion: raise it at least two cycles ahead so testing and approval fit).

**Migration as a change set:**

1. Run the full golden set on the candidate model in staging; run `eval_compare.py` against the
   current reference.
2. Re-run red-team families F1 to F5 (and F6, F7 for agents): safety behaviour changes between
   models.
3. Re-calibrate any LLM judge if the judge model changes.
4. Compare cost per task and latency on a replay of masked production samples.
5. Compliance check if provider, platform or region changes (vendor due diligence, residency).
6. Client approves; deploy; the new run becomes the reference baseline (old one kept).

Embedding model changes need a full re-index and retrieval re-test; schedule them as their own
change set.
