# Vendored provenance: ai-discovery-scoping

*Harvest sources are read-only copies in a local vendor mirror (`ai-kb/vendor/`), pinned per
its harvest manifest. The department-wide register is
`_shared/VENDORED.md` (owned by the lead). Nothing below was copied verbatim at length; all
material was adapted and rewritten.*

| Repo | Licence | Pinned SHA | File (upstream, under `~/ai-kb/vendor/<owner>__<repo>/`) | What was adapted | Where |
|---|---|---|---|---|---|
| anthropics/financial-services | Apache-2.0 | `60565064557ca77b12f62aa7877f365d111c129d` | `plugins/vertical-plugins/private-equity/skills/ai-readiness/SKILL.md` | The three gate questions (is the data there, is there an owner, can we pilot in 30 days) with Go/Wait; ranking by impact, speed to value and probability; the "what we are not doing" list; "failed pilots are signal". Generalised from PE portfolio companies to a single client's use cases. Deliberately NOT adopted: "assume 30-50% FTE-hours saved" (an unsourced multiplier, conflicts with DDD's client-numbers-only rule) and EBITDA framing. | `references/use-case-qualification.md`, SKILL.md step 4 |
| alirezarezvani/claude-skills | MIT | `8f082544116fc0d014188e521ca40304cdfc86b0` | `c-level-advisor/skills/chief-ai-officer-advisor/SKILL.md` | Idea only: "what happens when the model is wrong" and "if no eval set, no ship" as discovery questions; build-vs-buy decision order as a pushback rule. Its embedded API and GPU prices are illustrative and unverified: not used. | `references/question-bank.md` s6, SKILL.md pushback |
| github/ai-adoption-playbook | CC BY 4.0 | `95c00131a3a88bf5c7df737b6676d2038e821fcf` | `github_ai_playbook.md` | Tiered tool policy (vetted tools for confidential data, unvetted tools for public data only), advocates network, communities of practice, dedicated program owner, as components of pattern P10. Attribution: "How to build an AI-powered workforce: GitHub's playbook", GitHub, licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); adapted and summarised. | `references/solution-patterns.md` P10 |

DDD-internal sources (not vendored, no licence issue): `odoo-discovery-scoping` house style
(facts before promises, time cost in the client's words, delivery buckets); Matthew's Timber
transcript 2026-10-30; `DDD Clients/Projects/ai-receptionist/CLAUDE.md`.
