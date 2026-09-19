# Build an agent memory harness that persists and retrieves task-relevant context across YOLO loop iterations

> Back to [[experiments-index]]

Source: **[Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](https://www.youtube.com/watch?v=xs-ob87TTzg)** · aie · 2026-09-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we engineer an explicit memory harness layer into an agent loop that stores and selectively retrieves prior task context, then agents maintain coherent long-running task state without requiring the full history in every context window because structured memory retrieval is more token-efficient and accurate than naive context accumulation.

## What they did

Based on title inference only — no transcript available. Ignacio Martinez presented on agent memory architecture ('Total Recall') and harness engineering patterns for giving agents persistent memory across sessions or tool calls.

## Relevance to YOLO loop

Directly relevant — the YOLO loop requires agents to maintain state across iterations; a formal memory harness pattern could replace ad-hoc context stuffing and improve both reliability and cost.

## Notes

No transcript available; inferred from title. Oracle context suggests enterprise-scale memory patterns — worth watching for harness architecture specifics.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-19-agent-memory-harness-engineering` |
| Channel | aie |
| Video | [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](https://www.youtube.com/watch?v=xs-ob87TTzg) |
| Published | 2026-09-19 |
| Ingested upstream | 2026-09-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
