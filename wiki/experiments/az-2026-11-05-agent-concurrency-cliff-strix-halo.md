# Find the parallel-agent concurrency cliff on the Strix Halo box

> Back to [[experiments-index]]

Source: **[I Thought 2 TB of RAM Was Overkill… My AI Agents Disagree](https://www.youtube.com/watch?v=nwXEAVW0jFE)** · az · 2026-11-05

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run the open-source Agent Headroom suite at 8, 12 and 16 concurrent coding agents against a local llama.cpp server on the 128 GB Strix Halo box, then we will find the lane count where conversation-cache evictions and rebuilds start, because the video showed that system memory capacity, not GPU speed, set the concurrency limit (16 agents on 128 GB RAM caused 10 failures and 30 rebuilds).

## What they did

Alex Ziskind benchmarked 8, 12 and 16 parallel coding agents with the open-source Agent Headroom suite on a Threadripper Pro workstation. At 128 GB RAM, 16 agents lost context to eviction, 10 agents failed and there were 30 conversation rebuilds. At 256 GB RAM all 16 agents finished with zero rebuilds, peaking at about 150 GB RAM. The 12-agent run dropped from 85 to 59 minutes. He also ran a 124B MoE model at 38 tokens/sec on a 32 GB GPU by offloading 90 GB of weights to system RAM.

## Relevance to YOLO loop

medium: It measures a practical limit on running parallel local agents, but it is a hardware benchmark rather than a new agent-practice technique.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-05 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `az-2026-11-05-agent-concurrency-cliff-strix-halo` |
| Channel | az |
| Video | [I Thought 2 TB of RAM Was Overkill… My AI Agents Disagree](https://www.youtube.com/watch?v=nwXEAVW0jFE) |
| Published | 2026-11-05 |
| Ingested upstream | 2026-11-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
