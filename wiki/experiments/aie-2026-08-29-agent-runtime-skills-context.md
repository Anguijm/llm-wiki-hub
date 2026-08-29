# Structure agent context as composable skill units with progressive disclosure to control context window bloat

> Back to [[experiments-index]]

Source: **[Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan](https://www.youtube.com/watch?v=32nrHU6zHU8)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we decompose agent instructions into independently testable skill units (each containing domain instructions plus tool execution), and compose context dynamically by loading only relevant skills per task with progressive disclosure of metadata, then we will reduce context-window overload and improve agent focus without sacrificing capability, because skills as units of context can be tested in isolation and reused across agents.

## What they did

Roberto and Uday described Navan's layered agent stack in production (high daily token volume, travel/expense domain). For context management they define 'skills' as two-part units: instructions/context for a domain or task, plus the agentic tool-execution component. The agent composes context dynamically from relevant skills, starting with limited scope and expanding via metadata progressive disclosure. For observability they intercept all pre-tool and post-tool hooks at the Claude agent level to capture exactly which tools were called, what decisions were made, and why—replacing log-trawling with structured trace replay. They also use A2A protocol for inter-team agent communication and maintain a single master agent with sub-agents rather than a flat multi-agent mesh.

## Relevance to YOLO loop

Skills as composable context units directly improves the YOLO loop's instruction management: instead of a monolithic system prompt, the loop loads the minimal skill set for the current task, reducing noise and improving reproducibility of agent behavior.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-agent-runtime-skills-context` |
| Channel | aie |
| Video | [Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan](https://www.youtube.com/watch?v=32nrHU6zHU8) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
