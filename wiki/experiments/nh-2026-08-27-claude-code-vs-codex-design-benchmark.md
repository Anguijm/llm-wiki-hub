# Run identical prompts through Claude Code and Codex and compare output tokens, cost, and quality

> Back to [[experiments-index]]

Source: **[I Tested Claude Code vs. Codex on Design. It Wasn't Even Close.](https://www.youtube.com/watch?v=bg0C-2iUUqM)** · nh · 2026-08-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run the same web-build prompts through both Claude Code (Opus 5) and Codex (GPT-4.1), then Codex will produce comparable quality output at significantly lower token cost and wall-clock time, because the speaker's 8-site benchmark showed Codex used ~550K vs ~3M output tokens and cost ~$100 vs ~$444 for equivalent results when prompts were sufficiently specific.

## What they did

Speaker built 8 identical websites using Claude Code and Codex with the same brand guidelines, logos, copy, and prompts. He measured sub-agents used, time taken, output tokens, and cost per build. Aggregate results: Claude Code used 25 sub-agents / 14 hours / ~3M output tokens / ~$444; Codex used 9 sub-agents / 5 hours / ~550K output tokens / ~$100. He also found that highly specific prompts produced nearly identical outputs from both tools, proving prompt specificity dominates model choice for deterministic tasks.

## Relevance to YOLO loop

Directly applicable to our build loop. We should run our standard scaffold generation task through both harnesses and compare cost-per-task. The finding that identical specific prompts yield identical outputs suggests we can switch to Codex for routine generation tasks and reserve Claude Code for exploratory/agentic work.

## Notes

Key insight: with highly specific prompts, outputs are nearly identical but Codex is ~4x cheaper and ~3x faster. Prompt specificity is the equalizer.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-27-claude-code-vs-codex-design-benchmark` |
| Channel | nh |
| Video | [I Tested Claude Code vs. Codex on Design. It Wasn't Even Close.](https://www.youtube.com/watch?v=bg0C-2iUUqM) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
