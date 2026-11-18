# _shared: the department knowledge base

Every skill reads this folder before acting. It holds the facts and conventions that keep 15 skills consistent with each other.

| File | What it does |
|---|---|
| `engagement-conventions.md` | The constitution: lifecycle stages and exit gates, size bands, risk tiers, verification rules (PENDING_VERIFICATION discipline), secrets handling, infrastructure-claim rules. Read first by every skill. |
| `regulatory-register.md` | 40+ row register of Australian (and mapped international) obligations relevant to AI engagements, each with status (in force, commencing, proposed, voluntary) and a verification date. |
| `client-faq.md` | Plain-English answers to the questions end clients actually ask (training on our data, where data lives, what happens when it is wrong), each answer sourced. |
| `DEFINITIONS.md` | Shared vocabulary so every skill means the same thing by risk tier, size band, engagement stage and similar terms. |
| `VENDORED.md` | Register of third-party repositories harvested during the build, with licences and pinned versions. |
| `check_freshness.py` | Rot check: flags any reference file whose verified facts are older than 60 days so stale claims never reach a client. Run it before relying on dated facts. |

## industry-packs/ (15 packs)

One pack per industry: the regulations that bite, the use cases that recur, and the questions to ask in discovery. Packs point at the regulatory register rather than restating it.

- README, aged-care-ndis, construction-trades, education, finance-banking, government, healthcare, insurance, legal, manufacturing, not-for-profit, professional-services, real-estate, recruitment-hr, retail-ecommerce
