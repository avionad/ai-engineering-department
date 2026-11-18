# Vendored provenance: ai-use-case-portfolio

*v0.1.0, 2026-11-08. SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`.
Department-wide list: `../../_shared/VENDORED.md` (maintained by ai-manager).*

| Used in (this skill) | Source file (upstream, under `ai-kb/vendor/<owner>__<repo>/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| Gates and ranking (via `ai-discovery-scoping/references/use-case-qualification.md`) | `plugins/vertical-plugins/private-equity/skills/ai-readiness/` | anthropics/financial-services | Apache-2.0 | 60565064557ca77b12f62aa7877f365d111c129d | Indirect: this skill reuses the qualification file, which adapted the three gate questions and ranking idea. Nothing copied here directly |
| `scripts/portfolio.py` | none | DDD | DDD own | n/a | Written from scratch; no harvested code |
| `references/intake-form.md`, `benefits-tracking.md` | none | DDD | DDD own | n/a | DDD design. Measurement principles from the Internal web research file (B1 step 7), which cites Microsoft, Gartner, McKinsey and NAIC sources |

Considered, not used: alirezarezvani/claude-skills `chief-ai-officer-advisor` cost calculators
(MIT, `8f082544116fc0d014188e521ca40304cdfc86b0`). They embed illustrative USD prices and
benefit assumptions; DDD's portfolio uses only client-supplied numbers, so nothing was taken.
GitHub research area 8 found no credible open use-case prioritisation tool (all under 5 stars).
