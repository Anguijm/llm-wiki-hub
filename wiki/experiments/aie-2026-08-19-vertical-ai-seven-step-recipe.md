# Scope Vertical AI Agents to a Single Narrow Task and Gate Expansion on ROI

> Back to [[experiments-index]]

Source: **[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](https://www.youtube.com/watch?v=Yphdry8ttAQ)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we constrain each AI agent to one very specific, well-defined task and evaluate ROI before expanding scope, then agents are more likely to reach production and justify their cost, because narrow scoping produces measurable alpha over baseline models on a bounded problem and prevents the common failure mode of building an agent that tries to do too much at once.

## What they did

Bhardwaj described a seven-step recipe abstracted from hedge fund and pharma AI work: (1) formulate a narrow problem statement rather than a broad one; (2) identify and curate proprietary data sources that generic models lack; (3) craft precise prompts for the narrow task; (4) observe behavior without iterating yet; (5) hire a small internal user group to form a learning loop; (6) iterate based on that loop until the agent delivers clear alpha over ChatGPT/Claude on the specific task; (7) ship to external paying users. He emphasized that domain expertise and proprietary data — not model infrastructure — are the real moat in vertical AI.

## Relevance to YOLO loop

Maps directly to how we scope new agent capabilities in our loop. The explicit gate of 'does this deliver alpha over baseline before we ship' is a useful forcing function to add to our backlog prioritization.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-vertical-ai-seven-step-recipe` |
| Channel | aie |
| Video | [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](https://www.youtube.com/watch?v=Yphdry8ttAQ) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
