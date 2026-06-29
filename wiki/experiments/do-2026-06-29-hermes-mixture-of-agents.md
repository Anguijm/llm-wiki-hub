# Configure Mixture-of-Agents preset in Hermes to surpass single-model quality

> Back to [[experiments-index]]

Source: **[Hermes Agent + Mixture of Agents is insane…](https://www.youtube.com/watch?v=40ikbH0Ba-g)** · do · 2026-06-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route hard problems through a Hermes MoA preset that fans out to multiple models (e.g. GPT-5.5, Opus 4.8, DeepSeek) and aggregates with the strongest available model, then response quality on complex coding and architecture tasks will exceed any single frontier model publicly available, because diverse model perspectives cover blind spots that a single model misses.

## What they did

David set up Hermes Agent on a VPS (Hostinger), created a Mixture-of-Agents preset selecting multiple provider models via OpenRouter and direct subscriptions, let parallel reference models each answer independently, then passed all responses to a single aggregator model for a final answer. He demoed building and auto-deploying a full-stack 3D Flappy Bird game end-to-end (~20 min, ~$20 spend) without any manual deployment steps.

## Relevance to YOLO loop

Directly upgrades the inference layer of our dev loop: instead of routing hard subtasks to a single model, we can fan out to MoA for architecture decisions, security reviews, or complex debugging where quality matters more than cost/speed.

## Notes

Cost ~$20 for a full app build; not suitable for quick/cheap tasks. Prompt caching savings still apply to all reference model calls. MoA should be reserved for highest-value, hardest problems.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-29-hermes-mixture-of-agents` |
| Channel | do |
| Video | [Hermes Agent + Mixture of Agents is insane…](https://www.youtube.com/watch?v=40ikbH0Ba-g) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
