# Industry pack: manufacturing and critical infrastructure

*v0.1.0, 2026-11-08. Manufacturing, logistics, utilities and other critical infrastructure.
Rules point at `../regulatory-register.md`.*

Here the dominant risk is physical safety and operational technology (OT), not personal data.
Telco and IT services share the agent-privilege risks (research matrix: OWASP Agentic, E8, SOCI
for telcos, least agency).

## High-ROI use cases

| # | Use case | Typical tier | Why that tier |
|---|---|---|---|
| 1 | Predictive maintenance | 2 (3 if it acts on equipment) | Safety consequences if wrong; human schedules work |
| 2 | Quality inspection vision | 2 | Product safety; drift on sensor data |
| 3 | SOP and maintenance assistant | 2 | Wrong procedure can injure; grounded in controlled documents only |
| 4 | Supplier document processing | 1 to 2 | Commercial data; supplier PI if sole traders |
| 5 | Production scheduling recommendations `[DDD addition]` | 2 | Operational impact; human approves |
| 6 | Agent with write access to OT or control systems `[DDD addition]` | 3 | Autonomous action with physical effect; often should not be built |

## Key risks

- OT safety incidents from AI control or from wrong maintenance advice.
- IP leakage (designs, formulas, process data) into third-party tools.
- Model drift on sensor data; silent accuracy decay.
- Agent privilege abuse on infrastructure.

## Governing rules

| Rule | Register | Status | What it means |
|---|---|---|---|
| WHS Acts (robotics, AI-driven OT) | Overlay | Named in research, no row | PCBU duties apply to AI-influenced work |
| NSW WHS Amendment (Digital Work Systems) Act 2026 | AU-21 | Commenced later | Algorithmic workload and monitoring for NSW workers |
| SOCI Act and critical infrastructure risk management program | Overlay | Named in research, no row | If the client owns a critical infrastructure asset |
| ACSC/CISA principles for secure integration of AI in OT | Overlay ([cyber.gov.au](https://www.cyber.gov.au/business-government/secure-design/operational-technology-environments/principles-for-the-secure-integration-of-artificial-intelligence-in-operational-technology)) | Voluntary | Reference for any AI touching OT |
| ACSC guidance, Essential Eight | AU-23 | Voluntary for most | Agent service accounts inherit E8 controls |

## Controls

- Human override and physical interlocks independent of any AI component.
- AI recommends, people act, for anything touching equipment state; read-only integration with
  OT by default.
- Drift monitoring with thresholds and an owner; recalibration schedule.
- Maintenance assistant answers only from controlled, current SOP versions, citing the document.
- IP classification: which documents may go to which tool tier.

## Discovery questions

1. Is any site or asset a critical infrastructure asset under SOCI?
2. Would the AI read from, or write to, OT or control systems?
3. What happens physically if the model is wrong, and who would notice first?
4. Which documents are your most sensitive IP, and where do staff paste them today?
5. How are SOPs version-controlled?
6. What sensor data exists, how far back, and how clean is it?
7. Which states are your workers in? (NSW DWS Act.)
