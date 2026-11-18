# ai-evals-security-testing

Designs the eval suite (golden set from the client's real examples, masked; test types per pattern for RAG, extraction, agents and chat; pass thresholds set with the client and recorded; baseline; regression rule), red-teams it against OWASP LLM and Agentic Top 10 IDs and MITRE ATLAS 2026.10 (prompt injection, leakage, PII, jailbreak, excessive agency, unbounded consumption, output handling, supply chain), compares guardrail options, runs promptfoo as the default harness, and writes the PASS / PASS WITH CONDITIONS / FAIL test report. Written authorisation first, always.

**When to use:** Use when an AI system the practice built or is authorised to test needs proving before go-live, after a material change, or in the monthly loop.

**Trigger phrases:** eval the AI, test the chatbot, red team the AI, AI security test, prompt injection test, jailbreak test, pre-launch AI test, golden set, eval baseline, regression test the prompt, permission leak test, PII leakage test, guardrails, NeMo Guardrails, Bedrock Guardrails, promptfoo, garak, PyRIT, OWASP ...

## How SKILL.md is organised

- Department relationships
- Hard rules
- Method (mirrors `ai-security-tester` Method 1 to 6)
- Guardrails (build choices, not test results)
- Tooling
- Outputs and locations
- Size bands
- Do not
- Known gaps (v0.1.0)

## References

| File | What it holds |
|---|---|
| `references/eval-design.md` | **Eval design: golden set, test types, thresholds, baseline, regression.** v0.1.0, 2026-11-08. Method step 2 of `ai-evals-security-testing`. Sources: research B6 (evals. |
| `references/guardrails-options.md` | **Guardrails: build choices.** v0.1.0, 2026-11-08. Guardrails are controls chosen at design time (`ai-architect`) and built by. |
| `references/red-team-catalogue.md` | **Red-team test catalogue.** v0.1.0, 2026-11-08. Method step 3 of `ai-evals-security-testing`. Run by `ai-security-tester`. |
| `references/tooling.md` | **Tooling: promptfoo (default), garak and PyRIT (extras).** v0.1.0, 2026-11-08. Sources: harvested promptfoo red-team docs (MIT, commit 2a6fdf9b), garak. |
| `references/vendored-provenance.md` | **Vendored provenance: ai-evals-security-testing.** v0.1.0, 2026-11-08. Every harvested file this skill read or adapted, with repo, licence and. |

## Templates

| File | What it holds |
|---|---|
| `templates/golden-set-template.csv` | **golden-set-template.**. |
| `templates/promptfoo-agent-example.yaml` | **promptfoo config template: tool-using agent (functional evals + red-team).** description: 'Example Retail refund agent: staging eval and red-team'. |
| `templates/promptfoo-rag-example.yaml` | **promptfoo config template: RAG knowledge assistant (functional evals + red-team).** description: 'Example Co policy assistant: staging eval and red-team'. |
| `templates/security-test-report.md` | **AI security and evaluation test report: {system name}.** Template v0.1.0 (ai-evals-security-testing), 2026-11-08. |
| `templates/test-plan.md` | **AI test plan: {system name}.** Template v0.1.0 (ai-evals-security-testing), 2026-11-08. |

## Scripts

| File | What it holds |
|---|---|
| `scripts/eval_compare.py` | **!/usr/bin/env python3.** """Compare two AI eval result CSVs (baseline vs current) and return a verdict. |

*Skill version 0.1.1. Start with `SKILL.md`; it reads the shared conventions in `../_shared/` first.*
