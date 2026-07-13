# Use Fable 5 as intent-parsing orchestrator to farm tasks to cheaper sub-models

> Back to [[experiments-index]]

Source: **[Your Next AI Subscription Shouldn't Be ChatGPT 5.6 Or Fable 5. It Should Be Both.](https://www.youtube.com/watch?v=jOWXBzP6nNg)** · nb · 2026-07-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Fable 5 as the central orchestrator that interprets high-level intent and decomposes tasks, then route subtasks to cheaper models (Luna, Grok, GLM), then overall cost drops while output quality stays high, because Fable's strength is generalizing intent and breaking it into actionable steps rather than executing every step itself.

## What they did

Nate built a tool called Ringer that uses Fable 5 as the architect/orchestrator. Fable parses intent and breaks down tasks; cheaper models execute the subtasks. He states he would still use Fable as orchestrator even after GPT 5.6's release because Fable consistently excels at understanding intent and front-end instincts. He also notes Anthropic has strong front-end capabilities.

## Relevance to YOLO loop

Maps directly to multi-agent orchestration in the YOLO loop: one high-capability model as planner/router, cheaper models as workers. Testable by comparing cost-per-task and quality between single-model runs vs. Fable-orchestrated fan-out.

## Notes

Ringer tool link mentioned in video description. Experiment could be replicated with Claude as orchestrator + GPT-4o-mini or Gemini Flash as workers.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-13-fable-as-orchestrator-ringer` |
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
