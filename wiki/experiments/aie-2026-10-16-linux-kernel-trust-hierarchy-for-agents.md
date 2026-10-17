# Replace star-topology agent orchestration with a Linux-kernel-style layered trust hierarchy

> Back to [[experiments-index]]

Source: **[Why One AI Agent Isn't Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc)** · aie · 2026-10-16

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we restructure multi-agent workflows from a single orchestrator receiving all PRs/outputs to a layered hierarchy where trusted sub-orchestrators filter and aggregate before escalating only exceptional cases, then throughput will scale and the human (or top-level agent) will stop being the bottleneck, because Linus's 2002 switch from star to tree topology solved the same scaling problem for Linux kernel contributions.

## What they did

CJ Avilla and Harrison Stall traced how Linus Torvalds moved from a star structure (all contributors emailing him directly) to a tree of trusted maintainers after hitting his personal scaling limit. They mapped this directly to multi-agent systems: instead of one orchestrator agent reviewing every sub-agent PR, build a trust hierarchy where sub-orchestrators handle routine merges and only escalate edge cases upward, mirroring the Linux maintainer model.

## Relevance to YOLO loop

high: directly actionable for scaling our Claude Code harness from single-agent to multi-agent—restructuring orchestration topology to avoid the human bottleneck.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-16-linux-kernel-trust-hierarchy-for-agents` |
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
