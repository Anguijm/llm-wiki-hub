# Shrink the system prompt for newer Claude models and remove constraining examples

> Back to [[experiments-index]]

Source: **[Field Guide to Fable — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=9fubhllmsBU)** · aie · 2026-07-06

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we reduce the Claude Code system prompt size and remove few-shot examples for Fable-class models, then task performance will improve because newer models are more imaginative than the examples we provide and examples actively constrain their output rather than guiding it.

## What they did

Thariq described that Anthropic removed 80% of the Claude Code system prompt when moving to the latest model class. He explained that the pattern has inverted over generations: early models needed small prompts with lots of examples, mid-generation models benefited from large prompts with many examples and tools, but the newest models (Fable) perform better with smaller prompts that provide context rather than constraints, and where few-shot examples are removed because the model is more imaginative than the examples given.

## Relevance to YOLO loop

Directly impacts our YOLO loop system prompt design. We should audit our current Claude system prompt, strip constraining do-not instructions and representative examples, and replace them with high-level context about goals and environment, then benchmark task completion quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-06 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-06-shrink-system-prompt-fable` |
| Channel | aie |
| Video | [Field Guide to Fable — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=9fubhllmsBU) |
| Published | 2026-07-06 |
| Ingested upstream | 2026-07-06 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
