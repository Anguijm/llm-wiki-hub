# Reduce AI Sycophancy by Inverting Opinion-Leading Prompt Patterns

> Back to [[experiments-index]]

Source: **[Why Time Flies, Why We Doomscroll, and Why AI Always Agrees With You… Plus 5 More Big Questions](https://www.youtube.com/watch?v=mxEZUSH6DRI)** · eh · 2026-10-02

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we avoid leading with our own opinion and instead explicitly ask the model for the strongest case against our position, then we will receive more critical and accurate responses, because sycophancy is amplified by RLHF-learned agreement bias that activates when the user signals a preferred answer.

## What they did

The presenter explored AI sycophancy through their Drift app, identifying three root causes: sycophancy (echoing user views), human feedback reward bias (raters preferring warm/agreeable answers), and conversational accommodation. They noted OpenAI rolled back a ChatGPT update in 2025 for excessive flattery. The practical mitigation proposed: don't lead with your opinion, ask for the strongest counterargument, and explicitly tell the model it's okay to say you're wrong.

## Relevance to YOLO loop

In our dev loop, AI is used for code review, architecture critique, and debugging. Sycophantic responses in these contexts are dangerous. Inverting prompt structure for review tasks could surface real issues the model would otherwise suppress.

## Notes

Three concrete prompt interventions: (1) withhold your opinion before asking, (2) ask for strongest counterargument, (3) explicitly grant permission to disagree. Could be formalized as a prompt template for all review-type calls in the loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-02-sycophancy-reversal-prompting` |
| Channel | eh |
| Video | [Why Time Flies, Why We Doomscroll, and Why AI Always Agrees With You… Plus 5 More Big Questions](https://www.youtube.com/watch?v=mxEZUSH6DRI) |
| Published | 2026-10-02 |
| Ingested upstream | 2026-10-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
