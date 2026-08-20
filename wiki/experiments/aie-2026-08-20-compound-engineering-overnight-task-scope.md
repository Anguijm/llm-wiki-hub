# Run the 'boring middle' (plan/work/review) unsupervised overnight and review output in morning

> Back to [[experiments-index]]

Source: **[The Era of Compound Engineering — Kieran Klaassen, Every/Cora](https://www.youtube.com/watch?v=_ehJyfHg1Vk)** · aie · 2026-08-20

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we design the agent's plan-work-review loop to run fully autonomously overnight (without human involvement in the middle), then we can parallelize work across a manager/creator schedule and dramatically increase effective throughput, because the human's judgment is only needed at the task definition and review ends.

## What they did

Kieran described his concrete workflow: set up the task and context in the evening (the 'brainstorm/plan' phase requiring human judgment), let the agent run overnight without supervision through the full work-review cycle, then review and polish in the morning (applying taste and raising the bar). He emphasized that this only works if the system is set up correctly — the middle must be autonomous, well-tested, and boring. Failure to invest in making the middle autonomous means you stay in the loop and lose the compounding benefit. He described the morning review as: test everything yourself, write small readable PRs, never add reviewers to code you haven't read, and use the review to extract new learnings back into the memory system.

## Relevance to YOLO loop

Directly applicable as an operating model change: define tasks in the evening, run agents overnight, review and compound in the morning. This requires ensuring our AGENTS.md and skills files are robust enough that the middle truly runs without intervention — a good forcing function for improving our context infrastructure.

## Notes

Prerequisite: the middle (plan/work/review) must be solid enough to run without you. If you're still being pulled into the middle, fix the system before trying overnight runs. Hygiene tips: test before PR, small readable PRs, read all agent-generated code before adding reviewers. The review phase is where 'raising the bar' happens — not just QA but genuinely pushing quality up each iteration.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-20-compound-engineering-overnight-task-scope` |
| Channel | aie |
| Video | [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](https://www.youtube.com/watch?v=_ehJyfHg1Vk) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
