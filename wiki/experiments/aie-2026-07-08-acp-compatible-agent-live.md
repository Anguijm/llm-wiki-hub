# Add ACP (Agent Client Protocol) support to a custom coding agent so it can run inside any ACP-compatible editor

> Back to [[experiments-index]]

Source: **[Building an ACP-Compatible Agent Live — Bennet Fenner, Zed](https://www.youtube.com/watch?v=HsxQICTLF84)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement the four required ACP interface methods (initialize, createSession, prompt, cancel) using the TypeScript ACP SDK, then a custom coding agent becomes portable across any ACP-compatible client (Zed, JetBrains, Obsidian, etc.) because ACP provides a unified JSON-RPC interface abstracting agent-editor communication.

## What they did

Bennett from Zed live-coded adding ACP support to a minimal TypeScript coding agent that previously only had read-file and edit-file tools. He implemented initialize (returns protocol version), createSession (generates session ID, instantiates agent with working directory from client), prompt (looks up session, strips non-text content, runs tool-calling loop), and cancel. He then upgraded file reads/writes to proxy through ACP's filesystem capability so the editor's unsaved buffer state is visible to the agent. Finally he had the agent add a terminal tool to itself by prompting it to read the ACP docs and self-modify. The result ran live inside Zed.

## Relevance to YOLO loop

If our custom agents implement ACP, they become usable inside editors our team already uses, reducing friction in the dev loop and enabling editor-native agent invocation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-acp-compatible-agent-live` |
| Channel | aie |
| Video | [Building an ACP-Compatible Agent Live — Bennet Fenner, Zed](https://www.youtube.com/watch?v=HsxQICTLF84) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
