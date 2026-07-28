# Model the full signal-to-code pipeline as explicit stages with feedback loops

> Back to [[experiments-index]]

Source: **[How Forward Deployed Engineering is done at Factory — Eno Reyes](https://www.youtube.com/watch?v=wpOA-UXynoM)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we explicitly model each stage of our software development process (signal ingestion → triage → planning → implementation → validation → deployment) as discrete nodes with measurable throughput, then we can identify which stage is the bottleneck for agent automation, because treating it as a factory pipeline exposes hidden hand-offs that block end-to-end autonomy.

## What they did

Eno described a 'software factory' mental model where external signals (bug reports, Slack messages, executive decisions, customer conversations) flow in one side, get triaged and prioritized by humans or agents, converted into code changes, validated (code review, QA, security), and then deployed. He argued that every organization implicitly runs this pipeline and that Factory's product provides building blocks to make each stage explicit and automatable.

## Relevance to YOLO loop

The YOLO loop is exactly this pipeline. Making each stage explicit with measurable latency and error rates would let us systematically apply agents to the highest-friction stage rather than opportunistically.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-factory-signal-flow-software-factory` |
| Channel | aie |
| Video | [How Forward Deployed Engineering is done at Factory — Eno Reyes](https://www.youtube.com/watch?v=wpOA-UXynoM) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
