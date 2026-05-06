# Add a Self-Reflection Step That Rewrites the Agent's Own System Prompt

> Back to [[experiments-index]]

Source: **[This Agent Self-Evolves (Fully explained)](https://www.youtube.com/watch?v=2zhchG0r6iI)** · AIJasonZ · 2026-04-22

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we allow the YOLO loop agent to evaluate its own performance after each task and propose edits to its system prompt, then over multiple iterations it will drift toward more effective self-instruction, because agents with write-access to their own prompts can encode learned heuristics without human intervention.

## What they did

Speaker fully explained an architecture where an agent reviews its own outputs, scores them against a rubric, and then rewrites or appends to its own system prompt or memory store before the next run, creating a closed self-improvement loop without human prompt engineering.

## Relevance to YOLO loop

This is a direct architectural extension of the YOLO loop: rather than manually tuning prompts based on observations, the loop itself proposes and applies prompt updates, which could accelerate experimentation but also introduces risk of prompt drift that needs guardrails.

## Notes

[2026-05-06T19:43:19Z] DISCARD: Duplicate of experiments/self-evolving-agent/ (built and validated through 5 cycles, May 2026 session).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-22 | `backlog` | Extracted from YouTube RSS |
|  | `` | Triage 2026-05-05: Duplicate of experiments/self-evolving-agent/ (built and validated through 5 cycles, May 2026 session). |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-04-22-self-evolving-agent` |
| Channel | AIJasonZ |
| Video | [This Agent Self-Evolves (Fully explained)](https://www.youtube.com/watch?v=2zhchG0r6iI) |
| Published | 2026-04-22 |
| Ingested upstream | 2026-04-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
