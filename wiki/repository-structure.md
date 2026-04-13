# Repository Structure

> Back to [[index]]

---

## Directory Layout

```
llm-wiki-hub/
├── README.md                  # Project introduction and quick links
└── wiki/                      # All wiki content lives here
    ├── index.md               # Main entry point and table of contents
    ├── project-overview.md    # Purpose, goals, and inspiration
    ├── architecture.md        # System architecture and design decisions
    ├── repository-structure.md# This file — file and folder layout
    ├── dependencies.md        # Dependency map and external tooling
    ├── setup-guide.md         # Setup and usage instructions
    ├── contributing.md        # Contribution guidelines
    └── git-workflow.md        # Branching and versioning strategy
```

## File Descriptions

### Root Files

| File        | Purpose                                                                 |
| ----------- | ----------------------------------------------------------------------- |
| `README.md` | The repository landing page displayed on GitHub. Contains a brief description of the project and links into the wiki. |

### `wiki/` Directory

The `wiki/` directory is the heart of the repository. Every Markdown file in this directory is a wiki page, interlinked using the `[[wiki-links]]` convention.

| File                      | Purpose                                              | Key Links                                     |
| ------------------------- | ---------------------------------------------------- | --------------------------------------------- |
| `index.md`                | Central table of contents and entry point            | Links to all other pages                      |
| `project-overview.md`     | High-level project purpose and goals                 | [[project-overview]]                          |
| `architecture.md`         | Technical architecture and design rationale          | [[architecture]]                              |
| `repository-structure.md` | This page — describes the file layout                | [[repository-structure]]                      |
| `dependencies.md`         | Lists all runtime and development dependencies       | [[dependencies]]                              |
| `setup-guide.md`          | Instructions for cloning, browsing, and editing      | [[setup-guide]]                               |
| `contributing.md`         | Guidelines for submitting changes                    | [[contributing]]                              |
| `git-workflow.md`         | Branching model and commit conventions               | [[git-workflow]]                              |

## Conventions

1. **File naming** - All wiki files use `kebab-case.md` naming (lowercase, hyphens between words).
2. **One topic per file** - Each Markdown file covers a single topic to keep pages focused and linkable.
3. **Back-links** - Every page includes a "Back to [[index]]" link at the top and a "Related Pages" section at the bottom.
4. **No nested directories** (currently) - All pages reside at the top level of `wiki/`. See [[architecture]] for future plans on categorization.

---

## Related Pages

- [[architecture]] - Design decisions behind this layout
- [[index]] - Main table of contents
