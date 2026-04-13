# Architecture

> Back to [[index]]

---

## Overview

LLM Wiki Hub is a **static, file-based documentation system** with a three-stage processing pipeline. There is no runtime server, database, or build pipeline. The entire knowledge base is composed of plain Markdown files stored in a Git repository.

## Processing Pipeline

```
┌──────────────────┐     ┌──────────────┐     ┌──────────────────┐
│  active_sources/  │────►│    wiki/      │────►│  cold_storage/   │
│                   │     │              │     │                  │
│  Unprocessed      │     │  Generated   │     │  Processed       │
│  repo clones      │     │  markdown    │     │  repo clones     │
│                   │     │  docs        │     │  (archived)      │
└──────────────────┘     └──────────────┘     └──────────────────┘
     Clone repos           Analyze &            Move after
     from GitHub           generate docs        documentation
```

### Workflow

1. **Clone** - Public repos are cloned into `active_sources/`
2. **Analyze** - Each codebase is read: README, package.json, source files, architecture
3. **Generate** - A comprehensive wiki page is written to `wiki/` with architecture diagrams, dependency maps, key modules, and design decisions
4. **Archive** - The processed repo clone is moved to `cold_storage/`
5. **Link** - The new page is cross-referenced in [[index]] and related pages via `[[wiki-links]]`

## Design Decisions

### 1. Markdown as the Single Content Format

All wiki content is authored in GitHub-Flavored Markdown (GFM). This ensures:

- **Portability** - Files can be read in any text editor, GitHub's web UI, or static-site generators.
- **Diffability** - Git diffs are meaningful and human-readable.
- **Simplicity** - No compilation or transpilation step is required.

### 2. `[[wiki-links]]` Convention

Internal references between pages use the `[[page-name]]` double-bracket syntax. This convention:

- Is widely supported by tools like Obsidian, Foam, and GitHub Wiki.
- Keeps links short and readable compared to relative Markdown links.
- Creates an implicit knowledge graph that can be visualized by compatible tools.

Link resolution follows a flat namespace: `[[sportsdata]]` resolves to `wiki/sportsdata.md`.

### 3. Three-Stage Pipeline (active_sources → wiki → cold_storage)

- **`active_sources/`** holds repo clones during analysis. `.gitignore` excludes contents from version control.
- **`wiki/`** is the only directory committed to the repository. It contains the generated documentation.
- **`cold_storage/`** holds processed repos for reference. Also `.gitignore`'d.

This separation keeps the wiki repository lightweight (just markdown) while preserving full source access locally.

### 4. One Page Per Repository

Each public repo gets a dedicated wiki page following a consistent template:

- Overview and metadata table
- Architecture diagram
- Key modules listing
- Dependency table
- Notable design decisions
- Related pages (cross-links to sibling projects)

### 5. Cross-Project Mapping

The [[index]] page maps shared patterns across the portfolio:

- Council governance pattern (used by [[sportsdata]], [[yolo-projects]], [[pm-game]], [[harness-cli]])
- Technology stack overlap (Next.js, TypeScript, Tailwind CSS)
- Project relationships (e.g., [[urban-explorer]] → [[roadtripper]] database sharing)

### 6. Git as the Collaboration Layer

- **Branching** enables parallel documentation work (see [[git-workflow]]).
- **Pull Requests** provide a review mechanism.
- **History** offers a full audit trail of every edit.

## Future Considerations

| Consideration | Notes |
|---|---|
| Static-site generation | MkDocs or Jekyll could render the wiki into a hosted site |
| Automated re-processing | Cron job to re-clone and update docs when repos change |
| Link validation | CI check to verify all `[[wiki-links]]` resolve |
| Tagging / metadata | YAML front matter for filtering and categorization |

---

## Related Pages

- [[project-overview]] - Why this wiki exists
- [[repository-structure]] - Detailed file layout
- [[dependencies]] - Cross-project dependency map
