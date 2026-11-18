# DEFINITIONS: what is defined where

*v0.1.0, 2026-11-08. Owner: ai-manager. One page, one job: tell you which file owns each piece of
shared vocabulary in the `ai-automation` department, so no skill, agent or deliverable ever defines
it a second time. Written after a review found the department had built eleven numbering schemes
across sixteen skills with no map.*

**The rule for every row below: reference it, never restate it.** Cite the file and the token
(for example "Tier 3, conventions s6" or "class C4, data-class matrix s1") and move on. Do not copy
the table into your skill, your agent prompt or a client deliverable, and do not paraphrase a
definition into your own words. A restated definition is a second definition: it drifts, and then a
client gets two answers to the same question. If a definition is wrong or incomplete, change it in
the file that owns it and tell ai-manager, do not work around it locally.

**Where there is no definition, say so.** If you need a scale, a tier or a vocabulary that is not
below, it does not exist yet. Ask ai-manager to add it here and in its owning file, rather than
inventing one in your skill.

## 1. The map

| Vocabulary | Tokens | Canonical file | What it governs |
|---|---|---|---|
| **Risk tiers** | 1 Low, 2 Moderate, 3 High, 4 Prohibited / stop | `engagement-conventions.md` s6 | How much governance, review and testing a use case gets, and whether it may be built at all. Assigned by `ai-compliance-risk`, used by every skill |
| **Size bands** | S, M, L, XL | `engagement-conventions.md` s5 | The method, not just the volume: who decides, what governance is proportionate, whether SSO, landing zones and change management are in scope |
| **Finding severity** | Critical, High, Medium, Low | `engagement-conventions.md` s6a | What blocks a go-live and what is recorded with an owner and date. One scale for every skill and agent, including security findings and compliance findings |
| **Status vocabulary for a rule** | in force, commenced on a later date, proposed, voluntary | `engagement-conventions.md` s4 | How every statement about a regulation or standard is qualified. Never call voluntary guidance a requirement. Each register row carries its status in these words |
| **Department script contract** | the script table | `engagement-conventions.md` s6b | That all department scripts are stdlib-only, print to stdout, write a file only with `--out`, and that a non-zero exit is a finding to read rather than a crash. Exit codes per script live in that table, nowhere else. The table lists 8 scripts: 7 in skill `scripts/` folders plus `_shared/check_freshness.py` |
| **Delivery buckets** | `config-saas`, `integration-workflow`, `rag-knowledge`, `custom-agent-app`, `model-customisation`, `governance-compliance`, `change-training`, `discovery-measurement`, `run-ongoing` (9) | `../ai-discovery-scoping/references/delivery-buckets.md` | Which bucket a scope line belongs to, because each costs differently. **The slugs are enforced in code**: `../ai-proposal-pricing/scripts/estimate.py` rejects any bucket not in its `BUCKETS` list, so a renamed or invented slug fails the quote rather than quietly mispricing it. One line, one bucket |
| **Use-case ranking order** | value, then time to value, then feasibility, then risk tier | `../ai-discovery-scoping/references/use-case-qualification.md` (sub-scores s1, gate questions s2, ranking s3) | How candidates are ordered, plus the feasibility sub-scores (data, integration, complexity: take the lowest, not the average), the three gate questions and the practice's fourth gate (tier assigned and not 4). `../ai-use-case-portfolio` uses this same order; it does not define its own |
| **Human-in-the-loop tiers** | H1, H2, H3, H4 | `../ai-agents-automation/SKILL.md` | How much autonomy an automation or agent gets, and what the risk tier sets as the floor. Referenced by `ai-discovery-scoping` s4, the architecture design and the eval plan |
| **Data classes** | C0 Public, C1 Internal, C2 Confidential, C3 Personal, C4 Sensitive personal, C5 Highly restricted | `../ai-deployment-platforms/references/data-class-matrix.md` s1 | Which platforms and deployment types a flow may use. A flow takes the highest class of anything in it (prompt, retrieved context, output, logs) |
| **Platform conditions** | K1 to K9 | `../ai-deployment-platforms/references/data-class-matrix.md` s2 | The conditions attached to a "C" cell in the matrix. Numbered K deliberately so that no token means two things: **C is a data class, K is a condition** |
| **Security baseline controls** | B1 to B12 | `../ai-deployment-platforms/references/security-baseline.md` s1 | The minimum controls on every platform and engagement, and their per-platform mapping |
| **Golden-set rules** | the golden set itself, its item columns, source types (real / edge / production-failure / synthetic), masking, coverage, the held-out portion, versioning | `../ai-evals-security-testing/references/eval-design.md` s1 | What a golden set is, where items may come from and in what order, that no synthetic item enters without human review and synthetic never outnumbers real in a category, and that the set is versioned in the engagement repo. RAG retrieval metrics are **not** here: they belong to `../ai-rag-engineering/references/retrieval-and-evaluation.md` s6 |
| **Solution patterns** | P1 to P11 | `../ai-discovery-scoping/references/solution-patterns.md` | The reusable shapes a solution takes (document intake, support agent, knowledge agent, quote generation, decision support and so on), referenced by number across discovery, architecture and the use-case library |
| **Register row IDs** | AU-n, INT-n, EU-n, NZ-n | `regulatory-register.md` | Every regulation, standard and regulator signal the practice cites, each with jurisdiction, status, source URL and `date checked`. **No skill cites a rule without a row ID**, and a rule with no row is named as a question for the client's legal adviser (see `industry-packs/README.md`) |
| **Industry packs** | 14 packs | `industry-packs/README.md` | Per-industry use cases with a typical tier, key risks, governing rules with register rows, controls and discovery questions. The pack's "typical tier" is a starting point; `ai-compliance-risk` sets the actual tier |

## 2. The three scoring instruments are separate instruments

They are not three views of one score, they do not convert into each other, and nothing in the
department averages or combines them. Say which one you are quoting, every time.

| Instrument | Shape | Canonical file | Answers |
|---|---|---|---|
| **Readiness** | 7 dimensions scored 1 to 5 with evidence, plus Go/Wait gates | `../ai-readiness-assessment/SKILL.md` and `references/dimensions-rubric.md` | Is this **organisation** ready for AI, and what does it fix first. The governance dimension is scored against the Guidance for AI Adoption six practices and the APP 1.7 duty |
| **Risk screening** | 8 floor questions (each Yes sets a minimum tier), then a 16-item impact score out of 54 | `../ai-compliance-risk/references/screening-questionnaire.md` | What **tier** is this one project, and does APP 1.7 disclosure apply. The floors can set the tier on their own; the score sets it only when no floor applies, and otherwise ranks within a tier |
| **Portfolio** | four legs, ranked in order, with **no composite total** | `../ai-use-case-portfolio/SKILL.md` and the qualification file above | Which use case goes **first**. The four legs are value, time to value, feasibility and risk tier, ranked in that order deliberately: a weighted total would hide which leg is weak and start an argument about weights |

A readiness score of 4 does not make a project Tier 2. An impact score of 30 out of 54 is not a
readiness finding. A portfolio rank is not a score at all.

## 3. Token collisions to be careful with

Two unrelated schemes use `F`n, and they will be in the same engagement.

| Token | In `ai-compliance-risk` | In `ai-evals-security-testing` |
|---|---|---|
| F1 to F8 / F1 to F10 | **Floor questions** in the screening questionnaire: F1 to F3 are the three ADM limbs, F4 autonomous action, F5 regulated activity, F6 personal or confidential information, F7 public-facing, F8 vulnerable people | **Red-team families** in `references/red-team-catalogue.md`: F1 to F10, where F6 is excessive agency for agents and tools |

Always qualify it: "screening floor F6" or "red-team family F6", never a bare "F6". The same care
applies to `C` (data class, not control) and `B` (security baseline control, not bucket).

## 4. Definitions that belong to someone else

Do not restate these either, and do not paraphrase them: cite the ID and the source.

| Vocabulary | Owner | How we cite it |
|---|---|---|
| OWASP LLM and Agentic Top 10 IDs | OWASP (register INT-9, INT-10) | IDs only, edition-qualified (`LLMnn:2026`, ASI01 to ASI10), CC BY-SA. Re-mapped to the 2026 edition and verified against both official PDFs 2026-11-09 (evidence copies in `ai-kb/docs/`) |
| MITRE ATLAS tactics and techniques | MITRE (register INT-11) | `AML.T...` IDs against the pinned data version |
| ISO 42001, 23894, 42005, 42006 | ISO (register INT-1 to INT-4) | Clause structure by reference. **The practice cites no Annex A control IDs**, because two harvested sources number them differently (`ai-compliance-risk/references/vendored-provenance.md`) |
| NIST AI RMF and the Generative AI Profile | NIST (register INT-5, INT-6) | Function and risk names as published |
| Australian Privacy Principles, APP numbers | OAIC (register AU-6, AU-8) | APP numbers and the OAIC's own wording for the ADM limbs |
| Essential Eight and the ISM | ASD ACSC (register AU-23) | By reference to cyber.gov.au. ISM control identifiers are `PENDING_VERIFICATION` as at 2026-11-08 (`../ai-deployment-platforms/references/verify-live.md`) |

## 5. When you add a new scheme

1. Check this page first. If something close exists, use it rather than adding a near-duplicate.
2. Pick a letter prefix nobody has used (taken: B, C, F twice, H, I, K, P, plus AU/INT/EU/NZ).
3. Define it in exactly one file, the one that owns the method.
4. Add a row here with the canonical file and the one-line scope.
5. Tell ai-manager, so the department resources table and the agents stay consistent.
