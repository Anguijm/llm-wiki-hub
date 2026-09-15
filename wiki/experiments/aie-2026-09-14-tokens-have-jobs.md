# Test Advise/Grade/Dream Token Strategies Against a Pure Execution Baseline on Fixed Budget

> Back to [[experiments-index]]

Source: **[Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic](https://www.youtube.com/watch?v=PXj0p_mW9nI)** · aie · 2026-09-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we allocate tokens across specialized roles (executor + adviser, executor + grader, executor + dreamer) rather than spending all tokens on a single executing agent, then we can achieve higher task accuracy within the same token budget, because tokens doing different jobs (advising, grading, reflecting) provide error correction and learning signals that brute-force execution cannot.

## What they did

Katelyn Lesse and Angela Jiang from Anthropic presented experiments on a financial analysis benchmark designed to replicate expert human analyst performance. They tested four strategies: (1) Execute only — baseline, one-shot, 39k tokens, 15% accuracy; (2) Advise — executor calls out to an adviser agent for guidance on next steps; (3) Grade — a grader agent evaluates executor output against a rubric and triggers re-tries until the rubric is met; (4) Dream — a dreamer agent inspects executor transcripts, extracts learnings, and writes them to memory for the next run. Dream achieved the highest accuracy but used 600k tokens one-shot. On a fixed token budget, Advise and Grade proved most token-efficient relative to output quality. The conclusion: tokens are not fungible; strategy selection should depend on whether you're optimizing for token efficiency (use Advise) or answer reliability (use Grade or Dream). Claude Managed Agents provides these primitives out of the box, and the strategies compose — e.g., Execute + Advise + Grade + Dream can be chained.

## Relevance to YOLO loop

Our YOLO loop currently uses single-agent execution. Adding a grader agent that evaluates outputs against a rubric before passing results downstream is the lowest-effort first experiment — it would directly improve output reliability on tasks where we have clear success criteria, without requiring persistent memory infrastructure.

## Notes

Anthropic Claude Managed Agents provides Advise, Grade, and Dream primitives. The meta-harness coordination layer sits above individual agent harnesses. Key insight: Dream is most accurate but least token-efficient; Grade is the sweet spot for reliability within budget. Strategy selection is domain-dependent.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-14-tokens-have-jobs` |
| Channel | aie |
| Video | [Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic](https://www.youtube.com/watch?v=PXj0p_mW9nI) |
| Published | 2026-09-14 |
| Ingested upstream | 2026-09-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
