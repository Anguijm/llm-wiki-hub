# Add a context-aware privacy gate and per-user LoRA memory adapters to agents deployed in shared multi-user contexts

> Back to [[experiments-index]]

Source: **[Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi](https://www.youtube.com/watch?v=s67bE2Ur3bY)** · aie · 2026-07-30

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we deploy agents in group or shared-workspace settings with (a) a security gate that filters or redirects information based on context rather than just content, and (b) per-user LoRA adapters on top of a shared memory base, then agents will respect dynamic privacy boundaries (same data public in one context, private in another) without requiring explicit permission code, because the permissions are baked into the learned adapter weights rather than enforced through fragile rule systems.

## What they did

Sai Krishna described 8 months of production deployment of an agent called Judith in group settings (friend/family group chats, conference attendee groups). He identified three core challenges unique to group vs. single-user agents: (1) Security/gating: the agent must know when to respond in the group vs. DM privately — the same piece of information (e.g. salary) is public or private depending on conversational context, not just content. He proposed a roberta-style classifier to determine when the agent is allowed to speak. (2) Memory: group conversations evolve continuously, requiring a continuously-scoring relevance model (referencing 'learning what not to forget' paper) to decide what to compact vs. drop, plus a KV-cache-aware injection engine to avoid breaking prefix caches. (3) Routing: information must be routed to the right participant, not broadcast. For per-user privacy, he proposed training separate LoRA adapters per user on top of a shared memory base so permissions are encoded in weights rather than code. Also noted glasses-form-factor agents require output routing decisions (speak to glasses vs. car speaker) based on context.

## Relevance to YOLO loop

As our dev loop agents get shared across team members (shared Slack bots, shared coding assistants), these patterns become directly relevant. Near-term: implement a speak/stay-silent classifier before any agent broadcasts to a shared channel. Medium-term: explore per-user memory namespacing. The KV-cache-aware memory injection point is immediately applicable to any agent with long conversation history.

## Notes

Speaker's three-primitive summary for group agent harnesses: (1) Jatayu security gate — context-sensitive information filtering; (2) memory harness with continuous relevance scoring and KV-cache-aware injection; (3) intelligent routing to responsible parties rather than broadcast. Reference: 'The User as an Engram' paper for per-user LoRA memory approach.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-30-group-agent-memory-security-routing` |
| Channel | aie |
| Video | [Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi](https://www.youtube.com/watch?v=s67bE2Ur3bY) |
| Published | 2026-07-30 |
| Ingested upstream | 2026-07-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
