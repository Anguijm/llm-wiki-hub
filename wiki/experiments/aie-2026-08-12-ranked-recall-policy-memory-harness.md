# Replace Vector RAG Memory with a Ranked Decisions Ledger for Long-Horizon Agent Runs

> Back to [[experiments-index]]

Source: **[Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](https://www.youtube.com/watch?v=R3-anFK1YM8)** · aie · 2026-08-12

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we implement a structured ranked-recall policy in our agent memory harness—specifically a decisions ledger that records and prioritizes decisions per turn rather than relying on vector similarity retrieval—then long-horizon agents will retrieve the correct context more frequently at lower token cost because ranked policy recall outperforms similarity-based retrieval on tasks where the relevant memory is far outside the current context window.

## What they did

Stefania Druga from Sakana AI described building a memory harness on local models (Qwen 27B quantized and DeepSeek V4 Flash on an M3 Ultra) for long-running research agents. She framed memory as a write-manage-read loop. Her harness tested a ladder of recall modes: no memory baseline, vector RAG, a decisions ledger (tracking what decisions were made each turn with ranking), and an oracle (ground truth). Evaluated on the X-Bench long-horizon memory benchmark (68 questions, answers buried hundreds of steps back), the ranked decisions ledger outperformed vector RAG and even in some cases outperformed the oracle (because the oracle gave correct memories but didn't force the model to use them). She also found that bad memory is expensive—it wastes tokens and misdirects the agent—while a good structural recall policy saves tokens and improves accuracy across multiple models and benchmarks.

## Relevance to YOLO loop

Our long-running YOLO loop sessions suffer from context rot and repeated mistakes. Swapping from full-context replay or vector RAG to a ranked decisions ledger is a concrete architectural change to test on our longest agent runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-12-ranked-recall-policy-memory-harness` |
| Channel | aie |
| Video | [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](https://www.youtube.com/watch?v=R3-anFK1YM8) |
| Published | 2026-08-12 |
| Ingested upstream | 2026-08-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
