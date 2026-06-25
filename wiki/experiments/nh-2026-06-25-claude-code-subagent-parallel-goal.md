# Use /goal + parallel sub-agents to produce a full launch plan in under an hour

> Back to [[experiments-index]]

Source: **[I asked Claude Code to make me as much money as possible](https://www.youtube.com/watch?v=iTY8Q449YNQ)** · nh · 2026-06-25

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Claude Code's /goal command combined with multiple parallel sub-agents each owning a discrete deliverable (positioning, market research, launch plan, outreach templates, content calendar), then we can compress multi-day planning work into under an hour because sub-agents run independent tasks concurrently without the user being the bottleneck.

## What they did

Nate used /goal to declare a complete go-to-market outcome, which caused Claude Code to spin up six parallel sub-agents. Each produced a separate verified file in ~8 minutes. The outputs included ICP, competitor comparison table, 14-day launch plan, outreach drafts and a content calendar, all with citations.

## Relevance to YOLO loop

Maps directly to our planning and sprint-kickoff phases: instead of sequentially prompting for each artifact, issue a single /goal and let sub-agents produce all planning documents in parallel, then review and execute.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-25-claude-code-subagent-parallel-goal` |
| Channel | nh |
| Video | [I asked Claude Code to make me as much money as possible](https://www.youtube.com/watch?v=iTY8Q449YNQ) |
| Published | 2026-06-25 |
| Ingested upstream | 2026-06-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
