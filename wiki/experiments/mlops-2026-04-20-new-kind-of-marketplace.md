# Expose YOLO loop capabilities as composable marketplace primitives

> Back to [[experiments-index]]

Source: **[A New Kind of Marketplace](https://www.youtube.com/watch?v=q9e2e5Y8Q0k)** · MLOps · 2026-04-20

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we package individual YOLO loop steps as discrete, callable API primitives rather than a monolithic pipeline, then external agents or orchestrators can compose them on demand because marketplace-style decomposition enables reuse and selective invocation.

## What they did

The speaker described an emerging model where AI capabilities are offered as fine-grained marketplace services rather than bundled products, covering how teams can both consume and publish these primitives to create interoperable AI-powered workflows.

## Relevance to YOLO loop

Suggests decomposing the YOLO loop into independently addressable steps that could be registered, versioned, and called by external orchestration layers — useful if the loop needs to integrate with third-party agent frameworks or be shared across projects.

## Notes

"YOLO loop as composable marketplace primitives" — too abstract for tick-sized work, same category as the ai-replaced-managers discarded yesterday. No concrete deliverable path.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-20 | `backlog` | Extracted from YouTube RSS |
| 2026-04-22 | `discarded` | "YOLO loop as composable marketplace primitives" — too abstract for tick-sized work, same category as the ai-replaced-managers discarded yesterday. No concrete deliverable path. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-20-new-kind-of-marketplace` |
| Channel | MLOps |
| Video | [A New Kind of Marketplace](https://www.youtube.com/watch?v=q9e2e5Y8Q0k) |
| Published | 2026-04-20 |
| Ingested upstream | 2026-04-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
