# Encode Domain Expert Knowledge as a Reusable Agent Skill to Unblock Specialist Review Bottlenecks

> Back to [[experiments-index]]

Source: **[How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner](https://www.youtube.com/watch?v=I2LL_wd89-A)** · aie · 2026-10-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we encode an expert's domain knowledge (e.g., accessibility best practices, security patterns, API conventions) into a versioned agent skill that every developer can invoke, then we will eliminate the bottleneck of waiting for that expert's review and propagate their standards consistently, because the skill is maintained by the area owner and applied automatically by every agent invocation.

## What they did

The VS Code team distilled their accessibility expert's knowledge into a reusable skill. Previously, every feature needed the accessibility owner to be pulled in for review. After encoding their standards into a skill, any developer or agent can invoke it automatically. The speaker also described tracking 'code survival rate' (percent of agent-written code that gets committed) rising from 55% with GPT-4.1 to 86% with Claude Opus 4, and using this metric to measure developer trust as a leading indicator of shipping velocity.

## Relevance to YOLO loop

Directly maps to the YOLO loop's skill-library layer: packaging expert knowledge as callable skills reduces serial review dependencies and lets agents apply institutional standards without human-in-the-loop at every step.

## Notes

Track code survival rate as a proxy metric for agent trust in your own loop. Start by identifying one repeated specialist review (security, style, domain correctness) and encoding it as a skill. VS Code moved from monthly to weekly releases using this pattern.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-04-vscode-agents-md-accessibility-skill` |
| Channel | aie |
| Video | [How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner](https://www.youtube.com/watch?v=I2LL_wd89-A) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
