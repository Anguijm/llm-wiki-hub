# Run Claude on 'low' effort setting for knowledge-work financial modeling to benchmark cost-quality tradeoff

> Back to [[experiments-index]]

Source: **[Everyone's Testing Claude Fable 5.1 On Code. It Made Me A 37-Second Film.](https://www.youtube.com/watch?v=55rDzRkUVdE)** · nb · 2026-09-04

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we use Claude Fable 5.1 on its lowest effort setting for a complex financial modeling task (DCF model + executive deck), then we get a usable but incomplete artifact (missing sources/checks sheets) at significantly lower token cost, because the model still finishes the core analytical work but skips verification scaffolding.

## What they did

Speaker gave Claude Fable 5.1 on 'low' effort setting a real acquisition (GoPro by Starman) and asked it to research the deal, build a post-acquisition DCF model in Excel, and produce a PowerPoint deck. It returned a 7-sheet workbook and 13-slide deck with working formulas, scenario analysis, and a price-per-share output ($1.15 base case), but lacked a dedicated sources sheet and formula-check sheet. Speaker then ran the same task on 'extra' effort for comparison.

## Relevance to YOLO loop

Directly tests the effort-level dial in a YOLO loop context — useful for deciding when to route tasks to cheaper/faster model settings versus full-effort runs, and for identifying what verification artifacts drop out at lower effort.

## Notes

Speaker notes Fable 5.1 is more token-efficient than Fable 5; cache reads dropped from $1 to $0.25/M tokens. Typical workload ~25% cheaper than Fable 5; highly agentic work ~45% cheaper. Subscription token limits still feel tighter than OpenAI.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-04-low-effort-dcf-model-deck` |
| Channel | nb |
| Video | [Everyone's Testing Claude Fable 5.1 On Code. It Made Me A 37-Second Film.](https://www.youtube.com/watch?v=55rDzRkUVdE) |
| Published | 2026-09-04 |
| Ingested upstream | 2026-09-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
