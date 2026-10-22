# Generate deterministic TypeScript jobs with Claude Code for the vault pipeline

> Back to [[experiments-index]]

Source: **[I Tried 100+ AI Tools. These 7 Are the Best](https://www.youtube.com/watch?v=hgLI491ajG0)** · nh · 2026-10-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we have Claude Code write and deploy fixed TypeScript scripts (e.g. on Trigger.dev or a local scheduler) for the mechanical steps of the capture-verify-publish pipeline, then the weekly newsletter run will be more repeatable and need less agent supervision because the scripts run the same way each time and don't depend on prompt stability.

## What they did

Nate Herk described prompting Claude Code to generate TypeScript scripts for background tasks such as document processing and data synchronization, then deploying them to Trigger.dev, which has a free tier with $5 of monthly execution credits. He pairs a general-purpose coding agent with deterministic serverless execution instead of paying for single-feature SaaS. He cautioned that these scripts still need active supervision when models change. This was described, not shown live.

## Relevance to YOLO loop

high: It applies the Claude Code practice of using the agent to author deterministic code rather than running it as the executor, which cuts token cost and variance in agent workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-19-claude-code-deterministic-jobs` |
| Channel | nh |
| Video | [I Tried 100+ AI Tools. These 7 Are the Best](https://www.youtube.com/watch?v=hgLI491ajG0) |
| Published | 2026-10-19 |
| Ingested upstream | 2026-10-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
