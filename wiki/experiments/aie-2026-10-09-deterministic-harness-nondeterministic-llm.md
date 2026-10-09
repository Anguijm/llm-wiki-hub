# Separate agent reasoning from execution by compiling LLM plans into deterministic workflow graphs

> Back to [[experiments-index]]

Source: **[Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](https://www.youtube.com/watch?v=NaOkR3VSfR4)** · aie · 2026-10-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we have the LLM produce a multi-step plan and then compile that plan into a deterministic workflow engine (e.g., Conductor) rather than letting the LLM drive each action step-by-step, then production agent reliability improves because non-determinism is confined to the planning phase while execution follows auditable, repeatable paths.

## What they did

Viren Baraiya (Orkes/Conductor) presented the harness-as-application pattern: agents should not be single components but orchestrated systems where the harness is the application. Key insight: harnesses must blend deterministic and non-deterministic parts—LLM handles reasoning/planning, deterministic workflow engine handles execution sequences where predictability is required (e.g., Kubernetes cluster restart, payment flows). He demoed an SRE agent that receives a problem, calls LLM to produce a multi-step remediation plan, compiles that plan via a 'plan and compile' tool into a Conductor workflow, executes it, then loops again to observe results and plan the next iteration. The agent proposed multiple steps at once rather than one at a time, improving efficiency. He also covered background agents, event-driven agents, long-running coordinators, and multi-agent systems as production patterns beyond chatbots.

## Relevance to YOLO loop

Directly relevant to YOLO loop architecture: compile agent plans into deterministic steps before execution to make the loop auditable and safe for production actions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-09-deterministic-harness-nondeterministic-llm` |
| Channel | aie |
| Video | [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](https://www.youtube.com/watch?v=NaOkR3VSfR4) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
