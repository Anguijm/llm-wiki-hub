# Implement pre-deployment adversarial red-teaming + continuous per-call monitoring loop for voice agents before production launch

> Back to [[experiments-index]]

Source: **[I Monitored Crime Audio. Voice Agents Scare Me More. — Sumanyu Sharma, Hamming AI](https://www.youtube.com/watch?v=qStB9GbppMU)** · aie · 2026-09-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run structured adversarial red-teaming on our voice agents before deployment and implement continuous per-call scoring in production, then we catch the ~10% real-world error rate and 1-in-5 adversarial jailbreak vulnerability before they compound at scale, because voice agents are centralized systems where a single prompt or architecture change can cause downstream failures across millions of calls simultaneously—unlike crime, which is decentralized.

## What they did

Sumanyu Sharma (founder/CEO, Hamming AI, formerly Citizen app monitoring thousands of hours of police radio) argued voice agent reliability is more concerning than crime because of scale and centralization. From monitoring 10,000 production agents, he found ~10% error rates (agents claiming to book appointments that weren't booked, skipping eligibility steps, applying unauthorized discounts, sharing wrong info). He described a red-teaming product they shipped that can break 1 in 5 agents adversarially—bypassing verification, extracting PHI/PII—across healthcare, financial services, and consumer sectors. He proposed a monitoring loop: identify failures, prioritize by impact (not all errors equal—some are trash fires, some are safety risks), understand the fix, execute, verify no regressions, continue monitoring. He specifically called out vocal quality and word choice as highest-impact levers and recommended 24/7 red-teaming for high-stakes deployments.

## Relevance to YOLO loop

Critical pre-production gate for any agentic system we deploy. The identify→prioritize→impact-size→fix→verify→monitor loop maps directly onto our YOLO loop as a reliability layer. Starting with a basic per-call scoring pass (does the agent actually complete the stated task?) is the minimum viable implementation.

## Notes

Hamming AI offers red-teaming and monitoring as a service. The 1-in-5 adversarial break rate is alarming and suggests this should be a standard pre-launch checklist item, not optional. AB testing vocal quality/wording changes requires production traffic—simulations alone are insufficient per Sharma.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-15-voice-agent-red-teaming-monitoring` |
| Channel | aie |
| Video | [I Monitored Crime Audio. Voice Agents Scare Me More. — Sumanyu Sharma, Hamming AI](https://www.youtube.com/watch?v=qStB9GbppMU) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
