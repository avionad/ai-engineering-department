# Industry pack: construction and trades

*v0.1.0, 2026-11-08. Builders, civil and commercial contractors, and trade service businesses
(plumbing, electrical, HVAC, carpentry, landscaping). Added after a review found the Sydney SMB
market the practice sells into is largely construction and trades, and the twelve original packs had no
row for it. Rules point at `../regulatory-register.md`.*

**No construction row exists in the research industry matrix,** so every use case here is
`[House addition]` (practitioner synthesis, not a sourced ROI claim) and the governing rules are the
general ones plus the overlays named below. The sector's own rules (licensing, the National
Construction Code, security of payment, home building contracts and warranties) are **not in our
register**: see the governing rules table.

Two things make this sector different from the other packs. The dominant risk is **physical safety
and document currency**, not personal data: building to a superseded drawing revision, or relying
on an AI-drafted safety document nobody competent reviewed, hurts people. And the dominant
commercial risk is that **an AI-generated number is a representation under the ACL** (AU-22): a
quote, a programme date or a compliance claim binds the business whether a person checked it or not.

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Quote and estimate drafting from plans, specifications and a rate file `[House addition]` | 1 to 2 | 1 where it assembles scope text only and prices come from the client's own rate rules; 2 once customer or site-owner personal information is in the inputs. Prices come from rules, never from the model |
| 2 | Tender, EOI and prequalification response drafting `[House addition]` | 1 | Organisational content; commercial-in-confidence pricing pushes it to 2 (floor F6) |
| 3 | Drawing, specification and RFI assistant for site staff `[House addition]` | 2 | Answers must cite the current revision; a wrong revision is a rework and safety event. Confidential client documents (floor F6) |
| 4 | Site diary, variation and defect report drafting from photos and voice notes `[House addition]` | 2 | Site photos and audio capture workers and bystanders (personal information); variations have contractual effect, so a person signs them |
| 5 | Subcontractor invoice and progress claim capture into the accounting system `[House addition]` | 2 | Sole-trader subcontractor data is personal information; financial effect, so it never initiates a payment |
| 6 | Safety documentation drafting: SWMS, toolbox talks, induction material `[House addition]` | 2, and 3 where the output determines the controls for high-risk construction work | A SWMS is a work health and safety control document. A competent person owns it, reviews it and signs it; AI drafts, never decides |
| 7 | Scheduling, delivery and trade-confirmation follow-up automation `[House addition]` | 2 | Supplier and sole-trader personal information; outbound messages in the business's name |
| 8 | Inbound enquiry handling and job booking for a trade services business `[House addition]` | 2 | Customer personal information; chatbot statements about price, timing and warranty bind the business (AU-22) |

## Key risks

- **Superseded documents.** An assistant answering from an old drawing or specification revision,
  or an estimate built from a withdrawn addendum. The most likely way an AI system in this sector
  causes a real loss.
- **Safety documents treated as a control because they exist.** An AI-drafted SWMS that no
  competent person reviewed is a compliance artefact with no safety value, and worse than none
  because it looks like the duty was met.
- **Quotes and programme dates as representations.** A model-generated price, inclusion, exclusion
  or completion date is the business's offer. Rework, disputes and ACL exposure follow.
- **Site imagery and audio.** Photos and voice notes capture workers, clients and the public;
  continuous capture starts to look like workplace surveillance, which is state law and not in our
  register.
- **Subcontractor and sole-trader data.** Sole traders are individuals, so their details are
  personal information even when the relationship looks business-to-business.
- **Algorithmic allocation of work** to workers or labour hire: workload, metrics and monitoring
  duties (AU-21 in NSW).
- **Confidentiality.** Client drawings, tender pricing and head-contract terms pasted into
  consumer AI tools.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| WHS Acts and the high-risk construction work provisions | Overlay | Named in the research (manufacturing row), no register row | PCBU duties apply to AI-influenced work. A competent person owns every safety document and control decision |
| NSW WHS Amendment (Digital Work Systems) Act 2026 | AU-21 | Commenced later (duties await proclamation) | Algorithmic workload, metrics and monitoring for NSW workers; union entry right to inspect systems |
| Australian Consumer Law | AU-22 | In force | AI-generated quotes, inclusions, timelines and compliance claims are the business's representations, including anything a chatbot says |
| Privacy Act and the APPs | AU-6 | In force | Confirm APP entity status with the client's legal adviser (turnover test plus the nine listed categories). Sole-trader subcontractor and customer data is personal information |
| ADM disclosure, APP 1.7 to 1.9 | AU-8 | Commenced later (from 10 Dec 2026) | Candidate where software screens, ranks or filters subcontractors, applicants or customers using their personal information. Run the ADM check in `../../ai-compliance-risk` |
| AHRC AI and recruitment compliance checklist | AU-24 | Voluntary, on binding anti-discrimination law | Applies the moment AI touches hiring of trades or labour hire: disclose AI use, no candidate removed solely by an automated decision |
| ASD ACSC guidance and Essential Eight | AU-23 | Voluntary for most businesses | Agent service accounts and credentials inherit these controls |
| Guidance for AI Adoption | AU-4 | Voluntary | Governance baseline; the free policy and register templates suit this sector's budget |
| SOCI Act and critical infrastructure risk management | Overlay | Named in the research, no register row | Only where the client works on or owns a critical infrastructure asset |
| **Building and trade licensing, the National Construction Code, security of payment legislation, home building contract and statutory warranty rules, and state workplace surveillance Acts** | **No register row. Not researched** | `PENDING_VERIFICATION` | These very likely bear on AI-drafted quotes, contracts, claims, certificates and site monitoring, but the practice holds no verified position on any of them. Identify them as questions and send them to the client's legal adviser. Do not state any of them as an AI requirement, and do not invent a rule to fill the gap |

## Controls

- **Document currency is the first control.** The assistant is grounded only in the current
  revision set, every answer cites the document and revision, and superseded documents are removed
  from the index rather than left in with a warning. Where the client cannot tell us which revision
  is current, that is a finding, not a build.
- **Competent-person sign-off on every safety output**, recorded, before it is issued or relied on.
  Configure the system to refuse to issue safety documentation directly to site.
- **Prices and dates by rule, not by model.** The model assembles scope and wording; quantities,
  rates, margins and programme dates come from the client's own rate file or scheduling tool, and a
  person approves every quote before it goes out.
- **No payment initiation.** Invoice and progress-claim automation writes a draft into the
  accounting system; a human approves and pays (human-in-the-loop tier H2 for anything with
  financial effect).
- **Site capture rules.** What may be photographed or recorded, how workers and the public are
  told, what is cropped or redacted before it leaves the site, and no continuous capture without a
  legal view from the client's adviser.
- **A sanctioned tool with business data terms**, so site and office staff have a safe alternative
  to free consumer tools for client drawings and pricing.
- **Chatbot hard limits** on any customer-facing assistant: no price, no completion date, no
  warranty or compliance statement outside a human-approved list, with a visible escalation path.

## Discovery questions

1. Where do your current drawings and specifications live, who controls revisions, and how would a
   site supervisor know today that they are looking at the current set?
2. How is a quote built now: who prices it, from what rate file, and who signs it before it goes to
   the client?
3. Who writes your SWMS and safety documentation, and who is the competent person who signs it?
4. How many subcontractor invoices and progress claims do you process a month, and what does each
   one cost you in admin time?
5. What do site staff photograph or record, where do those files end up, and have workers been told?
6. Does any system allocate work, shifts or jobs to workers or subcontractors, and which states are
   those workers in?
7. Do you use AI anywhere in hiring or labour-hire selection today?
8. Which head contracts or client agreements restrict where their documents may be processed or
   stored?
