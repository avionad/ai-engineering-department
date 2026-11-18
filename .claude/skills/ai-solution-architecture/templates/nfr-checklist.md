<!-- Appendix A of the solution design. Every row gets a target the client agrees, "not
required" with a reason, or an open question with an owner. Targets come from the client, never
from this template. Vendor capabilities carry URL + date or PENDING_VERIFICATION. -->

# Non-functional requirements checklist

| # | Area | Question | Target / answer | Agreed by | Evidence or source |
|---|---|---|---|---|---|
| 1 | Security | Who can access the system and its admin console? MFA and SSO enforced? | | | |
| 2 | Security | Credentials: where stored (Doppler), scope, rotation, who holds admin? | | | |
| 3 | Security | Untrusted input entry points identified and threat-modelled (LLM01:2026, ASI01)? | | | |
| 4 | Security | Encryption in transit and at rest for every store, including logs and vector stores? | | | |
| 5 | Security | Essential Eight maturity target the system must fit (client's own target)? | | | |
| 6 | Privacy | Personal information kinds, minimisation at each hop, purpose limits (APPs, AU-6)? | | | |
| 7 | Privacy | ADM check result and disclosure plan if in scope (AU-8, from 10 Dec 2026)? | | | |
| 8 | Privacy | Vendor training and retention terms on client data confirmed in contract? | | | |
| 9 | Privacy | Retention and deletion periods for inputs, outputs, logs, recordings? | | | |
| 10 | Residency | Processing, storage, logs, caches, backups and vector store regions; same region as the model? | | | |
| 11 | Residency | Foreign-law access caveat (e.g. CLOUD Act) acceptable to the client, or sovereign option needed? | | | |
| 12 | Availability | Hours of operation, acceptable downtime, what happens when it is down (manual fallback)? | | | |
| 13 | Availability | Dependence on a single vendor or region; failover need? | | | |
| 14 | Latency | Response time users or callers will accept for the key interaction? | | | |
| 15 | Throughput | Peak volume per hour or day; vendor rate limits checked? | | | |
| 16 | Cost | Monthly run-cost ceiling; caps and alerts on spend? | | | |
| 17 | Cost | Cost levers considered (batching, caching, model routing) where the vendor offers them? | | | |
| 18 | Accuracy | Success threshold on the eval set, and who set it? | | | |
| 19 | Observability | What is logged (model and prompt version, tool calls, approvals, cost), where, for how long, who can read it? | | | |
| 20 | Observability | Monitoring and alerting: what signals, which thresholds, who receives alerts? | | | |
| 21 | Human oversight | HITL tier per action; approval timeouts; kill switch tested? | | | |
| 22 | Maintainability | Pinned model and prompt versions; change process; who maintains after handover? | | | |
| 23 | Maintainability | Model retirement plan (hyperscalers retire versions on a schedule)? | | | |
| 24 | Accessibility | Any user interface meets the client's accessibility standard? | | | |
| 25 | Exit and portability | Data, prompts, workflows and configuration exportable; format; rebuild path on another platform? | | | |
| 26 | Exit and portability | Contract terms on termination, data return and deletion? | | | |
| 27 | Compliance | Sector overlays from the industry pack that impose technical requirements? | | | |
| 28 | Support | Hours, response times, escalation path, who handles the error queue? | | | |
