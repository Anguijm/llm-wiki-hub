# Repository Structure

> Back to [[index]]

---

## Directory Layout

```
llm-wiki-hub/
├── README.md                        Project introduction
├── queue.yml                        Inbox for URLs awaiting ingestion
│
├── scripts/                         Ingest scripts (Python, stdlib + optional deps)
│   ├── ingest-article.py            Fetch web articles (Medium, blogs)
│   └── ingest-youtube.py            Fetch YouTube transcripts via yt-dlp
│
├── active_sources/                  Unprocessed sources (contents gitignored)
│   ├── .gitignore
│   ├── repos/                       Cloned GitHub repos
│   ├── articles/                    Fetched article markdown + metadata
│   └── youtube/                     YouTube transcripts organized by channel
│
├── cold_storage/                    Processed sources (contents gitignored)
│   ├── .gitignore
│   ├── fingerprints.json            URL → content hash (for dedup + update detection)
│   ├── repos/                       Archived repo clones
│   ├── articles/                    Archived article sources
│   └── youtube/                     Archived YouTube transcripts
│
└── wiki/                            All wiki documentation (committed)
    ├── index.md                     Central hub and table of contents
    │
    ├── [Per-repo pages]
    │   ├── sportsdata.md
    │   ├── urban-explorer.md
    │   ├── roadtripper.md
    │   ├── yolo-projects.md
    │   ├── pm-game.md
    │   ├── mission-control.md
    │   ├── harness-cli.md
    │   ├── intermediate-python-course.md
    │   ├── origin.md
    │   └── ai-dev-team-template.md
    │
    ├── [External source indexes]
    │   ├── articles-index.md        Chronological list of processed articles
    │   └── videos-index.md          Chronological list of processed videos
    │
    ├── articles/                    One page per processed article
    │   └── <author>-<title-slug>.md
    │
    ├── videos/                      One page per processed video
    │   └── <channel>-<video-id>.md
    │
    └── [Meta-documentation]
        ├── project-overview.md
        ├── architecture.md          Processing pipeline
        ├── repository-structure.md  This file
        ├── dependencies.md          Cross-project dependency map
        ├── queue-schema.md          queue.yml format reference
        ├── setup-guide.md
        ├── contributing.md
        └── git-workflow.md
```

## Source Type Conventions

| Type | Slug Format | Example |
|---|---|---|
| Repo | Repo name | `sportsdata` |
| Article | `<author>-<title-slug>` | `karpathy-yes-you-should-understand-backprop` |
| YouTube video | `<channel>-<video-id>` | `andrejkarpathy-kCc8FmEb1nY` |

Slugs match `[a-z0-9-]+` and are unique within their type.

## `.gitignore` Strategy

`active_sources/` and `cold_storage/` track **only directory structure**, not contents:

```
# .gitignore pattern used in both directories
*
!.gitignore
!repos/
!articles/
!youtube/
!**/.gitkeep
repos/*
articles/*
youtube/*
!repos/.gitkeep
!articles/.gitkeep
!youtube/.gitkeep
```

`.gitkeep` files in each subdirectory preserve the empty-folder structure in Git.

## Conventions

1. **File naming** - All wiki files use `kebab-case.md`.
2. **One topic per file** - Each page covers a single repo, article, video, or meta-topic.
3. **Back-links** - Every page opens with "Back to [[index]]" and closes with "Related Pages".
4. **Consistent templates**:
   - Per-repo: Overview → Architecture → Key Modules → Dependencies → Notable Design Decisions
   - Per-article: Summary → Key Ideas → Quotes → Related Work
   - Per-video: Summary → Chapter Highlights → Key Quotes → Related Work
5. **Cross-linking** - Every new page adds/updates at least one `[[wiki-link]]` to an existing page.

---

## Related Pages

- [[architecture]] - Processing pipeline design
- [[queue-schema]] - `queue.yml` format
- [[setup-guide]] - How to run the pipeline
- [[index]] - Main table of contents
