# Industry pack: education

*v0.1.0, 2026-11-08. Schools, RTOs, universities, edtech. Rules point at `../regulatory-register.md`.*

Child users change the risk picture: the Children's Online Privacy Code (AU-9) is still proposed
but its registration deadline is 10 Dec 2026, and education AI is high-risk under the EU AI Act
where the client is EU-facing (EU-1, Annex III from 2 Dec 2027).

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Feedback and marking assistance | 3 | Assessment outcomes significantly affect students; bias risk |
| 2 | Lesson planning | 1 | Teacher-facing, no student PI |
| 3 | Student support chat | 2 (3 with child users or wellbeing topics) | Customer-facing; child privacy; age-appropriate content |
| 4 | Admin automation (enrolment paperwork, timetabling, parent comms) | 2 | Student and parent PI |
| 5 | Policy and procedure assistant for staff `[DDD addition]` | 1 | Internal documents |
| 6 | Course content drafting for RTO units `[DDD addition]` | 1 to 2 | Accuracy against training package requirements |

## Key risks

- Child privacy; age-inappropriate content from a student-facing tool.
- Academic integrity (students and staff).
- Bias in assessment or feedback across student groups.
- Student data used to train vendor models.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| Children's Online Privacy Code | AU-9 | Proposed (registration due 10 Dec 2026, commencement not set) | Plan for it on any service likely accessed by children; final obligations once registered |
| Australian Framework for Generative AI in Schools | Overlay (education.gov.au) | Voluntary (reviewed annually) | Reference framework for schools |
| State education department policies | Overlay | Named in research, no row | Check the client's state and sector (government, Catholic, independent) |
| Privacy Act; ADM disclosure | AU-6, AU-8 | In force / commenced later | Marking and admissions decisions are ADM candidates |
| EU AI Act (education as high-risk) | EU-1 | Commenced later for Annex III (2 Dec 2027) | Only for EU-facing providers |

## Controls

- Teacher remains the assessor; AI marking is a suggestion with the teacher's decision recorded.
- Age gating, content filtering and escalation to a staff member in any student-facing chat.
- Contract term: no training on student data; onshore storage where the department requires it.
- Bias sampling of feedback across cohorts each term.
- Academic integrity policy updated for AI, communicated to students and parents.

## Discovery questions

1. Sector and state: government, Catholic, independent school; RTO; university; edtech vendor?
2. Will students under 18 interact with the system directly?
3. Which learning platforms are in use and which AI features are already on in them?
4. Does any system contribute to marks, progression, admissions or wellbeing flags?
5. What does the department or system policy allow for GenAI tools?
6. Do you have EU students or sell the product into the EU?
