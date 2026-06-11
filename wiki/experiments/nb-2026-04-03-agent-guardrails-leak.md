# Add explicit guardrail and fallback layers to autonomous build agents

> Back to [[experiments-index]]

Source: **[I Broke Down Anthropic's $2.5 Billion Leak. Your Agent Is Missing 12 Critical Pieces.]()** · nb · 2026-04-02

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we add explicit guardrail layers (cost caps, output validation, rollback triggers) to YOLO build agents, then autonomous builds become safer for higher-stakes projects because failures are caught and contained before they propagate.

## What they did

The leaked Anthropic architecture implies production agents need guardrails as a distinct layer — not just prompting, but structural boundaries on agent behavior, cost, and output scope.

## Actionable steps

- Define cost guardrails: max tokens per build session, max files modified
- Add output validation: agent must pass linting + test before any commit
- Implement rollback trigger: if 3 consecutive test failures, stop and report instead of looping
- Wire guardrails into program.md as mandatory build constraints

## Success metric

Zero runaway build sessions (unbounded token spend or broken commits) over 10 builds.

## Relevance to YOLO loop

As YOLO builds become more autonomous (Dark Factory pattern), explicit guardrails prevent costly failures and give confidence to increase autonomy further.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Notes

Adopted 2026-04-07: formalize structural guardrails (cost caps, output validation, rollback triggers) on top of existing approval gate + pre-filter. Maps to current "3 attempts then escalate" pattern. Low net-new work — mostly capturing what we already do as explicit constraints in program.md.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-03-agent-guardrails-leak` |
| Channel | nb |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
