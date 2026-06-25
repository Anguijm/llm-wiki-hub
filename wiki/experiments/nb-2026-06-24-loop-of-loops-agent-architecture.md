# Implement a Loop-of-Loops Agent Control Pattern

> Back to [[experiments-index]]

Source: **[I Stopped Prompting AI One Task At A Time. This Works Better.](https://www.youtube.com/watch?v=A4zMyjkL0Dc)** · nb · 2026-06-24

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `high`

---

## Hypothesis

If we organize recurring dev tasks as named loops that share context and hand off to each other (a loop-of-loops), then we reduce the developer's cognitive load as coordinator because agents can notice what changed across loops and stop at the right boundaries without requiring a human to re-prompt each step.

## What they did

Nate described moving from one-off prompts to 'loops' (recurring jobs with memory) and then to a 'loop of loops' — a control pattern where multiple loops (e.g. packing, weather, calendar, message) observe each other's outputs, pass context between them, and pause before taking irreversible actions. He emphasized starting with low-stakes, tedious processes (e.g. generating use cases → Linear tickets → PRDs) rather than high-impact ones like banking, and challenged viewers to map their own recurring mental-load tasks to this pattern.

## Relevance to YOLO loop

Directly maps to the YOLO loop's need for agents that handle recurring dev tasks (ticket triage, PR drafting, test runs) without requiring constant human re-prompting; the loop-of-loops pattern would let the CI/issue/PR loops share state and hand off autonomously.

## Notes

Nate teased a detailed build walkthrough in a follow-up video on Friday; that video should be tracked as a companion card once available.

Backlog triage 2026-06-24 (owner-preference model). Named loops sharing context + handoff — loop-engineering / self-improving-loop family already adopted.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-24 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-24-loop-of-loops-agent-architecture` |
| Channel | nb |
| Video | [I Stopped Prompting AI One Task At A Time. This Works Better.](https://www.youtube.com/watch?v=A4zMyjkL0Dc) |
| Published | 2026-06-24 |
| Ingested upstream | 2026-06-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
