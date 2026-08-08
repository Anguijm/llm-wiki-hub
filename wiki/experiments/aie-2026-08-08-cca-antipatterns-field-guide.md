# Implement context-forking with token-count-gated compaction to prevent context bloat in long agent runs

> Back to [[experiments-index]]

Source: **[Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Z-c11pV_uvU)** · aie · 2026-08-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we fork agent subtasks into isolated threads (so their intermediate reasoning never pollutes the main context) and automatically trigger Claude's compaction algorithm when the main context exceeds a token threshold (e.g. 150k), then long-running agentic sessions will remain coherent and cost-efficient because unbounded context growth is the primary cause of degraded output quality and runaway token spend in multi-step loops.

## What they did

Frank Coyle walked through the Claude Certified Architect exam's production scenarios and their associated anti-patterns. For the developer-productivity scenario he demonstrated a pattern: fork an agent to scan logs, have it produce only a summary, inject just that summary into the main context, then programmatically check token count and invoke Claude's built-in compaction if over threshold. He also highlighted that running Claude Code in non-interactive (CI) mode eliminates costly permission-request interruptions in automated pipelines.

## Relevance to YOLO loop

Core reliability primitive for our loop: unbounded context is our most common failure mode in long YOLO sessions. This pattern gives a concrete, code-level mechanism to keep sessions from degrading or hitting limits mid-run.

## Notes

Also noted: Anthropic batch API gives 50% token cost reduction with ≤24h turnaround—viable for non-urgent overnight agent runs. CCA exam costs $99, available to individuals every 6 months.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-08-cca-antipatterns-field-guide` |
| Channel | aie |
| Video | [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Z-c11pV_uvU) |
| Published | 2026-08-08 |
| Ingested upstream | 2026-08-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
