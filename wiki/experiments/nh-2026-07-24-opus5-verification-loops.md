# Replace Fable 5 with Opus 5 as default agentic loop model and measure cost-quality tradeoff

> Back to [[experiments-index]]

Source: **[Claude Opus 5 is Going to Save You Money](https://www.youtube.com/watch?v=k7VI66CkKEY)** · nh · 2026-07-24

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we switch the default model in our agentic skills from Fable 5 to Claude Opus 5, then we maintain or improve output quality at lower cost because Opus 5 matches or beats Fable 5 on agentic terminal coding, business workflows, and multidisciplinary reasoning benchmarks while being priced the same as Opus 4.8 (half the cost of Fable).

## What they did

Reviewed Anthropic's release benchmarks for Claude Opus 5: 43% on Agentic Terminal Coding vs Fable 5's 33% and Opus 4.8's 21%; novel problem solving jumped from 1.5% (Opus 4.8) to 30% (Opus 5); Opus 5 beats Fable on agentic computer use, agentic business workflows, and multidisciplinary reasoning—all at Opus 4.8 pricing. Highlighted that Opus 5 specifically improved verification behavior (iterating carefully until success), which powers agentic loops. Noted Fable 5 is a 'wise planner' while GPT 5.6 Soul is a 'verification Rottweiler,' and Opus 5 appears to have adopted the verification strength.

## Relevance to YOLO loop

Directly applicable: swap model ID in Claude Code / skill configs from claude-fable to claude-opus-5, run the same benchmark suite of skills, and measure pass rate + credit consumption. Verification improvement is especially relevant to our iterative agentic loops where self-correction determines final output quality.

## Notes

Short reactive video; speaker commits to running full comparison experiments and publishing follow-up. Low effort to run ourselves: just update model config and rerun existing skill test suite. Key metric to watch: does Deep Suite score hold up as a leading indicator as mentioned in transcript.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-24-opus5-verification-loops` |
| Channel | nh |
| Video | [Claude Opus 5 is Going to Save You Money](https://www.youtube.com/watch?v=k7VI66CkKEY) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
