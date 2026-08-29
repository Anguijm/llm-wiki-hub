# Wrap hardware tool calls in an AWS Strands agentic layer to enable natural-language orchestration of physical devices

> Back to [[experiments-index]]

Source: **[Tell the Robot What You Want — Sandhya Subramani, AWS](https://www.youtube.com/watch?v=S6aSoQ6_u5A)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we place an agentic orchestration layer (AWS Strands) on top of a robot's preset programmable policies and expose those policies as tool calls, then a single agent can execute a near-unlimited variety of tasks in natural language without retraining the underlying robot, because the LLM selects which policy to invoke rather than requiring explicit per-task programming.

## What they did

Sandhya demonstrated Scout, a rover running three simultaneous Strands agents (thinker, communication, and voice) on a Raspberry Pi connected via 4G. The thinker agent continuously perceives and plans; the communication agent interfaces via Telegram and a web app; the voice agent (disabled during the talk) accepts spoken commands. The system uses Claude Opus as the underlying model, exposes robot motor/sensor functions as tool calls, and requires only 5 lines of Strands code to initialize. She also described using the rover to generate training datasets by manually driving it and capturing reasoning traces for later model improvement.

## Relevance to YOLO loop

Illustrates the tool-call abstraction pattern at the hardware level: the same agent-orchestrates-tools model used in software YOLO loops applies directly to physical actuators, suggesting the loop architecture is substrate-agnostic.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-strands-robot-agentic-layer` |
| Channel | aie |
| Video | [Tell the Robot What You Want — Sandhya Subramani, AWS](https://www.youtube.com/watch?v=S6aSoQ6_u5A) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
