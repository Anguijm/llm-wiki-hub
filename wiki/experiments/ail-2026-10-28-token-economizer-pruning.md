# Trial Token Economizer tool pruning in Claude Code

> Back to [[experiments-index]]

Source: **[This Is Microsoft's New Plan To Fix Claude's Usage Limits](https://www.youtube.com/watch?v=1kQ_1_QL5Es)** · ail · 2026-10-28

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we install Microsoft's Token Economizer with tool pruning enabled in a Claude Code project, then per-message context and session cost will drop by about 20-30% without lowering task completion, because tools unused across consecutive sessions are disabled automatically.

## What they did

The speaker installed the open-source Token Economizer plugin and configured lifecycle hooks. Tools unused across 10 messages over two consecutive sessions were turned off. On a sample project, 276 tools were disabled and per-message context fell from 34.3K to 24.4K tokens. A practical task dropped from 99 to 79 steps at 21% lower cost. The speaker checked results with the status, tool-prune and tool-prune-measure commands, and restored wrongly disabled tools with tool-prune-restore.

## Relevance to YOLO loop

high: Direct Claude Code harness practice (hooks, context pruning, token cost) that can be measured with before/after runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-28 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-10-28-token-economizer-pruning` |
| Channel | ail |
| Video | [This Is Microsoft's New Plan To Fix Claude's Usage Limits](https://www.youtube.com/watch?v=1kQ_1_QL5Es) |
| Published | 2026-10-28 |
| Ingested upstream | 2026-10-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
