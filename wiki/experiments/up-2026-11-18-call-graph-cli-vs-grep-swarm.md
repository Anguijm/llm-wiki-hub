# Replace grep sub-agent exploration with a precomputed call-graph CLI

> Back to [[experiments-index]]

Source: **[[un]prompted 2, 2026 - offstage: Vince Ovando](https://www.youtube.com/watch?v=h0zqGD0cnRw)** · up · 2026-11-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we generate a call graph for the Flutter calendar app with a small CLI and let the agent query it instead of launching grep sub-agents, then codebase-mapping tokens and wall-clock time will drop sharply because deterministic code does the traversal that an LLM swarm would otherwise do.

## What they did

Vince contrasted a 30-minute sub-agent grep swarm that consumed about 15 million tokens with a CLI call-graph utility that let a single agent map a codebase in about 15 seconds. His rule is to use deterministic code, heuristics and embeddings before reaching for an LLM.

## Relevance to YOLO loop

high: Swapping LLM-driven code exploration for a deterministic precomputed index is not in the practices already in place, and the token and time gain is measurable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-21 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `up-2026-11-18-call-graph-cli-vs-grep-swarm` |
| Channel | up |
| Video | [[un]prompted 2, 2026 - offstage: Vince Ovando](https://www.youtube.com/watch?v=h0zqGD0cnRw) |
| Published | 2026-11-18 |
| Ingested upstream | 2026-11-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
