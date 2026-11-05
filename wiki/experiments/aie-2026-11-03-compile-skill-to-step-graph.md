# Compile one prose skill into a YAML step graph and run it on a small model

> Back to [[experiments-index]]

Source: **[Make Your AI Agents Predictable With Graph Engineering - Zachary Blumenfeld, Neo4j](https://www.youtube.com/watch?v=g_NgCLTibiM)** · aie · 2026-11-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we compile the daily researched-stories newsletter skill into an explicit YAML step graph, with rule-based steps moved into deterministic scripts, and run it on a small model such as Haiku, then wall-clock time and token cost will drop with output quality about the same, because the graph fixes the routing and the small model only handles narrow steps.

## What they did

Blumenfeld compiled a lending-approval skill (markdown skill.md plus past decision traces) into a deterministic YAML graph. Hard policy checks ran as scripts or structured decision models instead of open LLM prompts. Execution time fell from about 7.5 minutes to about 2 minutes, and to under 30 seconds with smaller models. A lightweight model (Haiku) reportedly matched the accuracy of a frontier model. Timestamped traces of each branch were stored for audit. The Neo4j storage layer is optional for a first try.

## Relevance to YOLO loop

high: Turning a prose skill into an explicit step graph with scripted rule steps, then downshifting the model tier, is not among the current practices (on-demand skills, cost ladder on reasoning effort).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-04 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-11-03-compile-skill-to-step-graph` |
| Channel | aie |
| Video | [Make Your AI Agents Predictable With Graph Engineering - Zachary Blumenfeld, Neo4j](https://www.youtube.com/watch?v=g_NgCLTibiM) |
| Published | 2026-11-03 |
| Ingested upstream | 2026-11-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
