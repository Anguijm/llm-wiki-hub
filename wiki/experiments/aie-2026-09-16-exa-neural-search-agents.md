# Replace Keyword-Based Web Search with Neural Search (Exa) for Agent External Lookups

> Back to [[experiments-index]]

Source: **[The Search Engine for the Agentic Web — Will Bryk, Exa](https://www.youtube.com/watch?v=59AA5kIoqjA)** · aie · 2026-09-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we replace standard keyword web search (Google/Bing API) with a neural search engine designed for AI agents (Exa), then agent queries for complex or relational information (e.g., 'everyone in Singapore who works on AI search and their papers') will return semantically accurate results rather than keyword-matched links, improving the quality of external context retrieved during agent tasks.

## What they did

Will Bryk (Exa) described Exa as a search engine rebuilt for AI agents rather than humans. Unlike Google (a recommendation engine optimized for human click behavior), Exa is designed to return exact database-style results for complex semantic queries. It serves 5,000+ companies and 400,000+ developers including Cursor (technical docs), HubSpot (lead lists), and financial agents. Exa supports queries like 'find all biotech companies matching X' or 'most important US news across all media' that fail on traditional search. They also introduced a data marketplace where providers set prices for proprietary data (e.g., SimilarWeb traffic stats) that agents can purchase at query time, enabling enriched results combining public web and proprietary sources.

## Relevance to YOLO loop

When our coding agents need to look up external documentation, find library examples, or research technical topics, swapping in Exa for web search tool calls could yield significantly more precise results for complex multi-part queries.

## Notes

Exa API is available and used in production by Cursor. Key differentiator vs Google: neural/semantic matching vs keyword recommendation. Data marketplace for proprietary data enrichment is a newer feature. AI systems expected to exceed human search volume in 2026 per Exa projections.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-16-exa-neural-search-agents` |
| Channel | aie |
| Video | [The Search Engine for the Agentic Web — Will Bryk, Exa](https://www.youtube.com/watch?v=59AA5kIoqjA) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
