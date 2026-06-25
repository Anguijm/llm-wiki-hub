# Integrate a CSP inspector into MCP app development workflow to catch missing domain declarations before store submission

> Back to [[experiments-index]]

Source: **[Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](https://www.youtube.com/watch?v=c-2eEv2ou7Y)** · aie · 2026-06-15

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we add a CSP inspector tool (like Alpic's Skybridge CSP inspector) to the MCP app dev workflow, then we catch missing Content Security Policy domain declarations during local development rather than at app store submission or production, because the double-iframe sandboxing in ChatGPT/Claude enforces CSP strictly and missing domains silently break third-party API calls.

## What they did

CTO of Alpic (MCP hosting company) deep-dived into why ChatGPT and Claude render MCP app views inside a double-nested iframe: the outer iframe isolates the host CSP from the view's CSP requirements, while the inner iframe executes the actual view HTML/JS. Explained that views are simple HTML documents advertised on tool-list calls, cached or served on tool execution, and injected with tool results dynamically. Demonstrated Skybridge (open-source superset of the official App SDK) which includes a CSP inspector dev tool: starts a local server, lists exposed tools, renders views live, and highlights any domains accessed by the view that are missing from the metadata manifest — preventing the most common cause of app store rejections.

## Relevance to YOLO loop

Any YOLO loop that builds or tests MCP apps with UI views needs this. The CSP inspector pattern (compare declared domains vs. actually-called domains at dev time) is a low-effort addition to the local dev server that eliminates a whole class of silent production failures.

## Notes

Skybridge is open source — scan QR or find on GitHub. Speaker noted OpenAI recently added a developer mode that removes CSP in dev (so you only discover missing domains in prod) — Skybridge CSP inspector solves this gap. Talk also covers end-to-end type safety between MCP server and app widgets, polyfills for host-specific APIs.

Backlog triage 2026-06-24 (owner-preference model). CSP inspector for MCP app-store submission — workflow the loop doesn't run.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-15 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-15-double-iframe-csp-mcp-apps` |
| Channel | aie |
| Video | [Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](https://www.youtube.com/watch?v=c-2eEv2ou7Y) |
| Published | 2026-06-15 |
| Ingested upstream | 2026-06-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
