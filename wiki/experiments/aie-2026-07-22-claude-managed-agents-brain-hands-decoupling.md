# Decouple Agent Harness (Brain) from Execution Sandbox (Hands) with an Append-Only Session Log

> Back to [[experiments-index]]

Source: **[Claude for Long-Horizon Tasks — Lance Martin, Anthropic](https://www.youtube.com/watch?v=9QebvrrY3KY)** · aie · 2026-07-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we separate the agent harness into a stateless process that communicates with an append-only session log, and isolate execution into disposable sandboxes with credentials stored in a separate vault, then long-running agents become resilient to container failures and safe from credential exposure because the session is never lost even if the harness or sandbox crashes.

## What they did

Lance Martin described the architecture underpinning Claude Managed Agents (released April 2025). The core insight from early prototypes: putting the harness and sandbox in the same container means a container crash loses the entire session. Solution: the harness becomes a stateless process; the session is an external append-only event log (the agent's persistent context object); sandboxes (hands) are ephemeral containers that do the actual work; credentials live in a separate vault never injected into the sandbox. Claude can manage many sandboxes in parallel from one harness. Context management improves because the model can always fetch old context from the persistent log rather than relying on what survived compaction. He also described 'dreaming' — an offline process where the agent reviews its session log and memory store, updates memory with corrected or consolidated information, validated via evals showing dreaming improves task performance. Key memory advice: use a general substrate (file system or DB) and let the model structure its own memory rather than prescribing a schema.

## Relevance to YOLO loop

The YOLO loop's current architecture likely co-locates harness and execution. Implementing brain/hands decoupling with an append-only session log would make the loop resilient to mid-run failures, enable the loop to resume from any checkpoint, and allow parallel execution branches. The dreaming pattern maps directly to the loop's post-run reflection and memory consolidation step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-22-claude-managed-agents-brain-hands-decoupling` |
| Channel | aie |
| Video | [Claude for Long-Horizon Tasks — Lance Martin, Anthropic](https://www.youtube.com/watch?v=9QebvrrY3KY) |
| Published | 2026-07-22 |
| Ingested upstream | 2026-07-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
