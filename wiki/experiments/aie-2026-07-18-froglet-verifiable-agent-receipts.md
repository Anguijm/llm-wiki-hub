# Add cryptographically-signed execution receipts to agent tool calls for auditability and replay

> Back to [[experiments-index]]

Source: **[Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio](https://www.youtube.com/watch?v=Fu45geO3zX8)** · aie · 2026-07-18

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If every agent tool call produces a signed receipt capturing inputs, outputs, and execution context, then multi-agent workflows become auditable and reproducible because any step can be independently verified and re-executed without trusting the agent's self-reported history.

## What they did

Armanas Povilionis introduced Froglet, an open-source protocol where each node generates a key pair at creation and signs every artifact in a chain. Agents can discover external services via a marketplace node, negotiate execution terms, pay for work across organizational boundaries, and receive a verifiable receipt. He demoed Claude invoking a Froglet MCP to publish a service, call it, and receive a signed result—all without stuffing extra context into the LLM. The protocol is transport-agnostic and does not require all nodes to share the same stack.

## Relevance to YOLO loop

The YOLO loop currently has no tamper-evident audit trail for tool calls; integrating receipt-based verification would enable post-hoc debugging, compliance auditing, and safe multi-agent collaboration without requiring full execution replay infrastructure.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-18-froglet-verifiable-agent-receipts` |
| Channel | aie |
| Video | [Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio](https://www.youtube.com/watch?v=Fu45geO3zX8) |
| Published | 2026-07-18 |
| Ingested upstream | 2026-07-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
