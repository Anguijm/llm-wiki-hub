# Benchmark Claude Against Your Primary Copilot on Internal Tasks

> Back to [[experiments-index]]

Source: **[Microsoft Is Testing Claude Against Its Own Copilot. Here's Why.](https://www.youtube.com/watch?v=JvCtGjrn_N0)** · NateBJones · 2026-04-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run Claude and our current AI copilot side-by-side on the same real dev tasks, then we will surface concrete quality gaps and justify model-switching decisions because blind internal benchmarking removes vendor bias.

## What they did

Speaker reported that Microsoft is internally pitting Claude against GitHub Copilot on coding and reasoning tasks, using structured evaluation to decide where each model performs better rather than assuming their own model wins.

## Relevance to YOLO loop

Directly applicable to the YOLO loop's model-selection layer. We can run parallel completions from Claude and our current default model on loop-generated prompts and score outputs, feeding results back into model routing logic.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-30-microsoft-claude-vs-copilot` |
| Channel | NateBJones |
| Video | [Microsoft Is Testing Claude Against Its Own Copilot. Here's Why.](https://www.youtube.com/watch?v=JvCtGjrn_N0) |
| Published | 2026-04-30 |
| Ingested upstream | 2026-04-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
