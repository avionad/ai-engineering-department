# Data class to platform matrix

*v0.1.0, 2026-11-08. DDD default positions, built from research B2 and B4, the client FAQ and the
regulatory register. They are **defaults for design discussion, not legal conclusions**: the
client's own data classification policy, contracts, sector rules and legal advice override them
(conventions s3 and s4). Every platform cell assumes the facts in `platforms.md` have been
re-verified live for the specific model and deployment type.*


*Conditions are numbered K1 to K9 so that no token means two things: C0-C5 are DATA CLASSES, K1-K9 are CONDITIONS.*


## 1. Data classes

Map the client's own scheme onto these where it has one; otherwise use these.

| Class | Examples | Notes |
|---|---|---|
| C0 Public | Published website content, public policies, marketing copy | No restriction beyond accuracy |
| C1 Internal | Internal procedures, non-sensitive operational data | Business terms, no training on data |
| C2 Confidential | Contracts, pricing, financials, client files without personal information, IP | Commercial harm if disclosed |
| C3 Personal | Personal information under the APPs (register AU-6): customer and staff records, contact details, CVs | Privacy Act obligations; cross-border disclosure (APP 8, register AU-6) goes to `ai-compliance-risk` |
| C4 Sensitive personal | Health information, TFN, biometric, criminal record, and the other categories in the Privacy Act's definition of sensitive information (check the definition) | Highest privacy risk; health and TFN bring extra rules (industry packs) |
| C5 Highly restricted | Government information at PROTECTED-level handling, legal professional privilege, defence-adjacent, information the client's policy says must stay on its own infrastructure | Client security assessment decides; sovereignty and CLOUD Act exposure in scope |

A flow takes the **highest class** of anything in it (prompt, retrieved context, output, logs).

## 2. Matrix

Legend: **Y** allowed by default with the security baseline. **K**n allowed only with condition
n below (an inline bracketed note is the condition itself). **N** not by default (only with the client's documented risk acceptance and legal
review). **X** do not use. (The letter C is never used in cells: C is a data class, K is a condition.)

| Platform / deployment | C0 | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|---|
| Consumer AI tools and free tiers | Only with no client data at all (OAIC guidance AU-11) | X | X | X | X | X |
| Vendor direct, business or enterprise terms (Anthropic, OpenAI; US or global processing per research [secondary] / `PENDING_VERIFICATION`) | Y | K1 | N | N | X | X |
| Vendor SaaS product with AI features | Y | K2 | K2 | K3 | N | X |
| AWS Bedrock `au.*` profile (Sydney/Melbourne) | Y | Y | Y | K4 | K5 | K6 |
| AWS Bedrock `global.*` profile | Y | K1 | N | N | X | X |
| Azure Standard (regional) deployment, Australia East | Y | Y | Y | K4 | K5 | K6 |
| Azure Data Zone or Global deployment | Y | K1 | N | N | X | X |
| Vertex AI, model processed in an Australian region | Y | Y | Y | K4 | K5 | N |
| Vertex AI `global` endpoint or model not processed in AU | Y | K1 | N | N | X | X |
| Self-managed VPS, Australian data centre | Y | Y | K7 | K7 | K8 | N |
| On-premises GPU (client infrastructure) | Y | Y | Y | Y | K8 | K9 |

### Conditions

- **K1** No-training and retention terms verified for the exact product tier (FAQ Q3); no
  confidential or personal content in prompts, enforced by policy and, at M+, by the gateway's
  data-classification gate.
- **K2** Vendor due diligence passed (`ai-compliance-risk` mode g, including residency and
  training-on-data gate sections); data processing region in the vendor's terms recorded.
- **K3** As K2, plus the vendor's processing region is Australian or the APP 8 cross-border
  analysis is done and accepted by the client; privacy check done.
- **K4** Model confirmed available in that region and deployment type on the day; every other
  component (embeddings, vector store, logs, guardrails, parser, cache) in the same Australian
  region(s); private networking; SSO; logging with restricted access; no-training terms verified.
- **K5** As K4, plus customer-managed encryption keys where the service supports them, an impact
  assessment where tier 3, minimised data (redaction per `ai-rag-engineering`), restricted log
  content, and the client's privacy officer sign-off.
- **K6** Only where the service's IRAP assessment covers the level the client needs (research:
  Bedrock excluding Marketplace, and Azure Australian regions, assessed to PROTECTED, check service
  by service), the client's own security assessment accepts it, and the CLOUD Act caveat is
  documented and accepted. Otherwise on-premises or sovereign options.
- **K7** Provider assessed by the client (location, access, certifications verified with the
  issuer), hardened host, private access only, encrypted disks, backups in Australia, patching
  owner named.
- **K8** As K7 (or client infrastructure), plus everything in K5 that applies to self-hosting, and
  the client accepts the operations burden in writing.
- **K9** Client's security team designs and approves; DDD advises and builds in the client's
  environment only under the client's controls.

## 3. How to use it

1. Classify each flow (prompt, retrieval, output, logs, training data).
2. Read across the matrix for the highest class per flow; note the conditions.
3. If different flows land on different platforms, that is the case for hybrid routing.
4. Record the mapping in the platform decision record (section 3), with the live-verified facts.
5. Any **N** used anyway needs the client owner's written risk acceptance and goes to
   `ai-compliance-risk` as a finding.

## 4. Australian-specific notes

- **Onshore is not sovereign.** US-headquartered providers remain exposed to foreign-law access
  (for example the CLOUD Act) even in Australian regions (research B4, [secondary]).
- **APRA-regulated entities**: AI providers may be material service providers under CPS 230
  (register AU-13); APRA's AI letter (AU-15) flags over-dependence on single suppliers and untested
  exit plans. The decision record must include a substitution path.
- **Commonwealth agencies and their suppliers**: DTA policy (AU-17) and the client's own IRAP and
  ISM requirements decide; treat the matrix as a starting point only.
- **Health**: the healthcare industry pack and AHPRA guidance (AU-19) apply; recording consent for
  voice tools (FAQ Q17).
