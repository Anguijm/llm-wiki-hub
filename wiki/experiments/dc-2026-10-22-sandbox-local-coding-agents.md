# Sandbox local coding agents in containers with least-privilege git

> Back to [[experiments-index]]

Source: **[My two cents on the DeepSeek ban in the US and model backdoors](https://www.youtube.com/watch?v=MPj-puRyPTM)** · dc · 2026-10-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run Claude Code and local-model coding agents inside Docker containers with write access limited to feature branches and no direct commits to main, then a poisoned or misbehaving model has a bounded blast radius because it cannot reach host credentials or protected branches.

## What they did

Described confining local AI coding agents (Pi, Codex in VS Code) inside containerized Docker environments, enforcing least privilege by restricting write access to dev branches or forks and forbidding direct commits to main, and running only official upstream weights or verified quantizations in SafeTensors/GGUF formats.

## Relevance to YOLO loop

high: Containerized sandboxes and branch-restricted permissions are a direct harness safeguard for Claude Code agent workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-22 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `dc-2026-10-22-sandbox-local-coding-agents` |
| Channel | dc |
| Video | [My two cents on the DeepSeek ban in the US and model backdoors](https://www.youtube.com/watch?v=MPj-puRyPTM) |
| Published | 2026-10-22 |
| Ingested upstream | 2026-10-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
