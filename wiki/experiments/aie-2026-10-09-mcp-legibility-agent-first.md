# Rebuild MCP tools with scoped capabilities and human verification checkpoints instead of full API exposure

> Back to [[experiments-index]]

Source: **[Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto](https://www.youtube.com/watch?v=jJQoVkd5yLg)** · aie · 2026-10-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace an MCP server that exposes every API endpoint as a tool with one that provides scoped, sequenced capabilities and surfaces human-verifiable checkpoints at high-stakes steps, then agent reliability and user trust improve because auto-mode agents operating on full-surface MCPs confidently produce unverifiable outputs that neither user nor agent can explain.

## What they did

Avi (Reducto) built an initial MCP by wrapping every API endpoint as a tool in one file. Internal team use immediately broke it: agents given half-baked prompts would build entire workflows end-to-end with high confidence but produce outputs no one could verify or explain. Root cause: auto-mode with full surface area gives the agent nowhere to check in with humans. Rebuild principle: 'agent experience in service of the user'—structure tools so the agent has rich but scoped capabilities, the human can verify work at each stage, and the agent earns trust by being legible. Specific change: the agent now generates a plan/schema for the pipeline first (cheap to verify), then builds with human approval. Instrumentation added: every MCP session logged prompts, human overrides, low-confidence moments, and Claude Code session exports. This data fed back into long-term MCP guidance, creating a self-improving loop per org. Outcome: sales team spontaneously started using the agent before customer calls without being told to, and trusted the output enough to demo to high-value customers.

## Relevance to YOLO loop

Core architectural lesson for YOLO loop MCP design: scope tool surface area, add plan-first checkpoints, and instrument every session to feed improvements back into the harness.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-09-mcp-legibility-agent-first` |
| Channel | aie |
| Video | [Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto](https://www.youtube.com/watch?v=jJQoVkd5yLg) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
