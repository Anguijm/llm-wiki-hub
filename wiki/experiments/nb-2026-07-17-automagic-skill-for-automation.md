# Package an 'Auto-Magic' Problem-Discovery Prompt as a Reusable Skill File

> Back to [[experiments-index]]

Source: **[Codex vs Fable: Which AI Agent Picked the Better Problem?](https://www.youtube.com/watch?v=uCWKXIyvM_8)** · nb · 2026-07-17

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we encode the problem-discovery-and-automation workflow as a portable, parameterized skill file rather than a one-off prompt, then we can consistently replicate the outcome across different projects, team members, and AI backends (Codex, Claude, etc.) because skill files externalize the reasoning constraints and anti-patterns (e.g., 'do not think small') in a shareable, evolvable format.

## What they did

After running the Codex vs. Fable comparison, Nate extracted the prompting pattern into a reusable skill file. The skill instructs the agent to: audit the user's unique context (files, comms), root-cause the most pressing problem, pick strategically rather than defaulting to the most obvious voiced issue, and then build a complete automation solution including security and authentication considerations. The skill is scoped by an optional focus parameter (specific project, business area, or personal domain). Data never leaves the user's AI instance. Nate positions this as an 'automagic button' that produces a bespoke automation tuned to the caller's situation without Nate seeing any of the data.

## Relevance to YOLO loop

A skill file is a first-class artifact in the YOLO loop's skill library. This specific skill bootstraps the loop by generating the first automation target autonomously—it's the meta-skill that populates the backlog.

## Notes

Skill file should include: (1) instruction to think big / not self-bound, (2) requirement to build completely not partially, (3) security/auth checklist, (4) optional scope parameter. Compatible with both Codex and Claude backends per Nate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-17-automagic-skill-for-automation` |
| Channel | nb |
| Video | [Codex vs Fable: Which AI Agent Picked the Better Problem?](https://www.youtube.com/watch?v=uCWKXIyvM_8) |
| Published | 2026-07-17 |
| Ingested upstream | 2026-07-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
