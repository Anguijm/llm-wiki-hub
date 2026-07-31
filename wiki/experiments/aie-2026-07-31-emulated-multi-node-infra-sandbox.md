# Simulate distributed cluster failures inside a single-node sandbox for infra agent training

> Back to [[experiments-index]]

Source: **[Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang](https://www.youtube.com/watch?v=zkX03APVj0M)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we emulate multi-node distributed systems (with flapping nodes, stale replicas, network failures, live traffic) inside a single containerized sandbox, then agents will encounter the full complexity of real infrastructure incidents during training, improving their ability to reason about blast radius and operational consequences.

## What they did

Emulated built sandboxes that simulate distributed clusters (e.g., etcd consensus clusters) within a single node environment. The sandbox includes failing nodes, stale deprecated nodes, rolling deployments, live traffic, and organizational context (tickets, postmortems, customer conversations). Agents must complete infrastructure tasks—like migrating hardware without downtime—while reasoning through unforeseen problems in real time, extending far beyond a simple code diff.

## Relevance to YOLO loop

If our agents need to handle infrastructure tasks, building even a simplified single-node simulation of distributed failure modes (network partition, stale node, rolling deploy conflict) would provide richer training signal than static code environments.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-emulated-multi-node-infra-sandbox` |
| Channel | aie |
| Video | [Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang](https://www.youtube.com/watch?v=zkX03APVj0M) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
