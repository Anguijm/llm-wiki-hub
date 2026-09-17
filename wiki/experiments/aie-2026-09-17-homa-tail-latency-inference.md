# Benchmark Homa vs TCP tail latency for small coordination messages in a multi-node inference setup

> Back to [[experiments-index]]

Source: **[Homa: The End of TCP for AI Clusters — John Ousterhout, Stanford](https://www.youtube.com/watch?v=eZ8WWZzoaR0)** · aie · 2026-09-17

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we replace TCP with the Homa protocol for inter-node coordination messages in a distributed inference or agentic workload, then P99 latency for small messages will drop by an order of magnitude, because Homa uses receiver-driven flow control, SRPT scheduling, and hardware priority queues to prevent incast head-of-line blocking that plagues TCP when small and large messages compete.

## What they did

John Ousterhout (Stanford professor emeritus) presented Homa, a clean-slate data center transport protocol. He argued that AI workloads are shifting from large bulk transfers (training gradients, throughput-bound) toward small coordination messages (KV-cache lookups, barrier synchronization, token streaming) where tail latency dominates. He showed benchmarks where Homa achieves sub-100-microsecond P99 for small messages vs. over 1 millisecond for TCP — a 13x improvement — while also beating TCP by nearly 2x on large messages via run-to-completion scheduling. He noted that when computation phases shrink to milliseconds (agentic token generation), synchronization latency becomes a meaningful GPU idle fraction.

## Relevance to YOLO loop

If the YOLO loop runs inference across multiple nodes or coordinates between agent sub-processes over a network, small-message tail latency directly translates to GPU idle time and overall loop throughput. Replacing TCP with Homa for the coordination plane (while keeping existing data paths) is a targeted experiment. Ousterhout offered direct collaboration for early adopters.

## Notes

Homa is open source; Ousterhout is actively maintaining it and offered hands-on help. Prerequisite: first instrument current setup to confirm small-message latency is actually a bottleneck (audience poll showed ~30% of practitioners already seeing this). Linux kernel module available. Start with a synthetic incast benchmark before testing on real inference workloads.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-17-homa-tail-latency-inference` |
| Channel | aie |
| Video | [Homa: The End of TCP for AI Clusters — John Ousterhout, Stanford](https://www.youtube.com/watch?v=eZ8WWZzoaR0) |
| Published | 2026-09-17 |
| Ingested upstream | 2026-09-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
