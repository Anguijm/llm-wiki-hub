# Run an independent CLI model as PR reviewer

> Back to [[experiments-index]]

Source: **[Anthropic Just Revealed How Their Engineers Use Claude Code](https://www.youtube.com/watch?v=92ZDgn8bgLM)** · ail · 2026-10-21

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we spawn a separate CLI model (Codex CLI or a non-interactive Claude Code session) to review PRs instead of letting the authoring model review its own code, then we will catch more defects because the reviewer does not share the generator's blind spots.

## What they did

The video, reviewing Felix Rieseberg's framework, describes spawning Codex CLI or background non-interactive Claude Code sessions from the terminal to act as independent review judges on pull requests. It also describes sequential specialized sub-agents (for example recruiter or security auditor lenses) critiquing and modifying code, and a meta-prompt that rewrites requests into expert specs with named methodologies, tools and falsifiable proof criteria. The speaker cautions that models should never review their own code. These were described, not demonstrated.

## Relevance to YOLO loop

high: Independent review judges and multi-lens sub-agents are directly applicable verification-loop and council patterns for Claude Code.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-21 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-10-21-independent-cli-reviewer-and-altitude-prompts` |
| Channel | ail |
| Video | [Anthropic Just Revealed How Their Engineers Use Claude Code](https://www.youtube.com/watch?v=92ZDgn8bgLM) |
| Published | 2026-10-21 |
| Ingested upstream | 2026-10-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
