# AI Engineering Department

This repo IS the department: 15 skills in `.claude/skills/` and 5 agents in `.claude/agents/`,
covering an AI consulting engagement end to end (discovery, readiness, compliance, architecture,
platform choice, RAG, customisation, agents, rollout, evals/security, optimisation).

- Entry point for any engagement: `.claude/skills/ai-manager/SKILL.md` (the router). Load it first
  and follow its lifecycle gates.
- Shared facts, conventions, the Australian regulatory register and industry packs:
  `.claude/skills/_shared/`.
- Before relying on dated platform or regulatory facts, run
  `python3 .claude/skills/_shared/check_freshness.py` and re-verify anything stale against the
  primary source. Anything marked `PENDING_VERIFICATION` must be verified before it reaches a
  client deliverable.
- Agents are role-gated: architect designs (never builds), engineer builds in sandbox (never
  production), compliance reviews (never legal advice), security tests only with authorisation,
  optimiser proposes (never deploys).
