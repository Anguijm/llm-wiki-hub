# Replace ad-hoc agent prompting with a control graph (SOP as code) for reliable multi-step workflows

> Back to [[experiments-index]]

Source: **[I don't prompt agents anymore...](https://www.youtube.com/watch?v=_9OT25ZvrWs)** · aij · 2026-08-25

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we encode multi-step agent tasks as a control graph — either via injected skill/persona scripts or dynamic workflow JavaScript with explicit agent nodes, schemas, and dependencies — then agent output reliability will increase because each stage receives structured context from the previous stage rather than relying on a single monolithic prompt.

## What they did

Jason distinguished three things people conflate under 'graph engineering': control graphs (LangGraph-style SOPs for reliable agent flow), knowledge graphs (entity-relationship retrieval, unrelated), and graph-of-loops (multi-loop compounding, still experimental). He focused on control graphs as the practically useful concept. He described two implementation methods his team uses in production at Super Design: (1) large-model-as-graph — injecting skill/persona scripts so a single powerful model follows structured sub-roles without spawning new sessions; (2) dynamic workflow as code — an agent writes JavaScript using primitives (agent(), pipeline(), parallel()) to spawn a typed graph of agent sessions, each outputting a defined schema that becomes the prompt context for the next node. He showed a 'ship change' workflow: setup+implement → verify → simplify+PR, each phase a separate agent session with schema-typed outputs chained together. He emphasized that verification tooling (giving agents the ability to run and test code) is the most commonly missing piece that causes loops to fail.

## Relevance to YOLO loop

Directly maps to structuring the YOLO loop's multi-step coding tasks: instead of one giant prompt, encode the implement→verify→PR flow as a dynamic workflow graph with schema-typed handoffs, and ensure each agent node has execution/test tools available.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-08-25-control-graph-sop-for-agents` |
| Channel | aij |
| Video | [I don't prompt agents anymore...](https://www.youtube.com/watch?v=_9OT25ZvrWs) |
| Published | 2026-08-25 |
| Ingested upstream | 2026-08-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
