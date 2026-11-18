# Tooling: promptfoo (default), garak and PyRIT (extras)

*v0.1.0, 2026-11-08. Sources: harvested promptfoo red-team docs (MIT, commit 2a6fdf9b), garak
README and probe index (Apache-2.0, commit 89277920), GitHub research area 2 (PyRIT, deepteam,
Giskard). Install and run only inside an environment covered by the authorisation block.*

## 1. promptfoo: default harness

Why default: MIT licence, YAML configs that live in the engagement repo, one tool for functional
evals and red-team, presets for `owasp:llm`, `owasp:agentic` and `mitre:atlas`, and re-runnable
monthly without re-work (GitHub research: "the cheapest client-facing eval harness").

Shape of a config (see the two templates in `../templates/`):

- `targets` (or `providers`): the system under test. Use `id: https` with `url`, `method`,
  `headers`, `body` for an HTTP endpoint in staging, or `file://provider.py` for a custom provider
  that calls the RAG pipeline or agent directly (lets you test retrieval and generation
  separately, per promptfoo's RAG guide).
- `prompts`: for a passthrough target, `'{{query}}'`.
- `tests`: the golden set, each with `vars` and `assert`. Loading tests straight from a CSV
  file is not shown in the harvested docs: `PENDING_VERIFICATION` on promptfoo's live docs;
  until then generate the `tests:` block from `golden-set-template.csv` with a short script.
- `redteam`: `purpose` (describe the system, who uses it, what it may and may not access; this
  drives attack generation and grading), `plugins`, `strategies`, `numTests`, `contexts` (one per
  user role), `frameworks` (filter reporting to `owasp:llm`, `owasp:agentic`, `mitre:atlas`),
  `maxCharsPerMessage`, `language`.
- Custom rules: `policy` plugins, one rule each ("Do not disclose another customer's order").
- Severity overrides per plugin to match the practice table in `red-team-catalogue.md`.

Commands (from the harvested docs): `promptfoo redteam init`, `promptfoo redteam run`
(generate + eval), `promptfoo redteam report`; tag runs with `--tag key=value` (e.g. engagement,
change set ID, git SHA) so results trace to a change.

## 2. Data handling settings (mandatory before the first run)

From the harvested configuration doc:

- **Attack generation and grading use a separate "attacker" provider** (`redteam.provider`),
  not the target. By default promptfoo uses a local OpenAI key if present, and **otherwise
  proxies generation and grading to promptfoo's remote API**. The `purpose` text and generated
  test content then leave our environment.
- Set `PROMPTFOO_DISABLE_REDTEAM_REMOTE_GENERATION=true` and set `redteam.provider` explicitly
  to a provider covered by the engagement's data-handling agreement (for example the same
  Bedrock account in an Australian region, or a local model), **or** keep `purpose` and fixtures
  free of client-confidential detail. Record the choice in the test plan.
- The docs warn that some providers (they name Anthropic) may disable accounts used to generate
  harmful test cases. Use a provider and account whose terms permit red-team generation; confirm
  before a Tier 3 run (`PENDING_VERIFICATION` per provider).
- Local generation quality is lower per the docs; note it in coverage if used.
- Do not log in to promptfoo Cloud for client work unless the data-handling agreement covers it
  (cloud login prefers remote generation by default per the docs).

## 3. garak (extra)

Apache-2.0 LLM vulnerability scanner, model-endpoint focused. Use for a broad probe sweep against
the raw model or a simple endpoint when promptfoo's application-level tests are done, or when the
client self-hosts an open-weight model. CLI shape from the README:
`python3 -m garak --target_type <type> --target_name <name> --spec probes.<module>`; list probes
with `garak --list_probes`. Probe module names in the index include `promptinject`,
`latentinjection`, `web_injection`, `sysprompt_extraction`, `leakreplay`, `dan`, `tap`, `goat`,
`encoding`, `smuggling`, `divergence`, `packagehallucination`, `agent_breaker`. Confirm each
module's behaviour in its docs before relying on it.

## 4. PyRIT (extra, Tier 3)

MIT, multi-turn red-team orchestration (GitHub research; `microsoft/PyRIT`, the `Azure/PyRIT`
location is archived). Use for scripted multi-turn campaigns against high-risk chat or agent
systems. Not harvested: read the current docs at the time of use.

## 5. Others noted in research (not defaults)

deepteam (Apache-2.0, OWASP mapping), Giskard (Apache-2.0, agent testing and scan reports),
inspect_ai (MIT, credible for government clients per `ai-rag-engineering`), ragas and deepeval
(Apache-2.0, RAG metrics). Pick one only with a reason recorded in the test plan.

## 6. Cost control

Red-team runs make many calls: (plugins x numTests x strategies x contexts) generated tests, each
calling the target, plus attacker and grader calls. Estimate before running, set `numTests` low
for the first pass, run in sandbox with a spend cap, and get the practice owner's approval for anything
beyond the sandbox budget.
