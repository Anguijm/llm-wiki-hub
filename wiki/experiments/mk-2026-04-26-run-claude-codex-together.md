# Run Claude and Codex in Parallel on the Same Codebase

> Back to [[experiments-index]]

Source: **[You Can Run Claude AND Codex Together. Here's How.](https://www.youtube.com/watch?v=Fu5KIG2Jm1g)** · @Mark_Kashef · 2026-04-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we orchestrate Claude and OpenAI Codex to work simultaneously on different tasks within the same dev loop, then we can parallelize AI coding throughput and reduce wall-clock time per feature cycle because each model can be assigned to tasks that match its strengths without blocking the other.

## What they did

Speaker demonstrated a workflow where Claude (likely via Claude API or Claude Dev/Cursor) and OpenAI Codex (via CLI or API) are run concurrently on different subtasks of a project, coordinating outputs either manually or through a lightweight orchestration layer so their changes can be merged without conflict.

## Relevance to YOLO loop

Directly extends the YOLO loop by enabling multi-agent parallelism at the task level — instead of one AI agent per loop iteration, two agents work simultaneously, potentially doubling throughput for independent subtasks like writing tests while refactoring code.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-04-26-run-claude-codex-together` |
| Channel | @Mark_Kashef |
| Video | [You Can Run Claude AND Codex Together. Here's How.](https://www.youtube.com/watch?v=Fu5KIG2Jm1g) |
| Published | 2026-04-26 |
| Ingested upstream | 2026-04-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
