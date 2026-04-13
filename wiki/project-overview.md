# Project Overview

> Back to [[index]]

---

## Purpose

**LLM Wiki Hub** is a personal, Git-backed wiki that documents every public repository by [Anguijm](https://github.com/Anguijm). It is inspired by [Andrej Karpathy's LLMwiki](https://github.com/karpathy/LLMwiki) and provides a centralized knowledge base with interlinked documentation for a portfolio of 10 projects spanning sports analytics, travel apps, board games, AI tooling, and autonomous build systems.

## Goals

1. **Codebase Documentation** - Comprehensive wiki page for every public repo: architecture, dependencies, key modules, and design decisions.
2. **Cross-Project Mapping** - Surface shared patterns, dependencies, and technology choices across the portfolio.
3. **Processing Pipeline** - Automate the clone → analyze → document → archive workflow via `active_sources/` → `wiki/` → `cold_storage/`.
4. **Version-Controlled Content** - Leverage Git history to track every documentation change.
5. **Wiki-Style Navigation** - Use `[[wiki-links]]` for a densely interlinked knowledge graph.

## Scope

The wiki covers all public repositories:

### Active (8 projects)

- [[sportsdata]] - Sports analytics platform with prediction models
- [[urban-explorer]] - Photo scavenger hunt app for 185 cities
- [[roadtripper]] - Road trip planner with persona-based recommendations
- [[yolo-projects]] - 210+ autonomous single-file HTML apps
- [[pm-game]] - Drydock Masters digital board game
- [[mission-control]] - AI agent monitoring dashboard
- [[harness-cli]] - AI development governance CLI
- [[intermediate-python-course]] - Python dice-roller course

### Archived / Empty (2)

- [[ai-dev-team-template]] - Predecessor to harness-cli (archived)
- [[origin]] - Empty placeholder

## Inspiration

Karpathy's LLMwiki demonstrated that a simple GitHub repository of Markdown files can serve as an effective knowledge base. LLM Wiki Hub adopts the same philosophy while adding a processing pipeline for automated documentation generation and `[[wiki-links]]` for cross-referencing.

---

## Related Pages

- [[architecture]] - How the wiki and processing pipeline work
- [[repository-structure]] - Full layout including active_sources and cold_storage
- [[dependencies]] - Cross-project dependency map
