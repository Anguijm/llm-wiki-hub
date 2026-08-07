# Build a Custom Voice Discovery Prompt to Prevent AI Slop Output

> Back to [[experiments-index]]

Source: **[AI Slop Is Costing You Hours. Here's How To Stop Sending It.](https://www.youtube.com/watch?v=AWGoOtNgw3c)** · nb · 2026-08-07

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a custom 'voice discovery' skill prompt that forces the AI to surface the user's distinctive perspective before drafting any output, then generated content will carry a recognizable authorial voice instead of generic AI slop, because the model is anchored to specific personal signals rather than statistical averages.

## What they did

Nate described creating a structured authorship skill that anyone can use with their AI to discover and encode their unique voice. The skill is designed so that each person who runs it gets a different output — a personal voice profile — which then guides subsequent AI-assisted writing. He argues that slop is produced when users skip the authorship step and ship raw model output, pushing the cognitive work downstream to readers. The antidote is a pre-writing voice extraction pass rather than a post-writing polish pass.

## Relevance to YOLO loop

Directly applicable to any step in the dev loop where the system generates user-facing text (changelogs, PR descriptions, docs, Slack summaries). Adding a voice-profile system prompt or pre-pass could reduce generic output before it reaches reviewers or stakeholders.

## Notes

Transcript truncated at ~5500 chars; the specific voice discovery skill mechanics were in the elided section. Would need to watch full video or find the skill template to implement concretely.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-07-voice-discovery-skill` |
| Channel | nb |
| Video | [AI Slop Is Costing You Hours. Here's How To Stop Sending It.](https://www.youtube.com/watch?v=AWGoOtNgw3c) |
| Published | 2026-08-07 |
| Ingested upstream | 2026-08-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
