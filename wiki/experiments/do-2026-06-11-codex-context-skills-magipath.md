# Inject structured design context and skills into Codex to improve frontend output quality

> Back to [[experiments-index]]

Source: **[Watch this 100x developer use Codex… it's insane](https://www.youtube.com/watch?v=mMuuLocDkog)** · do · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we provide Codex with a design.md context file and install domain-specific skills (e.g., a designer persona skill) before starting frontend tasks, then Codex frontend output quality will match or exceed Opus/Gemini alternatives because Codex's perceived frontend weakness is primarily a context problem rather than a model capability gap.

## What they did

Petro (founder of MagicPath, ex-Anthropic) demonstrated that he has not used Claude Code in 5 months, preferring Codex for its better agentic loop and lower token consumption per task. He showed that Codex frontend output looked better when MagicPath provided designer-persona context to the model. He argued Codex's frontend weakness is contextual, not intrinsic. He uses a design.md file and skills system to give Codex persistent context. His workflow: open Codex, attach files (design.md, skills), create a new chat thread, select model, run task. He also stressed that building with skills installed allows any coding agent (Cursor, Codex, Claude Code) to interact with external tools like MagicPath via a shared protocol.

## Relevance to YOLO loop

Tests whether our Codex sessions can match Claude Code for frontend work by improving context injection. Experiment: run identical frontend tasks in Codex with and without a design-persona skill and measure output quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-11-codex-context-skills-magipath` |
| Channel | do |
| Video | [Watch this 100x developer use Codex… it's insane](https://www.youtube.com/watch?v=mMuuLocDkog) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
