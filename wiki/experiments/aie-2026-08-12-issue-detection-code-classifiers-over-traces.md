# Replace Trace Clustering with Deterministic Keyword Signals and Code-Mode Classifiers for Issue Detection

> Back to [[experiments-index]]

Source: **[Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](https://www.youtube.com/watch?v=jHMiYtjoJfA)** · aie · 2026-08-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we stop using LLM clustering over agent traces to find issues and instead use deterministic signals (keyword frequency spikes, error pattern counts) to surface anomaly candidates, then feed those candidates to an agent for targeted investigation using code-mode classifiers run in a sandbox, then we will identify real actionable issues faster with fewer false clusters because deterministic signals are temporally trackable and anomaly investigation is more reliable than anomaly discovery for agents.

## What they did

Ben Hylak from Raindrop argued from first principles that naive trace clustering does not scale for issue detection: clusters have uncontrollable boundaries, mix different root causes, and cannot be tracked reliably over time. Instead, he recommended using deterministic signals like keyword frequency to surface anomaly candidates (a spike in a keyword doesn't confirm an issue but gives agents something tractable to investigate), then applying code-mode classifiers—LLM classifiers written as code, run in a sandbox at production scale—to analyze those candidates. He noted that asking agents to find anomalies fails, but asking agents to investigate already-found anomalies works well. He contrasted this with the eval theater problem: eval suites break with every model or harness change and delay shipping.

## Relevance to YOLO loop

We currently have no systematic issue detection on agent run traces. Adding keyword frequency monitoring as a lightweight first-pass filter, then routing flagged traces to an investigator agent, gives us an actionable improvement loop without the fragility of clustering.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-12-issue-detection-code-classifiers-over-traces` |
| Channel | aie |
| Video | [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](https://www.youtube.com/watch?v=jHMiYtjoJfA) |
| Published | 2026-08-12 |
| Ingested upstream | 2026-08-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
