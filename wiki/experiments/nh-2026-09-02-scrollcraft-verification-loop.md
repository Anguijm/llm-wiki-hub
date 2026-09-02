# Add Screenshot-Based Visual Verification Loop to UI Generation Tasks

> Back to [[experiments-index]]

Source: **[Fable 5.1 FINALLY Kills AI Website Slop](https://www.youtube.com/watch?v=FFWtxjvW2ts)** · nh · 2026-09-02

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we require the agent to take screenshots frame-by-frame during scroll animations and visually verify each state before proceeding, then AI-generated UIs will have significantly fewer layout, color, and out-of-bounds errors in the final output, because the model catches visual regressions in-loop rather than requiring human review at the end.

## What they did

Nate built multiple premium websites using Fable 5.1 with a skill called ScrollCraft. A key part of the workflow was instructing the model to screenshot the rendered page at each scroll position and analyze those screenshots iteratively, correcting issues like out-of-bounds elements, color mismatches, and broken animations before the session ended. He also verified mobile layouts in the same loop. He reported this verification loop as essential to eliminating AI UI slop.

## Relevance to YOLO loop

The YOLO loop's verification step currently relies on human review of agent output; adding automated screenshot-and-analyze cycles for any frontend task would catch visual bugs earlier and reduce the number of human correction rounds.

## Notes

Nate also found Fable 5.1 was 25–45% cheaper than Fable 5 on these agentic coding tasks, consistent with Anthropic's release claims. ScrollCraft skill available in his free School community.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-02-scrollcraft-verification-loop` |
| Channel | nh |
| Video | [Fable 5.1 FINALLY Kills AI Website Slop](https://www.youtube.com/watch?v=FFWtxjvW2ts) |
| Published | 2026-09-02 |
| Ingested upstream | 2026-09-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
