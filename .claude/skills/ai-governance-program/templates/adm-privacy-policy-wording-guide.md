<!-- Audience: client privacy officer and legal adviser. Save as
created/docs/security/adm-privacy-policy-draft-{client}-{YYYY-MM-DD}.md -->

# ADM-ready privacy policy wording guide (draft for the legal adviser)

*v0.1.0, 2026-11-08. Register row AU-8: POLA Act 2024, APP 1.7 to 1.9, **commences 10 December
2026**. OAIC final guidance 30 September 2026. Sources: [OAIC APP 1 guidelines](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information),
[Allens, Oct 2026](https://www.allens.com.au/insights-news/insights/2026/10/mandatory-automated-decision-making-disclosure-requirements-are-coming-key-takeaways-from-the-oaic-guidance/),
[Gilbert + Tobin](https://www.gtlaw.com.au/insights/automated-decision-making-transparency-under-the-privacy-act).*

> **DDD drafts; the legal adviser decides.** This guide and any wording produced from it identify
> regulatory considerations for review by the client's legal adviser. It is not legal advice.
> OAIC-prescribed wording or format, if any, is not in DDD's register: the adviser checks the
> OAIC guidance directly. Penalty exposure is `PENDING_VERIFICATION`; do not mention a figure.

## Inputs (from `ai-compliance-risk` mode c)

The ADM inventory table: every system and decision type with the three limbs answered, the
"solely by the program" vs "substantially and directly related" classification, and the kinds of
personal information used.

## What the policy must cover (for in-scope decisions)

1. The **kinds of personal information** used in the operation of the computer programs.
2. The **kinds of decisions made solely by** the operation of the programs.
3. The **kinds of decisions for which a thing substantially and directly related to making the
   decision is done** by the operation of the programs.

## Drafting principles

- **Kinds, grouped by what matters to the person**, not a list of product names. Group by
  decision type ("decisions about your application for credit"), then say what the program does.
- **Plain English.** The reader is the affected individual.
- **Do not imply human review removes automation.** If a person reviews a score, say the program
  produces the score and a person makes the decision; do not say "no automated decisions are made".
- **Cover vendor-embedded tools** the client has arranged to use.
- **Do not overclaim safeguards.** Only describe testing, review and contestability that exist
  (ACL, AU-22, applies to misleading statements).
- **Keep it maintainable.** The privacy officer updates it when the ADM inventory changes; link
  the inventory to the AI register.

## Skeleton (to adapt; illustrative, not approved wording)

> **Automated decision-making**
>
> We use computer programs to help make some decisions that could significantly affect you.
>
> *Decisions made by a computer program without a person deciding:* {kind of decision, e.g.
> "whether an online application is complete enough to proceed to assessment"}. {If none: "We do
> not currently make decisions of this kind solely by computer program."}
>
> *Decisions where a computer program does something substantially and directly related to the
> decision, and a person then decides:* {kind, e.g. "assessing applications for {service}: a
> program scores applications against our criteria and a staff member makes the decision"}.
>
> *Personal information used by these programs:* {kinds, e.g. "contact details, application
> answers, transaction history, identity verification results"}.
>
> *If you have questions about a decision,* {how to ask; how to request a person's review if
> offered}.

## Common situations

| Situation | Drafting note |
|---|---|
| Recruitment ATS ranks or filters candidates | Usually "substantially and directly related"; AHRC checklist (AU-24) also says no solely automated rejection: consider changing the process, not only the wording |
| Credit, insurance, tenancy scoring | Usually in scope; sector rules in the industry pack may add duties |
| Customer service chatbot that only answers questions | Often not a decision with significant effect; record the reasoning in the inventory |
| Chatbot that approves refunds or eligibility | Likely in scope |
| Spreadsheet formula deciding discounts or eligibility per person | Can be in scope: it is a computer program |
| Fraud flag that freezes an account | Likely in scope |

## Hand-over checklist

- [ ] ADM inventory attached and dated
- [ ] Draft wording marked DRAFT for legal review
- [ ] Systems where process change is better than disclosure listed separately
- [ ] Owner and review trigger for keeping the section current
- [ ] Target live date before 10 December 2026
