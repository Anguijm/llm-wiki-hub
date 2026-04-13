# pm-game

> Back to [[index]]

**Drydock Masters: a semi-cooperative digital board game of naval shipyard management for 2-6 players.**

| Property | Value |
|---|---|
| Repository | [Anguijm/PM-game](https://github.com/Anguijm/PM-game) |
| Language | TypeScript |
| Status | Active |
| Created | 2026-03-27 |

---

## Overview

Drydock Masters is a 12-round cooperative-competitive board game where players manage labor dice, work orders, and shared Shipyard Integrity (SI) while competing for individual Prestige Points. Built on Next.js 16 + Boardgame.io with online multiplayer via WebSocket and hot-seat local play via a "Pass Device" info-hiding system.

## Architecture

```
┌──────────────────────────────────────────────────────┐
│  CLIENT          Next.js 16 App Router + React 19     │
│                  Framer Motion animations              │
│                  Procedural audio (use-sound)           │
├──────────────────────────────────────────────────────┤
│  GAME ENGINE     Boardgame.io state machine            │
│                  Deterministic RNG (no Math.random)    │
│                  13 validated player moves              │
├──────────────────────────────────────────────────────┤
│  MULTIPLAYER     Socket.io (port 8001)                 │
│                  Vercel (frontend) + Render (server)   │
└──────────────────────────────────────────────────────┘
```

### Game Loop (5 Phases)

```
Contract Selection → Event/Planning → Action → Resolution
                    (repeat 12 rounds)
```

### Player Moves (13 total)

| Move | Phase | Description |
|---|---|---|
| selectContract | Contract Selection | Choose ship contract |
| draftCard | Planning | Draw work order or BAWP card |
| stageWork | Action | Place job in drydock slot |
| assignLabor | Action | Assign labor dice to job |
| procurement | Action | Buy supplies from market |
| coordinate | Action | Trade resources with ally |
| analyzeMarket | Action | View market state |
| hireForeman | Action | Hire specialist foreman |
| clearObstruction | Action | Remove persistent problem |
| trade | Action | Resource exchange |
| emergencyOvertime | Action | Burn dice for urgent work |
| expeditedShipping | Action | Rush delivery |
| pass | Any | End turn |

### Bot System

5 AI strategies for single-player or filling seats:

| Strategy | Behavior |
|---|---|
| Balanced | Even resource allocation |
| Aggressive | High-risk, high-reward |
| Cautious | Prioritizes SI preservation |
| Rush | Speed over quality |
| Hoarder | Stockpiles resources |

## Key Modules

```
src/
├── game/
│   ├── index.ts          Game object + 5 special event effects
│   ├── types.ts          Core interfaces (DrydockMastersState, PlayerState, card types)
│   ├── moves.ts          13 player moves with validation
│   ├── setup.ts          Deck shuffling, player/dice/slot initialization
│   ├── resolution.ts     Dice countdown, job completion, SI drain, milestones
│   └── bot.ts            5 bot strategies
├── data/
│   └── cards.ts          30+ card definitions (work orders, BAWP, events, foreman)
├── components/
│   ├── board/            GameBoard, TopBar, SITracker, GameOver
│   ├── phases/           Phase-specific views (5 phases)
│   ├── cards/            WorkOrderCard, ForemanCard, EventCardDisplay
│   ├── player/           HandPanel, DrydockSlot, MilestoneTracker
│   └── market/           MarketPanel, TradeModal
├── app/
│   └── page.tsx          Home/menu (local vs online play)
├── remotion/             Programmatic video assets (marketing trailer)
└── server.ts             Boardgame.io server (port 8001, CORS)
```

## Dependencies

| Dependency | Purpose |
|---|---|
| boardgame.io | Game engine: state machine, deterministic RNG, multiplayer |
| next (16) | React metaframework with App Router |
| react (19) | UI library |
| framer-motion | Dice countdown, phase transitions, SI gauge spring animations |
| socket.io | WebSocket multiplayer (Render server ↔ frontend) |
| remotion | Programmatic marketing trailer video rendering |
| @vercel/kv | Redis for daily challenge leaderboard |
| posthog-js | Analytics (tutorial dropoff, round engagement) |
| use-sound | React hook for procedural SFX |
| tailwindcss (4) | Styling |
| typescript (6) | Strict type checking |

## Testing

| Type | Details |
|---|---|
| Unit | 63 Vitest tests (setup, moves, resolution) |
| E2E | Playwright: 10 complete games to conclusion |
| Simulation | 3,400+ simulated games for balance tuning |
| Balance | 55% win rate across player counts; SI triggers in 37% of games |

## Deployment

| Layer | Platform |
|---|---|
| Frontend | Vercel |
| Multiplayer Server | Render (port 8001) |

## Notable Design Decisions

- **Two-AI governance** - Claude (Opus 4.6) as lead architect + Gemini (Pro) as adversarial auditor. Mandatory audit gates in `CLAUDE.md`.
- **Deterministic RNG** - Uses Boardgame.io's `random.Shuffle()` (not `Math.random()`) for identical card draws across all multiplayer clients.
- **Fail-forward growth work** - Jobs fail 15% of the time, forcing additional iterations. Prevents deterministic optimization.
- **Persistent problems** - Events that drain SI each round until actively cleared. Creates cooperative tension.
- **Cumulative milestones** - Per-player quotas at rounds 6/8/10 with escalating penalties.
- **Naval/industrial aesthetic** - Dark navy + steel gray + amber accents; spring animations on SI gauge; procedural SFX.

---

## Related Pages

- [[harness-cli]] - Council governance tool
- [[sportsdata]] - Another project with council governance
- [[index]] - All projects
