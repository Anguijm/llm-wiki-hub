# Benchmark Claude Haiku or Sonnet against Opus on YOLO Loop tasks and measure cost-quality tradeoff

> Back to [[experiments-index]]

Source: **[Claude Just Told Us to Stop Using Their Best Model](https://www.youtube.com/watch?v=1EPsUXSManU)** · nh · 2026-04-10

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we route routine YOLO Loop tasks to a smaller Claude model instead of defaulting to the flagship model, then we will achieve comparable output quality at significantly lower cost and latency because Anthropic's own guidance suggests flagship models are over-specified for many production tasks.

## What they did

Nate reported that Anthropic recommended against using their most capable model for typical use cases, implying that smaller models in the Claude family handle the majority of production tasks with better cost-efficiency and that the largest model should be reserved for specific high-complexity needs.

## Relevance to YOLO loop

Directly impacts model selection defaults in the loop; a simple routing experiment could reduce API costs significantly without degrading loop output quality.

## Notes

Adopted 2026-04-12: low-effort cost-quality benchmark. Directly complements model-eval-backbone already in tick queue. Merged scope: model-eval-backbone will now also test Haiku/Sonnet vs Opus, not just 'latest vs current'. No separate tick needed — folded into existing model-eval-backbone deliverables.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-10 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-10-claude-stop-using-best-model` |
| Channel | nh |
| Video | [Claude Just Told Us to Stop Using Their Best Model](https://www.youtube.com/watch?v=1EPsUXSManU) |
| Published | 2026-04-10 |
| Ingested upstream | 2026-04-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
