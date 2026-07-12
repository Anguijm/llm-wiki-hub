# Replace boolean task completion with a structured 'done object' enforced by the agent control plane

> Back to [[experiments-index]]

Source: **[What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip](https://www.youtube.com/watch?v=7P0elyLIxXo)** · aie · 2026-07-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we require every agent task to emit a structured completion object (artifact, scope, rubric, evidence, verifier, approver, risk, next action) rather than a boolean done flag, and wire a separate verifier agent (different model) to check that object, then we will reduce unverified AI-generated merges and catch more silent failures, because exhaustive human verification fails at high volume and a structured done-object forces agents to surface the claims that humans would otherwise have to infer.

## What they did

Dotta (creator, Paperclip) argued that 'done' is a bundle of distinct claims—artifact produced, evidence of completion, rubric met, verifier reviewed, approver authorized, next action known—and that most agent systems flatten these to a single green checkmark, creating a new failure mode where agents produce more work than humans can verify. Paperclip's liveness model enforces: (1) explicit state transitions with first-class blockers; (2) human approval moments that leave an audit trail; (3) watchdog agents (harness-agnostic: works with Pyi, OpenAI, Claude Code, Codex) that enforce a goal until all sub-tasks complete; and (4) a separation of author from verifier (use a different model to verify than the one that wrote the code). Practical checklist: define done precisely per task, separate verifier from author, require agents to provide evidence (screenshots, browser clicks, test runs), establish a clear chain of custody to the next agent.

## Relevance to YOLO loop

Our YOLO loop currently treats agent task completion as a boolean. Adding a structured done-object schema and routing completed tasks to a second verifier model is a concrete, incremental change that directly addresses the review-debt problem surfaced in the Sachin Gupta card above.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-12-done-as-object-liveness-model` |
| Channel | aie |
| Video | [What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip](https://www.youtube.com/watch?v=7P0elyLIxXo) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
