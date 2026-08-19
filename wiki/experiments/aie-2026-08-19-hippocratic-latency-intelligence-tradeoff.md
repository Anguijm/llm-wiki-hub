# Build a Vertically Integrated Inference Stack to Hit Both Latency and Clinical Accuracy Targets Simultaneously

> Back to [[experiments-index]]

Source: **[200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](https://www.youtube.com/watch?v=AN65uc645mE)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we vertically integrate our inference stack with hundreds of targeted optimizations rather than relying on off-the-shelf model APIs, then we can achieve both low latency and high clinical accuracy simultaneously, because generic stacks force a tradeoff between the two that can only be broken by controlling the full stack from model weights to serving.

## What they did

Hippocratic AI found that clinically safe models were too slow for real-time phone conversations (tens of seconds to over a minute), while fast models lacked clinical accuracy. They built a vertically integrated stack optimizing every layer, including a 96%+ KV cache hit rate on long clinical conversations (enabling 18x faster pre-fill), custom model training, and continuous benchmarking. They also built HEART, a purpose-built empathy benchmark, when no good one existed. For evals they use 7,000+ trained clinicians who have done 700,000+ clinical conversations to continuously evaluate the system, combined with synthetic data — because at 10,000 calls/day even 1% error means 100 wrong appointments, requiring ~450 test cases just to detect a 1% failure rate at 99% confidence.

## Relevance to YOLO loop

The sample-size math for catching low failure rates in high-volume agents is directly applicable to how we size our eval sets. The caching strategy for long-context agents is also worth trialing to reduce latency in our own agent loops.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-hippocratic-latency-intelligence-tradeoff` |
| Channel | aie |
| Video | [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](https://www.youtube.com/watch?v=AN65uc645mE) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
