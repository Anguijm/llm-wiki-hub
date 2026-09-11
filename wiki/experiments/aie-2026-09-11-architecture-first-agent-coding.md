# Shift Agent Coding Review to Architecture Decisions Before Code Generation

> Back to [[experiments-index]]

Source: **[Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition](https://www.youtube.com/watch?v=H7vFrcNWXzs)** · aie · 2026-09-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we invest the majority of human review time in software architecture and intent specification before handing tasks to coding agents, rather than reviewing generated code line-by-line after the fact, then the quality of agent-generated code will increase and post-hoc rejection rates will decrease because agents land their code on a well-structured substrate with clear constraints.

## What they did

Jonathan Kelly described the Dioxus team's hard-won lesson: they maxed out Claude Code subscriptions and generated tens of thousands of lines of Rust, but very little cleared their quality bar. They became 'slop cannons.' The fix was to shift effort upstream — most development time is now spent on architecture decisions, anticipating future feature evolution, and specifying intent precisely in prompts before generation. They still review every PR line-by-line but found that prompt quality is the primary lever on implementation quality. They also found agents excel at building fuzz test harnesses but fail at choosing the right tests, so humans enumerate test conditions while agents generate harness scaffolding.

## Relevance to YOLO loop

Directly applicable to our YOLO loop task design: we should front-load architecture docs and intent specs (e.g., detailed CLAUDE.md context, interface contracts) before triggering agent runs, and use agents for scaffolding and harness generation rather than open-ended feature implementation on poorly-defined substrates.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-11-architecture-first-agent-coding` |
| Channel | aie |
| Video | [Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition](https://www.youtube.com/watch?v=H7vFrcNWXzs) |
| Published | 2026-09-11 |
| Ingested upstream | 2026-09-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
