# Enrich structured knowledge artifacts (docs, specs, catalogs) with semantic attributes and buyer context before indexing for agent retrieval

> Back to [[experiments-index]]

Source: **[Keyword Search Is Dying. Is Your Catalog Ready for AI Agents? — PayPal](https://www.youtube.com/watch?v=YXb2Wx1r_Pk)** · aie · 2026-10-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we enrich our structured knowledge artifacts (API docs, tool specs, architecture docs) with semantic descriptions, contextual attributes, and usage examples before indexing them for agent retrieval, then agent recommendations and retrievals will be more accurate and relevant, because PayPal's experiment showed enriched catalog items consistently outperformed unenriched baselines head-to-head, with thinnest catalogs gaining the most, while over-enrichment with unstructured boilerplate text caused hallucination and degraded performance.

## What they did

Nixon Den from PayPal described their shift from keyword-based catalog discovery to intent-based and eventually delegation-based agent-driven commerce. They ran experiments enriching product catalog entries with attribute filling, description depth, buyer context, trust signals, and review data. Enriched entries significantly outperformed unenriched baselines in agent recommendation accuracy. Key finding: structured quality content wins; piling on unstructured text (e.g., boilerplate store descriptions) dilutes the signal and causes hallucination. Schema alone doesn't drive results—content quality does.

## Relevance to YOLO loop

Maps to how we structure and index our tool documentation, experiment cards, and architecture specs for agent retrieval. The finding that over-enrichment with unstructured text degrades performance is directly actionable: we should audit our current RAG corpus for boilerplate dilution and ensure semantic attributes are explicit and structured.

## Notes

Key takeaways from PayPal experiment: (1) enrichment always beats unenriched baseline head-to-head, (2) merchants with thinnest catalogs gain most, (3) over-enrichment causes hallucination, (4) schema doesn't matter as much as content quality, (5) boilerplate text is actively harmful to semantic retrieval.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-05-catalog-enrichment-for-agent-retrieval` |
| Channel | aie |
| Video | [Keyword Search Is Dying. Is Your Catalog Ready for AI Agents? — PayPal](https://www.youtube.com/watch?v=YXb2Wx1r_Pk) |
| Published | 2026-10-05 |
| Ingested upstream | 2026-10-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
