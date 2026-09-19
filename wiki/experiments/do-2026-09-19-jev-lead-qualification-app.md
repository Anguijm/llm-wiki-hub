# Build a Jev-powered lead qualification form that returns real-time scored decisions

> Back to [[experiments-index]]

Source: **[Build Anything with Jev, Here's How](https://www.youtube.com/watch?v=f6We53TnkbU)** · do · 2026-09-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace a static intake form with a Jev-backed classifier that scores leads as disqualified/mediocre/qualified/highly-qualified in ~100ms, then we can filter pipeline quality without an LLM round-trip because Jev returns calibrated probability decisions with no output tokens.

## What they did

David built a lead qualification web app using Jev (from TypeSafe AI) as the decision engine, deployed it on a Hostinger VPS via Coolify, and configured environment variables for authentication. Jev evaluated form submissions against configurable criteria and returned tiered qualification scores in real time. He delegated prompt configuration to an AI assistant (Astra) and showed the app correctly staying at 'mediocre' when trolling inputs were submitted, without any manual prompt tuning.

## Relevance to YOLO loop

Directly applicable as a fast classification layer in any YOLO loop intake or triage step — replaces slow LLM calls for routing/scoring with a sub-200ms Jev decision, freeing heavier models for generation tasks only.

## Notes

Jev available via TypeSafe AI waitlist or OpenRouter/Vercel gateway. Output tokens are free; only input tokens billed.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-09-19-jev-lead-qualification-app` |
| Channel | do |
| Video | [Build Anything with Jev, Here's How](https://www.youtube.com/watch?v=f6We53TnkbU) |
| Published | 2026-09-19 |
| Ingested upstream | 2026-09-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
