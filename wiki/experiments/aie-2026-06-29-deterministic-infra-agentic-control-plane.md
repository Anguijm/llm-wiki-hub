# Add a policy validation gateway between agent proposal and tool execution to prevent runaway retry loops

> Back to [[experiments-index]]

Source: **[Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](https://www.youtube.com/watch?v=APh1Vx0oLmQ)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we insert a policy engine between the model's tool-call proposal and the actual execution gateway (so the model only suggests actions, the infrastructure validates and approves them), then recursive retry amplification, cost explosions, and workflow deadlocks will be significantly reduced, because unconstrained model-directed retries are the primary mechanism by which minor API errors escalate into compute incidents.

## What they did

Nishant Gupta (Meta Superintelligence Labs) presented the 'great mismatch' between agentic workloads (stateful, long-running, dynamic execution paths) and cloud infrastructure designed for short-lived deterministic requests. He identified the most dangerous failure mode as uncontrolled retry loops (not hallucinations) and proposed an architecture: model generates proposals → infrastructure validates → policy engine approves → execution gateway enforces. He also advocated for: circuit breakers as tool isolation, rate limits as agent limits, multi-dimensional observability capturing planning decisions and state transitions, layered safety (prompt-level + tool permissions + policy validation + human approvals + audit), and treating humans as exception handlers for ambiguous/high-risk cases.

## Relevance to YOLO loop

Our YOLO loop directly exposes us to retry amplification if a tool call fails mid-run. Adding even a lightweight policy layer (e.g. max retries per tool, cost budget enforcement, escalation on unknown failure mode) before execution would bound blast radius and make production runs safer to leave unattended.

## Notes

Key principle: never let the model directly control production systems. Start minimal: add a retry cap and cost-budget check as the first policy layer. Multi-dimensional tracing (capture planning decisions, not just final outputs) is prerequisite for debugging agentic failures. Human-in-the-loop should be an explicit action in the agent's action space, not an exception path.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-deterministic-infra-agentic-control-plane` |
| Channel | aie |
| Video | [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](https://www.youtube.com/watch?v=APh1Vx0oLmQ) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
