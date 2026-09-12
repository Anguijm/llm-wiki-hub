# Replace Custom Tool Calls with Bash-First Agent Harness

> Back to [[experiments-index]]

Source: **[Pi Agent dev reveals his Agentic Engineering Workflow](https://www.youtube.com/watch?v=SxuQs9GGYbk)** · do · 2026-09-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we reduce our agent harness to primarily expose bash as the core tool instead of custom-built file/search/read tools, then context efficiency will improve and the agent will produce more creative, pipelined solutions because bash lets the model chain commands and add its own separation markers without pulling intermediate results into context.

## What they did

Armen (creator of Pi agent / Flask, founder of Arendelle) explained that Pi agent's winning approach is giving the model essentially just bash rather than a rich set of bespoke tools. He noted that even Codex has converged on this pattern — when Codex 'discovers files' it is actually calling ripgrep via bash. The key insight is that bash lets the model pipeline commands together (e.g. find files AND add separation markers in one shell invocation) so intermediate data never needs to be injected into the context window. He also mentioned that interleaved system messages in newer models now enable deferred tool loading, a pattern that was previously impossible and can further trim context overhead.

## Relevance to YOLO loop

Directly impacts the tool-layer of the YOLO loop. If our loop currently wraps file reads, searches, and edits in typed tool functions, stripping those back to a single bash tool could shrink prompt size per turn and let the model self-optimize its own command pipelines.

## Notes

Armen also flagged interleaved system messages as an enabling primitive for deferred tool loading — worth pairing this experiment with a second card or follow-up once we validate the bash-first baseline.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-09-12-bash-first-agentic-harness` |
| Channel | do |
| Video | [Pi Agent dev reveals his Agentic Engineering Workflow](https://www.youtube.com/watch?v=SxuQs9GGYbk) |
| Published | 2026-09-12 |
| Ingested upstream | 2026-09-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
