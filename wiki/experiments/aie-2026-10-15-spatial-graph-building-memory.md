# Store multi-temporal spatial scans as a graph to enable change-detection queries over physical environments

> Back to [[experiments-index]]

Source: **[Every Building Is a Balance Sheet: Spatial Memory for Real-World Assets — Jordi Spranger, Spranic](https://www.youtube.com/watch?v=Fe4aSMXsOZ4)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we store successive lidar/sensor scans of a physical space as aligned graph snapshots in a graph database, then we can answer ledger-style change-detection queries (what changed, when, who needs to know) in milliseconds instead of requiring a site visit, because the graph structure preserves object identity and spatial relationships across time.

## What they did

Jordi Spranger described Spranic's system built on Neo4j. An off-the-shelf sensor scans a space while walking; the scan produces a map in about one minute. Objects in the map are recognized and stored as nodes with edges representing spatial relationships. Repeated scans of the same space are aligned on a time axis, so the graph holds the full evolution of the space. Users can chat with the asset to ask spatial questions ('where can I heat myself?', 'is there a mug in the kitchen?') and get answers grounded in the map. Change detection compares two scans object-by-object and returns deltas with references to the actual capture as proof. Downstream use cases discussed: maintenance scheduling, compliance checks (e.g., expired fire extinguishers), insurance policy personalization based on verified building state at policy start and renewal, and digital twin input for robotics.

## Relevance to YOLO loop

Conceptually relevant if the YOLO loop needs to reason about physical environment state or asset inventories. The core pattern—temporal graph snapshots enabling diff queries—is transferable to any domain where state changes over time and queries need provenance.

## Notes

Spranic founded June 2026; very early stage. The graph+temporal-alignment pattern is the transferable insight; the specific hardware pipeline is domain-specific. Neo4j used as graph backend.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-spatial-graph-building-memory` |
| Channel | aie |
| Video | [Every Building Is a Balance Sheet: Spatial Memory for Real-World Assets — Jordi Spranger, Spranic](https://www.youtube.com/watch?v=Fe4aSMXsOZ4) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
