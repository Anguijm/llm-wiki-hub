# Route Claude Code through OpenRouter to use free or cheap models

> Back to [[experiments-index]]

Source: **[This Stealth Model Makes Claude Code Free. Here's How.](https://www.youtube.com/watch?v=_kK_4cOYF4o)** · nh · 2026-08-22

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we set ANTHROPIC_API_KEY to an OpenRouter key and override model slots in Claude Code's settings.json env block, then we can run Claude Code sessions against free or low-cost models (e.g. Stealth OX Alpha, GLM-5.2-free) because Claude Code treats the env vars as its backend and OpenRouter proxies them to any model.

## What they did

Nate edited the env section of Claude Code's settings file to point ANTHROPIC_BASE_URL at OpenRouter and set the model name to 'stealth/ox-alpha' (a $0/token anonymous model). He ran multiple parallel Claude Code tabs all day for ~13 cents total. He noted the model is slower (~5-10x), hits infrastructure errors occasionally, but can still invoke skills, use fetch/web search, and do knowledge work. He also showed how to swap in other free models like GLM-5.2-free by copying the model slug from OpenRouter.

## Relevance to YOLO loop

Useful for burst dev work when Anthropic credits are exhausted: swap the settings file to a free OpenRouter model to keep the loop running for lightweight tasks like scaffolding, research, or skill invocation, then switch back to Claude for quality-critical work.

## Notes

Only works in VS Code / terminal Claude Code, not the desktop app (desktop overrides env). Anonymous model origin unknown — avoid sending sensitive data. All model slots (default, sonnet, opus sub-agents) must be updated together so sub-agents don't fall back to paid Claude.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-22-free-models-claude-code` |
| Channel | nh |
| Video | [This Stealth Model Makes Claude Code Free. Here's How.](https://www.youtube.com/watch?v=_kK_4cOYF4o) |
| Published | 2026-08-22 |
| Ingested upstream | 2026-08-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
