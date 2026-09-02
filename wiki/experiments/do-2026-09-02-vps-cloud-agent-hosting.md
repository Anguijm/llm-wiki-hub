# Run Persistent Agentic Sessions on a Self-Hosted VPS to Escape Ecosystem Lock-In

> Back to [[experiments-index]]

Source: **[How I Ship Faster Than 99% of Devs (just copy me)](https://www.youtube.com/watch?v=c9nRxEy1kUY)** · do · 2026-09-02

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we host agent harnesses (e.g., Herder, BB) on a personal VPS rather than inside proprietary coding apps, then we can run multiple parallel long-lived agent sessions across any model subscription without being subject to app-level crashes, model restrictions, or vendor lock-in, because the runtime environment is fully under our control.

## What they did

David runs agents via open-source interfaces (BB, CMAX, Herder) and Ghost Ty terminal on a personal VPS rather than inside Cursor or Codex apps. He demonstrated spinning up multiple simultaneous agent sessions in work trees, tracking their states (idle/running/blocked/done), and switching between them without app crashes. He argued a VPS is essential infrastructure for serious agentic engineering in 2026.

## Relevance to YOLO loop

The YOLO loop currently runs agents locally or inside app sandboxes; moving the harness to a persistent VPS would allow always-on background agents, better multi-agent parallelism, and resilience to local machine interruptions.

## Notes

David also mentions giving agents read-only Postgres access to production DB for reality-checking features — a separate low-effort experiment worth considering for the YOLO loop's validation step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-09-02-vps-cloud-agent-hosting` |
| Channel | do |
| Video | [How I Ship Faster Than 99% of Devs (just copy me)](https://www.youtube.com/watch?v=c9nRxEy1kUY) |
| Published | 2026-09-02 |
| Ingested upstream | 2026-09-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
