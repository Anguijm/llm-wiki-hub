# Have domain experts author agent skills via narrated walkthroughs rather than engineering spec

> Back to [[experiments-index]]

Source: **[We Let Our Financial Planners Write the Agents — Matthew Ragone, Range](https://www.youtube.com/watch?v=gpmze-6ueGU)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we have the people who do the work write agent skills by narrating their judgment out loud through real cases (not just listing steps), then the resulting skills will encode firm-specific heuristics that generic AI knowledge lacks, because Range's financial planners produced 24 skills in 6 months—all maintained by non-engineers—that spread organically to sales, product, and marketing.

## What they did

Matt Ragone, a certified financial planner at Range, described a five-step skill-building method (Pick, Teach, Pack, Test, Ship) that requires no code. Step 1: pick a frequent, easily-judged workflow. Step 2: walk through several real past cases, narrating judgment aloud—not just steps but why. Step 3: encode as a skill with mandatory pre-start questions and hard limits (e.g., 'never send to client'). Step 4: run 5–10 times on real cases and fix edge cases. Step 5: assign an owner and a reviewer (not the author). Result: 24 skills in 6 months, 17 in planning; spread virally to other functions; all maintained by subject-matter experts.

## Relevance to YOLO loop

We write agent instructions from an engineering perspective. Inviting the actual domain users to narrate their judgment through a workflow would surface implicit heuristics our prompts miss and improve first-draft quality.

## Notes

Critical distinction: skills must include (a) questions the agent must ask before starting and (b) hard limits on what it never does autonomously. Steps alone produce a skill that runs on its own; questions + limits produce a skill you can trust.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-domain-expert-written-agent-skills` |
| Channel | aie |
| Video | [We Let Our Financial Planners Write the Agents — Matthew Ragone, Range](https://www.youtube.com/watch?v=gpmze-6ueGU) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
