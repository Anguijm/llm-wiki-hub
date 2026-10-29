# Add stopping rules and attention budgets to recurring agent tasks

> Back to [[experiments-index]]

Source: **[Are Your AI Agents Doing Real Work Or Productivity Theater? Here Are 4 Principles I Use.](https://www.youtube.com/watch?v=NIRFVjttNvA)** · nb · 2026-10-27

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we define explicit termination conditions and an attention budget before enabling any recurring scheduled agent task, then unread reports and wasted tokens will decrease, because unmonitored recurring output is a compounding tax on attention.

## What they did

The speaker set stopping rules before scheduling recurring tasks, such as terminating if unread for 3 days or when extra passes stop yielding new insight. They gave a chief-of-staff agent an attention budget so it interrupts humans only for high-leverage items. They required agents to show raw measurements and formulas, which exposed a contractor's wrong floor-area multiplier. They added a truth-teller meta-prompt to counter sycophancy and counted downstream human review hours before prompting.

## Relevance to YOLO loop

high: Directly applicable to scheduled and looping YOLO agents: termination conditions, show-your-work verification and anti-sycophancy checks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-28 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-27-agent-stopping-rules` |
| Channel | nb |
| Video | [Are Your AI Agents Doing Real Work Or Productivity Theater? Here Are 4 Principles I Use.](https://www.youtube.com/watch?v=NIRFVjttNvA) |
| Published | 2026-10-27 |
| Ingested upstream | 2026-10-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
