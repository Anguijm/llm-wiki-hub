# Write an AI constitution document to codify agent behavior rules, primitives, and trust-earning criteria

> Back to [[experiments-index]]

Source: **[Peter Smith & RK Sharma - Beyond the Chatbot (including demo) | [un]prompted 2026](https://www.youtube.com/watch?v=XKKFje5IkGs)** · up · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we create a written AI constitution that defines the eight operational primitives, rules for irreversible actions, human-approval thresholds, and audit logging requirements before deploying production agents, then agents will make fewer unsafe autonomous decisions and stakeholder trust will build faster because the constitution provides shared governance that all agents and humans reference.

## What they did

Salesforce SOC team described an AI constitution as a document capturing the rules for how to deliver an agentic SOC. Their constitution's first article defines the eight agent primitives (ask mode, plan mode, human in the loop, agent reasoning loops, etc.). They use it to ensure agents earn trust incrementally—starting with plan-and-approve flows and only granting broader autonomy as reliability is demonstrated. The document also serves as an audit trail artifact. The entire SOC pipeline config was written by Claude; no hand-written code was needed from the security engineers.

## Relevance to YOLO loop

We can draft an analogous AI constitution for our dev loop: define which actions require human approval, what constitutes an irreversible action, and what audit logging we require. Treat it as a living document updated as agents earn trust.

## Notes

Backlog triage 2026-06-24 (owner-preference model). AI constitution (rules, irreversible-action gates, audit logging) — matches adopted guardrails + security work.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `up-2026-06-11-salesforce-agentic-soc-ai-constitution` |
| Channel | up |
| Video | [Peter Smith & RK Sharma - Beyond the Chatbot (including demo) | [un]prompted 2026](https://www.youtube.com/watch?v=XKKFje5IkGs) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
