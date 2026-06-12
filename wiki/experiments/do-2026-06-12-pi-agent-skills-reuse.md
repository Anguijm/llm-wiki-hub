# Build Pi Agent Skills as Reusable Prompt Modules for Repeated Workflows

> Back to [[experiments-index]]

Source: **[Forget Claude Code, try Pi Agent instead…](https://www.youtube.com/watch?v=jcUqsNpDDDk)** · do · 2026-06-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we encode repeated multi-step agent workflows as Pi Agent skills (markdown prompt files loaded into context), then we will reduce prompt re-entry time and drift across sessions because skills are versioned files that can be committed to the repo and loaded deterministically.

## What they did

David demonstrated Pi's skills system where a skill is a markdown file containing a prompt template for a recurring task. He showed creating a skill, loading it into a session, and using it to drive consistent behavior. He noted that all skills, agents.md context, and prompt templates are stored as plain files that can be shared via the team's knowledge base (he uses a New Society classroom module). He also covered session resumption with /resume to continue previous conversations, enabling long-running projects to persist state across restarts.

## Relevance to YOLO loop

Skills are the Pi equivalent of our reusable prompt library. Adding a skills/ directory to our repo and wiring /resume into our session startup gives the YOLO loop persistent, versioned task memory without a database dependency.

## Notes

Pairs with the Pi minimal harness experiment. Consider maintaining a shared skills/ directory in the monorepo as a first implementation step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-12-pi-agent-skills-reuse` |
| Channel | do |
| Video | [Forget Claude Code, try Pi Agent instead…](https://www.youtube.com/watch?v=jcUqsNpDDDk) |
| Published | 2026-06-12 |
| Ingested upstream | 2026-06-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
