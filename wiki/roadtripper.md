# roadtripper

> Back to [[index]]

**Road trip planner that recommends curated stops along driving routes based on daily drive-time budget and travel persona.**

| Property | Value |
|---|---|
| Repository | [Anguijm/roadtripper](https://github.com/Anguijm/roadtripper) |
| Language | TypeScript |
| Status | Active |
| Created | 2026-04-04 |

---

## Overview

Roadtripper uses the [[urban-explorer]] database (102 cities, thousands of waypoints with vibe classifications) to surface persona-ranked recommendations along any driving route. Users select start/end cities, a daily drive-time budget, and one of 5 travel personas (Outdoorsman, Foodie, Gearhead, Culture, Nerd) to get personalized stop recommendations.

## Architecture

Three-layer client-server architecture optimized for minimal API billing:

```
┌──────────────────────────────────────────────────────────┐
│  SERVER COMPONENT (force-dynamic)                         │
│  Validate inputs → Google Routes API → polyline decode    │
│  → geometric filter → Matrix API → Firestore waypoints    │
├──────────────────────────────────────────────────────────┤
│  SERVER ACTION (recomputeAndRefreshAction)                 │
│  Stop add/remove → route recompute → candidate refresh    │
│  Returns discriminated union: {ok, status} | {ok:false}   │
├──────────────────────────────────────────────────────────┤
│  CLIENT STATE (PlanWorkspace)                             │
│  Persona swaps = zero API calls (client-side re-ranking)  │
│  URL sync via window.history.replaceState                 │
└──────────────────────────────────────────────────────────┘
```

### Candidate Pipeline

1. **Polyline decode** - Google Routes API returns encoded polyline
2. **Geometric filter (Phase 1)** - Sample every 50km, project 102 Urban Explorer cities against corridor
3. **Detour cost (Phase 2)** - Google Routes Matrix API for top 25 candidates by detour minutes
4. **Waypoint fetch** - Firestore query for top 10 cities (cached by sorted city-id tuple, <150KB)
5. **Client-side re-ranking** - Persona-based scoring with zero API calls

### Persona System

| Persona | Primary Types | Preferred Vibes |
|---|---|---|
| Outdoorsman | Parks, trails, nature | Adventurous, scenic |
| Foodie | Restaurants, markets, cafes | Local, authentic |
| Gearhead | Museums, tracks, garages | Industrial, mechanical |
| Culture | Galleries, theaters, landmarks | Historic, artistic |
| Nerd | Labs, bookstores, arcades | Quirky, educational |

## Key Modules

```
src/
├── app/
│   ├── plan/
│   │   ├── page.tsx            Server Component (force-dynamic)
│   │   └── actions.ts          recomputeAndRefreshAction
│   └── layout.tsx
├── components/
│   ├── PlanWorkspace.tsx        Client master (persona state, route, map)
│   ├── RouteMap.tsx             @vis.gl/react-google-maps
│   ├── RecommendationList.tsx   Persona-ranked waypoints
│   ├── PersonaSelector.tsx      5 persona cards
│   └── CityAutocomplete.tsx     Start/end city input
├── lib/
│   ├── routing/
│   │   ├── directions.ts       Google Routes API wrapper
│   │   ├── candidates.ts       Geometric filter + projection
│   │   ├── recommend.ts        Firestore waypoint fetcher
│   │   ├── scoring.ts          Isomorphic persona-based scoring
│   │   ├── rate-limit.ts       Per-IP burst/spacing/daily quota
│   │   ├── polyline.ts         Decode, sample, project
│   │   └── cache.ts            Client-side waypoint cache
│   ├── personas/               5 persona definitions + types
│   ├── urban-explorer/
│   │   └── cities.ts           102 cities + Zod schemas
│   └── firebaseAdmin.ts        Admin SDK (named "urbanexplorer" DB)
```

## Dependencies

| Dependency | Purpose |
|---|---|
| next (16) | App Router, Server Components, Server Actions |
| react (19) | UI library |
| @clerk/nextjs | Authentication |
| @vis.gl/react-google-maps | Map rendering (WebGL) |
| firebase-admin | Server-side Firestore reads |
| zod (v4) | Schema validation |
| tailwindcss (v4) | Styling |

## Notable Design Decisions

- **Force-dynamic + client state** - `/plan` is `force-dynamic` for fresh data, but avoids re-running expensive Routes API for persona swaps by keeping state in client `useState` with `window.history.replaceState` URL sync.
- **Isomorphic scoring pipeline** - `scoring.ts` runs on both server (initial render) and client (persona swaps) without refetching waypoints.
- **Discriminated-union error handling** - Server Actions return `{ok:true, status:"fresh"|"degraded"} | {ok:false, error}`. Never leaks upstream API error strings across RSC boundary.
- **Three-layer rate-limiting** - Per-IP burst/spacing/daily quota prevents abuse of expensive Google APIs.
- **Null-fallback pattern** - `liveRoute | null` and `liveWaypointFetch | null` enable clean reversion to server-rendered state when removing last stop.
- **Polyline precision fix** - Projects cities onto full encoded polyline (not just sampled points) to eliminate ~25km detour-time inflation bugs.

---

## Related Pages

- [[urban-explorer]] - Source database for city/waypoint data
- [[sportsdata]] - Another data-heavy analytics project
- [[index]] - All projects
