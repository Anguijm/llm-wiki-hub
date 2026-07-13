# Use microVM memory snapshots with layered lineage for low-latency sandbox creation and Monte Carlo agent exploration

> Back to [[experiments-index]]

Source: **[From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=OqM67QG_Ikk)** · aie · 2026-07-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we snapshot microVM memory state at each checkpoint of an agentic task and route new sandbox requests to nodes that already hold the required snapshot layers, then we get millisecond-latency sandbox creation and enable Monte Carlo tree search over agent execution paths, because restoring from a memory snapshot is orders of magnitude faster than booting a fresh VM, and layered snapshots allow branching from any prior state.

## What they did

Abhishek Bhardwaj (OpenAI RL & Agent Infrastructure) described the sandbox architecture behind ChatGPT Codex Web. Key techniques: (1) microVMs (Firecracker-style) for isolation of untrusted agent-generated code; (2) memory snapshots with layered lineage—each snapshot can have multiple ancestor layers; (3) just-in-time restore from snapshot in milliseconds as requests arrive; (4) orchestrator routes sandbox requests to nodes already holding the needed snapshot layers (highest cache hit score), minimizing data download; (5) tiered persistent storage using block-level cache backed by object storage (GCS/S3) via NBD inside the VM. He frames snapshot/restore as the key unlock for harnesses to recover from failures and perform Monte Carlo-like searches over agent decision trees.

## Relevance to YOLO loop

The snapshot-restore pattern is directly applicable to YOLO loop branching: checkpoint agent state before risky tool calls, branch and explore multiple continuations, restore on failure. Even a lightweight local version (e.g., snapshotting container state) could improve loop resilience and enable parallel hypothesis testing.

## Notes

Abhishek's previous talk 'How to Build an AI Sandbox from Scratch' is a recommended prerequisite. The Monte Carlo search framing is the most novel angle for our loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-13-microvm-sandbox-snapshot-restore` |
| Channel | aie |
| Video | [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=OqM67QG_Ikk) |
| Published | 2026-07-13 |
| Ingested upstream | 2026-07-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
