# Audit and Prune System Prompts and Skills After Each Major Model Upgrade

> Back to [[experiments-index]]

Source: **[I Deleted All My Claude Skills... And Claude Got Smarter](https://www.youtube.com/watch?v=XNQBCRcwXV4)** · nh · 2026-08-12

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we delete or significantly reduce accumulated skills, system prompt instructions, and hooks whenever a new major model releases, then agent output quality will improve because newer, more capable models are being constrained by instructions that were compensating for weaknesses that no longer exist.

## What they did

The speaker summarized an interview with Boris (creator of Claude Code) who revealed that Anthropic deleted over 80% of Claude Code's system prompt for Opus 5 because the model no longer needed corrections that prior models required. Boris recommended that users delete their skills, hooks, and system prompts every six months to see what the model can do natively. The speaker tested this by removing his Claude.md and all skills from a repo copy, finding that business context routing (where files live) remained valuable but task-specific instructions often got in the model's way. He framed it as analogous to giving a 10-year experienced worker the same micro-detailed instructions as a 10-year-old—it limits their ability to use their expertise.

## Relevance to YOLO loop

We accumulate system prompts and agent instructions over time; this experiment suggests we should schedule a pruning pass after each major model release to remove compensatory instructions and re-test baseline capability before re-adding only what is still needed.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-12-delete-skills-unhobble-model` |
| Channel | nh |
| Video | [I Deleted All My Claude Skills... And Claude Got Smarter](https://www.youtube.com/watch?v=XNQBCRcwXV4) |
| Published | 2026-08-12 |
| Ingested upstream | 2026-08-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
