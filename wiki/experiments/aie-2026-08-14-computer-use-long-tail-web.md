# Benchmark a Small Fast Computer-Use Model Against Frontier Models for Long-Tail Web Tasks on Cost and Latency

> Back to [[experiments-index]]

Source: **[Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](https://www.youtube.com/watch?v=Ki980nV0__0)** · aie · 2026-08-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a smaller, domain-specialized computer-use model instead of a frontier model for long-tail web automation tasks, then cost and latency drop by an order of magnitude with negligible accuracy loss because smaller models optimized for browser interaction can match frontier accuracy on saturated benchmarks while running at a fraction of the price.

## What they did

The speaker argued that the long tail of the web (restaurant menus as JPEGs, school district PDFs, Freedom-of-Information-gated data) will never expose APIs, so computer-use agents clicking like humans is the only durable solution. He presented Yutori's Navigator N1.5 model results: comparable accuracy to Opus 4.7 and GPT-4.5 on browser-use benchmarks (within statistical noise), but dramatically better on latency per step and cost per task — approximately $0.80 vs $230 per task on 20-30 step interactions. He also showed that the primary benchmark (internal human-eval trajectories) is now saturated at 97% and needs to be retired for a harder one.

## Relevance to YOLO loop

For YOLO loop steps that require web browsing (research, doc retrieval, form submission), swapping a frontier model for a smaller specialized computer-use model at the agent level could cut per-loop costs by 100-200x on those steps. Worth running a head-to-head on a sample of real loop tasks.

## Notes

Speaker's broader argument: don't wait for the web to provide APIs — it won't for the long tail. Plan the agent architecture assuming browser automation is the permanent interface for most real-world web targets. Model: Navigator N1.5 from Yutori.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-14-computer-use-long-tail-web` |
| Channel | aie |
| Video | [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](https://www.youtube.com/watch?v=Ki980nV0__0) |
| Published | 2026-08-14 |
| Ingested upstream | 2026-08-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
