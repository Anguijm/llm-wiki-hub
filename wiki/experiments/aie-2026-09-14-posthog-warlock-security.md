# Build a Deterministic Content Scanner (Warlock) as a Security Layer Around Agents with Shell Access

> Back to [[experiments-index]]

Source: **[We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog](https://www.youtube.com/watch?v=4lXks428C9o)** · aie · 2026-09-14

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we add a deterministic rule-based content scanner that inspects both inputs flowing into an agent and outputs/commands the agent produces — with deny-by-default enforcement and fail-closed behavior — then we can ship agents that execute real shell commands without catastrophic security failures, because prompt injection and supply-chain attacks compose in non-obvious ways that probabilistic prompt-based guards cannot reliably block.

## What they did

Sarah Sanders described building the PostHog Wizard (an agentic CLI that installs PostHog SDKs, instruments events, and sets up dashboards — running 8,000 times/week). She audited its security posture and found early versions relied only on prompts and an allow-list, which she deemed insufficient. She built the Warlock: a deterministic scanner with four-part rules (metadata: severity/category/action/direction; strings: patterns to match; condition: when the rule fires; tests: positive and negative examples). Key design principles: enforcement must be deterministic (not probabilistic), judgment adds nuance only where needed, the scanner fails closed (kills all wizard runs if it has a bad day), and rules are tested with negative cases to minimize false positives. Real-world impact (not scariness) determines severity — rm -rf is scary but common. Full security posture: prompts for steering only, sandbox execution, deny-by-default, vault for secrets, Warlock for content scanning (in and out), triage for noise reduction, and telemetry throughout. The Wizard, Warlock, and context mill are all open source.

## Relevance to YOLO loop

Our YOLO loop runs agents with tool access (file system, shell, APIs). Adding a Warlock-style deterministic scanner on tool call inputs and outputs — even starting with a small rule set for the most dangerous patterns — would provide a concrete security layer that doesn't rely on the model's own judgment for safety-critical decisions.

## Notes

Open source: Wizard, Warlock, and context mill available from PostHog GitHub. Key insight: 'attacks compose, code review doesn't' — most gaps were two innocent things shaking hands. Scan your own supply chain (context injected into the model), not just user inputs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-14-posthog-warlock-security` |
| Channel | aie |
| Video | [We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog](https://www.youtube.com/watch?v=4lXks428C9o) |
| Published | 2026-09-14 |
| Ingested upstream | 2026-09-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
