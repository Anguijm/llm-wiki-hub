# Replace multi-dashboard workflows with a unified MCP layer that exposes agent-optimized tool interfaces with stateful search and context-saving

> Back to [[experiments-index]]

Source: **[Dashboards Are Dead — Sarah Simionescu, Composio](https://www.youtube.com/watch?v=YiFqcu9YA38)** · aie · 2026-10-05

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we route agent tool calls through a unified MCP abstraction layer (rather than native per-app MCPs) that provides semantic tool search, execution planning, and context-window-efficient result handling, then agents will complete multi-app tasks more reliably and with fewer wrong-tool errors, because Composio's experiment showed their unified MCP consistently outperformed native per-app MCPs on the same tasks with the same model, and their Remote Workbench tool lets agents query large datasets without loading full results into context.

## What they did

Sarah Simionescu from Composio argued that dashboards are dying because she personally never opens them anymore—Claude does the work. She identified three failure modes of naive multi-MCP setups: agents have no memory across sessions, too many tool definitions drown the context window (GitHub toolkit alone has 200+ tools), and each app MCP is isolated so cross-app tasks require manual orchestration. Composio's solution: a unified MCP that agents query with a goal (not a specific tool), which returns the right tools plus a usage plan. She demoed Claude resolving a bug report by calling Composio search, which returned tools and plans for Slack, Sentry, and Datadog in parallel, then opened a PR. A second demo showed cross-source analytics (PostHog + Metabase) where results were saved without loading full datasets into context.

## Relevance to YOLO loop

Directly applicable: if the YOLO loop's agents are calling multiple tool MCPs, replacing them with a unified semantic search layer would reduce context bloat and wrong-tool errors. The Remote Workbench pattern (execute query, save result, reference by pointer rather than loading into context) is a concrete technique for keeping context windows lean on data-heavy tasks.

## Notes

Sarah's framing: 'You are now serving a new species of user. They don't have eyes.' Composio benchmarked against native MCPs listed in Claude marketplace—same tasks, same model, clear win for Composio. Remote Workbench is the specific tool for context-efficient large dataset handling. Live demo available at Composio booth.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-05-composio-mcp-agent-native-interface` |
| Channel | aie |
| Video | [Dashboards Are Dead — Sarah Simionescu, Composio](https://www.youtube.com/watch?v=YiFqcu9YA38) |
| Published | 2026-10-05 |
| Ingested upstream | 2026-10-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
