# Run Agents in Isolated Remote Sandboxes via Gemini Interactions API to Eliminate Local Environment Conflicts

> Back to [[experiments-index]]

Source: **[Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=oWTEiYpxl80)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we deploy agent tool execution into managed remote sandboxes (via Gemini Interactions API) rather than executing tools locally, then we eliminate environment setup friction, permission conflicts, and local state pollution, because the sandbox handles the full agent loop server-side including function calling, state management, and MCP server connections.

## What they did

Philipp Schmid from Google DeepMind presented the Gemini Interactions API as an alternative to responses-API-style development. Key features: server-side state management (pass only the previous interaction ID for follow-up turns), long-running async operations (get an ID, poll or stream), combined built-in tools (Google Search) with custom function calling, and managed remote sandboxes where the entire agent loop runs on Google's infrastructure. Demonstrated an agent exploring its own sandbox environment (Ubuntu, 8 vCPU, 16GB RAM, Python/pip installed) via bash commands. The sandbox loads an agents.md file on startup as system instructions, has skill files (Python functions that call other Gemini models via the same API), and files can be downloaded via API. Also previewed Nano Banana Light (image gen, $0.04/image) and Omni Flash on the Interactions API for video generation/editing.

## Relevance to YOLO loop

Offloading agent execution to a managed sandbox removes the local environment management burden from our YOLO loop and enables parallel agent runs without local resource contention or permission issues.

## Notes

Access via ai.google.dev or toi.dev. No setup required for free tier, Gmail login. Budget controls available inside AI Studio without going to Google Cloud. Anti-gravity agent templates available in model picker. agents.md file pattern is compatible with existing Claude/Codex agent file conventions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-gemini-sandbox-managed-agent` |
| Channel | aie |
| Video | [Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=oWTEiYpxl80) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
