# Implement a Priority Queue (Coral) for Multi-Agent Response Ordering

> Back to [[experiments-index]]

Source: **[How I Ship Faster Than 99% of Devs (just copy me)](https://www.youtube.com/watch?v=c9nRxEy1kUY)** · do · 2026-09-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we assign priority levels (P1–P4) to concurrent agent sessions and always surface the highest-priority finished agent first, then human review time will decrease and critical work will not be blocked by lower-priority completions, because attention is directed by importance rather than arbitrary finish order.

## What they did

David built a custom tool called Coral (a fork of Zeron) that assigns priority levels to running agent sessions. When multiple agents finish, the P1 agent surfaces at the top of the queue so the human operator never responds to a P4 task while a P1 result is waiting. He contrasted this with Herder's unordered completion model.

## Relevance to YOLO loop

The YOLO loop currently handles one agent interaction at a time; when parallelism increases, a priority queue for agent completions would prevent the human review step from becoming a bottleneck on low-value tasks while high-value outputs wait.

## Notes

Coral is not yet open-sourced as of the video recording. Could prototype a simpler version with a tmux layout + a small script that sorts finished panes by a priority tag in the session name.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-09-02-priority-queue-agent-orchestration` |
| Channel | do |
| Video | [How I Ship Faster Than 99% of Devs (just copy me)](https://www.youtube.com/watch?v=c9nRxEy1kUY) |
| Published | 2026-09-02 |
| Ingested upstream | 2026-09-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
