# Adopt CLI-first workflow with GitHub issue-to-agent delegation as primary development scaling pattern

> Back to [[experiments-index]]

Source: **[From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](https://www.youtube.com/watch?v=GdvKNwMcfd0)** · aie · 2026-07-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we start development sessions from the CLI (rather than an editor) and delegate GitHub issues directly to agents via 'assign to agent' — using multiple parallel terminals for different features — then we can close far more backlog items per day because agents work asynchronously on separate tasks while we review draft PRs only at completion.

## What they did

Chris proposed a three-step workflow shift: (1) start in CLI (GitHub Copilot CLI or equivalent) to create first drafts, manage issues/PRs, and kick off agents without opening an editor; (2) use the editor only for fine-grained adjustments; (3) scale via CLI or GitHub UI by assigning multiple issues to agents in parallel. He demoed GitHub Copilot's 'assign agent' feature on a GitHub issue ('add dark mode'), which spins up an agent that creates a draft PR and requests human review before merge. He showed 6+ simultaneous terminals each handling different delegated tasks. Guardrails (agents.md, skills, custom agents) are the critical enabler — without them, parallel delegation produces proportionally more slop.

## Relevance to YOLO loop

Extends the YOLO loop's task intake pattern — treating the GitHub issue tracker as the agent work queue enables structured delegation and keeps human review at the PR boundary rather than during execution.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-11-cli-first-github-delegation` |
| Channel | aie |
| Video | [From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](https://www.youtube.com/watch?v=GdvKNwMcfd0) |
| Published | 2026-07-11 |
| Ingested upstream | 2026-07-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
