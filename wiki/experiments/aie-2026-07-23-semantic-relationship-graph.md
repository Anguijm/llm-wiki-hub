# Link artifacts across sources into a cross-referenced meaning graph

> Back to [[experiments-index]]

Source: **[From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](https://www.youtube.com/watch?v=Btk8wDUVs74)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we explicitly link code changes, tasks, decisions, and communications into a traversable relationship graph (rather than storing them as isolated records), then an agent can trace the 'why' behind any artifact and provide explanations grounded in actual intent because the causal chain is encoded in the data model itself rather than inferred at query time.

## What they did

The speakers used the analogy of a single line of code: a comment tells you what it does, a git blame tells you who wrote it, a PR description tells you why, and a Monday board item tells you which customer complaint triggered it. Their 'Monday world model' encodes these cross-source relationships explicitly — connecting Slack messages to tasks, tasks to PRs, PRs to customer issues — so the agent can traverse the graph to understand meaning rather than just retrieve isolated records. They frame this as the core distinction between a system of record (stores facts) and a system of context (stores relationships and meaning).

## Relevance to YOLO loop

Our loop currently treats each artifact (file diff, test result, task description) as an independent input. Experiment with building a lightweight relationship index that links commits to the task that motivated them, test failures to the code change that introduced them, and decisions in chat to the files they affected. Even a simple JSON graph populated incrementally would let the agent answer 'why does this code exist?' without hallucinating.

## Notes

Simpler starting point than the full offline pipeline card above. Could begin by just writing a post-commit hook that appends a link between the commit SHA and the current active task ID to a local graph file. Incremental and cheap to test whether the agent actually uses the provenance links.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-semantic-relationship-graph` |
| Channel | aie |
| Video | [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](https://www.youtube.com/watch?v=Btk8wDUVs74) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
