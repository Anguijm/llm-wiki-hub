# Instrument agent traces to classify failure modes and calibrate harness rigidity

> Back to [[experiments-index]]

Source: **[Sandboxing, Agent Harnesses, and Agent Teamwork](https://www.youtube.com/watch?v=31IS2mnRV6Q)** · mlops · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we capture structured traces of every agent run and label failure modes (e.g., context flooding, excessive retries, wrong tool chosen), then we can make data-driven decisions about when to tighten or loosen harness constraints, because the pattern of failures reveals whether the harness is over-constraining or under-constraining the agent.

## What they did

The speakers described a practice of taking every failed agent investigation, running a post-mortem review on the trace, labeling what went wrong (too wide a log query flooding context, too many attempts at a single step, etc.), and using that label taxonomy to decide whether a failure is a harness design problem or a one-off. They emphasised that harnesses should evolve: early rigid custom tools made sense when models were weaker, but as models improved the rigid harness became the bottleneck. They also noted that monitors and traces are the prerequisite for knowing when to loosen constraints.

## Relevance to YOLO loop

Directly applicable to our agentic dev loop: we can add a lightweight trace-labelling step after each YOLO run failure, accumulate a failure taxonomy, and use it to tune prompts, tool definitions, and guard-rails rather than guessing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-07-20-agent-harness-calibration` |
| Channel | mlops |
| Video | [Sandboxing, Agent Harnesses, and Agent Teamwork](https://www.youtube.com/watch?v=31IS2mnRV6Q) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
