# Build an agentic performance engineering pipeline that auto-triggers profiling, identifies hot paths via LLM, and proposes diffs

> Back to [[experiments-index]]

Source: **[AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix](https://www.youtube.com/watch?v=CgsWxRUY5Eo)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build an agent that (1) triggers a profiler on a production service, (2) feeds the structured profiling output to an LLM to identify hot paths using known antipatterns, and (3) searches the codebase for the identified paths to generate a fix PR, then we can reduce performance bottleneck identification from ~20 human-minutes to seconds and run it continuously on a schedule, because profiling output is language-agnostic structured data that LLMs can reason about using training knowledge of common performance antipatterns.

## What they did

Rajat Shah described Netflix's AI performance engineering system. The traditional workflow required an engineer to manually trigger a profiler, download results, open a visualizer, spend 20+ minutes hunting hot paths, search the codebase, write a fix, and run a canary — done only reactively at 2am incidents. Their agent automates: trigger profiler → download output → LLM analyzes call stack for known antipatterns (O(n²) loops, loop-invariant computation, repeated object allocation, batching opportunities) → code search → generate fix suggestion → run canary. He described a three-level automation spectrum: Level 1 (LLM identifies hot paths, human does the rest), Level 2 (full tool-integrated orchestration with canary automation — what they built), Level 3 (fully autonomous with planning, requiring heavy security/sandboxing investment). He recommended starting at Level 1 and moving to Level 2.

## Relevance to YOLO loop

Directly applicable to our dev loop's performance feedback stage. Rather than waiting for slowness to be noticed, a scheduled performance agent could continuously surface regressions introduced by AI-generated code before they reach production.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-netflix-perf-agent-profiling-pipeline` |
| Channel | aie |
| Video | [AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix](https://www.youtube.com/watch?v=CgsWxRUY5Eo) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
