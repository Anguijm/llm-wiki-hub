# Select model based on personal work-pattern audit, not benchmark scores

> Back to [[experiments-index]]

Source: **[Your Next AI Subscription Shouldn't Be ChatGPT 5.6 Or Fable 5. It Should Be Both.](https://www.youtube.com/watch?v=jOWXBzP6nNg)** · nb · 2026-07-13

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we audit our own prompting habits and task types before picking a model, then we will get better outputs than choosing by benchmark scores alone, because model strengths (e.g., long-prompt persistence vs. high-level intent generalization) map to specific work patterns rather than universal quality.

## What they did

Nate describes a personal framework: instead of looking at benchmark scores first, examine your best work and the process you use to get there, then ask which model accelerates that loop. He uses lengthy verbal prompts via Whisper Flow, which suits GPT 5.6 Soul's persistence and steerability; others who wrestle with high-level ambiguity may prefer Fable 5's generalization. He also uses Fable as the architect/orchestrator in his Ringer tool to break down tasks for cheaper sub-models, and notes that coding-focused users may prefer Luna or Grok.

## Relevance to YOLO loop

Directly informs which model to invoke at each stage of the YOLO loop—orchestrator selection, code generation, and knowledge-work synthesis—based on the nature of the task rather than defaulting to the latest release.

## Notes

Nate also mentions a personal benchmark suite ('Dingo') scoring knowledge-work capability; Soul scored 93. Worth tracking when scores are published publicly.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-13-model-selection-by-work-pattern` |
| Channel | nb |
| Video | [Your Next AI Subscription Shouldn't Be ChatGPT 5.6 Or Fable 5. It Should Be Both.](https://www.youtube.com/watch?v=jOWXBzP6nNg) |
| Published | 2026-07-13 |
| Ingested upstream | 2026-07-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
