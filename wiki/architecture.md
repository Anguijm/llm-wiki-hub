# Architecture

> Back to [[index]]

---

## Overview

LLM Wiki Hub follows a **static, file-based architecture**. There is no runtime server, database, or build pipeline. The entire knowledge base is composed of plain Markdown files stored in a Git repository.

```
┌─────────────────────────────────────────────┐
│                  Git Repository              │
│                                              │
│  ┌──────────┐    ┌────────────────────────┐  │
│  │ README.md│    │       wiki/            │  │
│  │ (root)   │    │                        │  │
│  └──────────┘    │  index.md              │  │
│                  │  project-overview.md    │  │
│                  │  architecture.md        │  │
│                  │  repository-structure.md│  │
│                  │  dependencies.md        │  │
│                  │  setup-guide.md         │  │
│                  │  contributing.md        │  │
│                  │  git-workflow.md        │  │
│                  └────────────────────────┘  │
└─────────────────────────────────────────────┘
```

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

Link resolution follows a flat namespace: `[[architecture]]` resolves to `wiki/architecture.md`.

### 3. Flat File Hierarchy

All wiki pages live directly inside the `wiki/` directory without nested subdirectories. This keeps navigation simple and avoids deep path references. As the wiki grows, a category-based subdirectory structure (e.g., `wiki/models/`, `wiki/techniques/`) can be introduced.

### 4. Git as the Collaboration Layer

- **Branching** enables parallel content development (see [[git-workflow]]).
- **Pull Requests** provide a review mechanism for content changes.
- **History** offers a full audit trail of every edit.

### 5. No Build Step

The wiki is designed to be consumed as-is. There is no static-site generator, CI pipeline, or deployment target by default. Users who want a rendered site can plug in tools like MkDocs, Jekyll, or Docusaurus without modifying the source content.

## Data Flow

```
Author writes Markdown
        │
        ▼
  git add / commit
        │
        ▼
  git push to GitHub
        │
        ▼
  Readers browse on GitHub
  or clone locally
```

## Future Considerations

| Consideration             | Notes                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Static-site generation    | MkDocs or Jekyll could render the wiki into a hosted site   |
| Search                    | A client-side search index (e.g., Lunr.js) could be added   |
| Link validation           | A CI check could verify that all `[[wiki-links]]` resolve   |
| Tagging / metadata        | YAML front matter could enable filtering and categorization |

---

## Related Pages

- [[project-overview]] - Why this project exists
- [[repository-structure]] - Detailed file layout
- [[dependencies]] - External tools and requirements
