# Implement a Slack/paging human-in-the-loop interrupt for long-running agent jobs

> Back to [[experiments-index]]

Source: **[WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF](https://www.youtube.com/watch?v=htM02KMNZnk)** · aie · 2026-07-01

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add a Slack (or equivalent) notification channel that a long-running agent can use to page a human when infrastructure fails or an unexpected blocker occurs mid-run, then we will recover faster from silent failures in multi-hour agent jobs, because the agent can surface the exact failure point in real time rather than the engineer discovering it only when checking results.

## What they did

During the Cursor engineering keynote segment of the AI Engineer World's Fair, the speaker described a human-to-agent coordination pattern used internally: agents running long autonomous jobs (e.g. generating evals, solving difficult problems) are given a Slack/paging tool so that if infrastructure goes down or something goes wrong, the agent messages the engineer directly rather than silently failing. The explicit example given was 'you don't want to lose six hours because your infra was down — the model should page you right now.' The broader conference framing was 'loop stacking' — identifying which loop you are working in, going up a loop when ready to scale, going down a loop when debugging reliability.

## Relevance to YOLO loop

The YOLO loop already runs multi-step agent jobs; adding an outbound Slack interrupt tool closes the gap where silent failures waste compute and developer time. The 'go down a loop to fix reliability' heuristic also gives a concrete mental model for debugging agent reliability issues.

## Notes

Conference talk is long (463k char transcript). The Cursor engineering segment on human-to-agent coordination and the recursive self-improvement / brain-to-galaxy-brain meter sections are the most actionable for dev loop design. The 'loop craft' essay by Swix referenced in the keynote may be worth reading separately.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-01-software-factories-loop-stacking` |
| Channel | aie |
| Video | [WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF](https://www.youtube.com/watch?v=htM02KMNZnk) |
| Published | 2026-07-01 |
| Ingested upstream | 2026-07-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
