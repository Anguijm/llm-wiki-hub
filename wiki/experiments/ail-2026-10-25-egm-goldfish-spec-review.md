# Trial EGM zero-context goldfish reviewers on a feature spec

> Back to [[experiments-index]]

Source: **[EGM: Google's New Way To Use Claude Code Is Insane](https://www.youtube.com/watch?v=xxf6D9jynFw)** · ail · 2026-10-25

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we have fresh zero-context sub-agents review a Claude Code feature spec, then we catch flawed planning assumptions that a same-context reviewer would rubber-stamp, because the evaluators never see the prior conversation.

## What they did

AI LABS demonstrated Google's open-source Elephant Goldfish Model (EGM). They installed it into Claude Code (.claude/agents, .claude/EGM, .claude/skills) and ran 'egm bootstrap' to generate folder README files, with a confirmation prompt above 15 folders. They paired each README with CLAUDE.md or AGENTS.md. 'egm brainstorm' produced a concept brief, six zero-context goldfish sub-agents reviewed it, and 'egm draft' wrote the spec with critical user journeys. 'egm review' ran rounds 5 to 9, and 'egm drift report' compared code against the READMEs, catching a real bug where sold products were deleted instead of hidden. Google cautions it is overkill for small fixes.

## Relevance to YOLO loop

high: Isolated zero-context reviewers and drift checks are a verification-loop and council pattern we could adopt in the YOLO loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-26 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-10-25-egm-goldfish-spec-review` |
| Channel | ail |
| Video | [EGM: Google's New Way To Use Claude Code Is Insane](https://www.youtube.com/watch?v=xxf6D9jynFw) |
| Published | 2026-10-25 |
| Ingested upstream | 2026-10-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
