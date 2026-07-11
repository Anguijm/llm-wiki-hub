# Implement Python-level hard-stop and self-correcting runtime guardrails for agents

> Back to [[experiments-index]]

Source: **[Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](https://www.youtube.com/watch?v=vJukHCIv7Ck)** · aie · 2026-07-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we encode business constraints as Python hook functions (not prompt instructions) that intercept tool calls before execution, then agents cannot bypass the rules regardless of prompt injection or model drift, because enforcement happens at the code layer — and soft rules can trigger agent self-correction rather than hard blocking.

## What they did

Elizabeth demonstrated two guardrail patterns using AWS Strands hooks. First, neuro-symbolic guardians: Python functions that check tool call parameters against hard rules (e.g., 'booking cannot exceed 10 guests') and raise exceptions to block execution entirely. Second, runtime steering via AgentOps SDK: a 'student agent' pattern where a separate supervisory process intercepts rule violations and injects a correction message back to the model, allowing it to self-correct and complete the task (e.g., splitting a 50-guest booking into multiple smaller bookings) without a hard stop or user notification. Rules stored in DynamoDB update live without redeployment.

## Relevance to YOLO loop

Maps to the safety/guardrail layer of the YOLO loop — provides enforceable constraints on what agents can do without relying on prompt fragility, critical for autonomous overnight runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-11-neurosymbolic-runtime-guardians` |
| Channel | aie |
| Video | [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](https://www.youtube.com/watch?v=vJukHCIv7Ck) |
| Published | 2026-07-11 |
| Ingested upstream | 2026-07-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
