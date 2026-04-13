# Dependencies

> Back to [[index]]

---

## Overview

LLM Wiki Hub is intentionally minimal in its dependency footprint. Since the project is a collection of Markdown files versioned with Git, there are **no runtime dependencies** and only a small set of development-time tools.

## Dependency Map

```
llm-wiki-hub
│
├── [Required] Git ≥ 2.x
│     └── Version control, branching, collaboration
│
├── [Required] Text Editor / Markdown Viewer
│     └── Any editor: VS Code, Vim, Emacs, Obsidian, etc.
│
├── [Optional] GitHub Account
│     └── Remote hosting, pull requests, issue tracking
│
├── [Optional] Obsidian / Foam / Logseq
│     └── [[wiki-link]] resolution and graph visualization
│
└── [Optional] Static Site Generator (MkDocs, Jekyll, Docusaurus)
      └── Renders wiki into a hosted website
```

## Required Dependencies

| Dependency  | Version | Purpose                                   |
| ----------- | ------- | ----------------------------------------- |
| **Git**     | ≥ 2.x   | Source control and collaboration           |
| **Editor**  | Any     | Authoring and reading Markdown content     |

### Git

Git is the only hard requirement. It is used to:

- Clone the repository
- Track content changes
- Collaborate via branches and pull requests
- Maintain a full history of every edit

### Text Editor

Any editor capable of rendering or editing `.md` files will work. Recommended options:

- **VS Code** with the Markdown Preview extension
- **Obsidian** for `[[wiki-link]]` support and graph view
- **Vim / Neovim** for terminal-based editing

## Optional Dependencies

| Tool                    | Purpose                                          |
| ----------------------- | ------------------------------------------------ |
| **GitHub**              | Remote hosting and collaboration                 |
| **Obsidian / Foam**     | Enhanced wiki navigation and graph visualization |
| **MkDocs / Jekyll**     | Static site generation for hosting               |
| **markdownlint**        | Linting Markdown files for consistent style      |
| **link-checker**        | Validating that all `[[wiki-links]]` resolve     |

### Obsidian Integration

Obsidian natively supports the `[[wiki-links]]` convention. To use this wiki in Obsidian:

1. Open Obsidian and select "Open folder as vault."
2. Point it to the `wiki/` directory.
3. All `[[wiki-links]]` will become clickable, and the graph view will visualize page relationships.

See [[setup-guide]] for detailed instructions.

## Dependency Security

Because there are no package managers, lock files, or third-party code dependencies, the attack surface is effectively zero. All content is static Markdown rendered by the viewer of the reader's choice.

---

## Related Pages

- [[architecture]] - Design decisions that keep dependencies minimal
- [[setup-guide]] - How to install and configure required tools
- [[repository-structure]] - Where everything lives in the repo
