# Route tasks across model tiers by complexity to minimize token burn

> Back to [[experiments-index]]

Source: **[Don't Use Claude Fable 5 Until You See This](https://www.youtube.com/watch?v=113P6SBWAm8)** · mk · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we assign planning to Fable 5 max/high, execution to Opus 4.8 or Sonnet, and verification back to Fable 5, then we reduce cost significantly while maintaining output quality because the expensive model is only used at decision points, not for bulk work.

## What they did

Speaker analyzed Claude Fable 5's system prompt versus Opus 4.8, noted that Fable 5 auto-downgrades to Opus 4.8 for certain sensitive query types, and used this as a template for a voluntary tiered workflow: use Fable 5 for planning and verification gates, use cheaper models (Opus 4.8, Sonnet) for execution steps, and orchestrate via agents with MCPs and CLI access. He also noted that Fable 5 Medium beats Opus 4.8 Max, giving a cost-quality tradeoff ladder.

## Relevance to YOLO loop

Directly applicable to our agentic dev loop: we can gate expensive model calls to planning and verification phases while routing code generation and bulk edits to cheaper models, reducing token costs in continuous agent runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-11-fable5-tiered-effort-workflow` |
| Channel | mk |
| Video | [Don't Use Claude Fable 5 Until You See This](https://www.youtube.com/watch?v=113P6SBWAm8) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
