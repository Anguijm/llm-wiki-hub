# Pre-compute and inject a repository dependency graph as a file into each agent session to eliminate redundant graph-building work

> Back to [[experiments-index]]

Source: **[Why One AI Agent Isn't Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc)** · aie · 2026-10-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we generate the inter-module dependency graph ahead of time and upload it as a file into the agent's session context, then agents working on multi-repo tasks will skip expensive runtime graph traversal and produce faster, more accurate impact analyses because the costly structural information is already available at the start of each task.

## What they did

During the Q&A, the Anthropic presenters confirmed that for multi-repo bug hunting, agents must remount and re-analyse repositories per session. They advised that if a dependency graph is expensive to compute, pre-generate it and upload it as a file to the agent session (Claude's Files API), referencing its path in the initial prompt so the agent doesn't rebuild it from scratch.

## Relevance to YOLO loop

high: directly applicable to Claude Code harness—pre-computing project dependency maps and injecting them as context files at session start to reduce agent overhead on large codebases.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-16-dependency-graph-preloaded-into-agent-session` |
| Channel | aie |
| Video | [Why One AI Agent Isn't Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
