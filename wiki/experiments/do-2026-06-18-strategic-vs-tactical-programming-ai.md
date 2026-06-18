# Redesign Codebase Architecture Explicitly for Agent Readability (AX)

> Back to [[experiments-index]]

Source: **[Matt Pocock's Agentic Engineering Workflow (just copy him)](https://www.youtube.com/watch?v=nQwJVHCtDDY)** · do · 2026-06-18

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we treat codebase architecture as 'agent experience' (AX) — well-scoped modules, clear interfaces, minimal context bloat, and targeted documentation — then AI coding agents will produce higher-quality output on the first pass because the model receives richer, more navigable context and can delegate tactically without requiring human correction loops.

## What they did

Matt Pocock argued that AI has fully consumed 'tactical programming' (writing code, fixing bugs) and that the remaining human edge is 'strategic programming' — designing the hard parts up front, scoping tasks tightly, defining module interfaces, writing good tests, and maintaining just enough documentation to point AI to the right places. He emphasized that skills are a multiplier on AI output: a senior who understands good DX/AX will get dramatically more from agents than someone with weak fundamentals. He also recommended deleting all skills, MCPs, and agent config to baseline, then layering back only what is genuinely missed, ensuring each addition is a procedure skill rather than an ability skill.

## Relevance to YOLO loop

Directly targets our dev loop's scaffolding layer — if our repo structure, module boundaries, and CLAUDE.md are optimized for AX, every agent invocation in the loop starts with better context, reducing correction iterations and token waste.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-18-strategic-vs-tactical-programming-ai` |
| Channel | do |
| Video | [Matt Pocock's Agentic Engineering Workflow (just copy him)](https://www.youtube.com/watch?v=nQwJVHCtDDY) |
| Published | 2026-06-18 |
| Ingested upstream | 2026-06-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
