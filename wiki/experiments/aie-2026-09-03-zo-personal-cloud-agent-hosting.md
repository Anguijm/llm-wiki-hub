# Host your personal agent and its dependent services on a single self-owned cloud node

> Back to [[experiments-index]]

Source: **[Everyone Gets A Software Company — Benjamin Guo, Zo Computer](https://www.youtube.com/watch?v=Qr15lGAGKpo)** · aie · 2026-09-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we co-locate a personal agent, its skill integrations, and the web services it manages on a single user-owned cloud compute node (personal server), then the agent will have lower-latency access to context and tools, avoid depending on third-party SaaS credential chains, and allow services the agent builds to be immediately hostable without a separate deployment pipeline, because everything runs in one place under one identity with no middlemen.

## What they did

Ben Guo demonstrated Zo Computer, a personal cloud server with a built-in AI agent, browser automation, scheduled tasks, a skill library, and web hosting all on the same node. He showed the agent buying things on Amazon, hosting personal websites (including a Calendly replacement), and managing invoices — all from a single persistent personal cloud that the user owns and controls rather than renting from SaaS providers.

## Relevance to YOLO loop

We could experiment with running our YOLO loop agent on a dedicated personal VPS (e.g., a Hetzner node) that also hosts the web services it generates, giving the agent direct filesystem and service access with no credential-passing overhead and making every generated artifact immediately live-testable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-03-zo-personal-cloud-agent-hosting` |
| Channel | aie |
| Video | [Everyone Gets A Software Company — Benjamin Guo, Zo Computer](https://www.youtube.com/watch?v=Qr15lGAGKpo) |
| Published | 2026-09-03 |
| Ingested upstream | 2026-09-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
