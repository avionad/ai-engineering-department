# Mode (a) Screen: risk tier questionnaire

*v0.1.0, 2026-11-08. Assigns one of the four risk tiers in `../../_shared/engagement-conventions.md`
section 6. Takes 15 to 30 minutes with the client's project owner. Run it per project (or per use
case when a project bundles several), and re-run on any material change.*

*Provisional screen: before the client is in the room (pre-call prep, first scoping), run it
on what is known and label every answer `assumed` and the tier `PROVISIONAL`. A provisional tier
can steer discovery questions and a draft scope, never a quote sent to the client or a build.
Confirm with the project owner before stage 2 is marked complete.*

## Provenance (what this is adapted from)

| Source | What we took | What we did not take |
|---|---|---|
| Government of Canada Algorithmic Impact Assessment questionnaire, `canada-ca/aia-eia-js` `src/survey-enfr.json` (MIT, commit b62573389db4946b4d70b7fa62c4ca8d9990dba3) | The structure: separate **raw impact** questions (each answer carries points) from **mitigation** questions; the impact dimensions (reversibility, duration, rights, equality/dignity/privacy/autonomy, health and wellbeing, economic interests); data questions (personal information, multiple sources, third-party collection); system questions (judgement or discretion, full vs partial automation, continued learning, explainability) | Canadian-government specifics (TBS review, GBA Plus, Open Government Portal, Protected A/B/C classifications, legislative authority chain). Canada's level thresholds are computed in the tool's code, which was not harvested, so **our bands are the practice's own (v0.1, uncalibrated)** |
| Australian Guidance for AI Adoption AI screening tool (NAIC, Oct 2025; register row AU-4) | Its purpose as described in the research: decide the governance level per use case before a full risk assessment | Its question content. The tool's .docx could not be retrieved on 2026-11-08 (site timed out); alignment of our questions to it is `PENDING_VERIFICATION` |
| `engagement-conventions.md` section 6 | The four tiers and their minimum controls | - |
| POLA Act APP 1.7 to 1.9 (AU-8) | The three ADM limbs as a hard floor | - |

**Deliberate departure from Canada's AIA:** in the AIA, mitigation answers can lower the impact
level. Here they do not lower the tier. Controls reduce *residual risk* in the risk register
(mode d); the tier describes the *use*, and it decides which controls are mandatory. Lowering the
tier because controls exist would remove the requirement for those same controls.

## Step 1. Stop questions (any Yes = Tier 4, do not build)

| # | Question |
|---|---|
| S1 | Would the system covertly identify, track or monitor people using biometrics, or record people without the consent the law requires? (AU-7 tort; AU-19 recording consent; surveillance Acts) |
| S2 | Is it designed to manipulate people against their interests or exploit vulnerabilities (age, disability, financial distress)? |
| S3 | Does it generate non-consensual intimate imagery or child sexual abuse material, or could it be used to? (EU new Art 5 prohibitions from 2 Dec 2026, EU-2; unlawful in Australia regardless) |
| S4 | Where the client has EU users or market: is the use banned under EU AI Act Article 5? (EU-1; the legal adviser confirms; the Art 5 list itself is not itemised in the research beyond S3) |
| S5 | Would it be unlawful on its face for this client (e.g. using genetic information where an instrument forbids it, AU insurance overlay `PENDING_VERIFICATION`)? |

A Yes is not argued away in the meeting. Record it, explain why in plain language, and offer the
nearest lawful alternative if one exists.

## Step 2. Floor questions (each Yes sets a minimum tier)

| # | Question | Yes sets minimum |
|---|---|---|
| F1 | ADM limb 1: does a computer program make the decision, or do a thing substantially and directly related to making it (score, rank, recommend, filter, draft the outcome)? | (see F3) |
| F2 | ADM limb 2: could the decision reasonably be expected to significantly affect an individual's rights or interests (credit, insurance, employment, tenancy, health care, education, entitlements, access to services, pricing for that person)? | (see F3) |
| F3 | ADM limb 3: is personal information about that individual used in the program's operation? | **F1 + F2 + F3 all Yes = Tier 3** and APP 1.7 disclosure applies (run mode c). Human review does not change this |
| F4 | Does the system take actions with real-world effect without a person approving each one (sends, spends, deletes, changes records, controls equipment)? | Tier 3 |
| F5 | Is it part of a regulated activity (financial advice, credit, insurance underwriting or claims, clinical care, legal advice to clients, government entitlements, critical infrastructure operations)? | Tier 3 |
| F6 | Does it process personal or confidential information (customer, staff, patient, client-privileged, commercial-in-confidence)? | Tier 2 |
| F7 | Is it customer-facing or public-facing (people outside the organisation see its output directly)? | Tier 2 |
| F8 | Will it be used with or about children or other vulnerable people? | Tier 2 (Tier 3 if F2 is also Yes) |

## Step 3. Impact score (sets the tier when no floor applies, and ranks within a tier)

Score each item. Points are the practice's calibration v0.1, informed by the AIA's point pattern (impact
dimensions on a 1 to 4 scale; binary risk flags at 1 to 4 points).

| # | Question | Points |
|---|---|---|
| I1 | Reversibility of the worst plausible outcome | Reversible 1 / Likely reversible 2 / Difficult 3 / Irreversible 4 |
| I2 | How long could that outcome last? | Brief 1 / Months 2 / Years 3 / Perpetual 4 |
| I3 | Impact on people's rights or freedoms | Little 1 / Moderate 2 / High 3 / Very high 4 |
| I4 | Impact on equality, dignity, privacy, autonomy | 1 to 4 as above |
| I5 | Impact on health, safety or wellbeing | 1 to 4 as above |
| I6 | Impact on people's economic interests | 1 to 4 as above |
| I7 | Does the use require judgement or discretion that a person would normally exercise? | Yes 4 / No 0 |
| I8 | Full automation (no human before effect) or partial (human decides)? | Full 4 / Partial 2 / Human does, AI suggests 0 |
| I9 | Will the model keep learning or change in use (fine-tuning on feedback, memory, model updates outside your control)? | Yes 3 / No 0 |
| I10 | Will the reasoning be hard to explain to an affected person? | Yes 3 / No 0 |
| I11 | Could it be an attractive target for fraud or attack (money, credentials, sensitive data)? | Yes 3 / No 0 |
| I12 | Data comes from multiple sources, or from third parties the client did not collect from directly? | Yes 2 / No 0 |
| I13 | Does it connect to other IT systems (read or write)? | Read 2 / Write 4 / None 0 |
| I14 | Is the area under public scrutiny or frequent litigation for this client or sector? | Yes 3 / No 0 |
| I15 | Does it consider protected attributes, or variables that could be proxies for them? | Yes 3 / Unsure 2 / No 0 |
| I16 | Is the model or service built by a third party the client cannot inspect? | Yes 1 / No 0 |

Maximum = 6 x 4 + 4 + 4 + 3 + 3 + 3 + 2 + 4 + 3 + 3 + 1 = **54**.

| Score as % of 54 | Tier from score |
|---|---|
| under 25% (0 to 13) | Tier 1 |
| 25% to 49% (14 to 26) | Tier 2 |
| 50% and over (27 to 54) | Tier 3 |

**Final tier = the highest of: Stop result, floor results, score band.** Calibration status: the
bands are v0.1 and untested against real engagements. Record the score with every screen so the
bands can be tuned after the first five projects.

## Step 4. Mitigation readiness (recorded, does not change the tier)

Yes / No / Planned for each. These feed the risk register controls and the sign-off checklist.

| # | Question | Tier where it becomes mandatory |
|---|---|---|
| M1 | Named accountable owner for the system on the client side? | 1 |
| M2 | Entry in the client's AI register? | 1 |
| M3 | Privacy impact assessment done or updated? | 2 |
| M4 | Access permissions granted, monitored and revocable? | 2 |
| M5 | Logs of inputs, outputs, actions, model version and reviewer kept? | 2 |
| M6 | Eval baseline (golden test set) defined? | 2 |
| M7 | Bias or disaggregated testing planned? | 3 where people are affected |
| M8 | Human review designed (who, when, with what information, can they override)? | 3 |
| M9 | Way for an affected person to challenge the outcome? | 3 |
| M10 | Non-automated fallback if the system is unavailable? | 3 |
| M11 | Monitoring for performance change over time, with an owner and thresholds? | 3 |
| M12 | Incident plan covering this system? | 3 |

## Output

Write `ai-risk-screen-{project-slug}-{YYYY-MM-DD}.md` in the client's
`created/docs/security/` using this block, then continue to mode (b):

```
Project: ... | Size band: S/M/L/XL | Industry pack: ... | Jurisdictions: AU (+EU/NZ/UK if any)
Stop questions: all No / S? Yes -> Tier 4
Floors triggered: F? ... (ADM limbs: F1 Y/N, F2 Y/N, F3 Y/N)
Impact score: NN / 54 (NN%) -> Tier ?
FINAL TIER: ?  (reason in one sentence)
Mitigation readiness: M1..M12 Y/N/Planned
Screened by: ... with ... (client role) on YYYY-MM-DD. Re-screen trigger: material change.
```
