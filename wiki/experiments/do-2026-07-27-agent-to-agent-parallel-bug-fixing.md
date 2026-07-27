# Spawn child agents from a running agent to handle discovered bugs in parallel

> Back to [[experiments-index]]

Source: **[Agentic Engineering, explained by a 10x developer](https://www.youtube.com/watch?v=FU5_kpTAVDo)** · do · 2026-07-27

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If a primary coding agent can spawn a secondary agent on a separate branch when it discovers a secondary bug during its main task, then overall throughput increases and context pollution decreases because each agent maintains focused context on a single well-scoped problem rather than context-switching mid-task.

## What they did

Torsten Ball described AMP's agent-to-agent communication feature where a running agent, upon discovering an additional bug, can be instructed to launch a new 'orb' (agent instance) in a separate checkout on a separate branch to fix that bug independently, while the primary agent continues its original work. He described this as a recent release that meaningfully increased their shipping velocity.

## Relevance to YOLO loop

Extends our YOLO loop from linear agent sessions to a tree-structured execution model — the main session can delegate newly discovered issues to sub-sessions, keeping the critical path unblocked and enabling parallelism within a single logical task.

## Notes

AMP also uses separate git checkouts per agent to avoid workspace conflicts. The pattern requires a branch-per-agent convention and a way to surface child agent results back to the orchestrating developer for spot-check and merge.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-27-agent-to-agent-parallel-bug-fixing` |
| Channel | do |
| Video | [Agentic Engineering, explained by a 10x developer](https://www.youtube.com/watch?v=FU5_kpTAVDo) |
| Published | 2026-07-27 |
| Ingested upstream | 2026-07-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
