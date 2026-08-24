# Run the same vague prompt through Deepseek Harness and Claude Code to benchmark output quality and confidence calibration

> Back to [[experiments-index]]

Source: **[100 Hours Testing Deepseek Harness vs. Claude Code. What You Need to Know.](https://www.youtube.com/watch?v=UsfCe5fJK6A)** · nh · 2026-08-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we send identical vague prompts to both Deepseek Harness (with the same underlying model via OpenRouter) and Claude Code and compare outputs on depth, source count, and confidence calibration, then we will find meaningful differences in deliverable trustworthiness because the agentic harness—not just the model—shapes how information is structured, how conservatively claims are stated, and how well skills transfer across environments.

## What they did

Herk spent roughly 100 hours testing Deepseek Harness out of the box against Claude Code using identical vague prompts. He ran two head-to-head comparisons: a YouTube analytics Excel report and a STORM-skill research report on sugar's effects on the body. Findings: Claude Code produced more words, more sources (26 vs 14 load-bearing), more scientific depth, and more conservative fact claims; Deepseek Harness was faster, more readable, color-coded, but occasionally overconfident on claims he doubted. He concluded he would trust Claude Code deliverables more for client work, and noted that skills built for Claude Code are interpreted differently in Deepseek Harness, so harness-specific skill tuning would likely close the gap.

## Relevance to YOLO loop

Informs model-and-harness selection decisions in the YOLO loop; if the loop uses skills or structured prompts, this experiment framework (same prompt, two harnesses, measure depth/source count/confidence) can be run against any new agentic runtime we consider adopting.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-24-deepseek-harness-vs-claude-code` |
| Channel | nh |
| Video | [100 Hours Testing Deepseek Harness vs. Claude Code. What You Need to Know.](https://www.youtube.com/watch?v=UsfCe5fJK6A) |
| Published | 2026-08-24 |
| Ingested upstream | 2026-08-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
