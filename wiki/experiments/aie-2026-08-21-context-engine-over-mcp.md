# Add a pre-synthesis context layer between raw MCP data sources and the agent to reduce hallucinations from missing organizational knowledge

> Back to [[experiments-index]]

Source: **[Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked](https://www.youtube.com/watch?v=HvMyYLTfvhg)** · aie · 2026-08-21

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we insert a context engine that retrieves, reconciles, and summarizes task-relevant information (Slack threads, postmortems, tickets, docs) before passing it to the coding agent—rather than giving the agent raw MCP tool access—then the agent will make fewer confidently-wrong recommendations, because conflicts across data sources are resolved and irrelevant data is filtered before the agent reasons over it, keeping context windows focused and grounded.

## What they did

Speaker (founding engineer at Unblocked) demonstrated a Linear issue-enrichment agent that, without a context layer, incorrectly recommended re-enabling an async dispatch flag that had already caused an outage—because the agent lacked the subsequent Slack discussion and postmortem ticket. He then reran the same agent with Unblocked's context engine, which fetched and summarized the relevant postmortem and Slack thread before the agent reasoned over them. The agent's recommendation flipped from harmful to correct. He argued that naive MCP chaining gives agents raw access but not understanding, floods context windows with irrelevant data, and leaves conflict resolution to the agent ad hoc. A context engine instead builds an organization model, scopes data to access roles, reconciles conflicts, and delivers a synthesized slice to the agent.

## Relevance to YOLO loop

Directly relevant: our YOLO loop agents currently pull raw context from whichever files are in scope. Adding a lightweight pre-retrieval step that summarizes and reconciles relevant prior decisions, closed issues, and architecture notes before the main agent prompt could reduce confident wrong outputs and wasted retry loops.

## Notes

Speaker's key framing: 'The gap isn't intelligence, it's context.' MCP provides access; a context engine provides understanding. Simpler near-term proxy: add a mandatory 'retrieve and summarize prior decisions' tool call as the first step of any agent task plan before code generation begins.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-21 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-21-context-engine-over-mcp` |
| Channel | aie |
| Video | [Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked](https://www.youtube.com/watch?v=HvMyYLTfvhg) |
| Published | 2026-08-21 |
| Ingested upstream | 2026-08-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
