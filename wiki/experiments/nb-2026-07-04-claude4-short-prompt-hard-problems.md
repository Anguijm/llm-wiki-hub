# Use short, high-context prompts on Claude 4 for hard open-ended problems

> Back to [[experiments-index]]

Source: **[Free Fable 5 tokens this weekend? Here's how to max them](https://www.youtube.com/watch?v=RtxUdvSTQGc)** · nb · 2026-07-04

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we give Claude 4 a short prompt with dense novel context about a genuinely hard problem rather than a long prescriptive prompt, then the model will produce higher-quality solutions because preserving its degrees of freedom allows it to explore non-linear solution paths we would not have anticipated.

## What they did

Speaker described deliberately keeping Claude 4 (referred to as Fable 5) prompts short while front-loading differentiated context about a complicated problem domain, then letting the model figure out the approach. He argued against long prescriptive prompts on the basis that they constrain the model to linear solutions and waste its reasoning capacity. He also noted this aligns with Anthropic's own guidance.

## Relevance to YOLO loop

Directly applicable to how we write prompts in the YOLO loop's planning and task-decomposition steps. If shorter, context-rich prompts outperform long prescriptive ones for hard coding or architecture tasks, we should audit our system prompts and task descriptions to strip prescriptive scaffolding and instead front-load problem context.

## Notes

Speaker uses 'Fable 5' as a stand-in for Claude 4. Tip is model-agnostic in principle but specifically validated on Claude 4. Worth A/B testing short-context vs long-prescriptive prompts on our hardest loop tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-04-claude4-short-prompt-hard-problems` |
| Channel | nb |
| Video | [Free Fable 5 tokens this weekend? Here's how to max them](https://www.youtube.com/watch?v=RtxUdvSTQGc) |
| Published | 2026-07-04 |
| Ingested upstream | 2026-07-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
