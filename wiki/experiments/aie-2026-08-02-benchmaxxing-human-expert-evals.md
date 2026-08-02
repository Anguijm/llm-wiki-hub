# Replace LLM-as-judge evals with blind human expert comparisons for subjective output quality

> Back to [[experiments-index]]

Source: **[When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI](https://www.youtube.com/watch?v=-npY6XjM8CQ)** · aie · 2026-08-02

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace automated LLM-as-judge scoring for subjective tasks (writing quality, domain reasoning) with blind side-by-side comparisons by domain-expert humans, then our model evaluations will better reflect real-world usefulness because LLMs cannot reliably evaluate outputs that require taste, judgment, or domain expertise beyond the training frontier.

## What they did

Nick Heiner (Surge AI) diagnosed why benchmarks fail: cost pressures lead to AI-assisted task creation (can't push frontier from within frontier), contamination is the default outcome for public benchmarks (showed Claude Opus memorizing SWEBench verified verbatim), reward hacking exploits lazy verifier design, and benchmark saturation often means 20% of tasks are broken rather than the model being truly capable. He presented Hemingway Bench as a counter-example: thousands of professional writers (poets, journalists, technical writers, editors) doing blind model comparisons to produce a writing quality leaderboard. He argued that good benchmarks require domain expert humans to define tasks, success criteria, input data, and verifiers — with full two-way alignment between prompts and verifiers — plus a private holdout set to prevent contamination.

## Relevance to YOLO loop

YOLO loop evals currently rely on automated checks. For tasks involving prose, architecture decisions, or nuanced code review, substituting even a small panel of expert blind comparisons would surface quality gaps that LLM-as-judge systematically misses.

## Notes

Key antipatterns to avoid: using AI to generate eval tasks, public Q&A that gets memorized, broad verifiers misaligned with prompts, no private holdout. Hemingway Bench is the reference implementation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-02-benchmaxxing-human-expert-evals` |
| Channel | aie |
| Video | [When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI](https://www.youtube.com/watch?v=-npY6XjM8CQ) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
