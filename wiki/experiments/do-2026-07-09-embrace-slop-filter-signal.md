# Generate 100 variants and apply judgment to select the best output

> Back to [[experiments-index]]

Source: **["Stop prompting, start building LOOPS." - swyx](https://www.youtube.com/watch?v=EWk9PBbKqzc)** · do · 2026-07-09

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we intentionally generate large numbers of agent outputs (landing pages, designs, prototypes) and treat filtering and judgment as the primary skill, then the useful signal extracted per unit of developer time will increase, because the bottleneck shifts from generation to curation.

## What they did

swyx argued that when everyone can generate 100 landing pages or 100 designs for a single feature, the scarce skill becomes judgment. He said people who have the stomach for slop are underrated, and that non-consensus embrace of slop is a career bet with low downside since the company pays compute costs while the engineer gains first-mover advantage on novel agent use cases.

## Relevance to YOLO loop

Maps to the evaluation and selection step of the yolo loop: rather than prompting once and iterating manually, the loop fans out many generations and the developer's role becomes a ranker/filter, which can itself be partially automated with a critic agent.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-09-embrace-slop-filter-signal` |
| Channel | do |
| Video | ["Stop prompting, start building LOOPS." - swyx](https://www.youtube.com/watch?v=EWk9PBbKqzc) |
| Published | 2026-07-09 |
| Ingested upstream | 2026-07-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
