# Use a one-way data diode plus Apache Iceberg time-travel to create a physically secure, court-defensible AI inference system

> Back to [[experiments-index]]

Source: **[Guardians of the State: An Air-Gapped AI Fortress for Consumer Data — Rachna Srivastava, DFPI](https://www.youtube.com/watch?v=2WZsT-znFTQ)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we ingest external threat intelligence into an air-gapped AI system via a physical one-way data diode (fiber optic with laser transmitter on intake side only) and store all inference outputs in an immutable time-travel queryable store (Apache Iceberg), then we can guarantee no data exfiltration while still allowing the model to learn from new threat data, and we can reproduce the exact system state at any past decision point for legal defensibility.

## What they did

Rachna described DFPI's offline AI fraud-detection system built for courtroom defensibility. The initial attempt (download open-source model, add guardrails, push live data) collapsed in 2 hours because they treated the LLM as a magic box rather than a data pipeline. The solution separates concerns: Kafka for traffic buffering, sequential event ordering, and event replay (the replay capability is the courtroom proof); Spark for data processing and format normalization; LLM only for reasoning. To allow learning without a security hole they use a physical fiber-optic data diode—the cable is physically cut in half, with a laser transmitter on the internet-facing side and a laser receiver on the secure side, with no transmitter on the secure side, making data exfiltration physically impossible. Incoming data lands in a quarantine zone with Spark validation before reaching production. A semantic router forwards each request to the smallest capable model, achieving 3x throughput increase and 70% cost reduction with no new hardware. Apache Iceberg stores immutable snapshots so they can time-travel to the exact system state at any past decision.

## Relevance to YOLO loop

For YOLO loop deployments handling sensitive data, the Kafka-replay + Iceberg time-travel pattern provides both the audit trail and the reproducibility guarantee needed to debug agent decisions post-hoc; the semantic router pattern for model routing is directly applicable to reduce inference cost per task class.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-air-gapped-ai-data-diode` |
| Channel | aie |
| Video | [Guardians of the State: An Air-Gapped AI Fortress for Consumer Data — Rachna Srivastava, DFPI](https://www.youtube.com/watch?v=2WZsT-znFTQ) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
