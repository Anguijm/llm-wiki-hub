# Reverse-engineer a desired output into a Codex skill file using the BIKE feedback loop

> Back to [[experiments-index]]

Source: **[How to Build Codex Skills Better than 99% of People](https://www.youtube.com/watch?v=9KOtMsZ9I28)** · nh · 2026-09-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we start from a known-good output example and ask Codex to reverse-engineer the process into a skill.md file, then we get a more accurate and consistently reproducible agent skill because the agent has a concrete north-star artifact rather than an abstract specification.

## What they did

Nate described a six-step process for building Codex skills: (1) reverse-engineer from a real output example, (2) scope each skill to one specific job and one specific trigger, (3) set appropriate freedom/determinism level in the skill YAML front matter, (4) add a verification checklist step inside the skill, (5) walk the agent through the skill live before finalizing, and (6) apply the BIKE method — giving explicit good and bad feedback after each run and instructing the agent to update the skill file in place. He demonstrated with a YouTube-video-to-X-article skill, showing how invoking it by natural language automatically selects the right skill, and how post-run feedback propagates into the skill file to prevent repeated mistakes.

## Relevance to YOLO loop

Core methodology for codifying any repeatable YOLO loop task into a reusable agent skill — particularly the BIKE feedback loop maps directly to iterative loop improvement and the reverse-engineering step reduces spec ambiguity.

## Notes

Skill files are markdown (.md) with YAML front matter. Trigger can be natural language or a slash command. Freedom level in YAML controls how strictly the agent follows the recipe vs. improvising.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-19-codex-skill-reverse-engineering` |
| Channel | nh |
| Video | [How to Build Codex Skills Better than 99% of People](https://www.youtube.com/watch?v=9KOtMsZ9I28) |
| Published | 2026-09-19 |
| Ingested upstream | 2026-09-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
