# Define a Reliability Metric Beyond Demo Success Rate for Agent Pipelines

> Back to [[experiments-index]]

Source: **[Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics](https://www.youtube.com/watch?v=Sjfz1TqxzEs)** · aie · 2026-09-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we measure agent pipeline reliability using production-style metrics (failure modes, recovery rate, mean time between failures) rather than demo success rate, then we will surface real brittleness that polished demos hide because reliability requires handling edge cases that curated demos avoid.

## What they did

Jason Ma argued that robotics demos routinely succeed while production deployments fail, and described Dyna Robotics' approach to engineering for reliability rather than demo performance, including their testing methodology and failure recovery systems.

## Relevance to YOLO loop

We tend to judge our agents on happy-path demo success; this experiment would add a reliability harness to our eval suite that specifically probes failure modes and recovery, directly improving our verdict quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-24-dyna-robotics-reliability` |
| Channel | aie |
| Video | [Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics](https://www.youtube.com/watch?v=Sjfz1TqxzEs) |
| Published | 2026-09-24 |
| Ingested upstream | 2026-09-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
