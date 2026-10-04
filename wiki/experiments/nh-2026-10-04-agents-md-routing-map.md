# Build a Routing-Map agents.md to Eliminate Per-Session Context Re-Explanation

> Back to [[experiments-index]]

Source: **[Every Codex Concept Explained for Non-Coders](https://www.youtube.com/watch?v=DFlELTiSPk8)** · nh · 2026-10-04

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we create a detailed agents.md with a routing map that directs the agent to the correct file/folder for each knowledge domain, then we will eliminate the need to re-familiarize the agent at the start of each session, because the agent reads agents.md before every message and can self-navigate a large project without explicit prompting.

## What they did

The speaker maintains a Herk 2 project with an agents.md that contains: (1) role definition, (2) operating rules, (3) a routing map specifying which subfolder holds business info, credentials, voice style, course content, and active projects. Codex reads this file before every message. He demonstrated asking for a month recap without any context-setting and received an accurate structured summary across hundreds of project files.

## Relevance to YOLO loop

Directly improves the YOLO loop's initialization cost: a well-structured agents.md acts as persistent system context, making every new agent invocation start from a fully-briefed state rather than a blank slate.

## Notes

Speaker emphasizes agents.md is a living document that should evolve as the agent makes mistakes — pair with a review cadence, not a one-time setup.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-04-agents-md-routing-map` |
| Channel | nh |
| Video | [Every Codex Concept Explained for Non-Coders](https://www.youtube.com/watch?v=DFlELTiSPk8) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
