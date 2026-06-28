# Audit task distribution to identify center-vs-edge work before model switching

> Back to [[experiments-index]]

Source: **[GLM 5.2 Is Free And Beats Claude On Most Work. So Why Can't Companies Switch?](https://www.youtube.com/watch?v=Zp8lr6IzUnQ)** · nb · 2026-06-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we classify our AI task load by whether tasks are center-of-distribution (familiar patterns, easy to verify) vs edge-of-distribution (novel, ambiguous, high-stakes), then we can safely route center tasks to cheaper open-source models like GLM 5.2 and preserve frontier models only for edge tasks, because model quality differences matter far less for well-trodden problem shapes.

## What they did

Speaker evaluated GLM 5.2 across everyday AI tasks (brochure sites, PowerPoint outlines, routine synthesis, familiar coding problems) and found it matched or exceeded Claude for center-of-distribution work. He argued that companies fail to switch because they haven't measured their task distribution and because model-switching requires rewriting the entire harness (prompts, memory, tool calls) not just swapping an API endpoint. He cited Flo Crivello's Lindy team as a case study who had to rewrite their harness from scratch to move to DeepSeek.

## Relevance to YOLO loop

Directly informs which model to wire into each stage of the YOLO loop. A task-distribution audit would let us decide which loop steps (e.g. boilerplate generation, summarisation) can be routed to a free/cheap model vs which (e.g. novel architecture decisions, ambiguous debugging) need Claude Opus.

## Notes

Speaker also warns about 'renting company brain' to frontier providers via tools like Claude Projects — worth considering for long-term context ownership strategy.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-28-glm52-harness-last-mile` |
| Channel | nb |
| Video | [GLM 5.2 Is Free And Beats Claude On Most Work. So Why Can't Companies Switch?](https://www.youtube.com/watch?v=Zp8lr6IzUnQ) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
