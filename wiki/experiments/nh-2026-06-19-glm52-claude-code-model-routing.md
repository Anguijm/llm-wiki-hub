# Route Claude Code to open-source models via base URL override and per-directory settings.local.json

> Back to [[experiments-index]]

Source: **[GLM 5.2 in Claude Code is Blowing My Mind](https://www.youtube.com/watch?v=2OD14-0cot4)** · nh · 2026-06-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we override Claude Code's ANTHROPIC_BASE_URL and default model env vars in a project-scoped settings.local.json to point at an alternative provider (e.g. Z.AI serving GLM 5.2), then we can run 80%+ of knowledge-work tasks 5x cheaper and often faster than Opus while preserving the full Claude Code harness, because most tasks don't require frontier-model reasoning.

## What they did

Nate ran GLM 5.2 (via Z.AI API) inside Claude Code by setting ANTHROPIC_BASE_URL to Z's endpoint and replacing all default model references with GLM 5.2 in settings.local.json. He benchmarked it against Opus 4.8 across website design (GLM: 4min/cheaper vs Opus: 15min/5x cost), a homework assignment (Opus more precise on edge cases), a video editing /goal loop (1hr 15min, 357K tokens), and creative HTML generation. He concluded GLM 5.2 handles ~80% of tasks well and costs ~5x less, while Opus wins on heavy reasoning. He managed multiple models simultaneously by placing each in a separate directory with its own settings.local.json.

## Relevance to YOLO loop

Directly actionable: the YOLO loop can implement model routing by task complexity using per-project or per-task settings.local.json overrides, cutting cost significantly for the majority of loop iterations that don't require Opus-level reasoning.

## Notes

Nate promised to paste the exact env var snippet in the video description. Key vars: ANTHROPIC_BASE_URL, ANTHROPIC_API_KEY (set to Z API key), and default model overrides all to GLM 5.2. Also mentions open-source/local model direction as future content.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-19-glm52-claude-code-model-routing` |
| Channel | nh |
| Video | [GLM 5.2 in Claude Code is Blowing My Mind](https://www.youtube.com/watch?v=2OD14-0cot4) |
| Published | 2026-06-19 |
| Ingested upstream | 2026-06-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
