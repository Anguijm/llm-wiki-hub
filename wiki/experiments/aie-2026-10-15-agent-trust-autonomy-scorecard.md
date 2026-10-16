# Gate agent autonomy expansion with a four-stage scorecard tied to pre-defined value and control metrics

> Back to [[experiments-index]]

Source: **[The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale](https://www.youtube.com/watch?v=-a2oTS9J67U)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we deploy agents through four explicit autonomy stages (shadow mode → supervised draft → exception ensemble → exceptions only) gated by a scorecard combining value metrics and control metrics, then agents will earn expanded autonomy only when evidence supports it, because each stage surfaces failure modes before they cause unreviewed consequences in production.

## What they did

Michele Grant described an M&A integration scenario with an agent automating a weekly synergy reporting deck. She defined three required value metrics with pre-deployment baselines: cycle time (target: 5 days → 2 days), analyst capacity recovered (80 hrs/week, counted only when redeployed to lagging workstreams, net of compute and review cost), and detection time (lag from data slip to steering committee visibility). She applied a three-lines accountability model: management owns output, risk/compliance oversees, internal audit plans based on materiality. A one-page 'human work standard' maps every decision fork to an authorized human role, required evidence, and escalation path. The autonomy scorecard moves the agent through four stages, tracking override rate and independent sampling at stage four specifically—because a falling override rate can indicate shallower review rather than improved agent accuracy. Core math runs in deterministic code, not LLM prose; the LLM summary is explanation, not proof.

## Relevance to YOLO loop

The four-stage autonomy gate is directly applicable to any agentic step in the YOLO loop that touches consequential outputs. Instrumenting override rate and running periodic independent sampling are concrete telemetry additions. The 'human work standard' one-pager can serve as a per-agent policy document.

## Notes

Key insight: a falling override rate is ambiguous—it can mean the agent improved OR that review depth has slipped. Independent sampling at the exceptions-only stage is the diagnostic. Pre-deployment baseline is a hard prerequisite; if baseline is unknown, do not deploy.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-agent-trust-autonomy-scorecard` |
| Channel | aie |
| Video | [The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale](https://www.youtube.com/watch?v=-a2oTS9J67U) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
