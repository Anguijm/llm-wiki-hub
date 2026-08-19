# Place a Deterministic Code Layer Above the Model for All Irreversible High-Stakes Decisions

> Back to [[experiments-index]]

Source: **[Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](https://www.youtube.com/watch?v=YXEqC05WEI0)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we put a deterministic code layer that runs before the model on every turn and makes all irreversible high-stakes decisions (emergency escalation, 911 routing, clinician handoff) in code rather than in prompts, then those decisions are never subject to LLM probability or prompt injection, because code cannot be overridden by a user message the way a system prompt can.

## What they did

Hinge Health's approach: (1) strip PHI at the pipeline boundary at ingestion, never at log time; (2) run a deterministic code layer above the model on every turn that handles routing for emergency escalations and irreversible actions before the model sees the input; (3) let the model handle only the long tail of normal conversational turns; (4) treat compliance (HIPAA, FDA GMLP, state laws) as architectural inputs, not afterthoughts. For launch decisions they apply five rules: score by worst-case scenario, default to the safer mistake, calibrate to revealed (not stated) risk tolerance, treat fast-follows as committed debt not backlog, and always design for human-in-the-loop. They also emphasize validating the judge before changing the agent — when scores shift, first ask whether the judge is miscalibrated before modifying agent prompts.

## Relevance to YOLO loop

The code-above-model pattern is directly implementable in our agent architecture for any action that must not fail. The judge-validation discipline (check the scorer before changing the agent) is also immediately applicable to our eval loop to prevent chasing false signals.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-deterministic-code-layer-above-model` |
| Channel | aie |
| Video | [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](https://www.youtube.com/watch?v=YXEqC05WEI0) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
