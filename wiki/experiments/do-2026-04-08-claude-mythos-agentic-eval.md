# Benchmark Claude Mythos on Open-Ended Agentic Tasks in the YOLO Loop

> Back to [[experiments-index]]

Source: **[Claude Mythos might actually be AGI… wtf](https://www.youtube.com/watch?v=ZruZhMdFdl8)** · DavidOndrej · 2026-04-08

**Status:** `adopted` · **Verdict:** `adopted` · **Effort:** `low`

---

## Hypothesis

If we run Claude Mythos on our existing suite of multi-step agentic tasks inside the YOLO loop, then we will observe measurably fewer clarification requests and higher task completion rates compared to prior Claude versions, because the model reportedly demonstrates stronger autonomous reasoning and self-correction.

## What they did

Speaker demoed Claude Mythos performing complex, multi-step reasoning and agentic tasks with minimal human intervention, arguing its behavior qualitatively resembles AGI-level generalization across novel problems.

## Relevance to YOLO loop

If Mythos reduces mid-loop failures and clarification interrupts, it could replace or augment our current backbone model in the YOLO loop with minimal prompt changes, improving end-to-end task throughput.

## Notes

Adopted 2026-04-09: low-effort model-swap benchmark. Reframed from 'Claude Mythos' (unverifiable marketing name) to 'latest-Claude-vs-current-backbone on N historical YOLO build specs, measuring clarification requests, council retry count, and completion rate'. Promoted to tick_queue_approved as 'model-eval-backbone'.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-08 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-04-08-claude-mythos-agentic-eval` |
| Channel | DavidOndrej |
| Video | [Claude Mythos might actually be AGI… wtf](https://www.youtube.com/watch?v=ZruZhMdFdl8) |
| Published | 2026-04-08 |
| Ingested upstream | 2026-04-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
