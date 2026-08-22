# Design cloud agent sandboxes with bring-your-own-infrastructure and multi-harness support

> Back to [[experiments-index]]

Source: **[The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](https://www.youtube.com/watch?v=L173Z8DpaJg)** · aie · 2026-08-22

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we separate sandbox provisioning from harness selection and allow both managed and self-hosted compute, then teams can run long-running cloud agents without exposing infrastructure complexity to users because each primitive hides its own complexity layer.

## What they did

Safia described Warp's cloud agent platform architecture: isolated sandboxes (managed and self-hosted), pluggable harness support (Claude Code, Codex, custom), shared conversation state rehydration, artifact storage, event-driven automation triggers, and observability hooks — all structured so each primitive abstracts complexity from the user. She used the analogy of a master potter's workshop as a 'software factory' that is malleable, observable, and cost-effective.

## Relevance to YOLO loop

Relevant if we want to move long-running agents off local machines: the primitives (sandbox abstraction, harness portability, event triggers, state rehydration) map directly to how we'd scale our YOLO loop from local Claude Code sessions to cloud-scheduled agent jobs.

## Notes

Architectural talk, no open-source release mentioned. Key principle: platforms should absorb complexity before it reaches the user. Warp booth at UG 20.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-22-warp-cloud-agent-platform` |
| Channel | aie |
| Video | [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](https://www.youtube.com/watch?v=L173Z8DpaJg) |
| Published | 2026-08-22 |
| Ingested upstream | 2026-08-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
