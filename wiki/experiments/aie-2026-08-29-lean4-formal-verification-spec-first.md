# Use Lean4 Spec-First Workflow to Formally Verify Agent-Generated Code

> Back to [[experiments-index]]

Source: **[Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](https://www.youtube.com/watch?v=lRa9sPaMyy4)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we write a formal specification in Lean4 (or auto-formalize a natural language spec) before letting a coding agent implement a function, then we can prove correctness for all inputs rather than relying on probabilistic tests, because the Lean kernel mathematically checks that the implementation satisfies the specification.

## What they did

Varun Pant described a spec-driven development workflow where: (1) a human writes what 'correct' means as a specification in natural language or directly in Lean4, (2) an AI auto-formalizes it into Lean, (3) the human validates the spec, (4) a coding agent implements the code from the spec, and (5) the Lean formal verification tool proves the implementation matches the spec. He cited Andreo.AI converting zlib (a C compression library) to Lean with AI-generated proofs (32,000 lines), and Cedar (AWS authorization language) using Lean specs with Rust production code verified via 100 million nightly differential random tests.

## Relevance to YOLO loop

Directly targets the code-correctness gap in agent-generated PRs: instead of post-hoc human review or probabilistic LLM-as-judge, formal specs become a pre-commit gate in the dev loop, ensuring agent output is provably correct before merge.

## Notes

AWS open-source tool Strata mentioned as WIP for multi-language support. Start small: pick one well-bounded pure function in the codebase, write its spec in Lean4, and use Claude/Kiro to implement and prove it.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-lean4-formal-verification-spec-first` |
| Channel | aie |
| Video | [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](https://www.youtube.com/watch?v=lRa9sPaMyy4) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
