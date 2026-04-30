# Move YOLO Loop Execution Environment to Ephemeral Cloud Sandboxes

> Back to [[experiments-index]]

Source: **[Why Agents are Driving Software Development to the Cloud](https://www.youtube.com/watch?v=uT-jEi9Ledw)** · MLOps · 2026-04-27

**Status:** `in_progress` · **Effort:** `high`

---

## Hypothesis

If we run each YOLO loop iteration inside an ephemeral cloud sandbox (e.g., Modal, E2B, or Daytona) instead of a local environment, then agent-executed code will be safer, more reproducible, and easier to parallelize, because cloud sandboxes provide clean state, network isolation, and elastic compute per run.

## What they did

Speaker argued that AI coding agents are pushing development workflows toward cloud-native execution environments, specifically because agents need reliable, resettable, observable environments that local machines cannot consistently provide. Discussed tradeoffs of local vs. cloud execution for agentic loops.

## Relevance to YOLO loop

Directly challenges the assumption that the YOLO loop runs locally. If agent execution moves to cloud sandboxes, the loop's environment setup, file I/O, and git operations all need to be re-architected around remote ephemeral instances.

## Notes

[2026-04-29T08:05:00Z] Implemented at experiments/cloud-sandbox-adapter/. Adapters degrade to deterministic stubs without API keys, so the scaffold is runnable end-to-end. Promotion to tick queue is the next step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-27 | `backlog` | Extracted from YouTube RSS |
|  | `` | Implemented as research-spike scaffold at experiments/cloud-sandbox-adapter/. See README.md for design and usage. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-27-agents-software-dev-cloud` |
| Channel | MLOps |
| Video | [Why Agents are Driving Software Development to the Cloud](https://www.youtube.com/watch?v=uT-jEi9Ledw) |
| Published | 2026-04-27 |
| Ingested upstream | 2026-04-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
