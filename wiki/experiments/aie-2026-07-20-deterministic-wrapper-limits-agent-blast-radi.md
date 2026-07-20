# Wrap agentic reasoning in a deterministic orchestration layer that owns all credentials and side-effects

> Back to [[experiments-index]]

Source: **[We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](https://www.youtube.com/watch?v=LqLoYksJ6do)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we push all credential usage, CI triggering, and PR creation into a deterministic Go/script layer that the agent cannot directly invoke, and only use the agent for reasoning tasks (understanding CVE scope, diagnosing CI failures, deciding what to change), then the blast radius of an agent mistake is bounded by the deterministic layer's hard-coded permission set, because the agent never holds credentials and cannot perform side-effects it was not explicitly granted by the orchestrator.

## What they did

Moritz Johner described Form3's Patch Pilot: a Go application that deterministically discovers vulnerable OCI images, clones repositories, prepares a rich context directory for the agent, and then invokes CVE remediation and CI-diagnosis agents. Crucially, the Go app owns GitHub credentials, CI triggers, and PR creation — the agent only receives a local directory and a prompt, and returns a proposed changeset. The agent reasons about what the smallest effective change is and why CI failed (flaky vs. real failure vs. timeout), but cannot push to GitHub or trigger CI itself. He argued this architecture is the practical answer to 'the agent is a supply chain actor': give it the same guardrails as an engineer (code review, restricted prod credentials) but encode the guardrails in the deterministic layer rather than relying on agent self-restraint.

## Relevance to YOLO loop

Directly applicable pattern for our YOLO loop: we should audit which side-effects (git push, API calls, environment changes) our agents perform directly and move credential handling into the deterministic loop wrapper, leaving agents to only produce text/patch artifacts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-deterministic-wrapper-limits-agent-blast-radius` |
| Channel | aie |
| Video | [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](https://www.youtube.com/watch?v=LqLoYksJ6do) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
