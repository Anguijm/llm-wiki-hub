# Inject Inspiration URLs and a Layering Skill Prompt into Astra for One-Shot Premium Web UI Generation

> Back to [[experiments-index]]

Source: **[GPT-6 Astra FINALLY Kills AI Website Slop](https://www.youtube.com/watch?v=QhmhUgccaS0)** · nh · 2026-09-05

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we provide Astra with a domain-specific design skill prompt (encoding layering, parallax, typography rules) plus concrete inspiration URLs from sites like godly.design or 21st.dev, then one-shot website outputs will avoid generic AI slop because the model has both aesthetic constraints and concrete reference patterns to ground its generation.

## What they did

The creator used a custom 'ScrollCraft' skill (a prompt/instruction set shared via a free community) that encodes knowledge of parallax layering, typography, spacing, and depth. He fed Astra brand guidelines, copy, the skill, and URLs of inspirational websites or UI components. He ran one-shot prompts across multiple business types (agency, physical product, consulting, luxury goods) and iterated with natural language corrections. He also noted that matching the design style to the target audience persona (the 'three P's': pain, person, promise) was as important as the technical skill.

## Relevance to YOLO loop

Relevant to any UI generation step in the dev loop: packaging aesthetic constraints as a reusable skill file and pairing it with curated inspiration URLs is a repeatable pattern for getting high-quality first-pass outputs from Astra or Codex on frontend tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-05-astra-browser-website-scrollcraft` |
| Channel | nh |
| Video | [GPT-6 Astra FINALLY Kills AI Website Slop](https://www.youtube.com/watch?v=QhmhUgccaS0) |
| Published | 2026-09-05 |
| Ingested upstream | 2026-09-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
