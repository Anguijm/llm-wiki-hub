# Use thread compaction and voice-first input to sustain multi-week agentic sessions without context rot

> Back to [[experiments-index]]

Source: **[Full Workshop: Setting Yourself Up for Success — Jason Liu, OpenAI Codex](https://www.youtube.com/watch?v=il1c1a2FufU)** · aie · 2026-07-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we rely on Codex's thread compaction feature and use voice input (foot pedal transcribe + enter) rather than typed instructions, then we can maintain coherent 5-week-old threads with hundreds of sub-agents while reducing input friction, because compaction preserves task state across the full thread history and voice input removes the keyboard bottleneck from continuous delegation.

## What they did

Ran a live 70-minute workshop on Codex workflows at OpenAI. Key practices: (1) Thread compaction—has threads that are 5 weeks old with 400+ sub-agents that still know their job; compaction makes long-running delegation viable. (2) Voice input via foot pedal (one button = transcribe, one button = enter)—walks away from keyboard while delegating tasks, hands behind back. (3) AppShots (cmd+side-by-side)—annotate screenshot in-app and have Codex fix UI issues directly. (4) Chief-of-staff thread with heartbeat—a persistent thread that monitors Slack, email, and other inputs on a configurable schedule; can be set to sleep during off-hours autonomously. (5) Team plugins—skills built for personal use that get adopted by entire company (e.g., finalize-before-PR skill). (6) Low/medium reasoning by default—X-high is rarely needed and wastes tokens; even GPT-5.5 on low reasoning outperforms prior-gen models. (7) Stopping criteria in long-running tasks—explicit conditions like 'check every 5 minutes, switch to every 1 minute when queue drops below 5 minutes, stop when refund received.'

## Relevance to YOLO loop

Multiple directly applicable patterns: compaction for long-running skill threads, heartbeat pattern for persistent monitoring agents, stopping criteria for async tasks, and defaulting to low/medium reasoning to reduce cost. Voice input is a workflow change that could significantly increase delegation throughput.

## Notes

Speaker references a monorepo with pre-built skills available to clone. Blog post at 'codex maxing' (triple-x) has additional detail. The stopping-criteria pattern for async tasks (escalating check frequency as condition approaches threshold) is immediately usable in any polling skill. Chief-of-staff thread with dynamic heartbeat frequency is a compelling pattern for our own AIOS.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-24-codex-compaction-and-voice-workflow` |
| Channel | aie |
| Video | [Full Workshop: Setting Yourself Up for Success — Jason Liu, OpenAI Codex](https://www.youtube.com/watch?v=il1c1a2FufU) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
