# Prompt Coding Agents to Write Tests First (TDD-Style) Before Implementation

> Back to [[experiments-index]]

Source: **[How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](https://www.youtube.com/watch?v=5Bn0xro2ol8)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we instruct coding agents to follow a red-green TDD cycle (write failing test → implement to pass) rather than writing code and tests afterward, then the agent will produce fewer bugs and better-structured implementations, because the agent is given a concrete verifiable goal to strive toward rather than retrofitting tests to match already-written code.

## What they did

Alon Blum from Figma described their internal AI adoption journey and friction points. On the verification side, he recommended: (1) 'left-shifting' verification from humans to agents wherever possible (e.g., using Playwright + MCP so agents can explore the UI themselves), (2) encoding discovered agent-useful patterns into deterministic flows to save tokens and ensure repeatability, and (3) explicitly prompting agents to follow TDD red-green cycles — write the test first, then make it pass. He noted this consistently yields better results than writing code first and fitting tests afterward. He also described marking PR descriptions with human-written summaries at the top and AI-generated content below to calibrate reviewer attention.

## Relevance to YOLO loop

Directly applicable to any agent-driven coding task in the YOLO loop: changing the prompt structure to enforce test-first ordering is a zero-infrastructure change that could immediately reduce the rate of agent-generated code that passes tests trivially by making tests match bad code.

## Notes

Secondary finding worth tracking: Figma observed their best senior engineers became bottlenecks and slowest adopters because they could see all the failure modes. Consider explicitly offloading their institutional knowledge into written specs/CLAUDE.md so agents can access it without burdening those engineers.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-figma-tdd-agent-verification` |
| Channel | aie |
| Video | [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](https://www.youtube.com/watch?v=5Bn0xro2ol8) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
