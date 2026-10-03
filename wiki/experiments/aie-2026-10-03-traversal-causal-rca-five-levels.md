# Replace Symptom-Correlation Alerting With Causal Graph Search for Production Incidents

> Back to [[experiments-index]]

Source: **[The 5 Levels of Self-Driving Production — Eric Schwartz, Traversal](https://www.youtube.com/watch?v=y-OVWZD4j6U)** · aie · 2026-10-03

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build or adopt a root-cause analysis system that uses a causal graph of production entity relationships (rather than correlation-based observability dashboards), then incident resolution time will decrease significantly because multi-hop root causes (e.g., expired TLS certificate causing checkout API failure) can be found in minutes rather than hours of war-room debugging.

## What they did

Eric Schwartz of Traversal described their core thesis: RCA is a causal problem, not an observability problem. Their system builds a 'production world model'—a graph of relationships between all monitored entities—and uses a causal search engine to traverse it. In a demonstrated enterprise case, a checkout API failure required five to ten hops across dozens of services to reach the expired TLS certificate root cause. Traversal's agent found it and posted findings to a ServiceNow ticket, reducing a 53-engineer war room page to zero or one targeted page. They framed this as Level 4/5 on a self-driving production autonomy scale.

## Relevance to YOLO loop

Applies to our production reliability layer. Even a lightweight version of this—building a dependency graph of our services and scripting a causal traversal agent to check it on alert—would reduce the manual 'which service caused what' triage that currently interrupts development flow.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-03-traversal-causal-rca-five-levels` |
| Channel | aie |
| Video | [The 5 Levels of Self-Driving Production — Eric Schwartz, Traversal](https://www.youtube.com/watch?v=y-OVWZD4j6U) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
