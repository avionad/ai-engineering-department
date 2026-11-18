# Vendored provenance: ai-solution-architecture

*v0.1.0, 2026-11-08. SHAs from `~/ai-kb/vendor/_harvest-manifest-2026-11-08.json`.
Department-wide list: `../../_shared/VENDORED.md`.*

| Used in (this skill) | Harvested file (upstream, under `~/ai-kb/vendor/<owner>__<repo>/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| `references/build-vs-buy.md` (a file in this skill) | Upstream, all under `~/ai-kb/vendor/alirezarezvani__claude-skills/c-level-advisor/skills/chief-ai-officer-advisor/`: `references/model_buildvsbuy_strategy.md`, `references/ai_cost_economics.md`, `scripts/model_buildvsbuy_calculator.py` | alirezarezvani/claude-skills | MIT (c) 2025 Alireza Rezvani | 8f082544116fc0d014188e521ca40304cdfc86b0 | **Approach adapted**: multi-year TCO per path from a workload profile; hidden-cost categories on both sides (headings paraphrased); eval-first rule. **Not used**: every price, threshold, benchmark and team-size figure (illustrative USD values, unsourced for DDD clients); no code copied |
| Method step 2 (ladder) | DDD agent `~/.claude/agents/ai-architect.md` and Internal web research B3 | DDD | DDD own | n/a | The ladder is the agent's method step 2, expanded |

## Live DDD skills referenced (not vendored)

| Skill | Relationship |
|---|---|
| `product/documentation-and-adrs` (vendored by DDD from addyosmani/agent-skills, MIT) | ADR conventions inside code repositories; this skill's ADR template is DDD's own consultancy format and does not copy it |
| `product/app-stack-decision` | Stack and hosting for any app with a UI |
| `product/product-builder`, `n8n/n8n-architect` | Build hand-offs |

## Considered, not used (licences verified live 2026-11-08)

Neither repo was harvested and nothing was copied from either. Both licences were checked this
session against the GitHub API and the repo LICENSE file, replacing the earlier second-hand
statement from the Internal GitHub research file.

| Repo | Licence as verified 2026-11-08 | Source checked | Why not used |
|---|---|---|---|
| codenamev/ai-software-architect | **No licence at all.** `https://api.github.com/repos/codenamev/ai-software-architect/license` returns HTTP 404 "Not Found" and the repository record reports `"license": null`; a listing of the repository root (`/contents/`) shows no LICENSE file. With no licence granted, all rights are reserved: **reference only, never copy, never vendor** | https://api.github.com/repos/codenamev/ai-software-architect/license and .../contents/ , checked 2026-11-08 | ADR framework idea only; DDD's ADR template is its own consultancy format |
| tractorjuice/arc-kit | **MIT with two carve-outs**, from the LICENSE file's own leading note: the MIT grant does **not** extend to `plugins/arckit-uk-gcloud/` (proprietary, licensed separately) and the adapted arc42 template plus Q42-derived quality material are **CC BY-SA 4.0** (https://creativecommons.org/licenses/by-sa/4.0/), not MIT. MIT portion is Copyright (c) 2025 Mark Craddock. The GitHub licence API reports SPDX `NOASSERTION` because of the carve-outs | https://raw.githubusercontent.com/tractorjuice/arc-kit/main/LICENSE and https://api.github.com/repos/tractorjuice/arc-kit/license , read 2026-11-08 | Not harvested. If it is ever used, the CC BY-SA 4.0 share-alike duty on the arc42 and Q42 material has to be assessed first |
