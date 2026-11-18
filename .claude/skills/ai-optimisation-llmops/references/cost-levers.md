# Cost levers

*v0.1.0, 2026-11-08. Used at step 4 of the loop. **Pricing rule:** the only vendor pricing
statements the practice may repeat are the ones quoted below, with their source and the date they were
checked. For anything else (other vendors, cache write pricing, per-model rates, Bedrock, Azure or
Vertex equivalents) write "check the vendor's pricing page live" or `PENDING_VERIFICATION`. Lever
list adapted from harvested alirezarezvani `llm-cost-optimizer` (MIT); its percentage savings
claims are **not** adopted because they are unsourced.*

## Pricing statements on file

| Statement (as recorded in research) | Vendor | Source | Checked |
|---|---|---|---|
| Batch API: 50% discount on all tokens, results within a 24-hour window | Anthropic (direct API) | https://platform.claude.com/docs/en/about-claude/pricing and https://platform.claude.com/docs/en/build-with-claude/batch-processing.md, via Internal web research B6 | 2026-11-08 (research file date; "verified on pricing docs via search") |
| Prompt caching: cache reads at 10% of the base input rate; 5-minute and 1-hour cache durations | Anthropic (direct API) | Same pricing page, research B6 | 2026-11-08 |
| Batch and caching discounts stack | Anthropic (direct API) | Research B6 | 2026-11-08 |

Re-check the live page before these appear in a client deliverable if the row is more than
60 days old (conventions s3). Cache **write** pricing is not in the research: check live. Whether
the same discounts apply through AWS Bedrock (the practice's default route for Australian residency) is
`PENDING_VERIFICATION`.

## Levers (measure first, then pick one per cycle)

| Lever | When it fits | How to prove it | Risk |
|---|---|---|---|
| **Instrument first** | No per-feature or per-step cost breakdown | n/a: one period of data before any other lever | None; it is the precondition |
| **Model routing** | One model serves easy and hard tasks alike (llm-cost-optimizer calls this monoculture) | Golden set split by difficulty; cheaper model must meet thresholds on the easy split | Quality drop on misrouted cases: route on low confidence to the stronger model or a human |
| **Prompt caching** | Long, stable prefix (system prompt, policies, tool definitions, shared documents) sent on every call | Cache share and cost per task in `cost_trend.py` before and after; same eval scores | Cache invalidation by small prefix changes; check provider rules live |
| **Batch processing** | Work that can wait (overnight document processing, bulk classification, monthly evals themselves) | Turnaround still meets the business need; cost per task drop | Results not immediate; not for live chat |
| **Output length limits** | `max_tokens` not set per endpoint; verbose outputs | Output tokens per task down; eval scores steady | Truncated answers: test |
| **Context trimming** | Too many retrieved chunks or long histories | Input tokens per task down; faithfulness steady | Lost context: test retrieval recall |
| **Workflow step removal** | AI steps that duplicate a human or another AI step | Fewer calls per task; outcome unchanged | Removing a control by accident: check the agent control spec |
| **Distillation or a small open model** | High-volume, narrow, stable task | Separate project via `ai-model-customisation`; not a monthly change | Hosting cost and ownership move to the client |

## Proactive flags (from llm-cost-optimizer, re-worded)

Raise without being asked: no per-feature cost breakdown; every request on one model; a long
system prompt sent on every request with no caching; no output length limit per endpoint; no
cost alert configured; free or low-value traffic on the most expensive model.

## How savings are reported

From the data only: cost per task this month vs last month and vs baseline, from `cost_aud` in
the usage export, with volume shown beside it. Never "you saved X%" from a vendor discount rate:
the realised change depends on the client's traffic and is measured, not assumed.
