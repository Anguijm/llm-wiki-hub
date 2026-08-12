# Append Self-Verification Standards to Agent Task Prompts

> Back to [[experiments-index]]

Source: **[I Deleted All My Claude Skills... And Claude Got Smarter](https://www.youtube.com/watch?v=XNQBCRcwXV4)** · nh · 2026-08-12

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we end every agent task prompt with an explicit success-level goal (SL goal) that defines what 'done' looks like and requires the agent to verify its own output against measurable criteria before reporting completion, then output quality will increase because the agent iterates internally rather than stopping at a first-pass prototype.

## What they did

Drawing on Boris's interview about verification being the single most important thing people get wrong, the speaker described appending SL goals to his prompts: a high-level goal, explicit standards, verification methods the agent must run itself, and language like 'I'm not looking for a prototype—give me something tested and iterated 10 times, fully QA'd, and ready to go to market tomorrow.' He framed the skill shift as moving from prompt engineering to figuring out how to give Claude a hard task and make it possible for Claude to verify its own work along the way.

## Relevance to YOLO loop

Directly applicable to any YOLO loop agent task. Adding a verification clause to our standard task prompt template is a one-line change that could reduce the rate of mediocre first-pass outputs requiring human re-review.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-12-sl-goal-verification-prompt` |
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
