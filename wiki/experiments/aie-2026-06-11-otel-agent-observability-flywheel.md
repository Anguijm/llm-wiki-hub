# Instrument agent traces with OpenTelemetry auto-instrumentation then drive prompt/model experiments from the resulting dataset

> Back to [[experiments-index]]

Source: **[LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](https://www.youtube.com/watch?v=JsCCrBF7F1g)** · aie · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we add a single-line OpenTelemetry auto-instrumenter to our agent harness and pipe traces into an observability platform (e.g. Arize Phoenix OSS), then we can build curated datasets from real traces, run controlled prompt/model/config experiments against those datasets, and catch regressions before they reach production, because the trace-to-dataset-to-experiment loop closes the feedback cycle that is otherwise invisible in non-deterministic systems.

## What they did

Dat Ngo from Arize described their observability-eval-experimentation flywheel. They instrument agents via a one-line OTel auto-instrumenter that emits traces and spans capturing every tool call and branch. These traces feed into session views (multi-turn state), distributional agent graphs (branch frequency, latency hotspots), and trajectory evals. From traces, users curate datasets (input-output pairs) and run experiments—changes to prompts, models, orchestration, or configs—comparing eval scores across experiment versions to detect regressions. They also expose all primitives via CLI and MCP tools so Claude Code or other coding agents can call Arize directly to automate the observability loop. Open-source version is Arize Phoenix (single container, no Kubernetes).

## Relevance to YOLO loop

Directly maps to our YOLO loop's eval and experimentation phase. Adding OTel auto-instrumentation is low-effort and unlocks the full trace→dataset→experiment pipeline. Phoenix OSS removes any cost barrier for initial setup.

## Notes

Backlog triage 2026-06-24 (owner-preference model). OTel traces -> eval dataset — observability + eval flywheel; extends build_log/verify.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-otel-agent-observability-flywheel` |
| Channel | aie |
| Video | [LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](https://www.youtube.com/watch?v=JsCCrBF7F1g) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
