# Implement a ROW (Research → Outline → Write) skill file with mandatory verification step in Claude Code

> Back to [[experiments-index]]

Source: **[How Claude is Creating a New Generation of Millionaires](https://www.youtube.com/watch?v=pbrln2TVeh4)** · nh · 2026-07-03

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we define a structured skill file that forces Claude Code to (1) research and score an idea against real evidence before building, (2) produce a go/reshape/kill verdict, and (3) verify completion by running the output on a real example, then build quality will improve and wasted iteration cycles will decrease because the agent cannot proceed past each gate without evidence.

## What they did

The speaker described a multi-step Claude Code workflow: first a ROW skill (a file dropped into Claude that runs a research-outline-write pipeline automatically), then an idea validation console that scores each idea point against real data and returns a go/reshape/kill verdict before any build begins. After building, the agent is required to prove completion by running the output on a real example rather than self-reporting done. He noted that first outputs come back 60-70% right and that treating misses as feedback data (tell it what was wrong in plain English, let it fix its own work) compounds improvement because Claude remembers corrections across sessions.

## Relevance to YOLO loop

The go/reshape/kill validation gate before build and the mandatory verification-by-execution after build are directly applicable to our YOLO loop's task acceptance and completion criteria. The skill-file pattern (a portable prompt file that auto-runs a pipeline) is a low-effort way to standardize recurring agent workflows.

## Notes

Speaker offers the ROW skill file free in his School community. The verification pattern — 'make it prove it's done by running a real example' — is undersold in most agent demos and worth making a hard requirement in our loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-03-claude-code-row-skill-verification` |
| Channel | nh |
| Video | [How Claude is Creating a New Generation of Millionaires](https://www.youtube.com/watch?v=pbrln2TVeh4) |
| Published | 2026-07-03 |
| Ingested upstream | 2026-07-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
