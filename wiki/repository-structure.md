# Repository Structure

> Back to [[index]]

---

## Directory Layout

```
llm-wiki-hub/
├── README.md                           Project introduction
├── active_sources/                     Unprocessed repo clones (gitignored)
│   └── .gitignore
├── cold_storage/                       Processed repo clones (gitignored)
│   └── .gitignore
└── wiki/                               All wiki documentation (committed)
    ├── index.md                        Central hub and table of contents
    │
    ├── [Per-repo documentation]
    │   ├── sportsdata.md               Sports analytics platform
    │   ├── urban-explorer.md           Photo scavenger hunt app
    │   ├── roadtripper.md              Road trip planner
    │   ├── yolo-projects.md            210+ single-file HTML apps
    │   ├── pm-game.md                  Drydock Masters board game
    │   ├── mission-control.md          AI agent monitoring dashboard
    │   ├── harness-cli.md              AI dev governance CLI
    │   ├── intermediate-python-course.md  Python dice-roller course
    │   ├── origin.md                   Empty placeholder repo
    │   └── ai-dev-team-template.md     Archived predecessor to harness-cli
    │
    └── [Meta-documentation]
        ├── project-overview.md         Purpose, goals, and scope
        ├── architecture.md             Processing pipeline and design decisions
        ├── repository-structure.md     This file
        ├── dependencies.md             Cross-project dependency map
        ├── setup-guide.md              Setup and usage instructions
        ├── contributing.md             Contribution guidelines
        └── git-workflow.md             Branching and commit conventions
```

## Processing Pipeline Directories

### `active_sources/`

Temporary holding area for cloned repos awaiting documentation. Contents are excluded from Git via `.gitignore`. Once a repo is fully analyzed and its wiki page is written, it moves to `cold_storage/`.

### `cold_storage/`

Archive of processed repo clones. Also excluded from Git. Useful for local reference but not committed to the repository.

### `wiki/`

The heart of the repository. Every file here is committed and version-controlled. Contains two categories:

1. **Per-repo pages** - One page per public repository (e.g., `sportsdata.md`, `urban-explorer.md`)
2. **Meta-docs** - Pages about the wiki itself (e.g., `architecture.md`, `contributing.md`)

## Conventions

1. **File naming** - All wiki files use `kebab-case.md` (lowercase, hyphens).
2. **One topic per file** - Each page covers a single repo or meta-topic.
3. **Back-links** - Every page includes "Back to [[index]]" at the top and "Related Pages" at the bottom.
4. **Consistent template** - Per-repo pages follow: Overview → Architecture → Key Modules → Dependencies → Notable Design Decisions → Related Pages.
5. **No nested directories** - All pages reside at the top level of `wiki/`.

---

## Related Pages

- [[architecture]] - Processing pipeline design
- [[setup-guide]] - How to run the pipeline
- [[index]] - Main table of contents
