# Automate MCP Server Install and First-Run Testing via Astra Computer Use

> Back to [[experiments-index]]

Source: **[GPT-6 Astra's Computer Use Is Ridiculously Good](https://www.youtube.com/watch?v=tU-fO6cADvQ)** · mk · 2026-09-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Astra's computer use to install an MCP server into Claude Code and then operate Claude Code as an end user would, then we can simulate realistic first-run testing without manual QA because Astra can observe the full UI interaction path that a new user would experience.

## What they did

The creator had Codex use computer use to install an MCP server into Claude Code, then open Claude Code and interact with it as a naive user would—checking setup friction, timing how long it takes, and validating that the MCP tools behaved correctly. This was framed as a solution to the hard problem of simulating external user onboarding for MCPs you build.

## Relevance to YOLO loop

Maps directly to the testing/validation phase of the dev loop: using computer use as a synthetic QA agent to dog-food MCP servers or internal tools before shipping, catching setup and UX issues that unit tests miss.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-09-05-computer-use-mcp-install-test` |
| Channel | mk |
| Video | [GPT-6 Astra's Computer Use Is Ridiculously Good](https://www.youtube.com/watch?v=tU-fO6cADvQ) |
| Published | 2026-09-05 |
| Ingested upstream | 2026-09-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
