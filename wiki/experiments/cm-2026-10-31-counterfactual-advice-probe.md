# Probe agent recommendations with counterfactual queries before accepting them

> Back to [[experiments-index]]

Source: **[Anthropic's New Study: You're Not Controlling AI as Much as You Think You Are](https://www.youtube.com/watch?v=BlbxhsItZPg)** · cm · 2026-10-31

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we ask the agent 'what would change your advice so that option B is optimal?' before accepting any design recommendation, and log whether we changed or kept the decision, then we will catch more cases of passively deferring to its lean because the answer exposes the assumptions behind its advice.

## What they did

Cole Medin summarized an Anthropic study in which analysts followed a randomized agent lean 86% of the time and reused the agent's arguments 77% of the time, while only 15% credited the AI. He suggests countering this by setting high-level priorities before looking at options, and by prompting the agent with explicit counterfactual questions to expose its decision logic. He also suggests building cheap throwaway prototypes for uncertain choices. Caveat: the study amplified the agent's persuasion, covered one task and one model, and too many multiple-choice planning questions cause fatigue.

## Relevance to YOLO loop

high: Counterfactual probing of the agent's own recommendation, checking what would flip its advice and logging the outcome, is not covered by the existing reviewer, gate or spec-first practices, which check output rather than the operator's deference during decisions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-01 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-10-31-counterfactual-advice-probe` |
| Channel | cm |
| Video | [Anthropic's New Study: You're Not Controlling AI as Much as You Think You Are](https://www.youtube.com/watch?v=BlbxhsItZPg) |
| Published | 2026-10-31 |
| Ingested upstream | 2026-11-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
