# Evaluate MiniMax M3's 1M-token sparse attention context for long-horizon multi-round agentic tasks

> Back to [[experiments-index]]

Source: **[Why AI Agents Need Million-Token Context — Thomas Wolf & Olive Song, MiniMax](https://www.youtube.com/watch?v=5Cxe5dv2Xlw)** · aie · 2026-09-04

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we use MiniMax M3's MiniMax Sparse Attention (MSA) architecture to support 1M-token context in a multi-round agentic workflow with heavy tool responses, then the agent can complete significantly longer-horizon tasks without context truncation, because sparse attention selects high-salience context blocks rather than attending to the full quadratic sequence, making long context practically affordable at scale.

## What they did

Olive Song (MiniMax research) described how M3 (400B total params, 20B activated, multimodal) was built around MiniMax Sparse Attention — an index branch that scores context relevance at a high level, feeding a sparse attention branch that computes only on selected blocks. She explained that earlier MiniMax models (M1/01) demonstrated 10M-token context for passive retrieval, but M3 applies long context to active agentic settings where multi-round tool responses accumulate. Thomas Wolf and Olive discussed how this unlocks agent use cases like processing long videos, unstructured PowerPoints, and multi-step automated research workflows, with MiniMax internally using M3 to automate their own ML research harnesses.

## Relevance to YOLO loop

Directly relevant to YOLO loop context management: if long-horizon agentic runs accumulate large tool-response histories, a model with functional 1M-token sparse attention could avoid the context-truncation failures that cut short current loop runs. Worth evaluating M3 as an alternative backbone for long-running agent tasks.

## Notes

M3 is open-source and multimodal (vision + video). Olive confirmed M3 is already being used internally to help build M3.1. Community feedback requested especially on multimodality edge cases. Model supports thinking-effort control as a requested future feature. Thomas Wolf noted M3 was top open-source model at June 2026 release.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-04-minimax-sparse-attention-long-context-agents` |
| Channel | aie |
| Video | [Why AI Agents Need Million-Token Context — Thomas Wolf & Olive Song, MiniMax](https://www.youtube.com/watch?v=5Cxe5dv2Xlw) |
| Published | 2026-09-04 |
| Ingested upstream | 2026-09-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
