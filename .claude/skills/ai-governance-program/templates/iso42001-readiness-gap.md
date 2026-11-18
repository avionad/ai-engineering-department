<!-- Audience: client executive / compliance lead. Save as
created/docs/security/iso42001-readiness-gap-{client}-{YYYY-MM-DD}.md -->

# ISO/IEC 42001 readiness gap: method and report frame

*v0.1.0, 2026-11-08. ISO/IEC 42001:2023 is voluntary and certifiable (INT-1). **DDD does readiness;
DDD cannot certify.** Certification is done only by bodies meeting ISO/IEC 42006:2025 (INT-4),
for example the certification bodies the research names (BSI, Intertek SAI Global, A-Good
Certification Group). Enterprise tenders increasingly ask for 42001; this is why clients want a
gap view.*

> Readiness assessment only, for review with your legal adviser and chosen certification body.
> It is not an audit, legal advice, or a prediction of audit findings.

## When to offer it

- L and XL clients facing tender or customer questionnaires that ask about ISO 42001.
- Clients already certified to ISO 27001 or 9001 (management-system machinery can be extended).
- Not for S clients unless a customer contract demands it: the governance program artefacts
  give them more value per dollar.

## Method

1. **Scope.** Which AI systems, units and lifecycle stages would be in an AIMS scope. Pull from
   the AI register; vendor AI is included if it affects the client's services.
2. **Evidence inventory.** For each Clause 4-10 requirement, collect evidence and mark
   documented / partial / missing. Interview the owner of each.
3. **Score.** `python3 scripts/iso42001_readiness_gap.py evidence.json --md out.md`. Weighted
   readiness percentage plus a prioritised gap list with the DDD artefact that closes each gap.
   Weights (critical 4, major 2, minor 1) are a heuristic from the adapted upstream tool, not
   from ISO.
4. **Annex A.** Review against the client's own copy of the standard's Annex A controls. DDD
   does not quote Annex A control IDs from harvested sources (they disagree with each other).
   Ask the client for their licensed copy, or have their certification body confirm.
5. **Roadmap.** Sequence gaps into the governance program: policy and charter first (Clause 5),
   register and scope (Clause 4), risk and impact process (Clause 6, 8), training (Clause 7),
   monitoring, internal audit and management review (Clause 9), incident and corrective action
   (Clause 10).

## Report frame

1. What this means for you (60 seconds: readiness level, top three gaps, realistic path).
2. Scope assumed.
3. Readiness score and gap table (from the script).
4. Annex A observations (client's copy).
5. Roadmap with owners and dates.
6. What a certification body will do next (stage 1 and stage 2 audits, as described by the
   client's chosen body; do not describe audit mechanics from memory).

Sub-clause numbers in the script follow the harvested alirezarezvani reference (MIT) and are
unverified against the standard. Confirm against the client's copy before quoting.
