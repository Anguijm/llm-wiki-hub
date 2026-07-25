# Benchmark Opus 5 vs Fable 5 on Real Coding Workflows Inside Claude Code

> Back to [[experiments-index]]

Source: **[I Tested Opus 5 vs. Fable 5. What You Need to Know.](https://www.youtube.com/watch?v=2J3uX8iRNng)** · nh · 2026-07-25

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run identical coding tasks through both Opus 5 and Fable 5 inside Claude Code and track cost, time, and token usage, then we can identify which model delivers better value per task type because Opus 5 is half the price but uses significantly more tokens, making the cost comparison non-obvious.

## What they did

Nate ran ~10 sessions with Opus 5 and ~8 sessions with Fable 5 inside Claude Code on identical prompts including bug-finding in large codebases. He tracked input/output tokens, total cost, and active time per session. He used Codex as an independent judge to score outputs. He found Opus 5 used ~2M output tokens vs ~832K for Fable, took longer on average (~63 min vs ~25 min per session), and despite being half the per-token price, sometimes ended up more expensive due to verbosity. On one coding task Opus scored 93/95 vs Fable's 66/95; on another Fable edged out Opus on code cleanliness. He also tested a tip of using Fable as a delegating orchestrator to preserve context window while Opus handles subagent work.

## Relevance to YOLO loop

Directly informs model selection strategy for our dev loop. The orchestrator/subagent split tip (Fable delegates, Opus executes) is immediately applicable to reduce context burn. Token and cost tracking methodology can be adopted to instrument our own loop sessions.

## Notes

Consolidated results doc offered in Nate's free School community. Key headline: Opus 5 per-token is cheaper but produces far more tokens, so real-world cost depends heavily on task verbosity and verification loop design.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-25-opus5-vs-fable5-claude-code-comparison` |
| Channel | nh |
| Video | [I Tested Opus 5 vs. Fable 5. What You Need to Know.](https://www.youtube.com/watch?v=2J3uX8iRNng) |
| Published | 2026-07-25 |
| Ingested upstream | 2026-07-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
