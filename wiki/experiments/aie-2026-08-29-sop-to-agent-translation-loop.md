# Build a refinement loop that translates human SOPs into agent-executable SOP corpus and measures correction rate over time

> Back to [[experiments-index]]

Source: **[Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk](https://www.youtube.com/watch?v=dQ-_i1tZiws)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we treat the agent's SOP corpus (preconditions, decision points, backend calls, validation steps, recovery paths, evidence of execution) as the primary asset rather than the agent loop itself, and instrument a correction-capture feedback loop, then accuracy will compound over time because each expert correction becomes an executable change that generalizes to all future similar cases.

## What they did

Dmitry described Maersk's production shipping exception-handling system: 200+ concurrent agent instances processing shipment exceptions, with latencies of minutes to 10 minutes due to legacy system dependencies. The key insight was that legacy SOPs describe what a human sees and clicks (screenshots in sequence) while agent SOPs require preconditions, identifiers, backend calls, validation, and recovery. The team built a three-part architecture: SOP memory corpus (20:1 ratio to runtime, country-specific variants), execution runtime, and a theme-feedback capture system that clusters failures and hands back actionable priorities. Over 9 months they accumulated 100,000+ corrections, visualized as heat maps to align experts and engineers on the same priorities. They explicitly do not use MCP because it produces bloated responses; they distill via function calling.

## Relevance to YOLO loop

The correction-capture and corpus-refinement loop is a meta-level YOLO loop operating on the agent's own instructions: failed traces feed back into SOP improvement, which is directly applicable to any YOLO loop that operates against a process playbook.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-sop-to-agent-translation-loop` |
| Channel | aie |
| Video | [Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk](https://www.youtube.com/watch?v=dQ-_i1tZiws) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
