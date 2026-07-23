# Model agent pipeline execution as a DAG and detect structural drift and timing anomalies against a learned baseline

> Back to [[experiments-index]]

Source: **[Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase](https://www.youtube.com/watch?v=u1yaOeEX4e8)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we represent each agent pipeline run as a directed acyclic graph of execution steps with timing metadata, and compare it against a learned baseline DAG, then we can detect anomalies (new steps appearing, steps removed, latency spikes at specific nodes) in near-real-time because structural and statistical deviations from baseline are more actionable than raw log aggregates.

## What they did

Ritvik Pandya from JP Morgan Chase described 'learned execution graphs' for payments API monitoring. Every request is modeled as a DAG of processing nodes (edge layer, gateway, auth, orchestration, etc.) with timing per node. The system learns a per-client baseline DAG (not a global average), then classifies deviations as structural drift (new or removed nodes), scale deviation (timing outside threshold), or distributional drift (pattern shift over time requiring baseline reset). A tiered check system: tier-1 checks the full execution baseline; only if anomalous does it escalate to tier-2 root cause analysis. He reported mean-time-to-discovery reduced to a single window and cited open telemetry + Kafka as the async data feed. Key lesson: label anomalies per endpoint type (not per HTTP method globally) to reduce false positives.

## Relevance to YOLO loop

Our yolo loop's agent runs are currently opaque — we know what was called but not whether the execution structure deviated from normal. Instrumenting each loop run as a DAG and comparing against a baseline would let us detect when agents are taking unusual paths (extra tool calls, skipped steps, latency outliers) before they produce bad outputs, enabling earlier intervention.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-execution-dag-anomaly-detection` |
| Channel | aie |
| Video | [Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase](https://www.youtube.com/watch?v=u1yaOeEX4e8) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
