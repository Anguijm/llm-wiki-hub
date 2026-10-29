# Add a harness finish gate and rendered plan state

> Back to [[experiments-index]]

Source: **[We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI](https://www.youtube.com/watch?v=YIhvrvHtonk)** · aie · 2026-10-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we render plan state in messages and add a hook-enforced finish gate that blocks ending a turn while planned items remain open, then agents will conclude prematurely less often and burn fewer calls on to-do tools, because planning lives in deterministic code rather than model tool calls.

## What they did

Arize moved planning, math and aggregation out of the model into harness code after iterating on to-do list tools more than 20 times. Plan state was rendered directly in conversation messages. A finish gate stopped agents from ending turns with open items. Oversized JSON tool outputs were truncated, and the agent queried the full data with jq. They converted production traces into CI regression fixtures and found failures like 43 identical tool calls in one turn.

## Relevance to YOLO loop

high: Deterministic gates and trace-based regression fixtures are verification-loop patterns that can be built as Claude Code hooks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-28 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-27-deterministic-finish-gate` |
| Channel | aie |
| Video | [We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI](https://www.youtube.com/watch?v=YIhvrvHtonk) |
| Published | 2026-10-27 |
| Ingested upstream | 2026-10-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
