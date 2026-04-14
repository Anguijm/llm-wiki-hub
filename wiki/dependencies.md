# Dependencies

> Back to [[index]]

---

## Overview

This page maps dependencies across the entire portfolio. The wiki itself has zero runtime dependencies, while the documented projects span a range of technologies.

## Wiki Hub Dependencies

```
llm-wiki-hub
├── [Required] Git >= 2.x
├── [Required] Text Editor / Markdown Viewer
│
├── [Optional] Python >= 3.10     (for ingest scripts)
│   ├── readability-lxml          (better article extraction)
│   ├── html2text                 (HTML -> Markdown)
│   ├── pyyaml                    (queue.yml parsing for --from-queue)
│   └── yt-dlp                    (YouTube transcript fetching)
│
├── [Optional] Obsidian / Foam    (for [[wiki-link]] navigation)
└── [Optional] Static Site Generator (MkDocs, Jekyll)
```

All Python dependencies are optional -- ingest scripts use stdlib fallbacks when packages are missing, though quality improves with them installed.

```bash
pip install readability-lxml html2text pyyaml yt-dlp
```

## Cross-Project Dependency Map

### Frameworks

| Framework | Version | Projects |
|---|---|---|
| Next.js | 16 | [[urban-explorer]], [[roadtripper]], [[pm-game]], [[mission-control]] |
| React | 19 | [[urban-explorer]], [[roadtripper]], [[pm-game]], [[mission-control]] |
| Tailwind CSS | 4 | [[urban-explorer]], [[roadtripper]], [[pm-game]], [[mission-control]] |
| Vite | 8 | [[sportsdata]] |
| Boardgame.io | 0.50 | [[pm-game]] |
| Commander.js | 14 | [[harness-cli]] |

### Data & Storage

| Technology | Projects | Purpose |
|---|---|---|
| Firebase / Firestore | [[urban-explorer]], [[roadtripper]] | Cloud database (named "urbanexplorer" DB) |
| Convex | [[mission-control]] | Serverless real-time database |
| better-sqlite3 | [[sportsdata]] | Embedded SQLite with WAL mode |
| @vercel/kv | [[pm-game]] | Redis for daily challenge leaderboard |
| @upstash/redis | [[urban-explorer]] | Rate limiting |

### AI / ML Services

| Service | Projects | Purpose |
|---|---|---|
| Anthropic Claude SDK | [[harness-cli]] | Council persona LLM calls |
| Google Gemini | [[urban-explorer]], [[yolo-projects]], [[pm-game]] | Content generation, photo verification, council review |
| Gemini Vision | [[urban-explorer]] | Photo task verification |

### Authentication & Payments

| Service | Projects | Purpose |
|---|---|---|
| Clerk | [[urban-explorer]], [[roadtripper]] | User auth + subscription metadata |
| Stripe | [[urban-explorer]] | Subscription billing |

### Maps & Geo

| Library | Projects | Purpose |
|---|---|---|
| @vis.gl/react-google-maps | [[urban-explorer]], [[roadtripper]] | Map rendering (WebGL) |
| Google Routes API v2 | [[roadtripper]] | Route computation + matrix API |
| Google Places API | [[urban-explorer]] | POI data |
| react-leaflet | [[urban-explorer]] | Map fallback + offline |

### Visualization

| Library | Projects | Purpose |
|---|---|---|
| @observablehq/plot | [[sportsdata]] | Grammar-of-graphics charting |
| scrollama | [[sportsdata]] | Scroll-driven narrative |
| framer-motion | [[pm-game]] | Animation (dice, SI gauge, transitions) |

### Testing

| Tool | Projects |
|---|---|
| Vitest | [[pm-game]], [[mission-control]] |
| Playwright | [[urban-explorer]], [[pm-game]] |
| Custom test harness | [[yolo-projects]] (55 checks across 3 scripts) |

### Deployment

| Platform | Projects | Layer |
|---|---|---|
| Vercel | [[pm-game]] | Frontend |
| Cloudflare Pages | [[sportsdata]] | Frontend static |
| Fly.io | [[sportsdata]] | API server + SQLite |
| Render | [[pm-game]] | Multiplayer server |
| Firebase App Hosting | [[urban-explorer]] | Full stack |
| GitHub Actions | [[sportsdata]], [[yolo-projects]] | CI/CD + cron |

## Dependency Philosophy

The portfolio shows a consistent preference for **minimal, focused dependencies**:

- [[sportsdata]] uses only 7 npm packages. Core logic is pure TypeScript with native Node HTTP.
- [[harness-cli]] has exactly 3 production dependencies.
- [[yolo-projects]] has **zero** frontend dependencies across 210+ projects -- all vanilla JS.
- [[intermediate-python-course]] uses zero dependencies (pure Python stdlib).

---

## Related Pages

- [[architecture]] - Design decisions behind dependency choices
- [[index]] - All projects
