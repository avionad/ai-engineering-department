# Workflow optimisation (not only the AI)

*v0.1.0, 2026-11-08. The AI step is often not where the time goes. the practice owner's brief for this skill:
optimise "the AI and workflow with time". DDD's payoff language is hours removed, manual steps
eliminated and systems connected (conventions s1). Method is DDD's own; process mapping style
follows `../../ai-agents-automation/references/process-selection.md`.*

## 1. Map the real flow once a quarter (or when overrides spike)

From traces, run logs and a short walk-through with the people doing the work, draw the end-to-end
flow (Mermaid) from trigger to outcome, including every human touch:

- each step, who or what does it, median wait before it and median work time in it;
- every approval, re-key, copy-paste, export or lookup in another system;
- every handoff between people, teams or systems, and where items wait;
- every rework loop (sent back, corrected, re-run).

Use the client's own timings where they exist; where they do not, measure from logs or say
"not measured".

## 2. Look for these patterns

| Pattern | Sign | Typical fix (each is a change set) |
|---|---|---|
| Manual step around the AI | Staff copy AI output into another system | Integration writes directly (with the same approval gate) |
| Double approval | Two people approve the same thing, or a human re-checks what a deterministic rule already checked | Merge approvals; keep one accountable approver; keep the human gate where the agent control spec requires it |
| Approval on everything | Every low-value item waits for a human | Move low-risk items to sampled review (human-in-the-loop H3) only with eval evidence and the owner's written approval (`ai-agents-automation` H-tiers) |
| Waiting handoff | Items sit in a queue between teams | Notifications, routing rules, SLAs set with the client |
| Rework loop | Same correction made repeatedly | Fix the cause (prompt, data, template) and add a golden-set test |
| Re-keying | Same data typed into two systems | Single source of truth plus sync |
| Exceptions by email | Edge cases leave the system | Exception queue inside the workflow with an owner |
| Unused step | A step whose output nobody uses | Remove it (check nothing downstream depends on it first) |

## 3. Guardrails on workflow changes

- Never remove a control the agent control spec or compliance sign-off relies on (approval for
  irreversible, financial or customer-facing actions; logging; kill switch).
- Moving down a human-in-the-loop tier (more autonomy) needs eval evidence and the accountable
  owner's written approval, and is a compliance trigger (re-check the tier and the ADM position
  with the APP 1.7 test -- output substantially and directly related to the decision -- via the
  adm-check in `ai-compliance-risk`; human review alone does not settle it).
- Workflow builds in n8n follow `n8n/n8n-architect`; staging first, like every change.

## 4. Measure

Report hours freed per step from the client's own timings, steps removed, approvals merged, and
median end-to-end time, before and after the deploy date. No assumed productivity multipliers.
