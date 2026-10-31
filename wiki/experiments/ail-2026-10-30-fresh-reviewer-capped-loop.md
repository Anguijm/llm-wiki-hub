# Build a fresh-context reviewer loop with a 3-round cap and risk tiers

> Back to [[experiments-index]]

Source: **[Anthropic Just Released A New System For Using Claude Code](https://www.youtube.com/watch?v=S49gppZl8H0)** · ail · 2026-10-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a separate fresh-context reviewer sub-agent with a rules-learned review.md, risk-tiered rigor, and a 3 to 5 round cap, then first-pass merge quality will rise and token waste will fall because the reviewer avoids self-confirmation bias and stops repeating the same issues.

## What they did

An orchestrator coordinates builder, verifier and reviewer sub-agents through a state.md file. The reviewer audits against review.md, and new bugs are appended to a permanent rules-learned section. PRs are classed low, medium or high risk by customer impact, and loops are capped at 3 to 5 rounds after Anthropic saw 50+ back-and-forth rounds with 59% of issues repeating. A first-time-user agent, blocked by hooks from reading source, tests the app through its UI.

## Relevance to YOLO loop

high: Provides a full builder/verifier/reviewer loop design with caps, memory of learned rules and a blind user-test agent.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-30 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-10-30-fresh-reviewer-capped-loop` |
| Channel | ail |
| Video | [Anthropic Just Released A New System For Using Claude Code](https://www.youtube.com/watch?v=S49gppZl8H0) |
| Published | 2026-10-30 |
| Ingested upstream | 2026-10-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
