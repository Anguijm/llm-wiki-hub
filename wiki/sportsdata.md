# sportsdata

> Back to [[index]]

**US sports data analytics platform with auto-research ratchet loop and council governance.**

| Property | Value |
|---|---|
| Repository | [Anguijm/sportsdata](https://github.com/Anguijm/sportsdata) |
| Language | TypeScript |
| Status | Active |
| Created | 2026-04-04 |

---

## Overview

Sportsdata is a full-stack analytics platform covering 6 major sports leagues (NFL, NBA, MLB, NHL, MLS, EPL). It implements Karpathy's auto-research ratchet loop for monotonic prediction improvement and council-governed analysis, combining automated scraping, statistical modeling, and Jon Bois-inspired scroll-driven visualization.

## Architecture

The platform follows a 4-layer architecture:

```
┌───────────────────────────────────────────────────┐
│  GOVERNANCE   Council personas + evaluation gates  │
├───────────────────────────────────────────────────┤
│  ORCHESTRATION  Ratchet loop + pipeline state machine│
├───────────────────────────────────────────────────┤
│  ANALYSIS     Prediction models + pattern detection  │
├───────────────────────────────────────────────────┤
│  DATA         Scrapers + SQLite + JSONL audit logs   │
└───────────────────────────────────────────────────┘
```

**Data flows:** Scrapers (ESPN, The Odds API, BallDontLie) → normalizers → SQLite (WAL mode) with JSONL audit logging → analysis/prediction engines → HTTP API (port 3001) → Vite frontend (port 4000).

### Ratchet Loop

The core innovation is a literal implementation of Karpathy's HYPOTHESIZE → MODIFY → EXECUTE → EVALUATE → KEEP OR REVERT cycle. Metrics tracked include Brier score, MAE, RMSE, and Pearson r. Iterations are logged to JSONL with revert reasons, ensuring monotonic improvement -- no regression is ever possible.

### Council Governance

Six expert markdown personas in `.harness/council/` define review mandates:

- **Data Quality** - completeness, freshness, schema conformance
- **Statistical Validity** - methodology, sample size, confounders
- **Prediction Accuracy** - calibration, backtesting, base-rate comparison
- **Domain Expert** - sport context validation
- **Mathematics** - statistical rigor
- **Resolver** - outcome resolution specification

Gates return FAIL / WARN / CLEAR verdicts; `devMode` allows logging-only for safe experimentation.

## Prediction Models

| Model | Type | Description |
|---|---|---|
| v5 Winner | Continuous sigmoid | Team differential + home advantage + injury adjustment + sport-specific calibration. Clamped [15%, 85%] |
| v4-Spread (ATS) | Expected margin | Compares predicted margin vs bookmaker line. Classifies picks as Strong / Lean / Skip |

**Sport-specific calibration constants:**

| Sport | Home Win Rate | Home Advantage |
|---|---|---|
| NBA | 0.57 | +3.0 pts |
| NFL | 0.57 | +2.5 pts |
| MLB | 0.54 | +0.5 runs |
| NHL | 0.55 | +0.3 goals |
| MLS | 0.49 | -- |
| EPL | 0.46 | -- |

## Key Modules

```
src/
├── schema/          TypeScript interfaces (game, team, player, prediction, provenance)
├── scrapers/        ESPN (6 leagues), Odds API, BallDontLie, injuries, normalizer
├── storage/         SQLite (WAL mode), JSONL append-only audit, repository interface
├── orchestration/   Ratchet loop, gates, pipeline state machine, scheduler
├── analysis/        Prediction models, interesting-things detector, resolvers
├── cli/             Status, inspect, findings, backfill, predict runners
└── viz/             Data API server (15+ JSON endpoints, port 3001)
web/                 Vite frontend (Observable Plot, Scrollama, port 4000)
.harness/council/    6 expert governance personas
```

## Dependencies

| Dependency | Purpose |
|---|---|
| better-sqlite3 | Embedded SQLite with WAL mode |
| @observablehq/plot | Grammar-of-graphics charting |
| scrollama | Scroll-triggered narrative (Jon Bois aesthetic) |
| vite | Frontend bundler (port 4000) |
| tsx | TypeScript executor for CLI scripts |
| typescript | Strict type checking (ES2022) |

**Total: 7 npm packages + 3 devDependencies.** No heavy frameworks -- core uses native Node HTTP, better-sqlite3 synchronous API, and native fetch.

## Deployment

| Layer | Platform | Notes |
|---|---|---|
| Frontend | Cloudflare Pages | Static Vite build, 300+ edges |
| API | Fly.io | Node 22 slim, persistent SQLite volume |
| Cron | GitHub Actions | Daily 05:00 + 22:00 UTC, bearer-token protected |

## Notable Design Decisions

- **Point-in-time prediction** - `GameForPrediction` interface excludes actual outcomes; `PredictionContext` contains only pre-game state. No future leakage.
- **Multi-source team ID normalization** - `team_mappings` table canonicalizes ESPN, Odds API, and BallDontLie IDs for cross-provider joins.
- **Jon Bois aesthetic** - White/light theme (#f8f8f8), Roboto sans-serif, no shadows or gradients. "Mundane tools revealing extraordinary stories."
- **Append-only audit trail** - JSONL logs for scrapes, analysis decisions, gate verdicts, and ratchet iterations. Immutable by design.

---

## Related Pages

- [[harness-cli]] - The council governance tool used by this project
- [[yolo-projects]] - Another project using the council review pattern
- [[index]] - All projects
