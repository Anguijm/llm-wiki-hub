# LLM Wiki Hub

**A personal wiki and codebase documentation hub for all public repositories by [Anguijm](https://github.com/Anguijm). Modeled on [Karpathy's LLM Wiki](https://github.com/karpathy/LLMwiki).**

---

## Project Portfolio

### Active Projects

| Project | Language | Description |
|---|---|---|
| [[sportsdata]] | TypeScript | US sports analytics with ratchet loop + council governance |
| [[urban-explorer]] | TypeScript | Photo scavenger hunts for 185 cities with Gemini AI verification |
| [[roadtripper]] | TypeScript | Road trip planner using Urban Explorer database + persona recommendations |
| [[yolo-projects]] | HTML/JS/Python | 210+ autonomous single-file HTML apps (games, tools, simulations) |
| [[pm-game]] | TypeScript | Drydock Masters: semi-cooperative naval shipyard board game (2-6 players) |
| [[mission-control]] | TypeScript | Internal dashboard for AI agent monitoring with real-time Convex backend |
| [[harness-cli]] | JavaScript | AI dev harness: expert council review + human circuit breaker |
| [[intermediate-python-course]] | Python | Dice-roller course delivered via GitHub Issues |

### Archived / Empty

| Project | Status | Notes |
|---|---|---|
| [[ai-dev-team-template]] | Archived | Concepts ported to [[harness-cli]] |
| [[origin]] | Empty | Placeholder repository |

---

## Cross-Project Architecture

### Shared Patterns

Many projects share a **council governance** pattern pioneered in [[harness-cli]]:

```
Feature/Idea → Expert Council Review → Human Approval → Implementation
```

Used by: [[sportsdata]] (6 council personas), [[yolo-projects]] (6-angle Gemini council), [[pm-game]] (Claude + Gemini dual governance)

### Technology Stack Overview

| Technology | Used By |
|---|---|
| Next.js 16 + React 19 | [[urban-explorer]], [[roadtripper]], [[pm-game]], [[mission-control]] |
| TypeScript (strict) | [[sportsdata]], [[urban-explorer]], [[roadtripper]], [[pm-game]], [[mission-control]] |
| Tailwind CSS v4 | [[urban-explorer]], [[roadtripper]], [[pm-game]], [[mission-control]] |
| Firebase / Firestore | [[urban-explorer]], [[roadtripper]] |
| Convex | [[mission-control]] |
| Boardgame.io | [[pm-game]] |
| Gemini AI | [[urban-explorer]], [[yolo-projects]], [[pm-game]] |
| Anthropic/Claude SDK | [[harness-cli]], [[sportsdata]] |
| SQLite | [[sportsdata]] |

### Project Relationships

```
harness-cli ──────► sportsdata (council governance)
     │
     └────────────► pm-game (governance concepts)

urban-explorer ───► roadtripper (shared Firestore database)

ai-dev-team-template ──► harness-cli (archived predecessor)
```

---

## External Sources

Beyond GitHub repos, the wiki ingests articles and YouTube transcripts:

- [[articles-index]] - Medium posts, blog articles, and long-form web content
- [[videos-index]] - YouTube video transcripts and channel scrapes
- [[queue-schema]] - How to queue sources for ingestion via `queue.yml`

---

## Wiki Meta-Documentation

- [[project-overview]] - Purpose, goals, and inspiration behind this wiki
- [[architecture]] - System architecture and design decisions
- [[repository-structure]] - File and folder layout
- [[dependencies]] - Cross-project dependency map
- [[setup-guide]] - How to set up and use the wiki
- [[contributing]] - Guidelines for contributing content
- [[git-workflow]] - Branching strategy and commit conventions

---

## Processing Workflow

This wiki uses a three-stage pipeline across three source types (repos, articles, YouTube):

1. **`active_sources/{repos,articles,youtube}/`** - Unprocessed sources awaiting wiki generation
2. **`wiki/`** - Generated markdown documentation (you are here)
3. **`cold_storage/{repos,articles,youtube}/`** - Processed sources (documentation already generated)

Sources enter via `queue.yml` → ingest scripts (`scripts/ingest-article.py`, `scripts/ingest-youtube.py`) → Claude summarization → wiki page → archive.

See [[architecture]] for the full pipeline and [[queue-schema]] for the queue format.

| Property | Value |
|---|---|
| Repository | `anguijm/llm-wiki-hub` |
| Primary Branch | `main` |
| Wiki Format | Markdown with `[[wiki-links]]` |
| Inspired By | [Karpathy's LLMwiki](https://github.com/karpathy/LLMwiki) |
