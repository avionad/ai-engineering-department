<!-- Audience: AI vendor (sent by the client) and client procurement. Save completed copies as
created/docs/security/ai-vendor-dd-{vendor-slug}-{YYYY-MM-DD}.md -->

# Third-party AI vendor due diligence questionnaire

*v0.1.0, 2026-11-08. Mode (g) of ai-compliance-risk. Sent by the client to any vendor whose
product uses AI on the client's data or makes or shapes decisions. Answers must be evidenced
(contract clause, policy URL, certificate, report) not just asserted.*

**Why these questions.** APRA's AI letter (30 Apr 2026, AU-15) flags over-dependence on single
AI suppliers and says few entities have tested exit and substitution plans; CPS 230 (AU-13) covers
material service providers; ASIC REP 798 (AU-16) found heavy third-party model reliance without
matching governance; OAIC guidance (AU-11) expects due diligence on AI products. These apply in
full to APRA-regulated and ASIC-licensed clients and are good practice for everyone else.

**Scoring.** Each answer: Meets / Partial / Does not meet / Not applicable, with the evidence
reference. Any "Does not meet" in a section marked **[gate]** blocks use for Tier 2 and above
until resolved or formally accepted by the client's accountable owner.

## A. The product and the AI in it
1. Describe the AI features and which are switched on by default.
2. Which models power them (provider, model family, version)? How are we told when they change?
3. Can AI features be switched off per feature, per user group, or tenant-wide?
4. Does any feature make, or do a thing substantially and directly related to, decisions about
   individuals (score, rank, filter, reject)? (Needed for our APP 1.7 ADM inventory, AU-8.)

## B. Data residency and location **[gate]**
5. Where is our data stored, and where is it processed for inference (country and region)?
6. Can processing be restricted to Australia? Is that contractual?
7. Does any request route to another region for capacity or fallback?
8. Which entities can access our data under foreign law (e.g. parent-company jurisdiction)?

## C. Use of our data for training **[gate]**
9. Is our data (prompts, files, outputs, metadata) used to train or improve any model, yours or a
   sub-processor's? Default and contractual position.
10. Is human review of our data by your staff possible? When, and with what controls?
11. Can we opt out in writing, and does the opt-out cover sub-processors?

## D. Sub-processors
12. List all sub-processors that receive our data, their role and location.
13. How much notice do we get of a new sub-processor, and can we object?

## E. Retention and deletion
14. Retention period for prompts, outputs, logs, files and embeddings.
15. How do we delete our data, and how is deletion confirmed (including backups and vector stores)?
16. What happens to our data at contract end?

## F. Security and access
17. SSO, MFA, role-based access, audit logs available to us?
18. Encryption at rest and in transit; key management options.
19. Protections against prompt injection and data leakage between tenants or users.
20. For agentic features: what actions can the AI take, with what permissions, and can we require
    human approval for irreversible actions?

## G. Incident notification **[gate]**
21. How quickly will you notify us of a security incident or data breach affecting our data, and
    through what channel? (We need this to meet our own Notifiable Data Breaches obligations, AU-6.)
22. Do you notify us of AI-specific incidents (harmful outputs, model failures, misuse)?

## H. Certifications and assurance
23. Current certifications and reports with scope and dates: ISO/IEC 27001, ISO/IEC 42001 (and
    the certification body), SOC 2 type and period, IRAP (assessment level, for government data).
    Note: we verify certificates with the issuing body; a logo on a website is not evidence.
24. Independent testing of the AI features (red-team, bias testing) and whether results are shared.
25. Responsible AI policy or model documentation (model or system card) for the features we use.

## I. Accuracy, bias and transparency
26. Known limitations and failure modes; how accuracy is measured for our use case.
27. Bias or fairness testing for features that affect individuals.
28. Can the product explain or show the basis for an output to our staff and to affected people?

## J. Continuity, exit and substitution **[gate for APRA-regulated or critical use]**
29. Model deprecation policy and notice period; version pinning options.
30. Service levels and history of outages for the AI features.
31. Export of our data, configurations, prompts and logs in a usable format.
32. What would we need to move to an alternative supplier, and how long would it take? Have you
    supported a customer exit before?
33. For our critical operations: can you support a tested exit or substitution exercise?

## K. Contract terms to confirm
34. Indemnity for IP claims arising from AI output.
35. Liability for AI-caused errors.
36. Audit and information rights (APRA-regulated clients: rights needed under CPS 230).

---
**Reviewer's summary (client fills):** gate results; open issues; decision (approve / approve with
conditions / reject); accountable owner; date. File with the AI register entry for the system.

*This questionnaire identifies considerations for review by your legal adviser. It is not legal
advice.*
