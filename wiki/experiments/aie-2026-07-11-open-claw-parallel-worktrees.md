# Use Open Claw as a spec-focused orchestrator above Claude Code to parallelize work across git worktrees

> Back to [[experiments-index]]

Source: **[Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](https://www.youtube.com/watch?v=9arM9b7JgOo)** · aie · 2026-07-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a separate orchestrator agent (Open Claw) that holds task spec and history context while delegating implementation to Claude Code worker agents running in parallel git worktrees, then we achieve higher task throughput because the orchestrator's context stays clean (spec/goals/history) while worker contexts stay focused on code implementation.

## What they did

Jeffrey described a layered agent stack where Open Claw acts as an orchestrator that understands Slack history, task specs, and goals — keeping ~25% of context budget for high-level reasoning rather than implementation details. Claude Code worker agents run in parallel git worktrees (managed via tmux terminals) handling actual code changes. He uses a staged environment pattern: local development worktree for active work, a sandbox/staging worktree for integration tests, merging to production only after gates pass. Model selection is cost-driven: Codex 5.3 as primary, falling back to MiniMax when budget runs low. He is actively working toward replacing his own orchestration responses with an agent.

## Relevance to YOLO loop

Maps directly to the YOLO loop's parallelization strategy — separating orchestration context from worker context prevents context contamination and enables multiple simultaneous agent tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-11-open-claw-parallel-worktrees` |
| Channel | aie |
| Video | [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](https://www.youtube.com/watch?v=9arM9b7JgOo) |
| Published | 2026-07-11 |
| Ingested upstream | 2026-07-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
