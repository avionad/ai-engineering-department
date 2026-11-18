# Vendored provenance: ai-enterprise-rollout

*v0.1.0, 2026-11-08. SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`.
Department-wide list: `../../_shared/VENDORED.md`.*

## Attribution (CC BY 4.0, required)

Parts of this skill are adapted from **"How to build an AI-powered workforce: GitHub's playbook"**
by GitHub, https://github.com/github/ai-adoption-playbook (commit
`95c00131a3a88bf5c7df737b6676d2038e821fcf`), licensed under the Creative Commons Attribution 4.0
International License, https://creativecommons.org/licenses/by/4.0/. **Changes were made**: the
material was summarised, rewritten in Australian English, extended (a third tool tier for
sensitive data, Australian regulatory considerations, risk measures, the practice gates and templates) and
combined with other sources. GitHub does not endorse the practice or this skill.

Any client deliverable that reproduces adapted playbook content (for example the champions
section of a rollout plan) carries a one-line credit: "Adapted from GitHub's AI adoption playbook
(CC BY 4.0), with changes."

| Used in (this skill) | Harvested file (upstream, under `ai-kb/vendor/<owner>__<repo>/`) | How used |
|---|---|---|
| `references/rollout-phases.md` s1, s2 | `github_ai_playbook.md` (policies and tooling; dedicated program leadership) | Program owner role ("enabler, not a gatekeeper"), two-tier tool policy and its one-line rule (quoted), tool request intake. Adapted; short quotes marked |
| `references/people-and-change.md` s1-s3 | `github_ai_playbook.md` (executive support, advocates, communities of practice, learning and development) | Volunteer recruitment, champion functions and support, communities, curate-not-build training, "don't say your job is safe" (quoted) |
| `references/measurement.md` s2, s3 | `github_ai_playbook.md` (metrics: breadth, depth, business impact; MAU, MEU, segmentation 10+ / 2-9 / 1 days) | Phasing and segmentation defaults, adapted |
| `templates/rollout-plan.md` 90-day table | `github_ai_playbook.md` (strategic checklist, first 30 and 90 days) | Structure adapted and merged with research B1 and the practice gates |

## Other sources

| Source | Licence | Commit | Used for |
|---|---|---|---|
| Internal web research 2026-11-08, section B1 | The practice | n/a | Microsoft adoption phase names and playbook emphasis, Microsoft CAF phases, Gartner 26 May 2026 tiered governance, McKinsey workflow-redesign finding, IBM 2026 shadow AI figures, the B1 platform-control list and measure list |
| `_shared/regulatory-register.md` rows AU-6, AU-8, AU-11, AU-15, AU-21, AU-24 | The practice | n/a | Consultation and workplace considerations table |

The `pillar_docs/` deep-dives **are on disk** (7 files at
`ai-kb/vendor/github__ai-adoption-playbook/pillar_docs/`: `advocates.md`,
`communities_of_practice.md`, `dri.md`, `exec_support.md`, `policies_and_guardrails.md`,
`right_fit_tooling.md`, `training.md`), so they were harvested, but they were **not read or mined**
for v0.1.0. Every adapted passage above traces to the main
`ai-kb/vendor/github__ai-adoption-playbook/github_ai_playbook.md`, which covers the advocates
network, communities of practice, the DRI role and the two-tier tool policy in full. A v0.2 pass
should mine the deep-dives for the champions and training sections. Reconciled with
`../../_shared/VENDORED.md` and `../../ai-readiness-assessment/references/vendored-provenance.md`
on 2026-11-08.

Considered, not used: adimango/ai-adoption-playbook (MIT) was listed in GitHub research area 8
but not harvested; nothing taken from it.
