# Apply distributed-systems patterns (idempotency, scoped credentials, circuit breakers, explicit transactions) to every agent tool call

> Back to [[experiments-index]]

Source: **[AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](https://www.youtube.com/watch?v=hD9-V56FNRI)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we design agent tool calls with idempotency keys, scoped read/write credentials, circuit breakers for unhealthy dependencies, and explicit compensating transactions for irreversible actions, then we will prevent the class of agent failures caused by timeout ambiguity, credential overreach, retry storms, and cascading failures, because agents act as probabilistic coordinators whose mistakes compound without deterministic controls.

## What they did

Salman walked through the architectural gap between traditional deterministic service coordinators and probabilistic agent coordinators. He used the Air Canada chatbot (stale policy data causing incorrect refunds) and Replit agent (deleting a production database) as examples of failures preventable by standard distributed-systems hygiene. Specific recommendations: persist every step of the agent loop (plan, action, observation, decision) so failures are recoverable; define explicit compensating transactions per step; make all tool calls idempotent so retries are safe; use separate read/write DB permissions with an explicit tool allow-list; tie human approvals to specific parameters (actor, timestamp, action, expiration) not blanket permission; implement circuit breakers to prevent cascading failures on unhealthy dependencies; set max-turns, max-parallelism, and max-spend budgets; trace model called, prompt, tool calls, responses, errors, retrieved context, writes, and approvals for full replay.

## Relevance to YOLO loop

This is a direct safety checklist for the YOLO loop's tool-execution layer: each of these patterns (idempotency, scoped creds, circuit breakers, budget caps, compensating transactions) should be verified before any agent is given write access to production systems.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-distributed-systems-agent-guardrails` |
| Channel | aie |
| Video | [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](https://www.youtube.com/watch?v=hD9-V56FNRI) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
