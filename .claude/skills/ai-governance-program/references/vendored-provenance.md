# Vendored provenance: ai-governance-program

*v0.1.0, 2026-11-08. SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`.
Department-wide list: `../../_shared/VENDORED.md` (maintained by ai-manager).*

| Used in (this skill) | Harvested file (upstream, under `ai-kb/vendor/<owner>__<repo>/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| `scripts/iso42001_readiness_gap.py` (in this skill) | `ai-kb/vendor/alirezarezvani__claude-skills/ra-qm-team/skills/iso42001-specialist/scripts/aims_gap_analyzer.py` | alirezarezvani/claude-skills | MIT (c) 2025 Alireza Rezvani | 8f082544116fc0d014188e521ca40304cdfc86b0 | **Adapted code.** Clause list, statuses and weights kept; MIT header and attribution in the file; reframed to readiness (not certification), DDD artefact and GfAA practice per gap, Markdown output |
| Crosswalk sub-clause references | `ai-kb/vendor/alirezarezvani__claude-skills/ra-qm-team/skills/iso42001-specialist/references/iso42001_clauses.md` | alirezarezvani/claude-skills | MIT | 8f082544116fc0d014188e521ca40304cdfc86b0 | Sub-clause numbers and titles (4.1 to 10.2), flagged unverified against the standard |
| Considered | Upstream, under `ai-kb/vendor/alirezarezvani__claude-skills/`: `compliance-os/skills/aims-audit/SKILL.md` and `c-level-advisor/skills/chief-ai-officer-advisor/references/ai_risk_governance.md` | alirezarezvani/claude-skills | MIT | 8f082544116fc0d014188e521ca40304cdfc86b0 | Read for checklist ideas (scope must name vendor AI; policy must commit to human oversight). US-state and EU material not used |
| Crosswalk NIST categories | Upstream, under `ai-kb/vendor/Sushegaad__Claude-Skills-Governance-Risk-and-Compliance/plugins/nist-ai-rmf/skills/nist-ai-rmf/`: `SKILL.md` and `references/rmf-profiles.md` (upstream paths, not files in this skill) | Sushegaad/Claude-Skills-Governance-Risk-and-Compliance | MIT (c) 2026 Hemant Naik | 5a9afcfce98efa4d64f75bead5e544ee06c38154 | NIST AI RMF category numbering (GOVERN 1-6, MAP 1-5, MEASURE 1-4, MANAGE 1-4). Its NIST-to-ISO Annex A mapping was **not** used because its Annex A numbering conflicts with alirezarezvani's |
| Crosswalk (control titles) | `ai-kb/vendor/cosai-oasis__secure-ai-tooling/risk-map/yaml/controls.yaml` | cosai-oasis/secure-ai-tooling | Apache-2.0 | 622605a13fafaa2784acbdbe3f8d23ee22da4be7 | Control names referenced for incident response and governance controls |

Government templates (NAIC AI policy guide and template, AI register template, AI screening tool;
AU-4) were **not retrieved**: the download timed out on 2026-11-08. Nothing from them is copied;
alignment is `PENDING_VERIFICATION`.
