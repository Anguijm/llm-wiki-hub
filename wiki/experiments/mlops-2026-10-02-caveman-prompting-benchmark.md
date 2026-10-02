# Benchmark the Quality Cliff of Minimal 'Caveman' Prompts

> Back to [[experiments-index]]

Source: **[The Caveman Prompting Challenge](https://www.youtube.com/watch?v=2QHE75oWT2w)** · mlops · 2026-10-02

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we systematically reduce prompt verbosity ('caveman prompting') across tasks of varying complexity, then we can identify a quality cliff point per model where output degrades, because models differ in how much context they need to maintain coherent output.

## What they did

In conversation, the host proposed a benchmarking challenge: measure how far you can push minimal/caveman-style prompts (few words, stripped context) before output quality falls off, across different task complexities and models. The framing was cost reduction — caveman prompting saves tokens, but over-compression degrades output, especially when compacting conversation history. The idea was to test multiple models, vary task complexity, and map the degradation curve.

## Relevance to YOLO loop

Directly relevant to prompt engineering and cost optimization in the dev loop. If we can identify per-model verbosity thresholds, we can auto-select compression level based on task complexity and model, reducing token costs without quality loss.

## Notes

Proposed as a community/friend challenge in the podcast. No formal methodology described — would need to design task set, complexity tiers, and quality rubric from scratch.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-10-02-caveman-prompting-benchmark` |
| Channel | mlops |
| Video | [The Caveman Prompting Challenge](https://www.youtube.com/watch?v=2QHE75oWT2w) |
| Published | 2026-10-02 |
| Ingested upstream | 2026-10-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
