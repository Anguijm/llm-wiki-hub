# Build a personal AI signal engine using the 'Build Signal Engine' skill to generate a daily filtered digest from hundreds of sources

> Back to [[experiments-index]]

Source: **[How I Keep Up with AI Without Drowning in It (Free Skill)](https://www.youtube.com/watch?v=2i_ZyqDmtio)** · cm · 2026-10-15

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we use Cole's 'Build Signal Engine' skill to have a coding agent construct a personalized content engine — pulling from Reddit, YouTube, RSS, Hacker News, GitHub changelogs via Apify, deduplicating deterministically, then filtering with Jev/LLM against a personal interest profile — then we can replace hours of manual AI news triage with a concise daily digest covering only what we actually care about, because the skill encodes six months of refinement into a six-stage autonomous build process.

## What they did

Cole described and demonstrated his AI content engine, which he's run daily for 6+ months. The system: (1) pulls from hundreds of sources — Reddit, YouTube, RSS, Hacker News, GitHub repos, Claude Code changelogs — via Apify and direct APIs; (2) deduplicates against a central database before any LLM processing; (3) applies deterministic code filters (stale posts, low-engagement thresholds) to minimize token spend; (4) uses Jev/LLM to filter remaining items against a personal interest profile; (5) formats a concise daily digest. He published this as a free skill ('Build Signal Engine Signal Content') in his GitHub skills repo. The skill interviews the user upfront (sources, fetch methods, what they care about, pain points), then autonomously executes a six-stage build with testing after each stage, and produces a profile document for future adjustments.

## Relevance to YOLO loop

high: the signal engine is a meta-tool for staying current on agent harness developments — directly feeds the operator's ability to track Claude Code, Pi, and other harness primitives without drowning in noise.

## Notes

Skill is free and in Cole's public GitHub skills repo. Apify used for YouTube/Reddit where APIs are restricted. The profile document pattern (natural language config that agent reads when you want to change behavior) is worth adopting for other skills too.

Backlog triage 2026-10-17 round 3 (operator: "I want you to evaluate the yolo cards"). Settled maybe, cut: Assessment: the YOLO research feed and newsletter_gather.sh already do dedup and cheap filters before billed calls.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-10-15-ai-content-engine-signal-filter` |
| Channel | cm |
| Video | [How I Keep Up with AI Without Drowning in It (Free Skill)](https://www.youtube.com/watch?v=2i_ZyqDmtio) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
