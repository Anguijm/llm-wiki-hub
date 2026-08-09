# Benchmark Multiple Coding Models Against Your Own Codebase to Stay Model-Agnostic

> Back to [[experiments-index]]

Source: **[Multiplayer agentic engineering — Arjun Singh, Superconductor](https://www.youtube.com/watch?v=OL7kfezynJM)** · aie · 2026-08-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If teams run internal benchmarks comparing coding models (e.g., Codex, Claude Code, GLM) on their own tasks and codebase, then they can switch models with minimal disruption and always use the best cost/quality tradeoff because the evaluation data is project-specific rather than generic.

## What they did

Superconductor ran systematic comparisons of coding agents on their own pull requests. They found Codex had 4x more sessions than Claude Code at lower overall cost, while Claude Code cost $10K/day in tokens at 3,300 runs. They maintained model-agnostic infrastructure so switching defaults (e.g., from Claude to Codex to Fiable and back) caused no meaningful workflow disruption. They're now building automatic task-routing based on these internal benchmarks.

## Relevance to YOLO loop

Highly relevant—the YOLO loop should not be hard-coded to one model provider. Running periodic benchmark sweeps on representative tasks from our own repo gives empirical data to justify model switches and optimize the cost/quality frontier of the generation step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-09-model-agnostic-benchmarking` |
| Channel | aie |
| Video | [Multiplayer agentic engineering — Arjun Singh, Superconductor](https://www.youtube.com/watch?v=OL7kfezynJM) |
| Published | 2026-08-09 |
| Ingested upstream | 2026-08-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
