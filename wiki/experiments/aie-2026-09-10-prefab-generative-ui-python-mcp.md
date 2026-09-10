# Stream Agent-Generated UI via MCP Apps to Bypass Context-Window Bottleneck

> Back to [[experiments-index]]

Source: **[Generative UI... in Python? — Jeremiah Lowin, Prefect](https://www.youtube.com/watch?v=Krzs8GeiWTc)** · aie · 2026-09-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route interactive UI delivery through MCP app extensions rather than through the agent's context window, then users get full interactive experiences (forms, tables, charts, file uploads) at dramatically lower token cost and latency, because the UI payload never passes through the agent brain.

## What they did

Jeremiah Lowin described FastMCP's 'Prefab' library: a Python-native scoped UI framework that lets agents return HTML/CSS/JS UIs directly to users via MCP apps, bypassing the agent context window entirely. Key findings: (1) The Python representation of a UI is ~70% smaller than equivalent JSON, so they now stream Python over the wire, execute it in a sandbox, convert to JSON server-side, then render—yielding major token efficiency and latency gains; (2) A generative UI demo showed Claude streaming a UI in real-time by calling a tool that accepts the Prefab protocol serialization, with broken JSON healed and rendered progressively; (3) File upload use case: instead of the agent copy-pasting file contents token-by-token into an MCP tool, the MCP app lets users drag-drop files that go directly to the server, bypassing the agent entirely. Prefab is open-sourced and integrated into recent FastMCP versions.

## Relevance to YOLO loop

Highly relevant for any step in our YOLO loop that currently passes large data blobs through agent context (file ingestion, form collection, table display). The 70% token reduction from Python-vs-JSON representation is an immediate optimization target. The generative UI streaming pattern could replace static tool-output rendering in our agent UIs.

## Notes

Prefab docs at prefab.pref.io. Already integrated in recent FastMCP versions. File upload bypass pattern is the most immediately applicable to our pipeline.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-10-prefab-generative-ui-python-mcp` |
| Channel | aie |
| Video | [Generative UI... in Python? — Jeremiah Lowin, Prefect](https://www.youtube.com/watch?v=Krzs8GeiWTc) |
| Published | 2026-09-10 |
| Ingested upstream | 2026-09-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
