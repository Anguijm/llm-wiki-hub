# Use MCP to connect build agents to professional tools

> Back to [[experiments-index]]

Source: **[A Markdown File Just Replaced Your Most Expensive Design Meeting (Google Stitch)](https://www.youtube.com/watch?v=CDClFY-R0dI)** · @NateBJones · 2026-03-28

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we connect the builder agent to external tools via MCP (e.g., image generation, 3D rendering, browser testing), then project ambition increases because the agent can leverage capabilities beyond just writing code.

## What they did

Nate described MCP as 'USB for AI' — a universal connector letting AI agents interact with Blender, Remotion, and other professional tools. This removes the need for manual tool operation.

## Actionable steps

- Identify 2-3 MCP servers that would benefit the YOLO loop (e.g., browser automation, image gen, Figma)
- Install and configure them in the Claude environment
- Build one project that leverages an MCP tool the agent couldn't use before

## Success metric

One project successfully built using an MCP-connected external tool.

## Relevance to YOLO loop

The YOLO builder currently only writes code. MCP integration would expand what it can build (e.g., generate assets, test in real browsers).

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

MCP is already the backbone of the YOLO loop: gemini-analyze-code for code review, gemini-brainstorm for idea evaluation, gemini-youtube-summary for Phase 4 ingestion. The experiment is already fully adopted. Future expansion: add browser testing MCP, image generation MCP for asset creation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `done` | Already in use — Gemini MCP used throughout Phase 2/4 |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-28-mcp-tool-integration` |
| Channel | @NateBJones |
| Video | [A Markdown File Just Replaced Your Most Expensive Design Meeting (Google Stitch)](https://www.youtube.com/watch?v=CDClFY-R0dI) |
| Published | 2026-03-28 |
| Ingested upstream | 2026-03-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
