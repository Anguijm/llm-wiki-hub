# Replace a large set of discrete agent tools with a single persistent-state REPL tool

> Back to [[experiments-index]]

Source: **[Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](https://www.youtube.com/watch?v=HEFSExa0xl0)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace 10-15 discrete tools with a single Node.js (or Python) REPL tool that maintains state across calls, then agent task completion speed and accuracy will improve significantly because the agent can compose multiple operations in one call, combine results, reuse variables across turns, and avoid the sequential latency and context fragmentation of many individual tool calls.

## What they did

Nuno's team spent 4 months improving coding agents on spreadsheet tasks. After trying many approaches (SQL, XML, CSV views, HTML rendering), the biggest breakthrough was collapsing ~15 tools into a single Node.js REPL with persistent state. Before: agents made 10-15 sequential tool calls per task, frequently timing out. After: agents combined all needed operations in one REPL call and reused variables across calls. This is distinguished from 'code mode' by persistence: variables defined in one REPL invocation remain available in the next. The underlying spreadsheet logic was implemented in C# while the REPL scripting layer used JavaScript, demonstrating the pattern works with a polyglot implementation. Accuracy on a financial analysis benchmark went from ~50% to 92%.

## Relevance to YOLO loop

Directly applicable: if our agent currently calls many small tools sequentially, collapsing them into a REPL with state persistence should reduce round-trips, token usage, and latency in our dev loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-repl-tool-replaces-15-tools` |
| Channel | aie |
| Video | [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](https://www.youtube.com/watch?v=HEFSExa0xl0) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
