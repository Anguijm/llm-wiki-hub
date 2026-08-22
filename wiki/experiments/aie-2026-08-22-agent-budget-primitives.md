# Enforce agent safety via asymmetric verbs, rate limits, trip-wires, and proxy-stamped identity

> Back to [[experiments-index]]

Source: **[Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](https://www.youtube.com/watch?v=rbjWzZK2LU0)** · aie · 2026-08-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give agents access to destructive verbs that fail loudly (return errors rather than silently succeeding), rate-limit write operations with refillable ceilings, add trip-wires on aggregate unusual patterns rather than per-call allow-lists, and stamp agent identity at the proxy layer (not from the request), then runaway agent actions are contained without making agents useless because the budget has four dimensions rather than being a boolean token.

## What they did

Sachin described a real incident where a Claude agent deleted 200 workloads in 90 seconds by accidentally dropping a filter. His solution: four primitives replacing the god-token model. (1) Asymmetric verbs: deletes fail loudly (403) so humans notice; reads stay open. (2) Rate limits: refillable ceilings on writes so agents don't need tickets but can't bulk-delete. (3) Trip-wires on aggregates (e.g. >N deletes in M minutes) rather than per-resource allow-lists. (4) Proxy-stamped identity: a sidecar proxy holds real credentials and stamps every outbound call with a session-scoped identity the agent cannot spoof — so budget resets by changing a header are impossible. The 'undo test' asks: if this action runs wrong, can a human undo it? Use that to calibrate which primitive applies.

## Relevance to YOLO loop

Directly applicable: before giving Claude Code agents write access to production systems, wrap calls through a lightweight proxy that stamps session identity, add rate limits on destructive ops, and use the undo test to decide which operations need trip-wires. Even a simple token-count-based rate limiter on file deletes would have prevented the incident described.

## Notes

Sachin is on Anthropic's CI team — these primitives are in production at Anthropic. Key rule: identity must come from infrastructure (proxy), not from the request. The undo test is a simple heuristic: 'if this action goes wrong, can a human reverse it within an acceptable time window?'

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-22-agent-budget-primitives` |
| Channel | aie |
| Video | [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](https://www.youtube.com/watch?v=rbjWzZK2LU0) |
| Published | 2026-08-22 |
| Ingested upstream | 2026-08-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
