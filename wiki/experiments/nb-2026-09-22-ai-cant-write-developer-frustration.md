# Benchmark AI Code Agents on Documentation and Comment Writing Quality

> Back to [[experiments-index]]

Source: **[Why Developers Are Losing Their Minds Over AI That Can't Write](https://www.youtube.com/watch?v=tYugqJ9YytQ)** · nb · 2026-09-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add explicit documentation and inline comment generation as a graded evaluation criterion in our agent loop, then code output quality improves measurably because AI models deprioritize readable prose writing in favor of functional code, creating a hidden quality gap.

## What they did

Nate Jones examines why developers are frustrated with AI coding tools that produce functional code but fail at writing clear documentation, comments, READMEs, and explanatory prose, arguing this is a significant underappreciated failure mode of current AI dev tools.

## Relevance to YOLO loop

Our YOLO loop evaluates correctness of generated code but likely does not score documentation quality. Adding a prose/documentation rubric to our eval harness would catch this failure mode before it accumulates as technical debt.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-22-ai-cant-write-developer-frustration` |
| Channel | nb |
| Video | [Why Developers Are Losing Their Minds Over AI That Can't Write](https://www.youtube.com/watch?v=tYugqJ9YytQ) |
| Published | 2026-09-22 |
| Ingested upstream | 2026-09-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
