# yolo-projects

> Back to [[index]]

**Autonomous overnight build system: 210+ single-file HTML apps spanning games, simulations, dev tools, creative art, and more.**

| Property | Value |
|---|---|
| Repository | [Anguijm/yolo-projects](https://github.com/Anguijm/yolo-projects) |
| Language | HTML / JavaScript / Python |
| Status | Active |
| Created | 2026-03-21 |

---

## Overview

Yolo Projects is an AI-assisted autonomous build system that generates single-file HTML applications via hourly cron triggers. The system proposes project ideas through Claude Code remote agents, validates them through a 6-angle Gemini council review, and only ships code after human sign-off. Over 210 projects built to date.

## Architecture

### Tick-Tock Build Cycle

```
Hourly Cron
    │
    ├── TICK: New project proposal
    │   └── Claude Sonnet → idea → 6-angle Gemini council
    │       → human approval → build → test → ship
    │
    └── TOCK: Flagship feature development
        └── markdown-deck or naval-scribe enhancements
```

### Single-File Philosophy

Every project is a self-contained `index.html` implementing complete functionality in 300-5,000 lines of vanilla JavaScript, CSS, and HTML. No build step, no bundler, no external CDN dependencies. Open in browser = instantly functional.

### Quality Pipeline

```
Phase 1: Duplicate resolution
Phase 2: Usefulness refinement
Phase 3: Final usefulness cull (5+ score required or culled)
Phase 4: YouTube research (7 monitored channels → experiments)
```

### 6-Angle Gemini Council

Every build is reviewed across:

| Angle | Threshold |
|---|---|
| Bugs | Must pass |
| Security | Must pass |
| UI | Must pass |
| Guide/Docs | Advisory |
| Usefulness | 5+ score required |
| Cool-factor | Advisory |

## Project Categories

### Dev Tools (70+)

jwt-decode, json-explorer, regex-playground, ssl-check, dns-lookup, diff-painter, shader-forge, yaml-fmt, http-playground, url-dissect, env-inspector, git-xray, git-time-machine, commit-log, token-count, sql-explain, cron-studio, chmod-calc, ip-cidr, unicode-char, curl-converter, schema-viz, and more.

### Creative Tools (40+)

beat-haus (drum sequencer), beat-forge (music composition), note-lab (audio scratchpad), sprite-forge (pixel art), color-forge (palette generator), haiku-gen (poetry), glitch-studio (image effects), sonic-sight (audio visualization), shader-forge (GLSL editor), and more.

### Games & Simulations (50+)

neon-tetra (Tetris), sudoku, picross, connect-four, chess-clock, asteroids-evolved, dungeon-descent, regex-quest, life-canvas (Conway's Game of Life), neural-playground, circuit-sim, automata-lab, gravity-sim, fluid-sim, cloth-sim, particle-life, lenia, and more.

### Productivity & Utilities (30+)

markdown-deck (presentations with PPTX export), naval-scribe (military correspondence formatter with OOXML), kanban-board, pomodoro-flow, habit-grid, flash-cards, bookmark-dash, countdown-wall, and more.

### Visualization & Learning (25+)

algo-vision, attractor-zoo, fractal-forge, mandelbrot-explorer, lissajous-lab, penrose, epicycle, fourier-draw, iso-city, file-treemap, graph-calc, reaction-diffusion, crystal-growth, chladni-sim, and more.

## Key Files

```
yolo-projects/
├── [249 project directories]
│   └── index.html          Single-file app
│   └── README.md           Project description
│   └── plan.md             Council review planning doc
│   └── council_*.json      4 council review artifacts
├── README.md               System overview
├── design.md               Unified design system
├── program.md              Builder methodology
├── learnings.md            3000+ lines accumulated knowledge
├── yolo_log.json           223 builds: 97 working, 5 built, 42 culled, 79 failed
├── session_state.json      Tick-tock state + approval queues
├── experiments.json        Phase 4 experiment tracker (44 experiments)
├── test_project.py         7 automated checks
├── eval_bugs.py            26-pattern bug scanner
├── security_scan.py        22-rule security scanner
└── sync_project_ui.py      Accessibility override injector
```

## Dependencies

**Frontend: Zero.** All projects use native HTML5 Canvas, Web Audio API, localStorage, Fetch API, and ES6+ JavaScript. CSS is inline. Strict CSP meta tags prevent external requests.

**Backend (optional):** Python stdlib only for tooling scripts. No pip installs required.

**AI Models:** Claude Sonnet 4.6 (builder), Gemini Pro (council reviewer). 15-call Gemini budget per session.

## Design System

Codified in `design.md`:

| Property | Value |
|---|---|
| Background | #0a0a0a → #111 → #1a1a1a |
| Typography | Monospace font stack, responsive clamp sizing |
| Status Colors | Green / Amber / Red |
| Buttons | Ghost buttons (transparent + border) |
| Accessibility | Min 15px fonts, 7.6:1 color contrast (enforced by `sync_project_ui.py`) |

## Test Harness

55 total automated checks:

| Script | Checks |
|---|---|
| `test_project.py` | 7 structural checks |
| `eval_bugs.py` | 26 bug patterns |
| `security_scan.py` | 22 security rules |

Circuit breaker: 3 test failures = full stop.

## Notable Design Decisions

- **Governance as code** - `session_state.json`, `experiments.json`, `yolo_log.json` form an append-only audit trail. No silent failures.
- **Cost-capped AI** - 15-call Gemini budget per session; no visual-only simulations.
- **Learned patterns** - `learnings.md` captures 3000+ lines: vertical planning beats iterative; "boring but high-ROI filter" beats novelty.
- **27 process improvements** adopted from Phase 4 YouTube research.

---

## Related Pages

- [[harness-cli]] - The council governance tool that inspired this system
- [[sportsdata]] - Another project using council review patterns
- [[index]] - All projects
