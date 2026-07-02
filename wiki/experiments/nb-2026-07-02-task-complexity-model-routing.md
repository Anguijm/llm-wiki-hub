# Route tasks by complexity: cheap model for center-of-distribution work, frontier model for novel tasks

> Back to [[experiments-index]]

Source: **[Your AI Model is Probably Wrong for This Job](https://www.youtube.com/watch?v=lq2fP7wC7d8)** · nb · 2026-07-02

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we classify tasks as either 'center-of-distribution' (familiar artifacts like memos, summaries, CRM cleanups) or 'novel/messy' (unclear shape, requires generalized reasoning) and route accordingly to GLM 5.2 vs. Claude/GPT, then we reduce cost without sacrificing quality because cheap models perform near-frontier on well-represented task shapes while frontier models earn their cost only on genuinely hard generalization.

## What they did

Speaker described a two-tier model selection framework: a 'cheap workhorse' (GLM 5.2) for familiar, repeatable tasks with well-known shapes (PowerPoints, landing pages, meeting summaries, routine code, CRM cleanups) and a 'daily driver' frontier model (Claude, ChatGPT) reserved for messy, novel work where the task shape itself is unclear. He emphasized the decision criterion is task hardness and familiarity, not cost alone, and that the harness (how work gets in/out) matters as much as model intelligence.

## Relevance to YOLO loop

Directly applicable to our dev loop's model selection step: we can add a pre-dispatch classifier that scores task novelty/familiarity and routes to the appropriate model tier, reducing API spend on boilerplate generation tasks while preserving frontier quality for architecture decisions and novel problem-solving.

## Notes

Speaker also flagged harness quality as a separate axis from model intelligence (e.g., Gemini strong model, weak harness). Worth evaluating Z.AI as harness for GLM 5.2.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-02-task-complexity-model-routing` |
| Channel | nb |
| Video | [Your AI Model is Probably Wrong for This Job](https://www.youtube.com/watch?v=lq2fP7wC7d8) |
| Published | 2026-07-02 |
| Ingested upstream | 2026-07-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
