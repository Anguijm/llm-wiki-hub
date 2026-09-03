# Audit your agent stack against the six knowledge-work primitives

> Back to [[experiments-index]]

Source: **[From coding to Knowledge work agents — Karan Vaidya, Composio](https://www.youtube.com/watch?v=xxfMT-bPEmU)** · aie · 2026-09-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we evaluate our agent infrastructure against the six primitives (centralization, history/record, context, guardrails, governance, reversibility), then we will identify the specific gaps causing knowledge-work agents to underperform compared to coding agents, because coding agents succeeded precisely because all six were present in the code ecosystem by default.

## What they did

Karan Vaidya argued that coding agents succeeded because the surrounding infrastructure (repo, git history, CI/CD, linters, revert) provided six primitives for free: centralization of truth, a record of past actions, two types of context (architectural and business), guardrails, governance over what the agent can reach, and reversibility. He then described how Composio is building each of these primitives for knowledge-work domains (e.g., a unified connection layer for centralization, action logs for history, sandbox environments for irreversible actions).

## Relevance to YOLO loop

Directly maps to how we instrument our dev loop agents: we can score our current YOLO loop against each primitive and prioritize which missing infrastructure to build first, especially reversibility (sandboxed dry-runs before mutations) and record-keeping (action logs per agent run).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-03-composio-knowledge-work-six-primitives` |
| Channel | aie |
| Video | [From coding to Knowledge work agents — Karan Vaidya, Composio](https://www.youtube.com/watch?v=xxfMT-bPEmU) |
| Published | 2026-09-03 |
| Ingested upstream | 2026-09-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
