# Benchmark Single-Model vs. Orchestrated Multi-Model API on Identical Task Suite

> Back to [[experiments-index]]

Source: **[I Battle Tested Sakana Fugu's Fable Killer](https://www.youtube.com/watch?v=GpSqBjW6hR4)** · nh · 2026-06-23

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run the same structured task suite against a single best-in-class model (e.g., Claude Opus) and an orchestrated multi-model API (e.g., Fugu Ultra), then we will find that orchestration does not reliably beat the single model on quality but costs significantly more and takes 4-5x longer, because the manager-model overhead and cross-provider latency outweigh the specialization gains for most tasks.

## What they did

Speaker ran Fugu Ultra (Sakana AI's multi-agent API that dynamically routes to Claude Opus, GPT, Gemini, and others via a conductor model) against Claude Opus 4.8 across 38 pass/fail tasks covering puzzles, traps, specs, and heavy algorithms, graded by Codex. Results: models tied almost every time, Opus won twice, Fugu never won outright. Fugu took 357 total minutes vs 80 for Opus. Fugu cost $50 vs $10 for Opus across all runs — 5x more expensive. Speaker concluded Fugu adds latency and cost without quality uplift for his use cases, while acknowledging the orchestration pattern is the right long-term direction.

## Relevance to YOLO loop

We already manually route tasks between Claude Code and Codex. This experiment quantifies whether automated orchestration (via a conductor API) beats our manual routing on cost, latency, and quality. If manual routing is cheaper and faster, we should document our routing heuristics as a reusable prompt/config rather than paying for an orchestration layer.

## Notes

Speaker used Fugu Ultra inside Claude Code via a markdown config file + API key. He is sharing that config in his free School community. Key metric to track if we run this: total wall-clock time, total cost, and pass/fail rate per task category. Fugu benchmark wins on paper come from benchmark-specific orchestration, not general task quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-23-fugu-multi-model-orchestration` |
| Channel | nh |
| Video | [I Battle Tested Sakana Fugu's Fable Killer](https://www.youtube.com/watch?v=GpSqBjW6hR4) |
| Published | 2026-06-23 |
| Ingested upstream | 2026-06-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
