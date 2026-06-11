# Use LLM-as-judge on conversation logs to understand true user satisfaction beyond explicit ratings

> Back to [[experiments-index]]

Source: **[The Latency Goldilocks Zone Explained](https://www.youtube.com/watch?v=dH-1INvvELo)** · mlops · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we apply an LLM judge to full conversation transcripts rather than relying on explicit user ratings or CSAT surveys, then we will get more accurate signals about user satisfaction because users frequently contradict themselves (saying they hate a recommendation they actually liked) and standard survey questions yield unreliable answers that overstate or understate true preference.

## What they did

iFood ILO team described that standard satisfaction metrics were misleading: users would say they hated a recommendation but the conversation context revealed they actually liked it, and vice versa. They adopted LLM-as-judge on the actual conversation content to extract genuine sentiment. They also discovered through this process that users were using their food recommendation agent as a customer support bot, creating an unexpected multi-intent routing problem. The team emphasized that truly understanding what customers need requires deep conversation analysis, not surface-level feedback collection.

## Relevance to YOLO loop

We can apply LLM-as-judge to our own agent interaction logs to evaluate whether agent outputs are actually useful vs. what simple thumbs-up/down feedback would suggest, improving our experiment evaluation quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-11-ifood-latency-goldilocks-recommender` |
| Channel | mlops |
| Video | [The Latency Goldilocks Zone Explained](https://www.youtube.com/watch?v=dH-1INvvELo) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
