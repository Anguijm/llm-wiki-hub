# Decouple session log and harness from the sandbox container to make agents cattle not pets

> Back to [[experiments-index]]

Source: **[Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](https://www.youtube.com/watch?v=Uv0nAf_7tyU)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we move the session log and harness outside the execution container so that only the sandbox runs inside the container, then agent sessions become stateless and disposable (cattle), enabling reliable restarts and horizontal scaling without losing session history, because Anthropic's first architecture kept everything in one container and found it created fragile 'pets' that were hard to recover when containers failed.

## What they did

Priyanka (Anthropic) described the evolution of Claude Managed Agents architecture. V1 put session log, harness, and sandbox all inside one container—easy to build but sessions became 'pets' (hard to replace). V2 decoupled: session log and harness live outside the container as durable services; the sandbox is ephemeral and replaceable. This enables the harness to make model-specific assumptions (e.g., context-reset for Sonnet 4.5's 'context anxiety') independently of the sandbox, and to update those assumptions per model release without touching the sandbox layer.

## Relevance to YOLO loop

Our dev-loop agent runs conflate session state with execution environment. Separating them would let us resume sessions after sandbox crashes and swap execution environments without losing conversation context.

## Notes

Anthropic's managed agent primitives: Environment (sandbox template with networking/packages), Agent (model + system prompt + tools), Session (unit of work = agent + environment + event stream). Harness encapsulates model-specific quirks and must be updated per model release.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-claude-managed-agents-decoupled-harness` |
| Channel | aie |
| Video | [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](https://www.youtube.com/watch?v=Uv0nAf_7tyU) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
