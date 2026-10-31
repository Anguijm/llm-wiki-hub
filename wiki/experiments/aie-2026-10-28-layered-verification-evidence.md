# Require agent-generated verification evidence in a layered review pipeline

> Back to [[experiments-index]]

Source: **[How Anthropic Merges 30,000 Code Changes a Day - Manish Kapur, Sonar & Addy Osmani, Anthropic](https://www.youtube.com/watch?v=AnsXWH2_EBU)** · aie · 2026-10-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we make coding agents attach evidence (e2e results, browser recordings, screenshots, lint output) and run deterministic static analysis before agentic review, then more defects will be caught before human review because each layer checks a different failure class.

## What they did

The speakers describe a three-layer pipeline: deterministic static analysis, agentic review of intent and logic, and supply-chain security. Agents generate verification evidence such as headless browser recordings and screenshots for UI PRs. A first-pass Claude Code review runs before human maintainers, team taste is codified in shared claude.md and agents.md files, and sandbox boundaries keep agents contained.

## Relevance to YOLO loop

high: Defines a layered verification and evidence-artifact pattern for agent harnesses.

## Notes

Statistics in the talk come from vendors (Sonar, CircleCI); treat as context, not evidence.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-30 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-28-layered-verification-evidence` |
| Channel | aie |
| Video | [How Anthropic Merges 30,000 Code Changes a Day - Manish Kapur, Sonar & Addy Osmani, Anthropic](https://www.youtube.com/watch?v=AnsXWH2_EBU) |
| Published | 2026-10-28 |
| Ingested upstream | 2026-10-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
