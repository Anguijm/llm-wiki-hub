# Score Agent Tasks on Step-Uncertainty vs Acceptance-Criteria-Uncertainty Before Assigning to Agents

> Back to [[experiments-index]]

Source: **[Mousepower: agents that can't be measured, can't be managed. — Maximillian Piras, Yutori](https://www.youtube.com/watch?v=8KkibGU_DDY)** · aie · 2026-09-10

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we evaluate candidate agent tasks on two axes—uncertainty in task steps and uncertainty in verifying success—then we can identify the 'sweet spot' tasks (moderate step uncertainty, low verification uncertainty) where agents deliver the best ROI, and avoid wasting tokens on tasks that are either scripting-trivial or unverifiable.

## What they did

Maximillian Piras (founding designer at Yutori, computer-use model company) proposed a 2x2 mental model for valuing agent tasks: X-axis = uncertainty in the steps to perform the task (low = just write a script; high = out-of-distribution, sparse RL rewards, bad agent fit); Y-axis = uncertainty in acceptance criteria/verification (high = verification is indistinguishable from execution, waste of tokens; low = easy to validate). The sweet spot is moderate step-uncertainty (interesting enough for an agent, not so unpredictable it can't be modeled) combined with low verification uncertainty (NP-style: easier to verify than execute). For tasks in this zone, you can also build a verifier agent, creating a compound system where one agent does the work and another validates it cheaply.

## Relevance to YOLO loop

Directly applicable as a pre-task filter in our YOLO loop: before spinning up an agent for a task, score it on both axes. This should reduce failed/wasted runs and help us prioritize which parts of our dev loop are good candidates for agentic automation vs. deterministic scripting.

## Notes

Framework is conceptual/in-progress per speaker. Formalize as a scoring rubric (e.g., 1-5 on each axis) and apply retrospectively to recent agent tasks to calibrate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-10-mousepower-agent-task-uncertainty-matrix` |
| Channel | aie |
| Video | [Mousepower: agents that can't be measured, can't be managed. — Maximillian Piras, Yutori](https://www.youtube.com/watch?v=8KkibGU_DDY) |
| Published | 2026-09-10 |
| Ingested upstream | 2026-09-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
