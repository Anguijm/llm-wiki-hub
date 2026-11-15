# Sweep temperature, top-k and top-p on the Push to Talk cleanup model

> Back to [[experiments-index]]

Source: **[LLM Fundamentals Crash Course (& Why Every Dev Should Learn It!)](https://www.youtube.com/watch?v=Kaigs9LNoO0)** · pl · 2026-11-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run a fixed set of 30 dictation transcripts through the llama.cpp cleanup model at temperature 0, 0.2 and 0.5, with top-k and top-p variants, then edit-distance drift and hallucinated insertions will drop at low temperature because sharper probability distributions favor deterministic greedy-like token choices.

## What they did

Lackner explained how the final decoding stage turns probabilities into tokens. Lowering temperature sharpens the distribution toward greedy selection, and raising it flattens the distribution and adds variance. Top-k and top-p cut off the low-probability tail. He warned that too high a temperature picks low-probability tokens that cause errors and hallucinations.

## Relevance to YOLO loop

medium: Sampling parameter tuning is useful but is a standard setting rather than a new agent-practice technique.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-14 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `pl-2026-11-11-sampling-sweep-ptt-cleanup` |
| Channel | pl |
| Video | [LLM Fundamentals Crash Course (& Why Every Dev Should Learn It!)](https://www.youtube.com/watch?v=Kaigs9LNoO0) |
| Published | 2026-11-11 |
| Ingested upstream | 2026-11-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
