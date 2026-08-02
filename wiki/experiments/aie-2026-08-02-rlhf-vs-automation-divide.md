# Separate your agent tasks into human-in-loop (RLHF-suited) vs. fully-automated (requires new post-training) and route accordingly

> Back to [[experiments-index]]

Source: **[What's Next After RLHF? — Diogo Almeida, TypeSafe AI](https://www.youtube.com/watch?v=cJ0EOzey--o)** · aie · 2026-08-02

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we explicitly classify each agent task as either 'goal is to please a human in the loop' (RLHF-optimized models excel) versus 'goal is to remove the human from the loop entirely' (RLHF-optimized models fail), then we will stop deploying the wrong model class to automation tasks and reduce costly failures, because RLHF intrinsically optimizes for human preference signals which are absent in headless automation contexts.

## What they did

Diogo Almeida (ex-OpenAI, co-author of GPT-4/ChatGPT/InstructGPT, now TypeSafe AI) argued that the assistance/automation divide explains the paradox of AI solving hard math while failing at basic customer service automation. His thesis: RLHF (and all current LLMs trained with it) is exceptional at tasks where the goal is to please a human in the loop (coding assistants, chat, writing) but systematically fails at tasks where the goal is to eliminate the human from the loop (background automation, decision-making with business stakes). He identified RLHF's hallucination problem as intrinsic — reward model asymmetry encourages mode-dropping and false confidence, similar to GANs. He previewed TypeSafe AI's third paradigm: post-training optimized for calibrated decision-making rather than human preference or pure correctness (RLVR), targeting the automation gap.

## Relevance to YOLO loop

The YOLO loop mixes assistance and automation tasks. This framework provides a decision rule for which tasks to trust current Claude/GPT models on and which require either human checkpoints or a different model class — directly shaping where to add guardrails in the loop.

## Notes

Almeida's heuristic: if the task's success criterion requires a human to evaluate it, RLHF models are appropriate. If success criterion is headless/automated, current RLHF models are unreliable. TypeSafe AI targeting calibrated decision-making post-training as the third paradigm after RLHF and RLVR.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-02-rlhf-vs-automation-divide` |
| Channel | aie |
| Video | [What's Next After RLHF? — Diogo Almeida, TypeSafe AI](https://www.youtube.com/watch?v=cJ0EOzey--o) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
