# urban-explorer

> Back to [[index]]

**Mobile-first web app that generates personalized photo scavenger hunts for neighborhoods worldwide.**

| Property | Value |
|---|---|
| Repository | [Anguijm/urban-explorer](https://github.com/Anguijm/urban-explorer) |
| Language | TypeScript |
| Status | Active |
| Created | 2026-01-11 |

---

## Overview

Urban Explorer lets users select a city and vibe, explore curated local spots via an interactive map, and complete photo missions with AI-powered verification. The tier-aware data model supports 185 cities across metro/town/village coverage levels with a cache-first architecture and real-time Gemini API fallback.

## Architecture

Three-tier cache-first architecture optimized for performance and quality:

```
┌──────────────────────────────────────────────────────┐
│  BUILD TIME   NotebookLM research → Gemini audit      │
│               → Firestore ingestion                    │
├──────────────────────────────────────────────────────┤
│  CACHE LAYER  185 cities pre-loaded in Firestore       │
│               Named "urbanexplorer" database           │
├──────────────────────────────────────────────────────┤
│  RUNTIME      Cache-miss → Gemini + Google Places API  │
│               Photo verification via Gemini Vision      │
└──────────────────────────────────────────────────────┘
```

**Data flow:** User enters city → `resolveLocationToCity` matches `global_city_cache.json` → Server fetches cached neighborhoods/waypoints/tasks OR generates via API → Client renders interactive map with POI markers, task list, and photo verification.

### Coverage Tiers

| Tier | Radius | Neighborhoods | Research Scope |
|---|---|---|---|
| Metro | 25 km | 6 | Full |
| Town | 10 km | 3 | Moderate |
| Village | 3 km | 1 | Minimal |

### Research Pipeline

1. **NotebookLM Deep Research** - Grounded in region-specific sources (Atlas Obscura, Reddit, The Infatuation, TimeOut)
2. **Gemini JSON Structuring** - Raw research → structured neighborhood/waypoint/task data
3. **Phase C Gemini Audit** - Hallucination removal, quality threshold validation
4. **Firestore Ingestion** - `build-vibe-cache.ts` with composite-index setup

## Key Modules

```
src/
├── app/
│   ├── page.tsx                    Landing (city search)
│   ├── select-neighborhood/        Vibe selector → neighborhood cards
│   ├── hunt/[slug]/                Dynamic hunt page with map + tasks
│   ├── my-hunts/                   Saved hunts + replay
│   ├── pricing/                    Subscription tiers
│   ├── admin/health/               Admin-only metrics dashboard
│   ├── api/                        Route handlers (neighborhoods, assignments, places, stripe)
│   └── actions/                    Server Actions (saveHunt, verifyAndCompleteTask)
├── components/
│   ├── HuntContent.tsx             Map + task list + photo checkoff
│   ├── GoogleMap.tsx               @vis.gl/react-google-maps renderer
│   ├── TaskVerification.tsx        Gemini Vision photo verification
│   └── PricingContent.tsx          Tier cards + Stripe checkout
├── lib/
│   ├── vibeCacheRetrieval.ts       Cache lookup + Firestore reads
│   ├── vibeCacheTypes.ts           Zod schemas (City, Neighborhood, Waypoint, Task)
│   ├── discoveryCacheManager.ts    LRU cache for API misses (7-day TTL)
│   └── rateLimit.ts                Upstash Redis rate limiter (30 req/min)
scripts/
├── research-city.py                NotebookLM → Gemini → JSON pipeline
├── batch-research.py               Parallel city research with circuit breaker
└── build-vibe-cache.ts             Firestore ingestion + hallucination filtering
```

## Dependencies

| Dependency | Purpose |
|---|---|
| next (16) | App Router, Server Components, Server Actions |
| react (19) | UI library |
| @clerk/nextjs | Authentication + subscription metadata gating |
| @google/generative-ai | Gemini API (neighborhoods, tasks, photo verification) |
| @vis.gl/react-google-maps | Map rendering (WebGL) |
| firebase-admin | Server-side Firestore reads (named "urbanexplorer" DB) |
| stripe | Subscription checkout + webhook processing |
| @upstash/ratelimit | Redis-backed rate limiting |
| zod | Schema validation for Firestore documents |
| react-leaflet | Map fallback + offline support |
| idb | IndexedDB for offline saved hunt state |

## Notable Design Decisions

- **Triad governance** - Claude (architect) → Gemini (auditor) → merge. Mandatory MCP audit protocol in `CLAUDE.md`.
- **Named Firestore database** - Uses `urbanexplorer` (not default) for isolated data versioning and cost tracking.
- **Photo verification via Gemini Vision** - Client uploads compressed JPEG, server calls Gemini Vision to semantically verify task completion.
- **City-local daily hunt seed** - Uses city longitude to estimate timezone offset (`lng / 15` hours), avoiding UTC midnight edge cases.
- **Multi-language support** - Schemas support 8 locales (en, ja, ko, zh-Hans, zh-Hant, es, fr, th).
- **339 tests** - Vitest + Playwright covering cache logic, Stripe pricing, coverage tiers, discovery pipeline, E2E hunt flow.

---

## Related Pages

- [[roadtripper]] - Uses this project's database for route recommendations
- [[mission-control]] - Another Next.js + real-time data project
- [[index]] - All projects
