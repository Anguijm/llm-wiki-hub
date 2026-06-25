# Store Agent Context as Obsidian Markdown Vault for Living File Access

> Back to [[experiments-index]]

Source: **[Hermes Agent + Obsidian = The Ultimate Second Brain](https://www.youtube.com/watch?v=Q0HTefP9DFU)** · do · 2026-06-21

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we store all persistent agent context (SOPs, playbooks, skills, research outputs) as markdown files in an Obsidian vault synced to a VPS, then agent outputs will improve and compound over time because agents can directly access, update, and cross-reference structured living files rather than relying on ephemeral chat context or inaccessible dead files.

## What they did

David connected Hermes agent to an Obsidian vault containing business info, goals, SOPs, and 185 custom skills (half pre-built, half custom). He explained the concept of 'living files' vs 'dead files': a living file is any markdown file accessible to an AI agent as skill, memory, reference, or prompt context. Dead files (disconnected drives, Google Drive without agent access) provide no leverage. By syncing the vault via Obsidian Sync to MacBook, phone, and VPS, the same files are available everywhere including the always-on VPS where Hermes runs. He demonstrated using the /go feature to have Hermes scrape the 50 highest-view YouTube videos about Claude Code, fetch transcripts, and save them as markdown files directly into the Obsidian vault — work he estimated would take 3-4 hours manually done in seconds.

## Relevance to YOLO loop

Our YOLO loop could benefit from a structured markdown vault as the canonical context store for agents. Instead of re-feeding context each session, agents read from and write to versioned markdown files — research outputs, experiment notes, agent configs — making each run's outputs persistent and reusable in future runs.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Obsidian+VPS vault — redundant with the in-repo markdown context (learnings/_hot/skills) already used.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-21 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-21-obsidian-living-files-agent-context` |
| Channel | do |
| Video | [Hermes Agent + Obsidian = The Ultimate Second Brain](https://www.youtube.com/watch?v=Q0HTefP9DFU) |
| Published | 2026-06-21 |
| Ingested upstream | 2026-06-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
