# Benchmark a small local llama.cpp model as a sub-second classifier gate

> Back to [[experiments-index]]

Source: **[My Jev Pi Durable Agent CURATES News: HYPE, FACT, or SIGNAL](https://www.youtube.com/watch?v=OLqP8jxJ0Wc)** · idd · 2026-10-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we serve a small quantized model via llama.cpp on the Strix Halo box and use it to classify short texts into labels, then we can approach the sub-half-second per-call latency shown in the video at no API cost because a small model on local Vulkan or ROCm hardware avoids network round trips and token billing.

## What they did

IndyDevDan showed his Jev classifier handling text classification requests in sub-half-second time per call. Its scores gated more expensive model calls in an always-on news curation pipeline backed by a durable SQLite agent daemon on an M4 Mac mini. He credited this cheap semantic gating with keeping the one-minute cron sweeps affordable.

## Relevance to YOLO loop

medium: A local classifier can serve as the cheap gate in always-on agent workflows, though the gain is mostly cost and latency.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `idd-2026-10-19-local-classifier-strix-halo` |
| Channel | idd |
| Video | [My Jev Pi Durable Agent CURATES News: HYPE, FACT, or SIGNAL](https://www.youtube.com/watch?v=OLqP8jxJ0Wc) |
| Published | 2026-10-19 |
| Ingested upstream | 2026-10-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
