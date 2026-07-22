# Replace Agent Markdown File Memory with a Neo4j Graph Store and Benchmark Retrieval Precision

> Back to [[experiments-index]]

Source: **[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=Q0VkgCyNVUg)** · aie · 2026-07-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace an agent's markdown-file memory (skills, daily notes, tool lists) with a Neo4j knowledge graph, then retrieval will be more precise and token-efficient because the graph preserves entity relationships and allows targeted node-traversal queries instead of loading all markdown into context hoping something is relevant.

## What they did

Stephen Chin ran a live demo comparing two Open Claw (Claude) agent configurations on his home lab: one using standard markdown-file memory (loaded ~100k tokens per round) and one using CrabRAG, a Neo4j graph-backed memory layer. For a query about exposed management ports, the markdown agent returned vague 'check your config' advice; the graph agent traversed from the PFSense router node directly to all related open-port nodes and returned precise actionable findings (specific services exposed to WAN). He also demoed image generation and document Q&A as secondary use cases. The graph memory was built by scanning his home lab infrastructure into Neo4j and exposing it via a modified Neo4j MCP server. He noted that at small scale markdown works but fails at enterprise scale where data exceeds the context window.

## Relevance to YOLO loop

The YOLO loop's agent currently relies on context-window-loaded markdown for task state and history. Migrating experiment records, outcomes, and code dependency maps into a Neo4j graph would reduce token waste and improve the agent's ability to retrieve relevant prior experiments by relationship traversal rather than keyword similarity.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-22-graph-memory-vs-markdown-for-agents` |
| Channel | aie |
| Video | [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=Q0VkgCyNVUg) |
| Published | 2026-07-22 |
| Ingested upstream | 2026-07-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
