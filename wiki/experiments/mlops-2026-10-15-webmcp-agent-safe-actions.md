# Add WebMCP annotations (read-only, user-generated-content, consequential hints) to web app surfaces before wiring agent automation

> Back to [[experiments-index]]

Source: **[Agents Acting Safely on Our Behalf](https://www.youtube.com/watch?v=mNY62rPQpUE)** · mlops · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we annotate our web app UI surfaces with WebMCP hints — marking read-only state, user-generated content zones, and consequential actions — then agents acting on those surfaces will be safer and more deterministic, because the annotations give the agent an explicit semantic contract rather than forcing it to infer intent from DOM scraping or screenshots.

## What they did

The guest (Sarah) described WebMCP as a client-side protocol that lets site builders expose explicit, annotated action surfaces to agents instead of having agents scrape the DOM or accessibility tree. Key annotation types: read-only (agent won't act on it), user-generated content (agent ignores for prompt-injection safety), and consequential hints (agent pauses and confirms with user before proceeding). She contrasted this with computer-use/browser-use agents that work non-deterministically from screenshots — token-inefficient and unpredictable. She demonstrated batch-processing tools built on WebMCP (e.g., 'close out my day' auto-carrying to-dos, dumping cart usuals) and noted WebMCP composes with MCP, REST, and GraphQL rather than replacing them.

## Relevance to YOLO loop

high: directly applies to agent harness design — WebMCP annotations are a mechanism for building safer, more deterministic human-in-the-loop checkpoints into any web surface an agent touches.

## Notes

Sarah mentioned an open-sourced shopping cart demo with WebMCP batch tools. Worth finding the repo. Node.js/npm required for WebMCP setup.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-10-15-webmcp-agent-safe-actions` |
| Channel | mlops |
| Video | [Agents Acting Safely on Our Behalf](https://www.youtube.com/watch?v=mNY62rPQpUE) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
