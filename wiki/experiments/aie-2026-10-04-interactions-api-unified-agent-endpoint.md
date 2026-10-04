# Migrate Agent Orchestration to a Unified Interactions API to Support Both Instant and Long-Running Agent Calls

> Back to [[experiments-index]]

Source: **[An Interaction Is All You Need — Ivan Leo, Google DeepMind](https://www.youtube.com/watch?v=8aVbXXvJUY4)** · aie · 2026-10-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Google DeepMind's Interactions API as a single endpoint for both quick model completions and extended agentic runs (e.g., deep research), then we will simplify our orchestration code and future-proof it for new model types, because the API is designed to handle the full spectrum from nano model calls to multi-minute agent sessions under one interface.

## What they did

Ivan Leo described the Interactions API as Google's unified API layer replacing fragmented endpoints for different model types. It supports everything from Gemini Nano image generation to deep research agents that run for 3+ minutes. Key features: (1) a man-in-the-middle proxy that dynamically injects secrets so agents never see raw credentials, (2) named agents (up to 1,000) with frozen environment configurations, (3) a Gemini API CLI for local iteration that packages and deploys agents with one command, (4) an interactions API skill that coding agents can consume to auto-migrate old Gemini API code to the new interface.

## Relevance to YOLO loop

Maps to the agent-orchestration and secrets-management layers of the YOLO loop: a unified API reduces integration complexity when mixing fast and slow agent calls, and the proxy-based credential injection pattern is directly applicable to any agent that needs to call external APIs safely.

## Notes

The man-in-the-middle proxy pattern for credential injection is immediately actionable regardless of using DeepMind infra — implement the same pattern locally: agent receives a placeholder token, a sidecar proxy replaces it with the real secret before the outbound call.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-04-interactions-api-unified-agent-endpoint` |
| Channel | aie |
| Video | [An Interaction Is All You Need — Ivan Leo, Google DeepMind](https://www.youtube.com/watch?v=8aVbXXvJUY4) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
