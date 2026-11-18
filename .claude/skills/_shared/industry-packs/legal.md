# Industry pack: legal

*v0.1.0, 2026-11-08. Law firms and in-house legal teams. Rules point at `../regulatory-register.md`.
The practice never gives legal advice to lawyers either: we build and govern the tooling.*

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Discovery review (classification, privilege flagging) | 2 to 3 | Confidential client data; privilege; 3 if review outcomes are relied on without sampling |
| 2 | Contract clause extraction and comparison | 2 | Confidential; lawyer reviews |
| 3 | Research memos | 2 | Fabricated-citation risk; lawyer must verify every authority |
| 4 | Matter intake (conflict checks, triage) | 2 | Prospective client PI; 3 if it declines matters automatically |
| 5 | Precedent and know-how search over the firm's own documents `[House addition]` | 2 | Confidential; permission-aware retrieval needed (matter walls) |
| 6 | Time narrative and billing draft clean-up `[House addition]` | 1 to 2 | Internal; client names present |

## Key risks

- Fabricated citations reaching a court document.
- Privilege waiver or confidentiality breach through public AI tools.
- Breach of court practice notes on GenAI in evidence (AU-20).
- Ethical walls breached by a retrieval system that ignores matter permissions.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| NSW Supreme Court Practice Note SC Gen 23 | AU-20 | In force (practice note) | Affidavits, witness statements and references must reflect the person's own knowledge, not GenAI. Other courts have similar notes (not itemised in the research: check the court in question) |
| Professional conduct rules | Overlay | Named in research, no row | Firm's own professional obligations; firm's general counsel or risk partner owns interpretation |
| Privacy Act; OAIC AI guidance | AU-6, AU-11 | In force / voluntary | Client PI not in public tools |
| ADM disclosure | AU-8 | Commenced later | Only if a system makes decisions about individuals (e.g. automated intake declines) |

## Controls

- Private tenancy only; no client material in consumer AI tools.
- Mandatory citation verification step before any AI-assisted document is filed or sent; the
  verification is recorded.
- Retrieval filtered by the querying user's matter permissions at query time; deny by default.
- Practice-note check built into document templates for affidavits and witness statements.
- Sampling regime for AI-assisted discovery review, with recall measured.

## Discovery questions

1. Which courts and tribunals do you appear in, and have you mapped their AI practice notes?
2. Which AI tools do lawyers and staff use today, including personal accounts?
3. How are ethical walls enforced in your DMS, and would a new search tool respect them?
4. Who verifies citations in research output, and how is that evidenced?
5. Has a client restricted AI use on their matters in engagement terms or outside counsel
   guidelines?
6. What volumes do you review in discovery per year, and what does review cost per document?
