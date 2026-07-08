# Use a file-based goal prompt with never-ask and multi-agent orchestration directives to build a full deliverable set autonomously

> Back to [[experiments-index]]

Source: **[Fable 5 Just Built Me a Business With One Prompt](https://www.youtube.com/watch?v=R0qF17BVl9w)** · nh · 2026-07-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we encode a complete mission, guardrails, phases, deliverables, and a definition-of-done in a file and instruct the model to read it as a slash-goal with a never-ask rule, then the model will autonomously orchestrate parallel agents, run internal tournaments, and adversarially verify outputs until all deliverables are complete because removing the human feedback loop forces the model to make all judgment calls itself.

## What they did

Speaker wrote a large instruction file specifying: find a real painful problem via open internet research, design a business around it, build the product, brand, website, and launch videos, prove viability, never ask questions mid-run, use multi-agent workflows aggressively including parallel researchers, tournament-style idea selection with judge panels, skeptic agents to adversarially refute claims, and a completeness critic before calling any phase done. He passed this via a 'read this file' prompt to Claude Fable 5 with API keys for HeyGen avatar and ElevenLabs voice clone. In 3-4 hours the system produced a landing page, working SaaS dashboard, two launch videos (one with screen recording and music sync), business plan, market research, brand guidelines, and logo candidates.

## Relevance to YOLO loop

Demonstrates a fully async yolo-loop where the agent runs to a definition-of-done without any human checkpoints; the file-based instruction pattern and never-ask rule are directly portable to our own long-running agent tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-08-single-goal-prompt-full-company` |
| Channel | nh |
| Video | [Fable 5 Just Built Me a Business With One Prompt](https://www.youtube.com/watch?v=R0qF17BVl9w) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
