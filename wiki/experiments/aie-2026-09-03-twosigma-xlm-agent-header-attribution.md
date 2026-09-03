# Add an X-LLM-Agent HTTP header to all agent-initiated requests for audit attribution

> Back to [[experiments-index]]

Source: **[Tethered: Our Agents Are Us — Shu Fang, Two Sigma](https://www.youtube.com/watch?v=wCIYViPd4SU)** · aie · 2026-09-03

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we inject a standard X-LLM-Agent header on every HTTP request made by an agent (while keeping the underlying user identity unchanged), then we can attribute any downstream action to either a human or an agent in logs and audit trails without needing a separate identity system, because the header is propagated through spans and trace IDs alongside the originating user identity.

## What they did

Two Sigma adds an X-LLM-Agent header to every RPC/HTTP call originating from an agent session. The header is not the sole identity signal (the underlying user identity still authenticates the request) but it allows their logging and audit systems to distinguish agent-initiated actions from human-initiated ones, enabling targeted review, blocking rules, and attribution without a full dual-identity architecture.

## Relevance to YOLO loop

This is an immediately actionable quick win: we can add this header to our agent HTTP client wrapper today. Any external API calls, webhook triggers, or internal service calls made during a YOLO loop run would be instantly distinguishable in server logs, making debugging and incident response dramatically faster.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-03-twosigma-xlm-agent-header-attribution` |
| Channel | aie |
| Video | [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](https://www.youtube.com/watch?v=wCIYViPd4SU) |
| Published | 2026-09-03 |
| Ingested upstream | 2026-09-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
