# Apply classical software engineering disciplines (decomposition, SoC, idempotency, threat modeling) explicitly when designing agents

> Back to [[experiments-index]]

Source: **[Build Systems, Not Code - Angie Jones, Agentic AI Foundation](https://www.youtube.com/watch?v=ZD9-4fW2HhM)** · aie · 2026-06-25

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we design agentic systems using explicit software engineering disciplines — decomposing giant prompts into single-responsibility skills, defining stop/retry/escalate workflow termination states, writing an agent's-in-D file per system level, enforcing idempotent actions with lint passes, and applying least-privilege threat modeling to untrusted inputs — then agents will be more reliable and maintainable than those designed by letting a coding agent scaffold them, because the coding agent will produce a giant prompt without proper separation of concerns.

## What they did

Angie walked through designing a 'Relocation Scout' house-hunting agent as a concrete example. She identified five engineering disciplines that directly transfer: systems thinking (the agent is a component with dependencies and failure modes, not the whole system), workflow design (explicit stop/retry/escalate paths shape the architecture), decomposition (giant prompts are a code smell; she split one prompt into four distinct responsibilities), separation of concerns (decide whether logic belongs in the prompt, a skill, a schema, or a sub-agent), idempotent actions (a lint pass checks what state was written before retrying, preventing duplicate emails), and threat modeling (treat all external listing content as untrusted input; wall high-impact actions like submitting offers behind human approval to reduce blast radius). She also mandated an agent's-in-D maintainability file at every system level so any agent or human can cold-start without reverse-engineering prompts.

## Relevance to YOLO loop

High relevance as a design checklist for any new agent we add to our loop: use her five disciplines as a pre-build review gate, especially the idempotency lint pass and the human-approval wall for irreversible actions.

## Notes

Backlog triage 2026-06-27 (owner-preference model). Classical SWE disciplines for agents (decomposition, SoC, termination states, threat modeling) — skills + guardrails + harness-health fit.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-25 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-25-build-systems-not-code-agent-design` |
| Channel | aie |
| Video | [Build Systems, Not Code - Angie Jones, Agentic AI Foundation](https://www.youtube.com/watch?v=ZD9-4fW2HhM) |
| Published | 2026-06-25 |
| Ingested upstream | 2026-06-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
