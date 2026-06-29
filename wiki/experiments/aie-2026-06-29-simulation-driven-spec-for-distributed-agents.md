# Use a deterministic simulation environment to let agents design distributed algorithms before implementing them

> Back to [[experiments-index]]

Source: **[The Prompt is the Platform - Dominik Tornow, Resonate HQ](https://www.youtube.com/watch?v=DqtmZE6Hl0g)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we give a coding agent a deterministic simulation environment (with injected failures, full version history, and 'forbidden fruit' trace events showing hidden state) before asking it to write a production implementation, then the agent will produce correct distributed algorithms on the first implementation pass because it can discover and verify correct behavior under partial failure in simulation before committing to concrete infrastructure choices.

## What they did

Dominik Tornow (Resonate HQ) described building a Resonate durable execution server on top of NATS.io. Direct abstract-spec-to-implementation failed: the agent produced a prototype that broke on concurrency, process failure, and network failure. Inserting a concrete specification step (human-driven, making explicit schema/index/transaction boundary decisions) helped but meant the agent couldn't participate in design. The breakthrough was adding a deterministic simulation environment: a Python simulator of the NATS key-value store that (a) injects stale reads via deterministic random generator, (b) enforces optimistic concurrency, (c) emits 'forbidden fruit' trace events revealing whether a read was fresh/stale and what the hidden latest value was. The agent built a proof-of-concept in simulation, derived a concrete spec from verified simulation behavior, then generated the production implementation. Process: abstract spec → simulation → concrete spec → production implementation.

## Relevance to YOLO loop

For any distributed or stateful component in our loop (task queues, memory stores, checkpoint systems), asking the agent to implement directly from spec is risky. Building a thin simulation harness first — even a simple in-process mock with injected failures — gives the agent a feedback-rich environment to discover correct algorithms before touching production infrastructure.

## Notes

Key insight: 'forbidden fruit' trace events (information the production algorithm cannot use but the debugging agent can) are what enable the agent to understand why an algorithm was wrong, not just that it was wrong. The simulation must be deterministic and repeatable to allow the agent to repair against a specific failing trace. Resonate's Discord is the contact point for questions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-simulation-driven-spec-for-distributed-agents` |
| Channel | aie |
| Video | [The Prompt is the Platform - Dominik Tornow, Resonate HQ](https://www.youtube.com/watch?v=DqtmZE6Hl0g) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
