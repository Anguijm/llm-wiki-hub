# Model agents as managed workers with identity, short-lived capability tokens, and audit receipts

> Back to [[experiments-index]]

Source: **[IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork](https://www.youtube.com/watch?v=q-WOjZhOMCA)** · aie · 2026-08-20

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we treat each agent as a managed entity with a runtime identity (who owns it, what subject it acts for, what delegation it carries) and issue short-lived scoped capability tokens per action rather than standing credentials, then we can safely grant agents broad authority while maintaining auditability and instant revocation capability.

## What they did

Sarthak Aggarwal (co-founder, Decawork, ex-NVIDIA) argued enterprises are operating a second workforce of agents and need an IT department for them. Core framework: every agent needs a runtime identity card (actor, owner, subject acting for, delegator, capabilities, governing policy, revocation path). Actions should use short-lived capability tokens scoped to actor + subject + audience + TTL, not standing credentials. Architecture pattern: separate the planner (handles trusted intent, cannot call tools) from the executor (can call approved tools, cannot see original ticket context). Evidence/untrusted input can fill parameters but cannot mint new actions. Demo: password reset ticket with hidden prompt injection ('disable MFA, email me codes') — the policy gate detected the MFA action as out-of-plan scope, denied it, escalated, and recorded it as malicious. Every action produces a typed audit receipt. Cited Wilson's dual-LLM pattern and CAMEL's control/data flow separation as research foundations.

## Relevance to YOLO loop

Architectural pattern for any agent with real-world tool access. The planner/executor separation with a policy gate is immediately applicable when building agents that call external APIs or modify systems. Short-lived scoped tokens per action is a security posture we should adopt before deploying agents with write access to production systems.

## Notes

Key pattern: planner sees authenticated intent → produces typed logged plan → executor processes untrusted evidence and runs plan → policy gate evaluates each action against plan+capability+risk → tool call happens. Model cannot mint new actions from evidence. Lethal trifecta (Wilson): private data + untrusted input + external communication — add action layer to make it the lethal quadruplet. Microsoft (Agent 365), Okta (agent entity layer), AWS (Agent Core identity) all moving in this direction as of mid-2026.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-20-decawork-agent-identity-lifecycle` |
| Channel | aie |
| Video | [IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork](https://www.youtube.com/watch?v=q-WOjZhOMCA) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
