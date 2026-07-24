# Add Kimi K3 as a routed model for frontend and legal tasks

> Back to [[experiments-index]]

Source: **[Build Anything with Kimi K3, Here's How](https://www.youtube.com/watch?v=ZW7R3qNw4nk)** · do · 2026-07-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route frontend code generation and legal document review tasks to Kimi K3 instead of Claude/GPT defaults, then we get higher task-level performance at lower cost because Kimi K3 leads the Frontend Code Arena benchmark and scores 26.7% vs Fable's 14.2% on Harvey's legal benchmark.

## What they did

Benchmarked Kimi K3 (2.8T parameter open-source model from Moonshot AI) head-to-head against Claude Fable 5 and GPT 5.6 Soul across multiple evals. Found Kimi K3 beats all closed-source models on Frontend Code Arena, is 3x cheaper than Fable while matching it on many benchmarks, and nearly doubles Fable's score on Harvey's legal benchmark (26.7% vs 14.2%). Demonstrated live: ran Kimi K3 inside Claude Code and Codex via API substitution, had it analyze an Apple vs OpenAI lawsuit PDF page-by-page and render a probability estimate. Referenced Fireworks AI research showing per-task model routing over 1,000+ agentic tasks always outperforms single-model approaches.

## Relevance to YOLO loop

The YOLO loop can support multiple model backends. Adding a routing layer that sends frontend scaffold tasks and contract/legal review tasks to Kimi K3 via its API could reduce cost and improve output quality on those specific task types without changing the overall harness architecture.

## Notes

Video is sponsored by Kimmy API; benchmark claims should be independently verified. Open-source weights expected ~July 27 per transcript, which would enable self-hosted inference. Key routing signal: frontend + legal = Kimi K3; planning/ideation = Fable; verification-heavy loops = GPT 5.6 Soul.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-24-kimi-k3-task-routing` |
| Channel | do |
| Video | [Build Anything with Kimi K3, Here's How](https://www.youtube.com/watch?v=ZW7R3qNw4nk) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
