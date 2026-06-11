# Stress-Test Knowledge Retrieval Under Load Conditions

> Back to [[experiments-index]]

Source: **[Karpathy's Wiki vs. Open Brain. One Fails When You Need It Most.](https://www.youtube.com/watch?v=dxq7WtWxi44)** · nb · 2026-04-22

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we benchmark Karpathy's Wiki-style retrieval against Open Brain under high-demand or edge-case queries, then we will identify which system degrades gracefully and which fails silently, because reliability under stress is often hidden in demos but critical in production.

## What they did

Speaker compared Karpathy's wiki-based knowledge retrieval approach to Open Brain, demonstrating that one system fails precisely when queries are most complex or time-sensitive, arguing that failure modes matter more than average-case performance.

## Relevance to YOLO loop

Directly relevant to how the YOLO loop sources context and knowledge; choosing the wrong retrieval backend could cause silent failures during complex coding tasks where correctness is hardest to verify.

## Notes

[2026-05-06T19:43:19Z] DEFER: Reactor commentary on Karpathy. Now that @AndrejKarpathy is in the channel roster (since 2026-04-30), we get his content directly.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-22 | `backlog` | Extracted from YouTube RSS |
|  | `` | Triage 2026-05-05: Reactor commentary on Karpathy. Now that @AndrejKarpathy is in the channel roster (since 2026-04-30), we get his content directly. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-22-wiki-vs-openbrain-reliability` |
| Channel | nb |
| Video | [Karpathy's Wiki vs. Open Brain. One Fails When You Need It Most.](https://www.youtube.com/watch?v=dxq7WtWxi44) |
| Published | 2026-04-22 |
| Ingested upstream | 2026-04-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
