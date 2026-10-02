# Use Hierarchical 'Level' Prompting to Decompose Complex ML Concepts with an AI Research App

> Back to [[experiments-index]]

Source: **[Why Bigger AI Can Make Fewer Mistakes](https://www.youtube.com/watch?v=yU6aNTQ4tyE)** · eh · 2026-10-02

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we structure AI research queries as iterative level-deepening prompts (e.g. 'go deeper', 'show me the numbers', 'wander into X'), then we will produce richer, more connected conceptual maps than a single flat query, because each level surfaces implicit assumptions and edge cases from the prior answer.

## What they did

The presenter used their Drift app to explore why large AI models don't overfit, progressively deepening across 7 levels: data coverage → implicit regularization → double descent → benign overfitting → minimum norm solutions → gradient descent path dependence → early stopping as a directional filter. Each level was triggered by a follow-up question or a pointed challenge to the prior answer. The final map contained 28 connected ideas from one seed question.

## Relevance to YOLO loop

This prompting pattern (iterative level-deepening with explicit challenge prompts) can be applied directly in our research and design phases. Rather than one large context dump, we can chain targeted depth queries to build richer understanding trees before coding.

## Notes

This is both a demo of Drift and an implicit prompting methodology. The actionable experiment is replicating the level-deepening structure in our own tooling or chat interface.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-02-overfitting-seven-levels-drift` |
| Channel | eh |
| Video | [Why Bigger AI Can Make Fewer Mistakes](https://www.youtube.com/watch?v=yU6aNTQ4tyE) |
| Published | 2026-10-02 |
| Ingested upstream | 2026-10-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
