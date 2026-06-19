# Build agent loops with explicit checkable goal, hard stop condition, and separate checker agent

> Back to [[experiments-index]]

Source: **[Finally. Agent Loops Clearly Explained.](https://www.youtube.com/watch?v=EuzYhzB0vbI)** · nh · 2026-06-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we structure agent loops with a clearly objective/checkable goal, a hard stop condition, and a separate verifier agent that judges completion independently of the acting agent, then quality per attempt will ramp faster than human-in-the-loop iteration because the feedback cycle is automated and consistent.

## What they did

Nate explained agent loops as a reason-act-observe cycle where the agent iterates until a stop condition is met. He built a concrete example: a loop that scraped 45 sources (articles, YouTube transcripts, posts), synthesized content, built an HTML artifact, screenshotted it, reviewed it, and iterated to V7 before stopping. He also described a video editing loop that runs /goal, retrieves transcript, cuts mistakes, makes beats, syncs beats, renders, verifies beats are in-bounds and aligned—all unattended. Key ingredients he listed: checkable goal, hard stop, good tools, memory, a separate checker, planning first, logging, and cost awareness. He cautioned against blindly copying power-user patterns (e.g. 24/7 swarms) when your use case doesn't warrant it.

## Relevance to YOLO loop

This is a direct blueprint for the YOLO loop's core architecture: the reason-act-observe primitives, the separate checker agent for stop-condition verification, and the /goal trigger pattern all map 1:1 to loop design decisions.

## Notes

Nate's distinction between cadence-triggered vs event-triggered loops vs continuous 24/7 loops is useful for deciding loop scheduling strategy in YOLO loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-19-agent-loop-reason-act-observe` |
| Channel | nh |
| Video | [Finally. Agent Loops Clearly Explained.](https://www.youtube.com/watch?v=EuzYhzB0vbI) |
| Published | 2026-06-19 |
| Ingested upstream | 2026-06-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
