# Restructure dev workflow around AI-assisted code generation with human review gates

> Back to [[experiments-index]]

Source: **[The Modern Software Engineer](https://www.youtube.com/watch?v=jOe4fJSc2IE)** · MLOps · 2026-04-20

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we explicitly define which parts of the dev loop are AI-owned versus human-reviewed, then we will ship faster with fewer regressions because ambiguity about responsibility is the primary source of AI-assisted development failures.

## What they did

The speaker outlined a framework for how software engineers should reposition themselves relative to AI tooling — treating LLMs as junior pair programmers, owning system design and review, and using AI for implementation throughput rather than architecture decisions.

## Relevance to YOLO loop

Maps directly to how the YOLO loop assigns tasks between the AI agent and the human operator. Formalizing the human review gate positions and the AI generation positions would reduce loop failures caused by unchecked agent output.

## Notes

See tick_queue_approved entry 'adopt-ai-human-gate-spec' in session_state.json.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-20 | `backlog` | Extracted from YouTube RSS |
| 2026-04-22 | `adopted` | Promoted to tick queue as adopt-ai-human-gate-spec. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-20-modern-software-engineer` |
| Channel | MLOps |
| Video | [The Modern Software Engineer](https://www.youtube.com/watch?v=jOe4fJSc2IE) |
| Published | 2026-04-20 |
| Ingested upstream | 2026-04-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
