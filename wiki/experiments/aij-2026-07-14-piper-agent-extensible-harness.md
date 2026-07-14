# Use Pi Agent's Extension System to Self-Modify the Coding Harness at Runtime

> Back to [[experiments-index]]

Source: **[Why I switched to Pi...](https://www.youtube.com/watch?v=MsPhMhfvgD4)** · aij · 2026-07-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Pi Agent instead of Claude Code or Codex as the coding agent harness, then we can programmatically extend or modify tools, hooks, UI, and session management on the fly — including having the agent write its own extensions — because Pi's design philosophy exposes nearly every harness component as a pluggable extension rather than locking them behind a proprietary SDK.

## What they did

Jason explained that Pi Agent ships with only four core tools (bash, write, read, edit) but exposes a full extension API covering tools, hooks, context, session management, LLM providers, and even the terminal UI. He demonstrated having Pi write a weather-widget UI extension for itself live, reload it with /reload, and immediately see it active. He also showed installing community extensions from the Pi package catalog, building a web-hosted agent product (a Posia replica with 11 sub-agents) on the Pi SDK, and using the coding-agent package for local agent products with custom UI and task triggers.

## Relevance to YOLO loop

If our loop needs custom hooks (e.g., auto-checkpointing state, enforcing guardrails before tool calls, parallel session management), Pi's extension model lets us implement those without forking a proprietary harness. Worth benchmarking against our current Claude Code setup.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-07-14-piper-agent-extensible-harness` |
| Channel | aij |
| Video | [Why I switched to Pi...](https://www.youtube.com/watch?v=MsPhMhfvgD4) |
| Published | 2026-07-14 |
| Ingested upstream | 2026-07-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
