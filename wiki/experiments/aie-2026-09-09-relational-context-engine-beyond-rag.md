# Build a relational context engine that lets agents query structured repo/team data, not just RAG chunks

> Back to [[experiments-index]]

Source: **[Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](https://www.youtube.com/watch?v=KcVkq5L-0f0)** · aie · 2026-09-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we augment RAG with a schema-less relational lookup layer that agents can query deterministically, then agents will be able to answer structured questions like 'open PRs I worked on last week involving authentication' that pure vector search cannot answer, reducing doom loops and rework because the agent has precise, queryable context about how the codebase and team actually operate.

## What they did

Brandon Waselnuk (Unblocked) argued that curated markdown context files rot, and MCP servers suffer from 'satisfaction of search bias' (agent stops at the first plausible result). He presented three open-source tools: (1) a social commit network analyzer that maps who commits where and who reviews whose work, producing an experts graph for focusing context retrieval; (2) a repo rules agent that indexes all rules files across a repo, deduplicates conflicts, and builds a queryable index; (3) a workshop (delivered Monday) on building a relational context engine from scratch — six stacked PRs teaching schema-less lookup that allows an agent to discover a schema and write deterministic queries against it, complementing RAG for relational/filtered questions. He framed the adoption curve from tab-complete → inline agent → parallel agents → background agents, noting that bad context compounds in cost at each level.

## Relevance to YOLO loop

Maps to the context-injection phase of our dev loop. Adding a relational query layer alongside our existing RAG would allow agents to answer project-structure and team-topology questions that currently require manual prompting, reducing the review tax and doom loops in our agentic coding workflows.

## Notes

Workshop workbook available via QR code in talk. Tools are open source from Unblocked. Readiness self-assessment tool at readiness.unblocked.com. Booth P16 at conference for follow-up. The social commit network tool uses only deterministic programming (no LLM) by default; optional OpenAI/Anthropic key adds team labeling.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-09-relational-context-engine-beyond-rag` |
| Channel | aie |
| Video | [Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](https://www.youtube.com/watch?v=KcVkq5L-0f0) |
| Published | 2026-09-09 |
| Ingested upstream | 2026-09-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
