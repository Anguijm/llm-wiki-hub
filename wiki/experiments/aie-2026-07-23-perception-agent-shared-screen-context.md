# Give agents continuous visual perception of shared UI state so they can monitor, detect, and recover from step failures

> Back to [[experiments-index]]

Source: **[Perception Agents — Antje Barth, Amazon AGI Lab](https://www.youtube.com/watch?v=2JX6JYyQG4Y)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we give an agent persistent visual access to the same screen state a human would see during task execution (not just the action result), then the agent can detect when a step produced an unexpected outcome and self-correct before the error propagates, because most end-to-end workflow failures happen in the seams between steps where visual feedback is the primary signal.

## What they did

Antje Barth from Amazon AGI Lab argued that the gap between capable agents and reliable agents is not bigger models but shared context — specifically, the agent watching what happens after each action rather than fire-and-forget. She described 'perception agents' that maintain continuous screen observation, detect drift from expected state, and trigger recovery or human escalation. She demonstrated a workflow where a meeting transcript from a Bee device was fed to an agent that applied design changes to a website and immediately ran a visual compliance verification, flagging violations before a human had to review. She open-sourced the pattern on GitHub and framed it as: you don't need a bigger brain, you need the agent to see what you see.

## Relevance to YOLO loop

Our yolo loop agents likely execute actions and then proceed regardless of whether the action's visible effect was correct. Adding a perception layer — even a lightweight screenshot-diff check at key workflow steps — would catch failures at the seam rather than propagating them through downstream steps, reducing the need for full loop restarts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-perception-agent-shared-screen-context` |
| Channel | aie |
| Video | [Perception Agents — Antje Barth, Amazon AGI Lab](https://www.youtube.com/watch?v=2JX6JYyQG4Y) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
