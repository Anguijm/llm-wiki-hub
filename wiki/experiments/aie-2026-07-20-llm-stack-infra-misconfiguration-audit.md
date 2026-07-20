# Run a misconfiguration audit against the ML infrastructure using the four-pillar maturity checklist before adding new agent features

> Back to [[experiments-index]]

Source: **[Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA](https://www.youtube.com/watch?v=XjI-AR4pt7Y)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we audit our LLM serving infrastructure against four pillars (infrastructure security, access control, runtime security, culture/compliance) and fix the three most common misconfigurations (over-privileged accounts, flat networks, exposed secrets/model weights) before extending agent capabilities, then we will prevent the class of breaches that actually make the news, because Nvidia's analysis shows the vast majority of real ML security incidents are misconfiguration failures rather than novel AI attacks.

## What they did

Lovina D'Mello presented NVIDIA's analysis showing that virtually all high-profile ML infrastructure breaches (including thousands of open Ray clusters with auth off by default, exposed model weights in public buckets, over-privileged service accounts with non-expiring credentials) are boring misconfiguration failures, not exotic AI attacks. She proposed a four-pillar defence-in-depth model (infrastructure → access control → runtime security → culture/compliance) and a three-level maturity model, noting most teams believe they are at level three but are actually at level one or two. Her three actionable fixes: enforce least-privilege with expiring credentials, segment the network so one compromised component cannot reach all others, and use a secrets manager with automatic scanning to prevent hardcoded credentials.

## Relevance to YOLO loop

Prerequisite hygiene for any production YOLO loop deployment: a one-day audit using her checklist would identify whether our inference endpoints, model weights storage, and service accounts meet minimum security bar before we extend agent autonomy.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-llm-stack-infra-misconfiguration-audit` |
| Channel | aie |
| Video | [Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA](https://www.youtube.com/watch?v=XjI-AR4pt7Y) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
