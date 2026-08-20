# Codify team-specific coding standards and tribal knowledge as structured context for automated PR review

> Back to [[experiments-index]]

Source: **[The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](https://www.youtube.com/watch?v=s-aixZYJG4c)** · aie · 2026-08-20

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we codify our team's specific standards, tribal knowledge, and historical PR decisions as structured context accessible to an AI code reviewer, then automated review quality will improve significantly over generic model-based review, because context quality (not model capability) is the primary bottleneck in AI code review accuracy.

## What they did

Itamar Friedman (CEO/co-founder, Qodo) argued that model capability is no longer the bottleneck for automated code review — context is. Generic model review produces generic comments (e.g., 'did you consider error handling?') while context-rich review can make domain-appropriate judgments. He proposed a path to eliminating human line-by-line PR review through: (1) codifying standards and tribal knowledge (not just in AGENTS.md files but in a structured, agent-queryable location); (2) building real-time self-learning context from PR history, accepted/rejected suggestions, and production incidents; (3) graduating from reviewing diffs to visualizing the full software dependency graph (PRs as nodes, with contract-breaking relationships visible across concurrent PRs); (4) auto-approve/auto-block rules that accumulate over time. He argued that if you're shipping AI-generated code faster than humans can review it, you're already behind — the infrastructure needs to be built now. Vision: 'artificial wisdom' where the AI system holds the judgment that currently lives in senior engineer heads.

## Relevance to YOLO loop

Immediately actionable at low effort: start codifying our own PR standards and decision history as structured context. Medium-term: implement an AI code reviewer that loads this context. Long-term: build toward a software graph view that shows cross-PR contract risks. The auto-approve/auto-block graduation model is a concrete roadmap for reducing human review burden incrementally.

## Notes

Two purposes of code review: (1) quality/safety/maintainability validation, (2) alignment and teaching (senior dev as gatekeeper). Both can be automated with sufficient context. Key distinction: context must be located where agents know to find it and understand its role — not just dumped into files. Tribal knowledge to codify: what causes production outages, approval/block rules, architecture constraints, team-specific patterns. Analytics on which rules are actually being triggered vs. which are stale is a useful quality signal.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-20-qodo-ai-code-review-context-codification` |
| Channel | aie |
| Video | [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](https://www.youtube.com/watch?v=s-aixZYJG4c) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
