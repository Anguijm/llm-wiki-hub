# Run Identical Multi-Phase Build Prompts on Two Coding Agents and Compare Output Quality vs Cost

> Back to [[experiments-index]]

Source: **[I Made Codex and Claude Code Build the Same App. One Clearly Won.](https://www.youtube.com/watch?v=WCrnS09vpfo)** · nh · 2026-08-14

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we give Claude Code and Codex the exact same multi-phase /goal prompt (research → build → verify), then measurable differences in output quality, cost, and wall-clock time will surface because the two agent harnesses handle orchestration, testing depth, and token efficiency differently.

## What they did

The speaker issued an identical /goal prompt to both Claude Code and Codex asking them to build a production-ready Typeform alternative, instructing each to orchestrate specialized agents across three phases (research, build, verify) and not stop until the app was genuinely complete. Claude Code finished in ~5 hours, spent ~$447, used 35 sub-agents, and scored 9.8/10 on efficiency. Codex ran for 2.5 days, spent ~$800+, used far more sub-agents, scored 5.5/10 on efficiency but scored higher on testing breadth (cross-browser, property tests, fault injection). Claude Code won on speed and cost (~11x faster, ~6.6x cheaper); Codex won on testing coverage.

## Relevance to YOLO loop

Directly informs which coding agent to slot into the YOLO loop's build phase. The finding that Claude Code is dramatically cheaper and faster while Codex adds more exhaustive test coverage suggests a hybrid: use Claude Code for the primary build loop and optionally invoke a Codex adversarial-review pass for critical paths.

## Notes

Speaker notes the prompt lacked a planning phase between research and build — adding that phase is the recommended improvement for a follow-up run. Also mentions a Codex plugin for Claude Code that runs adversarial review and catches bugs/edge cases missed by the primary loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-14-codex-vs-claude-code-head-to-head` |
| Channel | nh |
| Video | [I Made Codex and Claude Code Build the Same App. One Clearly Won.](https://www.youtube.com/watch?v=WCrnS09vpfo) |
| Published | 2026-08-14 |
| Ingested upstream | 2026-08-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
