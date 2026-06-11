# Classify Each YOLO Loop Dependency by Shelf-Life and Replaceability

> Back to [[experiments-index]]

Source: **[You're Building AI Agents on Layers That Won't Exist in 18 Months. (What this Means for You)](https://www.youtube.com/watch?v=7HP1jFJ9W1c)** · nb · 2026-04-07

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we tag every external library, orchestration framework, and model API in our stack with an estimated deprecation horizon, then we can isolate business logic from ephemeral scaffolding and reduce future rework, because agent frameworks (LangChain, AutoGPT-style wrappers) are historically replaced by native model capabilities within 12-18 months.

## What they did

Speaker argued that current AI agent frameworks and middleware layers (orchestration libs, memory stores, tool-calling wrappers) will be absorbed directly into foundation models or superseded by new paradigms, making code tightly coupled to them a liability. Recommended building on thin abstractions or owning the logic layer independently of any specific framework.

## Relevance to YOLO loop

Directly applies to how the YOLO loop chains tools: if orchestration glue (e.g., specific agent frameworks) is ephemeral, the loop should be architected so the core spec-execute-eval cycle is framework-agnostic and the integration points are swappable.

## Notes

Adopted 2026-04-08 as a ONE-TIME deliverable, not ongoing infrastructure. Produce STACK_AUDIT.md for harness-cli listing each dependency (Next.js, Anthropic SDK, Gemini SDK, commander, chalk, etc.) with: estimated deprecation horizon, what would replace it, how tightly coupled our code is, and migration cost. Snapshot only — do not maintain ongoing horizon tags. YOLO single-file HTML tools pass this trivially (zero deps) so they need no audit.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-07 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-07-ephemeral-layers-stack-audit` |
| Channel | nb |
| Video | [You're Building AI Agents on Layers That Won't Exist in 18 Months. (What this Means for You)](https://www.youtube.com/watch?v=7HP1jFJ9W1c) |
| Published | 2026-04-07 |
| Ingested upstream | 2026-04-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
