# Client FAQ: questions end customers ask about AI

*v0.1.0, 2026-11-08. Owner: ai-manager. Written by the ai-discovery-scoping build.*

**Re-verify before use.** Every answer carries the date its sources were checked. If that date is
more than 60 days old, re-check the source before the answer goes to a client (conventions s3).
Items marked `PENDING_VERIFICATION` or **[secondary]** (law-firm or vendor blog only, not the
primary source) must not be stated to a client as settled fact. Vendor residency and model
availability change monthly: confirm against the vendor console or docs at design time.

**Legal framing.** Answers about law identify considerations; they are not legal advice. When an
answer is used in a client document, add: "This assessment identifies regulatory considerations
for review by your legal adviser. It is not legal advice."

All sources below come from the department's original research files (internal, not included in this repo)
unless noted. Date checked for all rows: 2026-11-08.

---

### 1. Does our data leave Australia?

It depends on the platform and how it is configured, so we decide it in the design, not by
default.
- **AWS Bedrock:** `au.*` inference profiles keep traffic between Sydney and Melbourne. Which
  models are available on them changes; we confirm at design time.
- **Azure OpenAI / AI Foundry:** a Standard (regional) deployment in Australia East is the route
  used for in-region processing, while Data Zone and Global deployments may process elsewhere. We
  confirm the exact behaviour for your deployment type against Microsoft's current documentation at
  design time rather than relying on this summary (internally still `PENDING_VERIFICATION`).
- **Google Vertex AI:** as at the check on 2026-11-08 only a small number of Gemini models had
  ML processing in Sydney (`australia-southeast1`) and no Claude models were available in
  Australian regions. The exact model list changes, so we read Google's data-residency page for
  your models on the day we design, never from this summary.
- **Anthropic's own API and Claude Enterprise:** global or US-only inference with US storage as at
  October 2026 **[secondary]**.
- **Self-hosted (a VPS in an Australian data centre, or your own servers):** you control the
  location. We would procure Australian hosting for your engagement; we do not hold an Australian
  VPS today, so do not read this as existing DDD infrastructure.
- The search index, logs and caches must sit in the same Australian region as the model, or the
  claim does not hold.

Sources: https://sjramblings.io/keeping-ai-workloads-sovereign-on-aws/ **[secondary]** ;
https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency ;
https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-australia-irap ;
https://www.futureability.com/claude-data-residency-australia **[secondary]**

### 2. If it is processed in Australia, can a foreign government still access it?

Onshore processing does not remove foreign-law access risk (for example the US CLOUD Act) for
providers headquartered in the US. Government and defence-adjacent clients may need sovereign or
on-premises options. **[secondary]**

Source: https://aivy.com.au/resources/ai-data-residency-australia-cloud-act/

### 3. Will the AI provider train its models on our data?

It depends on the product and the contract tier, so we check the specific terms before we
recommend a tool. Our designs require a business or enterprise tenancy whose terms exclude
training on your data (research B1: "enterprise tenancy with no-training terms"), and we do not
use consumer accounts for client data. Each vendor's current terms: `PENDING_VERIFICATION`,
checked per engagement. The OAIC expects due diligence on any AI product
before you use it with personal information.

Source: https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products

### 4. Our staff already use ChatGPT and similar tools. Is that a problem?

It can be. OAIC guidance says best practice is not to enter personal information, and especially
sensitive information, into publicly available generative AI tools. IBM's 2026 Cost of a Data
Breach report found security incidents involving unapproved AI rose from 20% to 43% of
organisations, and about two thirds of breached organisations had no AI governance policy (only 32%
had one, down from 37% the year before). Verified 2026-11-08 against reporting of the 2026 report
(https://www.kiteworks.com/cybersecurity-risk-management/ibm-2026-breach-report-ai-governance/); the earlier "63%" in this file was the 2025 figure. The fix is usually
an approved tool with business terms, plus a simple rule on which data may go where.

Sources: OAIC link in Q3 ; https://www.ibm.com/reports/data-breach

### 5. Who is accountable when the AI gets something wrong?

Your organisation, in the same way it is accountable for its staff and its other systems.
Treasury's 2025 review found the Australian Consumer Law already covers misleading AI claims and
chatbot misstatements. In health, AHPRA says practitioners remain responsible for AI used in their
practice. The national Guidance for AI Adoption (voluntary) starts with "decide who is
accountable". That is why we design human review, escalation and testing into every system.

Sources: https://treasury.gov.au/publication/p2025-702329 ;
https://www.ahpra.gov.au/Resources/Artificial-Intelligence-in-healthcare.aspx ;
https://www.industry.gov.au/publications/guidance-for-ai-adoption

### 6. Do we have to tell customers we use AI?

- **Automated decisions:** from **10 December 2026**, organisations covered by the Privacy Act
  must say in their privacy policy when a computer program makes, or does something substantially
  and directly related to, decisions that could significantly affect individuals' rights or
  interests using their personal information (APP 1.7 to 1.9). It catches everyday software such
  as spreadsheets and chatbots, not just "AI".
- **Other uses:** the research found Australia has no AI Act; it regulates AI through existing
  laws. Sector rules and good practice may still call for disclosure (for example, the Australian
  Human Rights Commission's recruitment checklist says to disclose AI use). If you serve EU
  customers, EU AI Act transparency rules (Article 50) have applied since 2 August 2026.
- We recommend telling customers when they are talking to an AI.

Sources: https://www.allens.com.au/insights-news/insights/2026/10/mandatory-automated-decision-making-disclosure-requirements-are-coming-key-takeaways-from-the-oaic-guidance/ ;
https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information ;
https://humanrights.gov.au/our-work/technology-and-human-rights/publications/ai-and-recruitment-compliance-checklist ;
https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/ **[secondary]**

Penalty exposure for a non-compliant privacy policy: `PENDING_VERIFICATION`.

### 7. If a person checks every AI output, do the automated decision rules still apply?

Usually yes, and sometimes no. The OAIC's fact sheet says a decision "may be within scope ...
even where a computer program output does not replace the entire decision-making process or is
subject to human review", and that advisory outputs count as much as determinative ones. So a
reviewer who routinely accepts the system's recommendation does not take you out of scope.

There is a qualified exception. The OAIC considers such outputs "would generally fall within
scope ... unless subject to extensive human oversight and control". Its own example of what can
tip a tool out of scope is a reviewer who interrogates the output, looks independently at the
underlying facts, narrows the system's parameters, and documents why they departed from its
recommendation.

Which side of that line a particular process sits on is a judgement on your facts, and one for
your legal adviser. What we do is map each decision, record the evidence either way, and design
the review step so the position is defensible rather than accidental.

Source: OAIC, APP 1.7-1.9 Transparency Obligation Fact Sheet, September 2026, https://www.oaic.gov.au/__data/assets/pdf_file/0021/269013/APP-1.7-1.9-Transparency-Obligation-Fact-Sheet.PDF (quotations
verbatim, read 2026-11-08).

### 8. Is there an Australian AI law we must comply with?

There is no standalone AI Act and no mandatory guardrails at this time. The National AI Plan (2
December 2025) regulates AI through existing laws (privacy, consumer, discrimination, work health
and safety, sector rules) and sector regulators, backed by voluntary guidance. Financial services
has the sharpest supervision: APRA's letter to industry on AI (30 April 2026) says it will take
stronger supervisory action where needed.

Sources: https://www.industry.gov.au/publications/national-ai-plan ;
https://www.apra.gov.au/news-and-publications/apra-letter-industry-artificial-intelligence-ai

### 9. What does it cost to run once it is built?

Running costs are separate from the build and depend on your volumes: model usage (charged per
token or per minute for voice), hosting, monitoring, and any ongoing improvement work. We quote
them from the vendor's current pricing page using your own volumes, with the date checked. Levers
that cut cost: Anthropic's Batch API is 50% off tokens processed within a 24-hour window, and
prompt caching reads cost 10% of the base input rate; routing simple tasks to smaller models and
trimming what is sent also help.

Sources: https://platform.claude.com/docs/en/about-claude/pricing ;
https://platform.claude.com/docs/en/build-with-claude/batch-processing.md

### 10. Should we use an open-source model or a commercial one?

Usually start commercial (through an Australian-region cloud where residency matters) and move to
open-weight models only for a measured reason: sovereignty, cost at high volume, or a narrow task a
smaller model handles well. The order that works is prompting, then retrieval over your documents,
then fine-tuning, then distillation; fine-tuning does not reliably add new facts. Open-weight
licences differ: Meta's Llama 4 licence needs a separate licence above 700 million monthly active
users and restricts multimodal rights for EU-based companies; some custom licences need legal
review; some government and critical-infrastructure clients object to certain model origins by
policy. Self-hosting brings operations work.

Sources: https://www.vellum.ai/blog/should-i-use-prompting-rag-or-fine-tuning **[secondary]** ;
https://the-decoder.com/meta-releases-first-multimodal-llama-4-models-leaves-eu-out-in-the-cold/ **[secondary]**

### 11. Can staff only see documents they are allowed to see?

Yes, if it is built that way, and we test it. The search must filter results by the logged-in
person's identity and groups at the moment they ask, never by the application's own access. We
also agree how quickly a removed permission stops showing up (revocation time), block documents
with missing permissions by default, and run "permission leak" tests before go-live. Azure AI
Search supports this natively, and Vertex AI Search supports access control on its data stores
(Cloud Storage, BigQuery, Google Drive and third-party sources, enforced against the logged-in
user's identity provider; verified 2026-11-08). The equivalent on Bedrock Knowledge Bases is
`PENDING_VERIFICATION`.

Sources: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview ;
https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control ;
https://genai.owasp.org/llm-top-10/

### 12. What happens if the vendor goes away, changes the model or raises prices?

Plan for it from the start. APRA's 2026 letter observed that few regulated entities had tested exit
and substitution plans for critical AI providers. Cloud providers retire model versions on a
schedule, so we pin versions and plan migrations. Our designs keep your data, prompts, test sets
and workflows in accounts you own, document how to switch providers, and include exit terms in
vendor due diligence.

Sources: APRA link in Q8 ;
https://techcommunity.microsoft.com/discussions/azure-ai-foundry-discussions/open-ai-model-continuity-plan-for-standard-deployments-in-australia-east/4485447

### 13. How do we know it is working, and keeps working?

Before go-live we build a test set from your real cases and agree a pass mark with you. After
go-live we monitor quality, cost and user feedback, and re-run the tests whenever the prompt,
model or data changes. MIT NANDA's 2025 study found most pilots that failed to show returns used
systems that did not learn from feedback, which is why we build a regular improvement loop in.

Sources: https://www.industry.gov.au/publications/guidance-for-ai-adoption (practice 5, test and
monitor) ; https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/

### 14. Will AI replace our staff?

AI changes tasks; what you do with the time is your decision. We measure hours removed and errors
avoided, and report those. GitHub's adoption playbook advises leaders not to say "your job is safe"
but to explain how jobs will change and how staff will be supported. McKinsey found redesigning
workflows, not just adding tools, has the biggest effect on results. In NSW, a new work health and
safety duty for digital work systems has passed but its duties have not yet commenced.

Sources: https://github.com/github/ai-adoption-playbook (CC BY 4.0) ;
https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai ;
https://australianworkplacesafety.com.au/nsw-digital-work-systems-act/ **[secondary]**

### 15. Will it make things up?

It can, which is why design matters. The industry security list (OWASP Top 10 for LLM
Applications 2025) names misinformation as a core risk (LLM07:2026). Controls: answer from your own
documents with citations, tell users when it does not know, test on real questions before launch,
and keep a person in the loop where errors would matter.

Source: https://genai.owasp.org/llm-top-10/

### 16. Can someone trick or hack the AI?

Yes, if it is not designed against it. Prompt injection was the top-ranked risk on the OWASP LLM list's 2025 edition; a 2026 edition has since changed the ranking, so we re-check before quoting an order, and
the OWASP Top 10 for Agentic Applications (December 2025) covers agents misusing tools or
permissions. For agents we apply "least agency": limited permissions, human approval for
irreversible actions, spending caps, a kill switch and full logs. The ACSC's guidance on careful
adoption of agentic AI services (May 2026) is the Australian reference.

Sources: https://genai.owasp.org/llm-top-10/ ;
https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/ ;
https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services

### 17. Can an AI receptionist or meeting scribe record calls?

Only with the right consent. AHPRA's guidance flags informed consent for tools that record
consultations and possible criminal exposure under surveillance and listening-device laws without
it. Those laws differ by state: state-by-state rules are `PENDING_VERIFICATION` in the regulatory
register. We build a disclosure and consent step into every voice agent.

Source: https://www.ahpra.gov.au/Resources/Artificial-Intelligence-in-healthcare.aspx

### 18. Can you certify us to ISO 42001?

No. Only accredited certification bodies can certify (ISO/IEC 42006 sets the requirements for
them). We prepare organisations for it: gap assessment, policies, register, risk and impact
processes. ISO/IEC 42001 itself is voluntary.

Sources: https://www.iso.org/standard/42006 ;
https://www.iso.org/home/insights-news/resources/iso-42001-explained-what-it-is.html

### 19. Do EU rules apply to us?

Possibly, if you place AI systems on the EU market or their output is used in the EU. After the EU
Digital Omnibus (in force 27 July 2026), high-risk obligations for areas such as employment,
credit and education apply from 2 December 2027, and transparency obligations have applied since
2 August 2026. If you have EU customers or staff, an applicability check is worth doing.

Sources: https://eur-lex.europa.eu/eli/reg/2024/1689/oj ;
https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act **[secondary]**

### 20. We heard 95% of AI projects fail. Is that true?

Not as usually quoted. MIT NANDA's 2025 report found 95% of organisations got zero measurable
return from generative AI pilots, based on 153 survey responses, 52 interviews and 300+ public
implementations. It is a pilot-to-profit finding on a small sample, and its stated cause is that
most systems did not learn or adapt. The practical lesson: pick a measurable problem, set a
baseline, and build in improvement.

Source: https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
