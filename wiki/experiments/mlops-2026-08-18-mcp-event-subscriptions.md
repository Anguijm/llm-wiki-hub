# Prototype MCP Event Subscriptions Using the Proposed Poll Delivery Mode

> Back to [[experiments-index]]

Source: **[Events Notifications in MCP | ​Aman Singh | MCP Release Party - Seattle](https://www.youtube.com/watch?v=XptRJZzPsdw)** · mlops · 2026-08-18

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we implement the proposed MCP events extension using polling delivery mode, then agents can be triggered by real-world events (incidents, emails, Slack messages) without holding a persistent connection open, because the poll mode works with serverless and firewall-constrained clients that cannot receive inbound webhooks.

## What they did

Aman Singh (Microsoft Azure CTO office) presented a design sketch from the MCP 'triggers and events' working group (led by Peter Alexander at Anthropic and Claire Liuri at AWS). The proposal adds a first-class events primitive where MCP servers declare event types with name, input schema for subscription parameters, payload schema, and supported delivery modes. Agents subscribe with filtered parameters (e.g., emails only from a specific domain). Three delivery modes are proposed: (1) poll—client sends name+arguments+cursor, gets back events+new cursor, works serverless/behind firewalls; (2) push—long-lived connection for low-latency local servers; (3) webhook—server POSTs to a client-provided URL, with signed deliveries and SSRF hardening. Payloads are intentionally minimal (triage-sized) to reduce prompt injection surface.

## Relevance to YOLO loop

Enables event-driven agent triggers in the dev loop—e.g., agents that wake on CI failures, PR events, or monitoring alerts without requiring the agent harness to poll continuously. The poll mode is the safest starting point given it requires no inbound network exposure.

## Notes

This is still a design sketch / GitHub PR as of 2026-07-28—nothing is in the spec yet. The working group has public weekly meetings. Implement against the PR draft, not a stable spec. Watch for SSRF hardening requirements on webhook mode before using that delivery path in production.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-18-mcp-event-subscriptions` |
| Channel | mlops |
| Video | [Events Notifications in MCP | ​Aman Singh | MCP Release Party - Seattle](https://www.youtube.com/watch?v=XptRJZzPsdw) |
| Published | 2026-08-18 |
| Ingested upstream | 2026-08-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
