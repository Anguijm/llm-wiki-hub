# Build the agent orchestration layer in TypeScript with Zod schemas shared end-to-end

> Back to [[experiments-index]]

Source: **[A Song of Types and Agents - Roberto Stagi, Ratel](https://www.youtube.com/watch?v=UlFB6efYN5Q)** · aie · 2026-07-12

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we implement our agent loop, tools, backend services, and UI in a single TypeScript codebase using Zod as the unified schema layer, then we will eliminate the type-synchronization overhead of a Python-agent + React-frontend split and get better AI coding-agent output quality, because coding agents now default to TypeScript and the NPM ecosystem provides native integrations for auth, payments, and infra that Python requires separate services for.

## What they did

Roberto Stagi (CTO, Ratel) argued that TypeScript overtook Python as the most-used GitHub language in August 2025 specifically because coding agents (Cursor, Claude Code, Codex) default to generating TypeScript for application-layer code. He made the case for TypeScript as the agent-layer language on four grounds: (1) coding agents will improve faster in TypeScript because more TypeScript apps feed their training data; (2) NPM is the richest package ecosystem (auth, payments, UI, infra all native); (3) one language for agent loop + tools + backend + UI eliminates the Python-service / React-app boundary and the dual-typing problem; (4) Zod can serve as a single schema definition used identically in model, backend, and UI. He noted Python remains dominant for training/inference/research but predicts the agent (application) layer will be NPM-shipped.

## Relevance to YOLO loop

Directly actionable for any new agent or tool we build: default to TypeScript + Zod rather than Python + Pydantic when the artifact is an application-layer agent, and measure whether coding-agent output quality and cross-layer type consistency improve.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-12-typescript-agent-layer` |
| Channel | aie |
| Video | [A Song of Types and Agents - Roberto Stagi, Ratel](https://www.youtube.com/watch?v=UlFB6efYN5Q) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
