<!-- Audience: client (system owners, council). Keep as a sheet the client owns; DDD seeds it.
Save the seed as created/docs/security/ai-register-{client}-{YYYY-MM-DD}.csv (+ .md summary) -->

# AI register template

*v0.1.0, 2026-11-08. Practices 1, 3, 4 (AU-4); ISO/IEC 42001 Clause 4 (4.3 scope per harvested
source); NIST Govern and Map. The register is the inventory of every AI system, including shadow
AI and AI features inside bought software.*

**Field alignment status.** The NAIC AI register template (AU-4, copies dated 2026-05 and
2026-06 on ai.gov.au) and the DTA use-case register (AU-17) are the government formats. The
research does not list their fields, and the template could not be downloaded on 2026-11-08 (site
timeout). The fields below are DDD's design, built so an export can be mapped to either format;
**exact field alignment is `PENDING_VERIFICATION`**. When the template is retrieved, add a
column-mapping table here and keep DDD-only fields at the end.

## Fields

| # | Field | Values / guidance | Why it is here |
|---|---|---|---|
| 1 | ID | AI-001 ... | Stable reference for screens, risk registers, incidents |
| 2 | System name | Plain name staff use | |
| 3 | Description and purpose | One or two sentences, business outcome | Practice 2 |
| 4 | Type | Built / bought (SaaS) / AI feature in existing software / staff-adopted (shadow) / agent | Shadow and embedded AI are where gaps hide |
| 5 | Vendor and model | Provider, product, underlying model and version if known | Value chain risk; vendor DD |
| 6 | Business owner | Named person | Practice 1 |
| 7 | Technical owner | Named person or vendor contact | |
| 8 | Users | Who uses it, approx. number | Size of exposure |
| 9 | Affected people | Customers, candidates, patients, staff, public | Practice 2 |
| 10 | Data classes used | Public / internal / confidential / personal / sensitive | Practice 3 |
| 11 | Personal information kinds | e.g. contact details, financial, health | APP 1.7 disclosure input (AU-8) |
| 12 | Data location | Storage and processing region | Residency |
| 13 | Vendor trains on our data? | No (contract ref) / Yes / Unknown | OAIC guidance (AU-11) |
| 14 | Decisions influenced | None / internal / about individuals (name the decision) | ADM screen |
| 15 | ADM limbs (1, 2, 3) | Y/N each; in scope if all Y | AU-8, from 10 Dec 2026 |
| 16 | Human role | Human does, AI suggests / AI does, human approves each / AI does, human samples / autonomous within limits | Practice 6 (research B5 HITL tiers) |
| 17 | Actions it can take | None / read / write records / send / spend / delete / control equipment | Least agency |
| 18 | Risk tier | 1 to 4, screen date | `ai-compliance-risk` mode a |
| 19 | Impact assessment | Not required / due / done (date, link) | Tier 3 |
| 20 | Vendor due diligence | Not required / due / done (date, link) | |
| 21 | Transparency | User notice in place? Model or system card link | Practice 4 |
| 22 | Monitoring | Metrics, owner, cadence | Practice 5 |
| 23 | Status | Proposed / pilot / live / paused / retired | |
| 24 | Go-live approval | Who, date | |
| 25 | Discovery source | Intake / survey / expense / extension / network / vendor notice | Shadow AI method |
| 26 | Last reviewed | Date | Review cadence |
| 27 | Notes and open actions | | |

## CSV header

```
id,system_name,description,type,vendor_model,business_owner,technical_owner,users,affected_people,data_classes,pi_kinds,data_location,vendor_trains_on_data,decisions_influenced,adm_limb1,adm_limb2,adm_limb3,human_role,actions,risk_tier,screen_date,impact_assessment,vendor_dd,transparency,monitoring,status,go_live_approval,discovery_source,last_reviewed,notes
```

## Size band notes

- **S:** a single sheet, fields 1-6, 10, 13-18, 23 are enough. Review quarterly with the owner.
- **M:** all fields; owned by the privacy or compliance lead.
- **L/XL:** all fields; integrated with the intake form and IT asset or SaaS management; council
  reviews changes monthly; XL can export to the DTA format if a government client asks.
