# Run a read-only agent resource audit on the dev box

> Back to [[experiments-index]]

Source: **[Mac Mini For AI Agents: How Much Memory You Need, And How To Use What You Have.](https://www.youtube.com/watch?v=xUl-RD4l4i4)** · nb · 2026-10-20

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run a read-only diagnostic agent prompt that audits large directories, crash logs, and lingering dev servers and headless browsers, then we will reclaim memory and disk and avoid exhaustion during parallel agent runs because agent tooling leaves behind runaway logs and idle processes.

## What they did

Nate B. Jones showed macOS Activity Monitor memory pressure and a diagnostic agent prompt that inspects large directory consumers, runaway crash logs and lingering processes without altering files. He recommended terminating abandoned test servers and headless browsers, queueing and sequencing agent workloads instead of running parallel builds, capping Docker Desktop VM memory, setting context lengths in Ollama or LM Studio, and offloading long-running work to a headless secondary machine over Tailscale. He cited public reports of 50 GB crash directories and 100 GB of checkpoint Git objects.

## Relevance to YOLO loop

high: Sequencing parallel agents and pruning leftover processes and logs is operational hygiene for running Claude Code loops.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-21 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-20-agent-memory-hygiene-audit` |
| Channel | nb |
| Video | [Mac Mini For AI Agents: How Much Memory You Need, And How To Use What You Have.](https://www.youtube.com/watch?v=xUl-RD4l4i4) |
| Published | 2026-10-20 |
| Ingested upstream | 2026-10-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
