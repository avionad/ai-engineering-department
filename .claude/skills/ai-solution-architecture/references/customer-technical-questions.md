# Answering end-customer technical questions

*v0.1.0, 2026-11-08. DDD method. Standing answers live in `../../_shared/client-faq.md`; this file
is how to answer anything, including questions not in the FAQ.*

## 1. Format

1. **Plain-English answer first**, two to four sentences, in the client's terms (their systems,
   their staff, their customers). Lead with the answer, not the background.
2. **What it means for them**: the decision or action, if any.
3. **Technical appendix for IT**: components, regions, protocols, standards, configuration, with
   a source URL and date for every factual claim about a vendor or a rule.
4. **Disclaimer** on anything regulatory: "This assessment identifies regulatory considerations
   for review by your legal adviser. It is not legal advice."

## 2. Rules

- Check `_shared/client-faq.md` first. If the answer there is older than 60 days, or the question
  goes beyond it, verify against the live vendor or regulator source before answering.
- Never state a model name, region, certification, price, retention period or feature from
  memory. If it cannot be verified now, say what will be checked and by when
  (PENDING_VERIFICATION), and do not guess.
- Distinguish what the design does from what the vendor promises from what the law requires.
- Answer the question asked. If the honest answer is "it depends", say on what, and recommend.
- No jargon in the plain-English part. Standard terms the client already uses (SSO, API) are fine.

## 3. Common questions and where the answer comes from

| Question | Plain-English answer comes from | Appendix comes from |
|---|---|---|
| Where is our data stored and processed? | The data-flow view and the platform ADR | Vendor region docs (URL, date); the deployment table in solution-patterns |
| Will the AI vendor train on our data? | The contract terms found in vendor due diligence | The vendor DD record (`ai-compliance-risk` mode g) |
| Who can see what? | The access-control section | IdP, roles, retrieval filter design, revocation latency |
| What stops it doing something wrong? | The agent controls summary | The agent control spec |
| How accurate is it? | The eval baseline on their own sample, never a vendor figure | Eval method and results (`ai-evals-security-testing`) |
| What does it cost to run? | The run-cost estimate from `ai-proposal-pricing` | Sourced unit prices |
| What happens if the vendor changes or goes away? | Exit path in the ADR and NFRs | Export formats, portability, rebuild estimate |
| Do we have to tell customers it is AI? | Obligations list from `ai-compliance-risk` | Register rows with status, plus the disclaimer |
| Is it secure? | Threat model summary and test results | OWASP IDs, controls, test report |

## 4. Worked shape (illustrative, not a real client)

> **Question (client IT):** Can staff only see documents they already have access to?
>
> **Answer:** Yes, that is how it is designed. When someone asks a question, the system searches
> only the documents that person can already open in SharePoint, using their own sign-in. If
> someone's access is removed, the assistant stops returning those documents once the next
> permission sync runs; we will agree how often that runs with you.
>
> **Appendix:** {identity provider, how the user's identity is passed to retrieval, ACL sync
> method and interval, deny-by-default rule, the permission-leak tests in the eval plan; vendor
> feature claims with URL and date, or PENDING_VERIFICATION}.
