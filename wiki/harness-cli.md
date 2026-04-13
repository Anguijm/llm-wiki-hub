# harness-cli

> Back to [[index]]

**AI-powered development harness that manages feature planning through an expert council of AI personas.**

| Property | Value |
|---|---|
| Repository | [Anguijm/harness-cli](https://github.com/Anguijm/harness-cli) |
| Language | JavaScript (ES modules) |
| Status | Active |
| Created | 2026-04-03 |

---

## Overview

Harness CLI orchestrates a multi-phase planning pipeline where three expert AI personas (security, architecture, product) review a feature description in parallel, a lead architect resolves conflicts, and the system generates implementation specs for coding tools -- all with mandatory human approval before any code execution.

This tool is the successor to [[ai-dev-team-template]] (archived) and is used as the governance layer in projects like [[sportsdata]], [[urban-explorer]], and [[pm-game]].

## Architecture

```
Feature Description
        │
        ▼
┌───────────────────────┐
│   COUNCIL PHASE       │  3 expert personas review in parallel
│   (Security, Arch,    │  Each outputs scored analysis
│    Product)           │  via configurable LLM models
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│   RESOLVER PHASE      │  Lead architect synthesizes
│                       │  council feedback into
│                       │  coherent architectural plan
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│   CIRCUIT BREAKER     │  CLI pauses for human
│   (Human Approval)    │  approval / rejection / editing
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│   HANDOFF PHASE       │  Generates implementation specs
│                       │  for Aider, Claude Code, or Cursor
└───────────────────────┘
```

## Commands

| Command | Purpose |
|---|---|
| `harness init` | Scaffolds `.harness/` directory, copies persona templates, initializes memory |
| `harness plan` | Core pipeline: council → resolver → circuit breaker → handoff |
| `harness review` | Run council review on existing code |
| `harness recipe` | Pre-configured workflows (bugfix, feature, api, refactor, devtool) |
| `harness learn` | Meta-learning: extracts patterns from completed plans into reusable recipes |

## Key Modules

```
src/
├── cli.js              Entry point (Commander.js command routing)
├── commands/
│   ├── init.js         Scaffolds .harness/ directory
│   ├── plan.js         Core planning pipeline + circuit breaker
│   ├── recipe.js       Pre-configured council workflows
│   ├── learn.js        Meta-learning from past plans
│   └── review.js       Council review on existing code
└── lib/
    ├── council.js      Parallel council execution (Anthropic SDK)
    ├── config.js       Custom YAML parser for harness.yml
    └── memory.js       Decision logging (.harness/memory/decisions.json)
templates/
├── harness.yml         Config template
└── council/
    ├── security.md     Security expert persona
    ├── architecture.md Architecture expert persona
    ├── product.md      Product expert persona
    └── resolver.md     Lead architect synthesis persona
```

## Dependencies

| Dependency | Purpose |
|---|---|
| @anthropic-ai/sdk | Anthropic API client for parallel LLM calls |
| commander | CLI argument parsing and command routing |
| chalk | Terminal color/styling for visual output |

**Only 3 production dependencies.** Deliberately minimal.

## Notable Design Decisions

- **Human-in-the-loop circuit breaker** - Sacred architectural principle. No autonomous coding without explicit user approval.
- **Declarative methodology** - Council personas, resolver logic, and decision memory are all version-controlled as markdown/YAML. Teams can fork and customize their AI engineering process.
- **Per-angle model overrides** - Config supports different Claude models per expert (e.g., security uses Sonnet, architecture uses Opus) for cost/quality optimization.
- **Async parallel council** - All three experts run concurrently via `Promise.all`, minimizing latency before resolver synthesis.
- **Custom YAML parser** - Lightweight implementation avoids heavy dependencies. Handles nested objects and arrays for project context injection.
- **Recipe system with meta-learning** - `harness learn` analyzes past successful plans to auto-generate domain-specific workflow templates.

## Integration Points

Projects using harness-cli store configuration in their root:

```
project/
├── harness.yml              Council configuration
└── .harness/
    ├── council/             Persona markdown files
    └── memory/
        └── decisions.json   Session memory (injected as context)
```

---

## Related Pages

- [[sportsdata]] - Uses council governance for prediction pipeline
- [[pm-game]] - Uses two-AI governance (Claude + Gemini)
- [[yolo-projects]] - Uses 6-angle Gemini council for project review
- [[ai-dev-team-template]] - Predecessor (archived)
- [[index]] - All projects
