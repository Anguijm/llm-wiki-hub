# Separate data-fetch tools from render tools in MCP apps so the model can filter before displaying

> Back to [[experiments-index]]

Source: **[MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed](https://www.youtube.com/watch?v=lbaXnx0KLA8)** · aie · 2026-09-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we split MCP tools into small composable data-retrieval tools and a separate render tool that accepts a filtered list of IDs, then the model can explore and reason over the full dataset before deciding what to surface to the user, producing a higher-quality UI experience because the model retains full semantic awareness of what it is displaying rather than treating the rendered component as a black box.

## What they did

Dustin Mihalik (Indeed) shared lessons from building MCP apps for Claude, ChatGPT, and their internal Career Scout agent. Key findings: (1) anything shown to the user must also be returned as structured data to the model or follow-up questions become unanswerable; (2) tool descriptions must explicitly state that results are displayed as UI components to prevent the model from redundantly re-describing them in text; (3) interactive elements (apply button, view-details modal) need their own tool calls so the model knows what the user is currently viewing; (4) the best architecture separates a search tool (returns up to 100 results as data) from a render widget tool (accepts a filtered list of IDs plus optional model-generated annotations like 'reason this is a good fit'). This allows the model to filter, rank, and annotate before rendering.

## Relevance to YOLO loop

Applies to any point in our loop where we surface agent results in a UI. The data-before-rendering principle and the separation of search vs. render tools directly improves result quality and context retention when we add visual output layers to our agent pipelines.

## Notes

Speaker noted it took a 'ridiculous number of hours and evals' to get Claude to consistently link to external URLs — MCP apps SDK resolves this by giving the tool control over the apply/link buttons. Pattern generalises to e-commerce, maps, any list-based UI.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-09-mcp-apps-data-first-rendering` |
| Channel | aie |
| Video | [MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed](https://www.youtube.com/watch?v=lbaXnx0KLA8) |
| Published | 2026-09-09 |
| Ingested upstream | 2026-09-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
