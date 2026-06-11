# Build MCP servers that expose UI components for human-in-the-loop agent steps

> Back to [[experiments-index]]

Source: **[MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps](https://www.youtube.com/watch?v=o-zkvb0iFDQ)** · aie · 2026-05-09

**Status:** `deferred` · **Effort:** `high`

---

## Hypothesis

If we add UI-bearing MCP tools that surface confirmation dialogs or inline forms to the human at key decision points, then agent safety and user trust will improve because humans can review and approve high-stakes actions without breaking the agentic flow.

## What they did

Speakers from MCP Apps described how to extend the MCP protocol with UI components, allowing MCP servers to render interactive elements (forms, confirmations, dashboards) that appear inside the agent interface at appropriate moments.

## Relevance to YOLO loop

Relevant for adding human-in-the-loop gates to our YOLO loop without fully stopping execution; a UI-bearing MCP tool could prompt for approval before destructive operations.

## Notes

Deferred 2026-05-10: MCP UI extensions only earn their slot when we have an MCP server worth fronting. Park until we ship one.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-05-09-mcp-ui-extensions` |
| Channel | aie |
| Video | [MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps](https://www.youtube.com/watch?v=o-zkvb0iFDQ) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
