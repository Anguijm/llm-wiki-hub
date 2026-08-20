# Build a deterministic agent workflow with a single CLI tool to automate repetitive research outreach at scale

> Back to [[experiments-index]]

Source: **[How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face](https://www.youtube.com/watch?v=FLUoowDJg4I)** · aie · 2026-08-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement a deterministic workflow agent (rather than a fully autonomous loop) with a single well-defined tool (e.g., Hugging Face CLI) and a structured decision tree, then we can safely scale a repetitive human task to hundreds of daily items with predictable quality and minimal slop risk.

## What they did

Niels Rogge (ML engineer, Hugging Face, 5 years) automated the community science team's workflow of opening GitHub issues and PRs to encourage researchers to upload model weights/datasets to Hugging Face. Manual workflow: find GitHub URL for arxiv paper → read README → check if artifacts are on HF → if not, open GitHub issue; if yes but incomplete, open PR with model card. Built a deterministic agent workflow (not fully autonomous loop) using only the Hugging Face CLI as the single tool, plus a sandbox. The agent completes a structured model card template based on paper content. Evaluation approach: followed Hamel Husain's LLM Evals FAQ to avoid slop. Side project: @DailyPapers Twitter account using same workflow, 90K followers, posts every 4 hours automatically. Open models (GLM 5.2, DeepSeek V4) now match closed models for this use case.

## Relevance to YOLO loop

Pattern to apply: when automating a repetitive task, start with a deterministic workflow (not an autonomous agent), minimize the tool surface to a single CLI, use a template-completion approach rather than free-form generation, and build in evaluation before scaling. The single-tool + sandbox pattern maps cleanly to our agent architecture.

## Notes

Key design choices: (1) deterministic workflow over autonomous loop for predictability; (2) single tool (HF CLI) reduces attack surface and failure modes; (3) template completion rather than free-form reduces slop; (4) evaluation discipline before scaling (reference: Hamel Husain LLM Evals FAQ). The agent included its own name in model cards without being prompted — shows emergent helpful behavior when context is rich. Papers With Code revival at paperswithcode.co is another side project from the same workflow pattern.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-20-huggingface-research-outreach-agent` |
| Channel | aie |
| Video | [How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face](https://www.youtube.com/watch?v=FLUoowDJg4I) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
