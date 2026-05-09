# Decouple agent memory from the model so workflows survive model swaps

> Back to [[experiments-index]]

Source: **[Your AI Agent Is Locked To One Model. OpenClaw Just Killed That.](https://www.youtube.com/watch?v=85Q9htV2CBE)** · NateBJones · 2026-05-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we store agent memory in a user-owned layer independent of any specific LLM, then our agentic workflows will survive model provider changes, pricing shifts, and capability updates because the memory and task state are not locked inside the model's context or a provider's infrastructure.

## What they did

Speaker described OpenClaw's April 2026 maturation into a serious agent runtime with swappable model backends. He introduced the open-sourced OpenBrain project as a memory architecture designed specifically for OpenClaw that keeps memory user-owned and model-agnostic. He outlined a stack: OpenClaw as action layer, models as swappable reasoning engines, task flow as durable loop, channels as human interface, and memory plus permissions as the trust and continuity layer.

## Relevance to YOLO loop

High relevance: our YOLO loop's persistence layer should be model-agnostic; experimenting with an OpenBrain-style memory store would let us route different models (Claude, GPT-4o, local) through the same workflow without rebuilding state.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-05-09-openclaw-swappable-model-memory` |
| Channel | NateBJones |
| Video | [Your AI Agent Is Locked To One Model. OpenClaw Just Killed That.](https://www.youtube.com/watch?v=85Q9htV2CBE) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
