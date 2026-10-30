# Try a screenshot-scored UI hill-climbing loop

> Back to [[experiments-index]]

Source: **[ELITE Agentic Engineers Are LEAVING THE LOOP... Here’s why](https://www.youtube.com/watch?v=52JX83rGPLc)** · idd · 2026-10-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we have an agent build a UI, screenshot it, score visual similarity against a mock and iterate until a threshold is met, then we get close design matches with little manual prompting because the score gives the loop an objective stop condition.

## What they did

IndyDevDan demoed DeepJ, a cloud-sandbox loop that takes a mock landing page screenshot, builds it, scores the similarity of the result and hill-climbs. The Astra agent reached an 86.1% visual match in a 30-minute loop. He cautions that such loops consume substantial compute and token budgets.

## Relevance to YOLO loop

high: It is a self-scoring verification loop pattern with an objective metric that can be reused in agent harnesses.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-29 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `idd-2026-10-26-recursive-ui-hill-climb-loop` |
| Channel | idd |
| Video | [ELITE Agentic Engineers Are LEAVING THE LOOP... Here’s why](https://www.youtube.com/watch?v=52JX83rGPLc) |
| Published | 2026-10-26 |
| Ingested upstream | 2026-10-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
