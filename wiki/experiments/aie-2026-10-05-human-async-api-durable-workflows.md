# Implement durable workflow primitives (wait condition + signal) for human-in-the-loop steps in multi-agent pipelines

> Back to [[experiments-index]]

Source: **[The Human Is an Async API — Melanie Warrick, Temporal](https://www.youtube.com/watch?v=jc3kbZkuHTo)** · aie · 2026-10-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we wrap human-in-the-loop approval steps in durable workflow primitives (a wait condition that pauses only the affected sub-workflow and a signal that resumes it on human input), then the rest of the agent pipeline continues running during the pause and the system recovers correctly after restarts, because Temporal's demo showed that durable execution replays event history on restart without re-executing completed steps, and the approval signal was correctly processed after the worker came back online.

## What they did

Melanie Warrick from Temporal demoed a multi-agent ice cream delivery system (fleet agent, customer agent, dispatch agent) integrated with Google's A2A framework and Temporal for state management. She showed a human order-change approval pausing only driver A's workflow while the rest of the system kept running. She then killed the worker mid-approval to show durable execution: on restart, the event log replayed to the last known state, the queued approval signal was processed, and the order was correctly routed. She articulated the two core primitives: wait condition (pause workflow) and signal (resume with result). She also discussed alert fatigue as the counter-pressure to excessive human-in-the-loop checkpoints.

## Relevance to YOLO loop

Directly applicable to YOLO loop steps that require human review or approval before proceeding. The wait+signal pattern lets us add human gates without blocking the entire pipeline, and the durable execution guarantee means we don't lose progress if a worker crashes during a long agent run.

## Notes

Temporal is integrated with Google A2A framework. The key design question per Melanie: 'What is the cost of being wrong?' to calibrate how many human-in-the-loop gates to add. Alert fatigue is the failure mode of too many gates. Demo code is on GitHub, linked via QR in the talk.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-05-human-async-api-durable-workflows` |
| Channel | aie |
| Video | [The Human Is an Async API — Melanie Warrick, Temporal](https://www.youtube.com/watch?v=jc3kbZkuHTo) |
| Published | 2026-10-05 |
| Ingested upstream | 2026-10-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
