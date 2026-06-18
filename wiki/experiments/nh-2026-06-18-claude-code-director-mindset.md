# Add 'Intent + Why' Preamble to Every Claude Code Task Spec

> Back to [[experiments-index]]

Source: **[How to Build Effective Claude Code Agents in 2026](https://www.youtube.com/watch?v=RzLV8sfFdMM)** · nh · 2026-06-18

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we prepend every Claude Code task with an explicit statement of intent (what we are building) and rationale (why we are building it), then the agent will make better architectural and implementation decisions because the 'why' shapes the 'how' and reduces misaligned tool calls and scope drift.

## What they did

Cole Medine (guest) described using Claude Code as a 'second brain' and treating yourself as a product manager or director of the agent rather than a coder. His key insight was 'intent engineering': always giving Claude Code the why behind a task, not just the what or how. He noted this feels anthropomorphic but measurably improves results. He also emphasized writing good specs and plans before any build, using Claude Code's planning phase more than its building phase, and structuring CLAUDE.md as an evolving system that the agent itself helps maintain over time.

## Relevance to YOLO loop

We can immediately add a 'context and rationale' section to our standard task prompt template in the YOLO loop, requiring every agent invocation to include the business or technical reason for the change before any implementation instructions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-18-claude-code-director-mindset` |
| Channel | nh |
| Video | [How to Build Effective Claude Code Agents in 2026](https://www.youtube.com/watch?v=RzLV8sfFdMM) |
| Published | 2026-06-18 |
| Ingested upstream | 2026-06-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
