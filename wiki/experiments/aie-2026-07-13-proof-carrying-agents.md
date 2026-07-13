# Air-gap agents from tool execution by reifying plans into provably safe programs before running

> Back to [[experiments-index]]

Source: **[In Code They Act, In Proof We Trust — Erik Meijer, Leibniz Labs](https://www.youtube.com/watch?v=-CnA2lGfymY)** · aie · 2026-07-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we have the LLM emit a reified program (a free monad / expression tree) representing its intended actions rather than executing tools directly, then we can perform static type-checking and taint analysis on the plan before execution, because programs are statically analyzable while direct tool calls are not, yielding mathematically provable safety guarantees.

## What they did

Erik Meijer (Leibniz Labs) presented a technique derived from proof-carrying code (1990s academia). Instead of letting the LLM call tools directly (signature: LLM(question) -> IO action), the model returns an expression of type IO A—a free monad representing the computation. A separate verifier performs data-flow analysis, type checking, and taint analysis on this program before any execution occurs. The proof that the plan is safe is generated without running the agentic loop. A simple inductive recursive interpreter then executes only proven-safe programs. He references a Harvard GitHub implementation. The key insight: the language is machine-generated and machine-consumed, so it need not be human-readable.

## Relevance to YOLO loop

Directly addresses the unsafe tool-call problem in agentic loops. Could be integrated as a pre-execution verification layer in the YOLO loop: agent proposes plan as AST, verifier checks safety, executor runs only if verified. Particularly relevant for file system, database, or shell tool calls.

## Notes

GitHub implementation mentioned exists at Harvard. Erik notes this is proof-carrying code reapplied; DSpy and other frameworks have related RLM implementations. High effort but high safety ROI for production agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-13-proof-carrying-agents` |
| Channel | aie |
| Video | [In Code They Act, In Proof We Trust — Erik Meijer, Leibniz Labs](https://www.youtube.com/watch?v=-CnA2lGfymY) |
| Published | 2026-07-13 |
| Ingested upstream | 2026-07-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
