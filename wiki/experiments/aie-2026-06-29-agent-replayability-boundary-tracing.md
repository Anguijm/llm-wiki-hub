# Instrument agent nodes with boundary-level trace capture to enable replay-based debugging and stubbed regression tests

> Back to [[experiments-index]]

Source: **[Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](https://www.youtube.com/watch?v=Lc8zRh9muoY)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we record inputs and outputs at every node boundary in our agent graph (not at the network layer) and store these as replayable traces, then we can debug production failures by replaying the exact recorded state with the model stubbed out, and convert those traces into deterministic regression tests at zero model-call cost, because the root cause of most agent failures is not model randomness but a specific state transition that can be isolated and re-run once recorded.

## What they did

Tisha Chawla and Sachin (Microsoft) demonstrated that setting temperature=0 does not make agents reproducible due to GPU non-determinism, floating-point non-associativity, batch variance, and MoE routing variability. They reframed the goal from 'bitwise determinism' to 'replayability': capturing what each node received and emitted so a failure can be re-validated without model calls. Their tool (Chronicle/Boundary) annotates node boundaries, records full envelopes (not just prompts — also LLM version, build ID, RAG chunks), and supports replay mode where any subset of nodes can be stubbed from the recorded trace while others run live. This enables: (a) deterministic debugging of a specific failure, (b) auto-generated test cases from production traces, (c) free regression runs (no model calls) by stubbing all LLM nodes.

## Relevance to YOLO loop

Production failures in our loop are currently hard to reproduce. Adding boundary-level tracing to our agent harness — even a lightweight version that logs node inputs/outputs to JSONL — would immediately improve debuggability and create a foundation for replay-based regression testing without waiting for the next failure to occur naturally.

## Notes

Chronicle/Boundary code and articles available via QR in the talk. Critical variables to log per session: LLM version, build ID, RAG chunk content/hashes. Behavioral testing (LLM-as-judge for tone, trajectory) is separate from deterministic testing (tool call outputs, guardrail triggers) — both are needed. Never pin temperature to zero as a debugging strategy.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-agent-replayability-boundary-tracing` |
| Channel | aie |
| Video | [Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](https://www.youtube.com/watch?v=Lc8zRh9muoY) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
