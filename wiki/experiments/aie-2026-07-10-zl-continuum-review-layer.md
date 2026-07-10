# Define a per-task review tier (output / task-direction / loop-design) and enforce it before merging agent work

> Back to [[experiments-index]]

Source: **[Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](https://www.youtube.com/watch?v=ZpK5PWX2YRM)** · aie · 2026-07-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we explicitly classify each agent task as requiring output-level review, task-direction review, or loop-design review based on criticality and capability drift, then we will maintain judgment quality as agent capability increases because the review requirement is preserved even when its location in the workflow shifts upward.

## What they did

Alex Volkov introduced the Z/L Continuum — a spectrum from 'zero-read, full delegation' (Ryan LeFebvre/OpenAI position: code is free, humans direct via prompts and guardrails) to 'read every line' (Mario Zechner position: critical code must be read because agents compound errors with delayed pain). He argued the correct position is not fixed but moves with capability drift: yesterday you reviewed outputs, today you review task direction, tomorrow you review loop design. He introduced 'loops' as the emerging primitive — fancy cron jobs that discover tasks, write plans, execute, and self-verify — and warned that when an agent loop grades its own work, review is hidden not removed, raising the stakes on where human judgment is applied. His conclusion: 'Not every line in 2026 needs your eyes. Every system still needs your judgment.'

## Relevance to YOLO loop

The YOLO loop currently has implicit, inconsistent review. Tagging each task with a review tier (output-read for critical paths, direction-check for standard features, loop-audit for self-healing loops) would make review explicit and ensure judgment is applied at the right layer as we adopt more autonomous loop-based execution.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-10-zl-continuum-review-layer` |
| Channel | aie |
| Video | [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](https://www.youtube.com/watch?v=ZpK5PWX2YRM) |
| Published | 2026-07-10 |
| Ingested upstream | 2026-07-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
