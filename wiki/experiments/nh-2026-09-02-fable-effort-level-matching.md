# Match Fable 5.1 Effort Level to Task Complexity to Reduce Token Burn

> Back to [[experiments-index]]

Source: **[I Analyzed How Anthropic ACTUALLY Prompts Fable 5.1](https://www.youtube.com/watch?v=FBVNS1l5Vb8)** · nh · 2026-09-02

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we deliberately dial Fable 5.1's effort level down to low or medium for routine tasks instead of leaving it on the default high setting, then we will consume significantly fewer tokens per session while achieving comparable output quality, because Fable 5.1 on low is approximately equivalent to Fable 5 on medium/high for most non-frontier tasks.

## What they did

Nate pulled Anthropic's official Claude platform documentation and found benchmark data showing Fable 5.1 on low effort performs comparably to Fable 5 on medium/high, yet costs less. He observed that most users leave the effort slider on high by default, which is overkill for the majority of tasks. He recommended auditing tasks and consciously choosing the lowest effort level that meets the quality bar.

## Relevance to YOLO loop

In the YOLO loop, many subtasks (file reads, simple edits, status summaries) don't require max reasoning; routing these to low-effort Fable calls would free up token budget for the high-complexity planning and verification steps.

## Notes

Nate also recommends running /claude-api prompt-audit on existing skills to remove redundant instructions that constrain Fable 5.1 unnecessarily. Pair that with effort-level tuning for compounding token savings.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-02-fable-effort-level-matching` |
| Channel | nh |
| Video | [I Analyzed How Anthropic ACTUALLY Prompts Fable 5.1](https://www.youtube.com/watch?v=FBVNS1l5Vb8) |
| Published | 2026-09-02 |
| Ingested upstream | 2026-09-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
