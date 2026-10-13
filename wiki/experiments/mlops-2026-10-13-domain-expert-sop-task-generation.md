# Generate eval tasks from domain-expert SOPs rather than synthetic prompts

> Back to [[experiments-index]]

Source: **[AAIF Reading Group: Measuring Agent Policy Compliance](https://www.youtube.com/watch?v=HglV1_EF7tA)** · mlops · 2026-10-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we derive agent eval tasks by having domain experts write down their actual SOPs and then generate task variants with verifiers from those SOPs, then our evals will better reflect real-world compliance failures, because the benchmark showed that SOP-grounded tasks expose failure modes that generic benchmarks miss.

## What they did

The paper's methodology involved recruiting two domain experts per domain, having them write SOPs, deriving tasks and variations from those SOPs, and building per-variation verifiers. This grounded evaluation in real procedural knowledge rather than synthetic or academic tasks.

## Relevance to YOLO loop

Our dev loop evals are currently synthetic. Introducing one SOP-derived task set for a domain we care about (e.g., code review policies) would give us a much higher-signal eval suite.

## Notes

Two domain experts per domain was sufficient in the paper. Start with one domain and one SOP to keep scope manageable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-10-13-domain-expert-sop-task-generation` |
| Channel | mlops |
| Video | [AAIF Reading Group: Measuring Agent Policy Compliance](https://www.youtube.com/watch?v=HglV1_EF7tA) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
