# Use a Local Graph Database as Agent Long-Term Memory with Offline Fallback

> Back to [[experiments-index]]

Source: **[I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j](https://www.youtube.com/watch?v=oUZEt4EiPbk)** · aie · 2026-10-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we back an agent's long-term memory with a graph database (Neo4j) running locally rather than a cloud vector store, then we will gain structured relationship traversal between memory nodes (people, themes, locations, concepts) and maintain functionality offline, because graph queries can surface non-obvious connections across memories that flat vector similarity misses.

## What they did

The speaker ran a Claude-based agent on a Raspberry Pi 4B with a Dockerized Neo4j instance for local persistent memory. He used voice-to-text to capture conference booth notes offline, stored them as graph nodes with exhibitor relationships, then later enriched the graph in cloud Neo4j — connecting exhibitors to theme nodes (e.g., 'evaluation and observability'). He also used Neo4j's agent memory service to ingest WhatsApp conversation history and distill it into structured memory nodes accessible via an MCP server from the same local agent.

## Relevance to YOLO loop

Maps to the persistent memory layer of the YOLO loop: replacing or augmenting flat conversation history with a graph structure enables agents to reason about relationships between past interactions, projects, and concepts — especially useful for long-running personal AI operating systems.

## Notes

MCP server wrapping Neo4j as memory backend is the key integration point — the agent can query its own memory graph via tool calls. Neo4j has a free tier; Docker setup is straightforward. Start with a simple schema: (Memory)-[:RELATES_TO]->(Theme).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-04-raspberry-pi-graph-agent-memory` |
| Channel | aie |
| Video | [I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j](https://www.youtube.com/watch?v=oUZEt4EiPbk) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
