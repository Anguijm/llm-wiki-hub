# Use Claude as thought-partner and Codex as executor in a two-model coding loop

> Back to [[experiments-index]]

Source: **[Build & Sell AI SaaS Products (2 HOUR COURSE)](https://www.youtube.com/watch?v=IVx8OSMbTss)** · nh · 2026-08-10

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we route planning and creative problem decomposition to Claude and route implementation and iterative execution to Codex (or similar execution-focused agent), then overall build quality and speed will improve compared to using a single model for both roles, because each model's behavioral profile (Claude: reflective/creative, Codex: persistent executor) is better matched to its assigned task type.

## What they did

Nate built a full AI SaaS product live, using Claude (with Fable persona) as a 'wise old owl' thought partner for ideation, planning, and stress-testing decisions, and Codex as a 'Rottweiler' that takes a command and executes relentlessly until completion. He also added Glido as a voice layer to remove typing as a bottleneck. The two models ran in parallel on the same project, with Nate acting as project manager adjudicating between their outputs and verifying correctness at each stage.

## Relevance to YOLO loop

The YOLO loop already uses Claude Code, but routes all tasks through a single model. Splitting the loop into a planning agent (Claude) and an execution agent (Codex/Gemini CLI) with a human-or-automated arbitration step maps directly to our current bottleneck: the same model context window gets polluted by both high-level design discussion and low-level file edits.

## Notes

Voice input via Glido is a secondary low-effort experiment worth testing independently to reduce input latency in long build sessions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-10-dual-model-coding-workflow` |
| Channel | nh |
| Video | [Build & Sell AI SaaS Products (2 HOUR COURSE)](https://www.youtube.com/watch?v=IVx8OSMbTss) |
| Published | 2026-08-10 |
| Ingested upstream | 2026-08-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
