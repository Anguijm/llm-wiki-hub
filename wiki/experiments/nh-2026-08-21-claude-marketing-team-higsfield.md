# Build a Claude Code project with brand guidelines and reusable skill files to generate consistent marketing assets via Higsfield

> Back to [[experiments-index]]

Source: **[Turn Claude Into a One Person Marketing Team in 38 Mins](https://www.youtube.com/watch?v=yCACmFTiCto)** · nh · 2026-08-21

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we encode brand guidelines (color palette, typography, the three Ps: pain, person, promise) and reusable workflow recipes ('skills') into a Claude Code project context, then AI-generated marketing assets will be consistently on-brand and repeatable without manual re-prompting each session, because the persistent project files act as a standing system prompt that constrains every generation.

## What they did

Speaker set up a Claude Code project for a fictional brand (Perk Form) containing brand guidelines, a three-Ps positioning document, and reusable skill files defining how each asset type (Instagram carousel, UGC ad, sizzle reel, BOGO creative) should always be produced. He connected Claude Code to Higsfield (a multi-model image/video platform with GPT Image 2, Kling, Sora, Cance 2.5, etc.) and had Claude orchestrate generation requests to Higsfield. After four rounds of asset generation he prompted Claude to auto-produce a branded Excel analytics tracker logging generation type, model used, credits spent, dollar cost, and campaign angle, enabling future performance analysis of which angles and copy worked best.

## Relevance to YOLO loop

Demonstrates the pattern of encoding persistent project context plus reusable skill/recipe files to make multi-step agentic workflows repeatable and auditable. The analytics tracker pattern (auto-logging each agent run's type, model, cost, and output) is directly transferable to our YOLO loop for tracking experiment runs and model spend per task type.

## Notes

Speaker released a free six-hour Claude Code course for non-coders. The auto-generated branded Excel tracker (color scheme, tabs matching brand guidelines) is a notable emergent behavior worth reproducing in our own run-logging setup.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-21 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-21-claude-marketing-team-higsfield` |
| Channel | nh |
| Video | [Turn Claude Into a One Person Marketing Team in 38 Mins](https://www.youtube.com/watch?v=yCACmFTiCto) |
| Published | 2026-08-21 |
| Ingested upstream | 2026-08-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
