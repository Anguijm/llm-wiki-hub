# Test Prompt Splitting to Reduce Token Consumption

> Back to [[experiments-index]]

Source: **[Does splitting the prompt cut token use in half?](https://www.youtube.com/watch?v=1v9m-RUfaEY)** · mlops · 2026-09-22

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we split a single large prompt into two smaller sequential prompts, then we can reduce total token usage (potentially near 50%) because each sub-prompt carries less redundant context and system instruction overhead.

## What they did

The speaker tested whether dividing one combined prompt into two separate calls meaningfully reduces token consumption, measuring actual token counts before and after splitting to evaluate the tradeoff between call count and token efficiency.

## Relevance to YOLO loop

Directly applicable to the YOLO loop's LLM call strategy — if prompt splitting reduces cost without degrading output quality, we can restructure multi-step agent prompts into chained smaller calls to lower API spend.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-09-22-split-prompt-token-reduction` |
| Channel | mlops |
| Video | [Does splitting the prompt cut token use in half?](https://www.youtube.com/watch?v=1v9m-RUfaEY) |
| Published | 2026-09-22 |
| Ingested upstream | 2026-09-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
