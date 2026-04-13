# Setup Guide

> Back to [[index]]

---

## Prerequisites

- **Git** (version 2.x or later) - [Download Git](https://git-scm.com/downloads)
- A **text editor** or Markdown viewer

See [[dependencies]] for the full dependency map.

## Clone the Repository

```bash
git clone https://github.com/anguijm/llm-wiki-hub.git
cd llm-wiki-hub
```

## Browse the Wiki

### Option 1: Obsidian (Recommended)

[Obsidian](https://obsidian.md/) provides the best experience for `[[wiki-link]]` navigation:

1. Download and install Obsidian.
2. Select **"Open folder as vault."**
3. Point to the `wiki/` directory.
4. All `[[wiki-links]]` become clickable. Use **Graph View** (Ctrl/Cmd + G) to visualize the knowledge graph.

### Option 2: GitHub Web UI

Navigate to the `wiki/` directory on GitHub. Start at `wiki/index.md`.

### Option 3: VS Code with Foam

Install the [Foam](https://foambubble.github.io/foam/) extension for `[[wiki-link]]` support via Ctrl/Cmd + Click.

### Option 4: Any Text Editor

Open any `.md` file directly. The `[[wiki-links]]` are human-readable even without tool support.

## Processing Pipeline

To add documentation for a new repository:

### 1. Clone into active_sources

```bash
cd active_sources
git clone https://github.com/Anguijm/<repo-name>.git
```

### 2. Analyze the codebase

Read the repo's README, package.json, source files, and architecture docs. Understand:
- What the project does
- Architecture and key patterns
- Major dependencies
- Notable design decisions

### 3. Generate wiki page

Create `wiki/<repo-name>.md` following the standard template:

```markdown
# repo-name

> Back to [[index]]

**One-line description.**

| Property | Value |
|---|---|
| Repository | [Anguijm/repo-name](https://github.com/Anguijm/repo-name) |
| Language | ... |
| Status | Active / Archived / Empty |
| Created | YYYY-MM-DD |

---

## Overview
## Architecture
## Key Modules
## Dependencies
## Notable Design Decisions

---

## Related Pages

- [[related-project]] - Why it's related
- [[index]] - All projects
```

### 4. Update the index

Add the new page to [[index]] in the Project Portfolio table.

### 5. Move to cold storage

```bash
mv active_sources/<repo-name> cold_storage/
```

### 6. Commit

```bash
git add wiki/<repo-name>.md wiki/index.md
git commit -m "add: wiki page for <repo-name>"
git push
```

## Edit Existing Pages

1. Open any `.md` file in `wiki/`.
2. Edit using standard Markdown + `[[wiki-links]]`.
3. Commit and push.

See [[contributing]] for content guidelines.

---

## Related Pages

- [[dependencies]] - Required and optional tools
- [[contributing]] - Content style guidelines
- [[repository-structure]] - Where to put new files
- [[architecture]] - Processing pipeline design
