# mission-control

> Back to [[index]]

**Internal command center dashboard for managing OpenClaw agents with real-time monitoring and task management.**

| Property | Value |
|---|---|
| Repository | [Anguijm/mission-control](https://github.com/Anguijm/mission-control) |
| Language | TypeScript |
| Status | Active |
| Created | 2026-02-16 |

---

## Overview

Mission Control is a dashboard application for monitoring and managing AI agents. It provides real-time monitoring, task management, content intelligence, kanban boards, and agent health tracking through a Next.js interface backed by Convex for real-time database operations.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  FRONTEND        Next.js 16 App Router + React 19    │
│                  Dark theme, sidebar navigation       │
│                  Real-time Convex hooks (useQuery)     │
├─────────────────────────────────────────────────────┤
│  BACKEND         Convex (serverless)                  │
│                  No traditional REST API layer         │
│                  Auto-generated TypeScript types       │
│                  Real-time subscriptions               │
└─────────────────────────────────────────────────────┘
```

**Convex-first architecture:** No REST API layer. All data operations happen directly from React components via Convex hooks (`useQuery`, `useMutation`). Changes in the database immediately reflect in the UI through subscriptions.

## Pages / Features

| Route | Feature |
|---|---|
| `/` | Command Center (main dashboard) |
| `/agents` | Agent monitoring with real-time health indicators |
| `/tasks` | Scheduled task management |
| `/kanban` | Kanban board for project tracking |
| `/content` | Content intelligence / syndication |
| `/brain` | Second Brain document management |
| `/productivity` | Productivity metrics |
| `/calendar` | Calendar view |
| `/search` | Full-text search across activities and documents |
| `/activity` | Activity feed (heartbeats, tool calls, syncs) |
| `/connections` | External service connections |
| `/settings` | Configuration |

## Key Modules

```
app/
├── page.tsx              Command Center dashboard
├── agents/               Agent monitoring + health checks
├── tasks/                Scheduled task management
├── kanban/               Kanban board state
├── content/              Content syndication
├── brain/                Document management
├── search/               Full-text search
├── activity/             Event feed
├── productivity/         Metrics
├── calendar/             Calendar view
├── connections/          External services
├── settings/             Configuration
└── api/agents/           REST fallback (mock data)
components/
├── ConvexClientProvider.tsx   Convex context wrapper
├── Sidebar.tsx                Navigation + agent status (ping animation)
└── TaskModal.tsx              Task creation/editing
convex/
├── schema.ts             Database schema (activities, tasks, kanban, agents, users, documents, content)
├── agents.ts             Heartbeat reporting, health checks (CPU/RAM)
├── activities.ts         Event logging with type categorization
├── tasks.ts              Scheduled task management
├── kanban.ts             Kanban board state mutations
├── content.ts            Content syndication queries
├── brain.ts              Document CRUD
├── search.ts             Full-text search indices
└── seed.ts               Database seed data
skills/
├── systematic-debugging.md
├── executing-plans.md
├── writing-plans.md
├── dispatching-parallel-agents.md
└── [6 more methodology guides]
```

## Dependencies

| Dependency | Purpose |
|---|---|
| convex | Serverless backend + real-time database + auto-generated types |
| next (16) | App Router framework |
| react (19) | UI library |
| tailwindcss (4) | Utility-first styling (dark theme) |
| lucide-react | Icon library |
| chokidar | File system watcher for real-time monitoring |

**Dev dependencies:** Vitest, @testing-library/react, jsdom

## Notable Design Decisions

- **Convex-first** - Eliminates REST API boilerplate. Type-safe queries/mutations auto-generated from schema.
- **Real-time by default** - All data updates automatically sync via Convex subscriptions. No polling or manual refresh.
- **Dark theme** - CSS custom properties (--bg-page, --text-primary, --brand-blue) for cohesive dark aesthetic.
- **Agent-centric sidebar** - Displays agent status with real-time health indicators (ping animation). Health checks return CPU/RAM/system metrics.
- **Skill documentation** - Extensive `/skills` directory covers development methodologies (TDD, debugging, git workflows, planning, code review).
- **Full-text search** - Convex indices on activities and documents for quick information retrieval.

---

## Related Pages

- [[urban-explorer]] - Another Next.js real-time application
- [[harness-cli]] - AI agent orchestration tool
- [[index]] - All projects
