# Build agent skill folders with progressive disclosure to eliminate repetitive context setup

> Back to [[experiments-index]]

Source: **[How to Onboard Your AI Team with Agent Skills (AgentCon - Dallas 2026)](https://www.youtube.com/watch?v=bHqNyGq1VGw)** · st · 2026-06-28

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we package reusable task instructions as skill folders (a skill.md plus references, templates, and scripts sub-folders) that agents load on demand via short descriptions at conversation start, then agents will execute recurring tasks correctly on the first attempt without back-and-forth, because the right context is injected automatically rather than relying on the user to re-explain it every session.

## What they did

Shaw described 'agent skills' as an open standard analogous to MCP — folder-based reusable instruction sets stored locally. Each skill has a skill.md with full instructions and optional sub-folders for reference docs, asset templates, and scripts. At conversation start, the agent sees only a short description of every skill; it pulls the full skill.md only when relevant (progressive disclosure). He demonstrated reducing a 30-minute back-and-forth marketing report workflow to a single correct first-pass by pre-defining data sources (HubSpot, Google Analytics), output format (TLDR bullets), and section structure inside a skill. He also showed skills stored in Claude's project knowledge or as local files, with YAML front matter for metadata.

## Relevance to YOLO loop

Skills are a direct mechanism for encoding the YOLO loop's recurring subtasks (e.g. 'run test suite', 'generate PR description', 'summarise diff') so the agent picks them up automatically each session without prompt engineering overhead.

## Notes

Shaw recommends starting skill creation by reviewing your calendar for the last 2 weeks and targeting the highest-time-cost recurring tasks. He reports non-technical users delegating 5-10 hours/week of busy work within 90 minutes of learning the approach.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-06-28-agent-skills-reusable-instructions` |
| Channel | st |
| Video | [How to Onboard Your AI Team with Agent Skills (AgentCon - Dallas 2026)](https://www.youtube.com/watch?v=bHqNyGq1VGw) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
