# Trial a home repo that lets one agent session reach all repos

> Back to [[experiments-index]]

Source: **[The Home Repo Pattern: Run agents across ALL your repos](https://www.youtube.com/watch?v=hWe-j78vNpc)** · mp · 2026-11-12

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we create a single home git repo with an agents.md listing relative paths and Git URLs for every project repo, and run the always-on Claude Code sessions from it, then cross-repo tasks will need less setup and skills will stop drifting out of sync, because one session can clone missing repos and spin up worktrees on demand.

## What they did

Matt Pocock keeps a central home repo holding private skills, settings.json, custom CLI tools and an LLM wiki. Its agents.md lists the path and Git URL of each managed codebase. Agents run only from this repo, clone missing repos, mount Git worktrees, and open PRs across several repos in one session. Flat path lists work up to roughly 20-40 repos, and hierarchical grouping (frontend, backend, internal) takes over beyond that. He warns that worktrees need periodic cleanup.

## Relevance to YOLO loop

medium: Centralising skills and steering files in one repo is an organisation pattern, not a new verification or loop technique.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-12 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mp-2026-11-12-home-repo-pattern` |
| Channel | mp |
| Video | [The Home Repo Pattern: Run agents across ALL your repos](https://www.youtube.com/watch?v=hWe-j78vNpc) |
| Published | 2026-11-12 |
| Ingested upstream | 2026-11-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
