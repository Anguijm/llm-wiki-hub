# Run Claude Code in Headless Mode as a Scriptable YOLO Loop Step

> Back to [[experiments-index]]

Source: **[32 Claude Code Hacks in 16 Mins](https://www.youtube.com/watch?v=jqoFP9QapXI)** · NateHerk · 2026-04-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we invoke Claude Code via its headless CLI mode inside YOLO loop shell scripts, then we can chain Claude-powered steps (plan, implement, test, commit) without any interactive UI, because headless mode accepts stdin prompts and returns structured output suitable for piping into downstream loop logic.

## What they did

Speaker demonstrated Claude Code's headless/non-interactive mode where you pass a prompt via CLI flag and Claude executes the full agentic task and exits, making it scriptable and composable with other shell tools. Also showed piping terminal output back into Claude for iterative debugging.

## Relevance to YOLO loop

Core enabler for the YOLO loop's automation layer. Headless Claude Code turns a conversational tool into a programmable subprocess, which is the missing link between a human-driven loop and a fully automated one.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-27-claude-code-headless-automation` |
| Channel | NateHerk |
| Video | [32 Claude Code Hacks in 16 Mins](https://www.youtube.com/watch?v=jqoFP9QapXI) |
| Published | 2026-04-27 |
| Ingested upstream | 2026-04-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
