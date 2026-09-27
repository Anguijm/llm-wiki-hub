# Use GEPA-Style Reflection Loops to Optimize Agent Behavior Without RL

> Back to [[experiments-index]]

Source: **[Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](https://www.youtube.com/watch?v=OA-Mc60Rboo)** · aie · 2026-09-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement a structured reflection loop (GEPA-style) where agents evaluate and revise their own outputs using natural language feedback rather than reward signals, then we can match or exceed RL-tuned agent performance because reflection provides dense, interpretable feedback that is cheaper and faster to iterate on than RL training.

## What they did

Lakshya Agrawal presents GEPA, a framework that uses LLM-based reflection as a substitute for reinforcement learning to optimize agent behavior across arbitrary tasks. The system generates natural language critiques of agent outputs, feeds them back as context, and iterates — reportedly outperforming RL baselines on several benchmarks.

## Relevance to YOLO loop

Directly applicable to the YOLO loop's self-improvement layer — GEPA's reflection mechanism could replace or augment manual prompt iteration with automated self-critique cycles.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-26-gepa-reflection-beats-rl` |
| Channel | aie |
| Video | [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](https://www.youtube.com/watch?v=OA-Mc60Rboo) |
| Published | 2026-09-26 |
| Ingested upstream | 2026-09-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
