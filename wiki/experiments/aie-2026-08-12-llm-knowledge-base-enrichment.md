# Build an Agent-Enriched Markdown Knowledge Base with Backlinks, Tags, Wikis, and Graph Visualization

> Back to [[experiments-index]]

Source: **[LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](https://www.youtube.com/watch?v=I3bpdgFJCUY)** · aie · 2026-08-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we store raw notes as markdown files and then use an agent to enrich them with backlinks to related notes, category tags, auto-generated wiki pages for recurring people/concepts/sources, and an HTML graph visualization, then we will surface forgotten ideas and knowledge gaps faster because interconnected structure makes latent relationships explicit and navigable for both humans and agents.

## What they did

Ben Holmes from Warp walked through a four-stage pipeline for LLM knowledge bases: (1) capture raw thoughts via voice dictation (tools like Handy or Voice Inc.) into unformatted markdown files, (2) enrich notes by having an agent add backlinks to related notes and apply category tags, (3) generate wikis—agent-created clickable pages for people, concepts, and sources referenced across notes, (4) generate graph visualizations via agent-written HTML/Tailwind that render notes as an interactive node graph with clickable drill-down. He demonstrated his own app 'Hubble' (hub.md, open source) as an agent-accessible Apple Notes alternative, and Warp's oz.dev automation platform for scheduling background note enrichment. He emphasized that agents can now build the visualization tooling itself on demand.

## Relevance to YOLO loop

Our dev loop generates decisions, experiment notes, and code context that currently lives in scattered files. Applying this enrichment pipeline to our existing markdown docs would make the knowledge base more navigable for both team members and agents operating in future sessions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-12-llm-knowledge-base-enrichment` |
| Channel | aie |
| Video | [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](https://www.youtube.com/watch?v=I3bpdgFJCUY) |
| Published | 2026-08-12 |
| Ingested upstream | 2026-08-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
