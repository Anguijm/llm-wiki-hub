# Classify and Tier Memories by Sensitivity to Improve Agent Context Hygiene

> Back to [[experiments-index]]

Source: **[Fable 5.1 Scores Better. So Why Is Its Prompt So Much Bigger?](https://www.youtube.com/watch?v=cHVB2e-V80Y)** · mk · 2026-09-02

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we adopt Fable 5.1's internal memory classification scheme (global/project memories vs. sensitive memories vs. banned/no-store items) in our own external memory files, then agents will retrieve context more precisely and avoid surfacing irrelevant or sensitive information in unrelated tasks, because structured memory tiers prevent noisy context injection.

## What they did

Mark analyzed the leaked Fable 5.1 system prompt (40,000 words vs. 17,500 for Fable 5) and found Anthropic added explicit memory classification instructions: writing-style memories merge into global memory; health/religion details are tagged as sensitive and only invoked when topically relevant; credit card numbers and self-harm content are in a no-store banned list. He noted this structured memory taxonomy is new in 5.1 and absent from Fable 5's prompt.

## Relevance to YOLO loop

The YOLO loop's CLAUDE.md and external memory files are currently flat; adding explicit sensitivity tiers (global, project, sensitive, banned) would let agents load only relevant context per task and avoid accidentally surfacing private details in general-purpose sessions.

## Notes

Mark also notes Anthropic's prompt now includes proactive skill/plugin suggestion — the model can identify that a current skill is insufficient and propose installing a better one mid-session. Worth testing whether Fable 5.1 actually surfaces this behavior in Claude Code.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-09-02-fable51-system-prompt-analysis` |
| Channel | mk |
| Video | [Fable 5.1 Scores Better. So Why Is Its Prompt So Much Bigger?](https://www.youtube.com/watch?v=cHVB2e-V80Y) |
| Published | 2026-09-02 |
| Ingested upstream | 2026-09-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
