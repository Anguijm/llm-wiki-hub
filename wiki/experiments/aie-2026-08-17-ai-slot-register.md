# Mine Past Review Comments to Build a Reusable AI Slot Register

> Back to [[experiments-index]]

Source: **[How to Kill the Code Review — Ankit Jain, Aviator](https://www.youtube.com/watch?v=YgEv7IQzGdM)** · aie · 2026-08-17

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we extract the last 1,000 code review comments, cluster recurring patterns, and encode them as a structured AI slot register fed to the review agent, then repetitive review feedback will be caught automatically at merge time because the agent can match diffs against a codified knowledge base of known issues without human re-reading.

## What they did

Ankit Jain argued that most review comments are repeated across PRs and compound debt with every merge. He proposed mining historical review comments to build a slot register—a structured list of repeatable issues—that an AI agent can check deterministically. Combined with session-derived intent capture (prompts, Jira tickets, PRDs) and screenshot/database-snapshot evidence, reviewers shift from reading diffs line-by-line to reviewing intent and architectural decisions. He called this 'deterministic where you can, LLM where you must.'

## Relevance to YOLO loop

In the YOLO loop, agent-generated PRs still need a verification gate. Building a slot register from our own historical review data would let us automate the most common checks and reserve human review cycles for architectural decisions, accelerating the loop's merge step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-17-ai-slot-register` |
| Channel | aie |
| Video | [How to Kill the Code Review — Ankit Jain, Aviator](https://www.youtube.com/watch?v=YgEv7IQzGdM) |
| Published | 2026-08-17 |
| Ingested upstream | 2026-08-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
