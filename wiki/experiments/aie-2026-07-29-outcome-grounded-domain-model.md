# Fine-tune a domain model on verified situation-action-outcome triples to outperform frontier models on domain-specific advice

> Back to [[experiments-index]]

Source: **[Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit](https://www.youtube.com/watch?v=Owb8g3yDyzo)** · aie · 2026-07-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we extract situation-action-outcome triples from historical domain records, train a reward model on them, and fine-tune an LLM to generate advice grounded in verified outcomes rather than internet text, then a mid-size model will outperform frontier models on domain-specific recommendations because the moat is in outcome-verified data, not model scale.

## What they did

Intuit studied 100,000 small businesses across time frames and found frontier models gave harmful generic advice (e.g., 'acquire a new customer' in 40%+ of cases, recommending a cash-negative business take on a second property). They built a three-step pipeline: extract situation-action-outcome triples from business records, train a reward model to rank which actions led to good outcomes for similar businesses, then fine-tune an LLM to generate that grounded advice. Their mid-size model beat all frontier models head-to-head. A Princeton study corroborated this: most frontier models bankrupted a simulated business within 500 days while a simple rules-based system outperformed them.

## Relevance to YOLO loop

The principle — that a smaller model grounded in verified outcomes beats a larger general model — applies to any domain-specific agent in the YOLO loop. Collecting outcome-labeled traces from our own dev loop could seed a domain-specific reward signal for fine-tuning.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-29-outcome-grounded-domain-model` |
| Channel | aie |
| Video | [Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit](https://www.youtube.com/watch?v=Owb8g3yDyzo) |
| Published | 2026-07-29 |
| Ingested upstream | 2026-07-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
