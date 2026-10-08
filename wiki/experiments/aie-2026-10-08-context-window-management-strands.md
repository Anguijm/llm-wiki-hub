# Implement Sliding-Window + Summarization Context Management in Agent Loops Using Strands

> Back to [[experiments-index]]

Source: **[Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS](https://www.youtube.com/watch?v=DrfyORO8RqA)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace unbounded context accumulation in long-running agents with a combination of sliding-window (keep last N messages) and summarization (compress older messages to a summary ratio), then we will reduce hallucination from attention-curve degradation and lower token costs, because models only reliably attend to the beginning and end of very long contexts and middle content is effectively lost.

## What they did

Elizabeth Fuentes Leone from AWS described the 'lost in the middle' attention curve problem for agents that accumulate context over long sessions (e.g. a log-monitoring agent that keeps appending logs). She presented the Strands framework (open-source, model-agnostic, free) which provides three conversation manager strategies in one line of code: sliding window (keep N recent messages), summarization (summarize oldest X% while preserving last N messages), and a hybrid of both. She also covered: long-term memory via vector DB, relational memory via entity graphs, invocation state pointers for sharing memory across swarm agents, max tool invocation counts to prevent infinite loops, and async MCP tool handling to avoid gateway timeouts.

## Relevance to YOLO loop

Our YOLO loop agents accumulate context across multi-step tasks. Adding a Strands-style summarization conversation manager would cap token burn and reduce mid-session hallucination on long coding or debugging runs.

## Notes

Strands is AWS open-source, model-agnostic. Key parameters: summary_ratio (e.g. 0.5 = summarize oldest 50%), preserve_last_n (e.g. 4 messages). Also implement max_tool_counts per tool to prevent infinite loops. Async MCP handler pattern useful for slow external APIs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-context-window-management-strands` |
| Channel | aie |
| Video | [Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS](https://www.youtube.com/watch?v=DrfyORO8RqA) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
