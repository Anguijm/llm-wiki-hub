# Add Explicit Web-Search Rules to Coding Agents for Dependency Bump and Breaking-Change Detection

> Back to [[experiments-index]]

Source: **[Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa](https://www.youtube.com/watch?v=cKhpeEBnT1o)** · aie · 2026-10-03

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add explicit instructions to our coding agent's system prompt specifying when to invoke a web search tool (e.g., whenever a diff bumps a dependency version or references a recently released API), then the agent will correctly identify breaking changes and required migration steps rather than silently approving incorrect code, because the agent's knowledge cutoff makes it blind to changes made after its training date.

## What they did

Jakub Hojsan of Exa demonstrated the knowledge cutoff problem with a concrete example: a PR diff removing an 'inertia check' parameter in a scikit-learn vector store. A model without web search approved it as a 'cleanup' because it predated the breaking change in its training data. With Exa's semantic search tool, the agent retrieved a 500-character highlight from the library's changelog explaining the required migration. He emphasized that adding the tool is insufficient—agents also need explicit rules in their prompts specifying when to invoke search (e.g., 'when a diff bumps a dependency, look up upstream changelog before approving'). Exa returns token-efficient highlighted snippets rather than full pages, and provides full trace/source transparency unlike native provider web search.

## Relevance to YOLO loop

Immediately applicable to our code review and dependency management steps. Adding a rule to our agent prompts—'any time you see a version bump or a recently released package, search for breaking changes before proceeding'—is a one-line prompt change that could prevent a class of silent regressions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-03-exa-web-search-knowledge-cutoff` |
| Channel | aie |
| Video | [Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa](https://www.youtube.com/watch?v=cKhpeEBnT1o) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
