# Vendored provenance: ai-compliance-risk

*v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and
pinned commit. SHAs from `~/ai-kb/vendor/_harvest-manifest-2026-11-08.json`. Department-wide
list: `../../_shared/VENDORED.md` (maintained by ai-manager).*

| Used in (this skill) | Harvested file (upstream, under `~/ai-kb/vendor/<owner>__<repo>/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| `scripts/ai_risk_register.py` (in this skill) | `~/ai-kb/vendor/alirezarezvani__claude-skills/ra-qm-team/skills/iso42001-specialist/scripts/ai_risk_register_builder.py` | alirezarezvani/claude-skills | MIT (c) 2025 Alireza Rezvani | 8f082544116fc0d014188e521ca40304cdfc86b0 | **Adapted code.** 5x5 thresholds and treatment heuristics kept; MIT header and attribution kept in the file; DDD rating labels, owner, residual, tier-minimum check, seed mode, CSV/MD output added; Annex A catalogue removed |
| Method notes (ISO 42001 clause structure context) | `~/ai-kb/vendor/alirezarezvani__claude-skills/ra-qm-team/skills/iso42001-specialist/references/iso42001_clauses.md` | alirezarezvani/claude-skills | MIT | 8f082544116fc0d014188e521ca40304cdfc86b0 | Read for structure; not copied |
| Considered, not used | Upstream, under `~/ai-kb/vendor/alirezarezvani__claude-skills/`: `c-level-advisor/skills/chief-ai-officer-advisor/scripts/ai_risk_classifier.py` and `ra-qm-team/skills/eu-ai-act-specialist/*` | alirezarezvani/claude-skills | MIT | 8f082544116fc0d014188e521ca40304cdfc86b0 | US-state and EU-centric classifier; our tiers are AU-first. EU Article lists in it were not cross-checked against the research, so not used |
| `references/screening-questionnaire.md` (in this skill) | `~/ai-kb/vendor/canada-ca__aia-eia-js/src/survey-enfr.json` (Algorithmic Impact Assessment) | canada-ca/aia-eia-js | MIT (c) 2019 Government of Canada | b62573389db4946b4d70b7fa62c4ca8d9990dba3 | **Structure adapted**: raw-impact vs mitigation split, impact dimensions, point pattern. Questions rewritten for Australian private-sector use; Canadian specifics dropped; level thresholds are DDD's own (the AIA's are in code not harvested) |
| `references/risk-catalogue.md`, seed list in the script (both in this skill) | Upstream, under `~/ai-kb/vendor/cosai-oasis__secure-ai-tooling/risk-map/yaml/`: `risks.yaml`, `controls.yaml`, `frameworks.yaml` | cosai-oasis/secure-ai-tooling | Apache-2.0 | 622605a13fafaa2784acbdbe3f8d23ee22da4be7 | Risk IDs, titles, categories and CoSAI's own OWASP/ATLAS/NIST mappings listed as data; descriptions paraphrased, not copied |
| `references/threat-model.md` (in this skill) | Upstream, under `~/ai-kb/vendor/mitre-atlas__atlas-data/`: `dist/ATLAS-latest.yaml` (harvested as a 20-byte pointer stub only) and `dist/v6/ATLAS-2026.10.yaml`, fetched from GitHub at the same commit on 2026-11-08 and now on disk (the folder holds 4 files; manifest corrected 2026-11-08) | mitre-atlas/atlas-data | Apache-2.0 (c) 2021-2026 MITRE | f56c1468731d6428e5bf875263b4643b46d67437 | Tactic, technique and mitigation IDs and names. File sha256 ac41ee9f99a47084ba5fdfc77ae83a28687e12390240fffeb37df7914ffe142d. Re-harvest of `dist/v6/` into the vendor folder is **done** (2026-11-08): `dist/v6/ATLAS-2026.10.yaml` and `dist/v6/ATLAS-latest.yaml` are on disk |
| Skimmed for cross-checks | Upstream, under `~/ai-kb/vendor/Sushegaad__Claude-Skills-Governance-Risk-and-Compliance/`: `plugins/nist-ai-rmf/skills/nist-ai-rmf/SKILL.md`, `plugins/nist-ai-rmf/skills/nist-ai-rmf/references/rmf-profiles.md` and `plugins/iso42001/skills/iso42001/references/*` (upstream paths, not files in this skill) | Sushegaad/Claude-Skills-Governance-Risk-and-Compliance | MIT (c) 2026 Hemant Naik | 5a9afcfce98efa4d64f75bead5e544ee06c38154 | Read only. Used to detect that two harvested sources number ISO 42001 Annex A controls differently (e.g. A.5.2 is "AI system impact assessment" in alirezarezvani, "AI risk assessment" in Sushegaad). DDD therefore cites no Annex A IDs |

## Non-harvested sources used (primary, fetched 2026-11-08)

| Source | Used for |
|---|---|
| NIST AI 600-1, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf (US government work) | The 12 GenAI risk names in `risk-catalogue.md` and the seed list |

## Cited by ID only (CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/, nothing copied)

- OWASP Top 10 for LLM Applications 2025 (LLM01 to LLM10)
- OWASP Top 10 for Agentic Applications 2026 (ASI01 to ASI10)

ID-to-short-name pairs are taken from the Internal web research file, not from OWASP pages.
