# Apply /compact at defined YOLO session milestones to preserve context within token limits

> Back to [[experiments-index]]

Source: **[18 Claude Code Token Hacks in 18 Minutes](https://www.youtube.com/watch?v=49V-5Ock8LU)** · nh · 2026-04-02

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we run /compact at defined YOLO session checkpoints (after reading learnings.md, after build completes, before logging), then we reduce mid-session token exhaustion while retaining all decision context because /compact preserves key information in a fraction of the tokens.

## What they did

Nate Herk shares 18 practical Claude Code token optimization techniques. Key relevant ones: use /compact aggressively at natural break points, write minimal CLAUDE.md files (every line costs tokens on every session), use sub-agents for isolated tasks to prevent context cross-contamination.

## Relevance to YOLO loop

Long YOLO sessions (Phase 2 refinement, multi-project builds) are most vulnerable to token runaway. Defining 3-4 explicit /compact checkpoints (post-context-load, post-build, pre-logging) would systematize what currently happens ad-hoc.

## Outcome

Added 3 compaction milestones to cron prompt: after reading learnings, after build completes, after council fixes. Each milestone summarizes and discards verbose output to preserve context quality.

## Notes

Extends nb-2026-03-24-context-compression (adopted) with specific /compact workflow. Also relates to nb-2026-04-02-session-isolation-per-task — use both together.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | Integrated into cron prompt |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-02-compact-at-milestones` |
| Channel | nh |
| Video | [18 Claude Code Token Hacks in 18 Minutes](https://www.youtube.com/watch?v=49V-5Ock8LU) |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
