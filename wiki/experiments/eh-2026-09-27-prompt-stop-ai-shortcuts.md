# Test an anti-shortcut system prompt to force thorough AI reasoning

> Back to [[experiments-index]]

Source: **[Can This Prompt Stop AI Taking Shortcuts?](https://www.youtube.com/watch?v=0hM27Q-zTs8)** · eh · 2026-09-27

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we prepend a specifically crafted anti-shortcut prompt instruction before coding or reasoning tasks, then the model will produce more complete and correct outputs because it counteracts the model's tendency to satisfice rather than fully solve.

## What they did

echohive designed and tested a prompt aimed at preventing AI models from taking shortcuts—stopping them from producing plausible-looking but incomplete or lazy responses—and evaluated whether it meaningfully changed output quality.

## Relevance to YOLO loop

High relevance: shortcutting behavior is a known failure mode in the YOLO loop where agents return superficially passing outputs. A validated anti-shortcut prompt could be added to our system prompt template to improve loop reliability.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-09-27-prompt-stop-ai-shortcuts` |
| Channel | eh |
| Video | [Can This Prompt Stop AI Taking Shortcuts?](https://www.youtube.com/watch?v=0hM27Q-zTs8) |
| Published | 2026-09-27 |
| Ingested upstream | 2026-09-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
