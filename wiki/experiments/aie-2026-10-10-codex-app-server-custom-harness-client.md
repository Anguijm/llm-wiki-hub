# Build a custom Codex harness client using the open-source App Server protocol for parallel agent threads and custom interfaces

> Back to [[experiments-index]]

Source: **[Building on the Codex Harness — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=9WiBJRO84yY)** · aie · 2026-10-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a custom client on top of the Codex App Server (JSON-RPC protocol) rather than scripting Codex CLI calls, then we can run multiple parallel Codex agent threads, inject custom tools marked as deferred, and build specialized interfaces (eval harnesses, IDE integrations, game environments), because the App Server exposes 120+ client messages including thread management, file system access, goal-setting, and plugin listing.

## What they did

Dominik Kundel (OpenAI) explained the Codex App Server: an open-source (Apache 2) JSON-RPC protocol that powers all first-party Codex interfaces (desktop app, VS Code extension, Xcode, JetBrains, Claude Code plugin). It can connect to any OpenAI-compatible API including Ollama/LM Studio. Key capabilities: send thread start/turn/modification messages, configure the underlying agent, expose custom functions to the agent, do file system operations, and stream deltas. He built a live inspector and demoed Codex running inside a Doom game mod. Three tips: (1) ship your own pinned version of the harness to avoid breaking changes; (2) expose custom functions as deferred so they don't pollute the context window unnecessarily; (3) add developer instructions rather than replacing the base system prompt to stay in distribution.

## Relevance to YOLO loop

If our YOLO loop needs to run multiple parallel agent tasks (e.g., running evals, multi-PR review, parallel feature branches), the App Server is the right abstraction rather than scripting Codex Exec calls sequentially. The deferred-function pattern is also directly useful for injecting loop-specific tools without degrading agent behavior.

## Notes

Codex App Server is Apache 2 licensed and open source. ACP (Agent Client Protocol) is a comparable alternative worth comparing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-10-codex-app-server-custom-harness-client` |
| Channel | aie |
| Video | [Building on the Codex Harness — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=9WiBJRO84yY) |
| Published | 2026-10-10 |
| Ingested upstream | 2026-10-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
