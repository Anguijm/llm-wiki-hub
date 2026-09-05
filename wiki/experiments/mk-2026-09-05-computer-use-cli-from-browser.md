# Use Astra Computer Use Once to Generate a Reusable CLI for API-less Tools

> Back to [[experiments-index]]

Source: **[GPT-6 Astra's Computer Use Is Ridiculously Good](https://www.youtube.com/watch?v=tU-fO6cADvQ)** · mk · 2026-09-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Astra's computer use to perform a workflow once against a tool that lacks an API and simultaneously instruct it to produce a CLI wrapping that workflow, then subsequent executions will be dramatically faster and cheaper because the CLI can be run by lower-tier models or agents without repeating full browser automation.

## What they did

The creator prompted Astra to search for flights via its internal browser and simultaneously build a reusable command-line interface for that search pattern. He benchmarked vanilla computer use (browser each time) against the generated CLI across two routes: Toronto-Lisbon went from 77s to 23s (~70% reduction) and Toronto-Seoul from 50s to 25s (~50% reduction). He then iterated the CLI to support multi-city routing and flexible date handling, explicitly testing it in a fresh session to confirm it was truly reusable.

## Relevance to YOLO loop

High relevance: any tool in the dev loop without an MCP or API (internal dashboards, legacy UIs, mobile apps) can have a CLI scaffold generated once by Astra and then called cheaply by sub-agents, reducing repeated computer-use overhead in automated pipelines.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-09-05-computer-use-cli-from-browser` |
| Channel | mk |
| Video | [GPT-6 Astra's Computer Use Is Ridiculously Good](https://www.youtube.com/watch?v=tU-fO6cADvQ) |
| Published | 2026-09-05 |
| Ingested upstream | 2026-09-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
