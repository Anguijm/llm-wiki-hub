# Fine-tune or prompt-engineer an LLM with domain-specific entity vocabulary

> Back to [[experiments-index]]

Source: **[Teaching LLMs to Speak Spotify — Yves Raimond & Jacqueline Wood, Spotify](https://www.youtube.com/watch?v=2LRIAfng7eA)** · aie · 2026-09-26

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we teach an LLM a domain-specific 'language' (entity IDs, metadata schemas, and relationship types from a product catalog), then the model can reason accurately over domain entities without hallucinating because grounding it in structured vocabularies reduces ambiguity.

## What they did

Spotify engineers described their approach to making LLMs fluent in Spotify's internal data language — likely involving structured entity representations, catalog grounding, and possibly fine-tuning or RAG over Spotify's music knowledge graph so the model can make meaningful recommendations and queries.

## Relevance to YOLO loop

Directly applicable to any system that needs an LLM to reason over a proprietary schema or entity graph; informs how we should structure context and grounding for domain-specific AI features.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-26-spotify-llm-music-language` |
| Channel | aie |
| Video | [Teaching LLMs to Speak Spotify — Yves Raimond & Jacqueline Wood, Spotify](https://www.youtube.com/watch?v=2LRIAfng7eA) |
| Published | 2026-09-26 |
| Ingested upstream | 2026-09-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
