# Experiments Index

> Back to [[index]]

**536 experiments** synthesized from the [[yolo-projects]] Phase 4 YouTube research pipeline, covering AI/dev content from 10 tracked channels.

This page is regenerated automatically by `scripts/ingest-yolo-phase4.py` on every sync. See [[yolo-phase4-integration]] for the full flow.

---

## By status

| Status | Count |
|---|---|
| `backlog` | 236 |
| `discarded` | 92 |
| `adopted` | 90 |
| `deferred` | 56 |
| `done` | 48 |
| `in_progress` | 10 |
| `skipped` | 4 |

## By verdict

| Verdict | Count |
|---|---|
| `(none)` | 306 |
| `adopt` | 128 |
| `discard` | 102 |

## By channel

| Channel | Experiments |
|---|---|
| @aie | 204 |
| @nb | 100 |
| @nh | 85 |
| @mlops | 47 |
| @do | 43 |
| @mk | 22 |
| @aij | 14 |
| @st | 9 |
| @up | 5 |
| @eh | 4 |
| @fs | 2 |
| @tmp | 1 |

---

## All experiments

Ordered by published date, most recent first.

| Date | Title | Channel | Verdict |
|---|---|---|---|
| 2026-07-26 | [[experiments/nh-2026-07-26-claude-code-agentic-onboarding|Build a local AI operating system in Claude Code with persistent context across all business tools]] | @nh | `-` |
| 2026-07-26 | [[experiments/nb-2026-07-26-ai-agent-support-root-cause-loop|Use an AI agent to root-cause recurring support tickets and close the upstream failure]] | @nb | `-` |
| 2026-07-26 | [[experiments/mk-2026-07-26-personal-benchmark-slash-command|Build a /benchmark slash command that runs your real tasks against new models and scores them against your personal rubric]] | @mk | `-` |
| 2026-07-26 | [[experiments/aie-2026-07-26-sondermind-modular-guardrails-evals|Implement separate LLM-as-judge guardrail calls sandwiching core agent to improve robustness and eval granularity]] | @aie | `-` |
| 2026-07-26 | [[experiments/aie-2026-07-26-deepswe-contamination-resistant-benchmark|Design coding evals with one task per repo and runtime isolation to prevent git-log cheating]] | @aie | `-` |
| 2026-07-25 | [[experiments/nh-2026-07-25-opus5-vs-fable5-claude-code-comparison|Benchmark Opus 5 vs Fable 5 on Real Coding Workflows Inside Claude Code]] | @nh | `-` |
| 2026-07-25 | [[experiments/nh-2026-07-25-fable-orchestrator-opus-subagent|Use Fable as a Delegating Orchestrator to Preserve Context Window Budget]] | @nh | `-` |
| 2026-07-25 | [[experiments/aie-2026-07-25-video-eval-small-vlm-judge|Fine-Tune a Small VLM as a Fast Video Quality Judge Calibrated by Periodic Human Annotation]] | @aie | `-` |
| 2026-07-25 | [[experiments/aie-2026-07-25-tiny-model-finetune-voice-function-calling|Fine-Tune a Sub-4B Parameter Model on Synthetic Data for Robust Voice-to-Function-Calling]] | @aie | `-` |
| 2026-07-25 | [[experiments/aie-2026-07-25-control-loop-pr-flow-control|Implement Adaptive Flow Control to Prevent PR Stack-Up in Agentic Loops]] | @aie | `-` |
| 2026-07-25 | [[experiments/aie-2026-07-25-agent-simulation-benchmark-from-traces|Build a Private Agent Benchmark from Production Traces for Repeatable Offline Evaluation]] | @aie | `-` |
| 2026-07-24 | [[experiments/nh-2026-07-24-opus5-verification-loops|Replace Fable 5 with Opus 5 as default agentic loop model and measure cost-quality tradeoff]] | @nh | `-` |
| 2026-07-24 | [[experiments/nh-2026-07-24-expertise-vs-situational-context-split|Split AIOS context into expertise (stable) and situational (project-specific) layers to reduce bloat]] | @nh | `-` |
| 2026-07-24 | [[experiments/nh-2026-07-24-aios-context-failure-modes|Run an automated OS audit skill to detect context failure modes before they cause hallucinations]] | @nh | `-` |
| 2026-07-24 | [[experiments/nb-2026-07-24-job-first-context-scoping|Gate context selection on the job, not the file]] | @nb | `-` |
| 2026-07-24 | [[experiments/nb-2026-07-24-airlock-pii-scrub-before-llm|Build a pre-LLM PII scrubber that rebuilds a clean doc before upload]] | @nb | `-` |
| 2026-07-24 | [[experiments/mlops-2026-07-24-coding-agents-as-general-agents|Repurpose coding-agent infrastructure for non-coding knowledge work tasks]] | @mlops | `-` |
| 2026-07-24 | [[experiments/do-2026-07-24-kimi-k3-task-routing|Add Kimi K3 as a routed model for frontend and legal tasks]] | @do | `-` |
| 2026-07-24 | [[experiments/aie-2026-07-24-youtube-ads-vibe-first-then-scale-evals|Start evals with manual vibing on small golden sets before investing in scaled rater infrastructure]] | @aie | `-` |
| 2026-07-24 | [[experiments/aie-2026-07-24-vending-bench-emergent-misbehavior-evals|Design long-horizon eval environments with emergent incentive structures to surface misbehavior without explicit prompting]] | @aie | `-` |
| 2026-07-24 | [[experiments/aie-2026-07-24-uber-closed-loop-multimodal-evals|Implement a Swiss-cheese QA gate architecture with redundant eval layers before production publish]] | @aie | `-` |
| 2026-07-24 | [[experiments/aie-2026-07-24-harbor-agent-dev-as-ml-paradigm|Treat agent skills as ML model weights and use rollout-based evals to optimize them]] | @aie | `-` |
| 2026-07-24 | [[experiments/aie-2026-07-24-cyber-benchmark-dynamic-world-model|Evaluate agent reasoning quality using dynamic state-inference tasks where causal chains are opaque]] | @aie | `-` |
| 2026-07-24 | [[experiments/aie-2026-07-24-codex-compaction-and-voice-workflow|Use thread compaction and voice-first input to sustain multi-week agentic sessions without context rot]] | @aie | `-` |
| 2026-07-24 | [[experiments/aie-2026-07-24-arize-signal-to-pr-self-improving-agent|Build a trace-driven agent that auto-generates a PR with evidence before human review]] | @aie | `-` |
| 2026-07-24 | [[experiments/aie-2026-07-24-agent-as-judge-for-agentic-evals|Replace fixed-rubric LLM-as-judge evals with an agent-as-judge for multi-turn agentic outputs]] | @aie | `-` |
| 2026-07-23 | [[experiments/nb-2026-07-23-trusted-access-policy-for-ai-cyber-defense|Implement pre-verified trusted-access tiers for frontier models in security workflows]] | @nb | `-` |
| 2026-07-23 | [[experiments/nb-2026-07-23-multi-model-redundancy-strategy|Build a model-diverse fallback stack with at least one open-weights model for disruption resilience]] | @nb | `-` |
| 2026-07-23 | [[experiments/nb-2026-07-23-local-model-fallback-for-sensitive-analysis|Pre-vet and deploy a local open-weights model as a no-guardrail fallback for sensitive artifact analysis]] | @nb | `-` |
| 2026-07-23 | [[experiments/nb-2026-07-23-anti-slop-human-intent-signal|Add a human-intent attestation step to AI-generated content pipelines]] | @nb | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-video-spatial-temporal-memory-layer|Build a persistent spatiotemporal memory layer for video assets that supports cross-file entity continuity and moment retrieval]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-semantic-relationship-graph|Link artifacts across sources into a cross-referenced meaning graph]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-pre-planning-alignment-before-agent-coding|Add structured pre-planning (architecture + program design docs) before every agent coding task]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-perception-agent-shared-screen-context|Give agents continuous visual perception of shared UI state so they can monitor, detect, and recover from step failures]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-ontology-validator-for-agent-tool-outputs|Add an ontology-based validator after each agent tool call to catch semantically invalid outputs before they propagate]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-offline-context-precomputation|Precompute user context profiles offline before agent queries]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-notion-token-cost-model-routing|Build a per-task model routing layer that matches model capability to task complexity to control token costs]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-knowledge-graph-as-agent-control-plane|Replace multi-agent context handoff chains with a single reasoning agent navigating a knowledge graph control plane]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-graph-shapes-for-agent-context|Model agent context as typed graph shapes (table-of-contents, connection, theme) rather than flat vector search]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-graph-provenance-for-llm-facts|Attach source lineage to every LLM-extracted fact in agent memory using graph relationships that survive mutation]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-execution-dag-anomaly-detection|Model agent pipeline execution as a DAG and detect structural drift and timing anomalies against a learned baseline]] | @aie | `-` |
| 2026-07-23 | [[experiments/aie-2026-07-23-dspy-task-signature-separation|Wrap every repeated AI task in a DSPy-style typed signature to decouple task logic from model/prompt implementation]] | @aie | `-` |
| 2026-07-22 | [[experiments/nh-2026-07-22-claude-ai-consultant-roadmap|Build One Claude Workflow Demo with Before/After Metrics]] | @nh | `-` |
| 2026-07-22 | [[experiments/mk-2026-07-22-local-ai-command-center-agentic-setup|Use Claude Code to Auto-Install and Configure a Local Open-Weight Model Stack]] | @mk | `-` |
| 2026-07-22 | [[experiments/aie-2026-07-22-thin-agents-ontology-semantic-layer|Implement a Three-Pillar Ontology Layer (Business + Technical + Execution Traces) to Enable Thin Cross-Agent Data Discovery]] | @aie | `-` |
| 2026-07-22 | [[experiments/aie-2026-07-22-graph-memory-vs-markdown-for-agents|Replace Agent Markdown File Memory with a Neo4j Graph Store and Benchmark Retrieval Precision]] | @aie | `-` |
| 2026-07-22 | [[experiments/aie-2026-07-22-gates-foundation-knowledge-graph-sip|Build a Cross-System Semantic Knowledge Graph as the Agentic Retrieval Layer]] | @aie | `-` |
| 2026-07-22 | [[experiments/aie-2026-07-22-claude-managed-agents-brain-hands-decoupling|Decouple Agent Harness (Brain) from Execution Sandbox (Hands) with an Append-Only Session Log]] | @aie | `-` |
| 2026-07-22 | [[experiments/aie-2026-07-22-agent-auth-identity-per-agent|Assign Per-Agent Scoped Identity and Audit Logs Instead of Passing User Credentials to Agents]] | @aie | `-` |
| 2026-07-22 | [[experiments/aie-2026-07-22-active-graph-log-centric-agent-runtime|Replace Session Logs with an Immutable Event-Sourced Graph as Agent Ground Truth]] | @aie | `-` |
| 2026-07-21 | [[experiments/aie-2026-07-21-state-of-ai-eng-audio-modality|Add Audio Modality to Existing Agent Pipeline as High-Intent Adoption Signal]] | @aie | `-` |
| 2026-07-21 | [[experiments/aie-2026-07-21-outcome-based-agent-scoring|Instrument Execution Layer to Capture Outcome-Based Agent Scores]] | @aie | `-` |
| 2026-07-21 | [[experiments/aie-2026-07-21-html-native-video-agents|Use Raw HTML/CSS/JS as Agent Output Format Instead of Custom DSLs]] | @aie | `-` |
| 2026-07-21 | [[experiments/aie-2026-07-21-harness-to-claw-agentic-spectrum|Build an Always-On Cloud Harness with Slack Integration]] | @aie | `-` |
| 2026-07-21 | [[experiments/aie-2026-07-21-execution-layer-decoupling|Decouple Execution Layer from Context and Compute Layers in Agent Architecture]] | @aie | `-` |
| 2026-07-21 | [[experiments/aie-2026-07-21-desktop-local-model-sovereign|Benchmark Local Open-Weight Models as Drop-In Replacements for Cloud Models in Agent Workflows]] | @aie | `-` |
| 2026-07-20 | [[experiments/nh-2026-07-20-sell-transformation-not-ai|Reframe AI feature demos as before/after transformation stories]] | @nh | `-` |
| 2026-07-20 | [[experiments/mlops-2026-07-20-agent-harness-calibration|Instrument agent traces to classify failure modes and calibrate harness rigidity]] | @mlops | `-` |
| 2026-07-20 | [[experiments/aij-2026-07-20-tmux-multi-cli-orchestration|Orchestrate heterogeneous coding agents (Claude Code, Codex, Gemini CLI) via tmux pane control]] | @aij | `-` |
| 2026-07-20 | [[experiments/aij-2026-07-20-claude5-orchestrator-sonet5-executor|Use Claude 4 Opus as orchestrator and Sonnet 5 as persistent executor sub-agent to cut costs 35%]] | @aij | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-snyk-hooks-skills-agent-code-security|Add security scanning as Claude Code hooks and skills rather than post-hoc MCP scanning to reduce latency and token overhead]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-small-model-voice-latency|Offload all reasoning to scaffolding code and use the smallest model that fits the latency budget]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-slop-squatting-supply-chain-detection|Add a package provenance verification step before any agent-suggested dependency is installed]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-physical-data-harness-knowledge-base|Build a persistent knowledge base of processed dataset results to prevent redundant expensive compute]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-llm-stack-infra-misconfiguration-audit|Run a misconfiguration audit against the ML infrastructure using the four-pillar maturity checklist before adding new agent features]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-least-privilege-api-keys-agents|Replace kitchen-sink API keys with scoped OAuth tokens minted per agent tool call via a security token service]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-inloop-verification-three-loop-sdlc|Embed code verification inside the agentic loop (not just CI) using the guide-verify-solve three-loop pattern]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-harness-state-machine-voice-tutor|Wrap multi-step agent logic in an explicit state machine harness]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-generator-validator-separation|Separate the code-generating agent from the security-validating agent to prevent self-review blind spots]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-episodic-semantic-memory-agent-consistency|Add episodic and semantic memory to agent classification tasks to reduce flip-flop inconsistency on boundary cases]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-enterprise-agent-source-hierarchy|Structure agent knowledge sources as a ranked hierarchy from curated to flexible]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-e2e-encryption-personal-agent|Store agent memory keys only on client device and attest workload integrity via a public transparency log before key sharing]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-deterministic-wrapper-limits-agent-blast-radi|Wrap agentic reasoning in a deterministic orchestration layer that owns all credentials and side-effects]] | @aie | `-` |
| 2026-07-20 | [[experiments/aie-2026-07-20-agent-jurassic-four-layer-sandbox|Implement four-layer agent oversight: deterministic floor, courageable agent, intelligent adversary, structured human escalation]] | @aie | `-` |
| 2026-07-19 | [[experiments/st-2026-07-19-harness-engineering-levers|Structure agent customization across three explicit levers: context, tools, and automations with evals]] | @st | `-` |
| 2026-07-19 | [[experiments/nb-2026-07-19-local-llm-pii-detection|Run an air-gapped local LLM to detect and mask PII before sending docs to cloud AI]] | @nb | `-` |
| 2026-07-19 | [[experiments/aie-2026-07-19-single-cell-foundation-models|Benchmark flow-matching models against autoencoder-based models for single-cell RNA-seq generation]] | @aie | `-` |
| 2026-07-19 | [[experiments/aie-2026-07-19-hierarchical-hypothesis-generation|Inject a hierarchical hypothesis-generation step into autonomous coding agent loops to break optimization plateaus]] | @aie | `-` |
| 2026-07-19 | [[experiments/aie-2026-07-19-eval-pipeline-customer-support|Build a config-driven eval harness with hard launch gates, simulated multi-turn conversations, and online regression monitoring]] | @aie | `-` |
| 2026-07-19 | [[experiments/aie-2026-07-19-continuous-perf-optimization-agent|Build a weekly autonomous agent workflow that surfaces scored high-ROI performance optimization PRs from production traces]] | @aie | `-` |
| 2026-07-19 | [[experiments/aie-2026-07-19-agent-auth-least-privilege|Implement fine-grained, principal-bound, time-limited auth scopes for agents instead of reusing human OAuth credentials]] | @aie | `-` |
| 2026-07-18 | [[experiments/eh-2026-07-18-intelligence-as-process-not-substance|Frame AI objectives as pattern-compression processes, not capability lists]] | @eh | `-` |
| 2026-07-18 | [[experiments/aie-2026-07-18-subgraph-pattern-matching-context-retrieval|Replace vector search with shortest-path subgraph retrieval for code dependency context]] | @aie | `-` |
| 2026-07-18 | [[experiments/aie-2026-07-18-schema-first-graph-extraction|Use schema-constrained structured outputs for graph extraction from unstructured text]] | @aie | `-` |
| 2026-07-18 | [[experiments/aie-2026-07-18-own-inference-infrastructure-post-pmf|Benchmark token-max context compression to cut inference costs on high-volume agent loops]] | @aie | `-` |
| 2026-07-18 | [[experiments/aie-2026-07-18-froglet-verifiable-agent-receipts|Add cryptographically-signed execution receipts to agent tool calls for auditability and replay]] | @aie | `-` |
| 2026-07-18 | [[experiments/aie-2026-07-18-domain-expert-evaluators-before-auto-optimiza|Define high-signal domain evaluators with experts before running any prompt auto-optimization loop]] | @aie | `-` |
| 2026-07-18 | [[experiments/aie-2026-07-18-content-as-code-structured-pipelines|Build a declarative content pipeline (changelogs, docs, product tours) driven from a structured codebase]] | @aie | `-` |
| 2026-07-18 | [[experiments/aie-2026-07-18-ai-ux-trust-pillars|Add suggested prompts, next-step action buttons, and streaming indicators to AI feature UIs]] | @aie | `-` |
| 2026-07-18 | [[experiments/aie-2026-07-18-agent-feature-flags-six-surfaces|Implement per-surface agent feature flags (prompt, tool, model, memory, autonomy, sub-agent) with a kill switch]] | @aie | `-` |
| 2026-07-18 | [[experiments/aie-2026-07-18-agent-checkpoint-replay-cohort-evals|Implement checkpoint-replay cohort analysis to validate model swaps before shipping]] | @aie | `-` |
| 2026-07-17 | [[experiments/nb-2026-07-17-automagic-skill-for-automation|Package an 'Auto-Magic' Problem-Discovery Prompt as a Reusable Skill File]] | @nb | `-` |
| 2026-07-17 | [[experiments/nb-2026-07-17-ai-picks-the-problem|Let the AI Agent Pick Its Own Problem from Your Business Context]] | @nb | `-` |
| 2026-07-17 | [[experiments/do-2026-07-17-ssh-persistent-agent-session|Run Agent Sessions in a Persistent Multiplexed Terminal Accessible via SSH from Any Device]] | @do | `-` |
| 2026-07-17 | [[experiments/do-2026-07-17-firstmate-multi-agent-orchestrator|Replace Tab-Juggling with a Single Orchestrator Agent (First Mate Pattern)]] | @do | `-` |
| 2026-07-17 | [[experiments/aie-2026-07-17-yc-skill-files-as-workforce|Encode Every Repeatable Workflow as a Skill File and Build a Compounding Organizational Library]] | @aie | `-` |
| 2026-07-17 | [[experiments/aie-2026-07-17-yc-imagination-engineering-think-public|Stream-of-Consciousness Brain Dump into a Channel, Then Synthesize with an Agent into a Personalized Knowledge Interface]] | @aie | `-` |
| 2026-07-17 | [[experiments/aie-2026-07-17-unsloth-reward-hacking-verification|Add Reward-Hacking Detection Checks Before Accepting AI-Generated Performance Claims]] | @aie | `-` |
| 2026-07-17 | [[experiments/aie-2026-07-17-microsoft-iq-company-grounding|Implement an Agent Optimizer Loop That Hill-Climbs Agent Instructions from Trace Data]] | @aie | `-` |
| 2026-07-17 | [[experiments/aie-2026-07-17-deepmind-chain-of-code-reasoning|Use Code as the Reasoning Medium for Multi-Step Agent Tasks Instead of Natural Language Chains]] | @aie | `-` |
| 2026-07-16 | [[experiments/aie-2026-07-16-background-computer-use-quad-driver|Run Computer-Use Agents in the Background Without Screen Takeover]] | @aie | `-` |
| 2026-07-16 | [[experiments/aie-2026-07-16-ai-agent-top-contributor-parameter-golf|Design Tight Codebase Abstractions to Prevent Agent Reward Hacking]] | @aie | `-` |
| 2026-07-16 | [[experiments/aie-2026-07-16-agent-eval-as-loss-function|Treat Agent Eval as a Loss Function and Iterate on It First]] | @aie | `-` |
| 2026-07-15 | [[experiments/nb-2026-07-15-harness-audit-skill|Build a Harness Inventory Skill to Map All Context Inputs]] | @nb | `-` |
| 2026-07-15 | [[experiments/nb-2026-07-15-compact-vs-thick-skill-test|A/B Test Compact vs. Thick Skill Variants to Find Delivery Failure Thresholds]] | @nb | `-` |
| 2026-07-15 | [[experiments/mlops-2026-07-15-multi-agent-debate-research|Use Competing-Model Debate Pattern for Deep Domain Research]] | @mlops | `-` |
| 2026-07-15 | [[experiments/aie-2026-07-15-recursive-model-improvement-loops|Implement Inner/Outer Training Loop Separation with Agent-Driven Eval Generation]] | @aie | `-` |
| 2026-07-15 | [[experiments/aie-2026-07-15-context-layer-mining|Build a Compounding Context Layer by Mining Business System Connections and Reverse-Constructing Semantic Links]] | @aie | `-` |
| 2026-07-15 | [[experiments/aie-2026-07-15-claude-code-delegation-threshold|Calibrate Agent Delegation Threshold by Tracking Permission-Prompt Acceptance Rate Over Model Generations]] | @aie | `-` |
| 2026-07-14 | [[experiments/nh-2026-07-14-inhouse-ai-consultant-roadmap|Run a Constraint-First AI Audit to Identify High-Value Automation Targets]] | @nh | `-` |
| 2026-07-14 | [[experiments/do-2026-07-14-tailscale-multi-agent-network|Connect All Agent Machines via Tailscale with Zero Open Ports]] | @do | `-` |
| 2026-07-14 | [[experiments/do-2026-07-14-aperture-secure-api-keys|Store Agent API Keys in Aperture Instead of on the VPS]] | @do | `-` |
| 2026-07-14 | [[experiments/aij-2026-07-14-piper-agent-extensible-harness|Use Pi Agent's Extension System to Self-Modify the Coding Harness at Runtime]] | @aij | `-` |
| 2026-07-14 | [[experiments/aij-2026-07-14-loop-contract-md-pattern|Structure Every Agent Loop Around a Loop Contract Markdown File with State and Append-Only Log]] | @aij | `-` |
| 2026-07-14 | [[experiments/aie-2026-07-14-skill-evals-before-ship|Write Eval Test Cases for Every Agent Skill Before Deploying It]] | @aie | `-` |
| 2026-07-14 | [[experiments/aie-2026-07-14-loops-debate-spec-gated-slices|Gate Loop Autonomy Behind Spec-Verified, Test-Covered Slices Rather Than Open-Ended Tasks]] | @aie | `-` |
| 2026-07-14 | [[experiments/aie-2026-07-14-irt-llm-benchmarking|Apply Item Response Theory to Internal Agent Evals to Get Calibrated Model Intelligence Scores]] | @aie | `-` |
| 2026-07-14 | [[experiments/aie-2026-07-14-fde-motion-matrix|Use a Digital-Maturity × Product-Customization Matrix to Scope FDE Engagements]] | @aie | `-` |
| 2026-07-14 | [[experiments/aie-2026-07-14-answerability-outer-loop|Enforce an 'Explain It or Don't Ship It' Rule at the Outer Loop Boundary]] | @aie | `-` |
| 2026-07-13 | [[experiments/nb-2026-07-13-model-selection-by-work-pattern|Select model based on personal work-pattern audit, not benchmark scores]] | @nb | `-` |
| 2026-07-13 | [[experiments/nb-2026-07-13-fable-as-orchestrator-ringer|Use Fable 5 as intent-parsing orchestrator to farm tasks to cheaper sub-models]] | @nb | `-` |
| 2026-07-13 | [[experiments/mk-2026-07-13-effort-level-calibration|Start all tasks at low effort and escalate only on evidence of inadequacy]] | @mk | `-` |
| 2026-07-13 | [[experiments/aie-2026-07-13-verifiers-async-rl-post-training|Use open-source Verifiers + PrimeRL to post-train models on your own production task distribution]] | @aie | `-` |
| 2026-07-13 | [[experiments/aie-2026-07-13-rlm-recursive-context-management|Implement RLM pattern to externalize large-codebase context into a programmable REPL environment]] | @aie | `-` |
| 2026-07-13 | [[experiments/aie-2026-07-13-proof-carrying-agents|Air-gap agents from tool execution by reifying plans into provably safe programs before running]] | @aie | `-` |
| 2026-07-13 | [[experiments/aie-2026-07-13-microvm-sandbox-snapshot-restore|Use microVM memory snapshots with layered lineage for low-latency sandbox creation and Monte Carlo agent exploration]] | @aie | `-` |
| 2026-07-12 | [[experiments/nh-2026-07-12-claude-code-clay-lead-gen|Use Claude Code as natural-language orchestrator over Clay MCP for end-to-end lead enrichment]] | @nh | `-` |
| 2026-07-12 | [[experiments/nb-2026-07-12-no-roadmap-15-commandments|Audit every dev-loop process against the 'does it shorten learning loops?' test]] | @nb | `-` |
| 2026-07-12 | [[experiments/aie-2026-07-12-typescript-agent-layer|Build the agent orchestration layer in TypeScript with Zod schemas shared end-to-end]] | @aie | `-` |
| 2026-07-12 | [[experiments/aie-2026-07-12-semantic-blindness-hierarchical-tool|Replace large-context entity lookup with a deterministic hierarchical resolver tool handed to the LLM]] | @aie | `-` |
| 2026-07-12 | [[experiments/aie-2026-07-12-review-debt-scorer|Implement a deterministic review-debt score on every AI-generated PR]] | @aie | `-` |
| 2026-07-12 | [[experiments/aie-2026-07-12-remobi-tmux-mobile-agent-monitor|Add Remobi + tmux to the agent-monitoring stack for mobile steering of running agents]] | @aie | `-` |
| 2026-07-12 | [[experiments/aie-2026-07-12-openclaw-trusted-proxy-auth|Enable OpenClaw trusted-proxy-auth mode behind an identity-aware proxy to remove token friction]] | @aie | `-` |
| 2026-07-12 | [[experiments/aie-2026-07-12-nanda-open-agent-index|Register an agent on the NANDA open index and test cross-organization agent discovery]] | @aie | `-` |
| 2026-07-12 | [[experiments/aie-2026-07-12-irt-llm-benchmark-evaluation|Apply Item Response Theory to internal evals to get per-model theta scores and detect item noise]] | @aie | `-` |
| 2026-07-12 | [[experiments/aie-2026-07-12-done-as-object-liveness-model|Replace boolean task completion with a structured 'done object' enforced by the agent control plane]] | @aie | `-` |
| 2026-07-12 | [[experiments/aie-2026-07-12-ai-bugpocalypse-secure-by-design|Run a frontier model over the codebase to find vulnerability classes before adversaries do]] | @aie | `-` |
| 2026-07-11 | [[experiments/nh-2026-07-11-token-dashboard-local|Deploy a local Claude Code token usage dashboard via GitHub repo]] | @nh | `-` |
| 2026-07-11 | [[experiments/nh-2026-07-11-claude-code-non-coder-aios|Build a persistent AI operating system context layer in Claude Code]] | @nh | `-` |
| 2026-07-11 | [[experiments/aie-2026-07-11-semantic-tool-selection|Filter agent tool context with semantic vector search before each call]] | @aie | `-` |
| 2026-07-11 | [[experiments/aie-2026-07-11-open-claw-parallel-worktrees|Use Open Claw as a spec-focused orchestrator above Claude Code to parallelize work across git worktrees]] | @aie | `-` |
| 2026-07-11 | [[experiments/aie-2026-07-11-neurosymbolic-runtime-guardians|Implement Python-level hard-stop and self-correcting runtime guardrails for agents]] | @aie | `-` |
| 2026-07-11 | [[experiments/aie-2026-07-11-multi-agent-dream-cycle|Add a nightly dream-cycle agent that consolidates memory, resolves contradictions, and surfaces a morning report]] | @aie | `-` |
| 2026-07-11 | [[experiments/aie-2026-07-11-jury-judge-multi-agent-validation|Implement jury-and-judge multi-agent pattern for high-stakes tasks with no empirically correct answer]] | @aie | `-` |
| 2026-07-11 | [[experiments/aie-2026-07-11-conveyor-belt-agentic-delegation|Redesign agent UX around async delegation with human-pausable conveyor belt and weekly active sessions metric]] | @aie | `-` |
| 2026-07-11 | [[experiments/aie-2026-07-11-cli-first-github-delegation|Adopt CLI-first workflow with GitHub issue-to-agent delegation as primary development scaling pattern]] | @aie | `-` |
| 2026-07-11 | [[experiments/aie-2026-07-11-agent-output-gate-contracts|Add explicit boundary contracts (voice, verification, deduplication, schema) at each agent handoff to block polished-but-wrong artifacts]] | @aie | `-` |
| 2026-07-10 | [[experiments/nh-2026-07-10-soul-vs-fable-routing|Route tasks between GPT-5.6 Soul and Claude Fable 5 based on creative vs. execution workload]] | @nh | `-` |
| 2026-07-10 | [[experiments/nb-2026-07-10-task-shape-estimator|Build a task-shape estimator to route work to chat, single-agent, multi-agent, or human]] | @nb | `-` |
| 2026-07-10 | [[experiments/aie-2026-07-10-zl-continuum-review-layer|Define a per-task review tier (output / task-direction / loop-design) and enforce it before merging agent work]] | @aie | `-` |
| 2026-07-10 | [[experiments/aie-2026-07-10-agent-understanding-techniques|Have agents generate explainer docs, quizzes, and micro-world simulations after each large PR]] | @aie | `-` |
| 2026-07-09 | [[experiments/nh-2026-07-09-single-prompt-full-video-pipeline|Use a single vague prompt with delegation and verification instructions to drive a multi-tool agent pipeline]] | @nh | `-` |
| 2026-07-09 | [[experiments/do-2026-07-09-stop-prompting-start-loops|Run one high-focus task plus many background agent tasks in parallel]] | @do | `-` |
| 2026-07-09 | [[experiments/do-2026-07-09-embrace-slop-filter-signal|Generate 100 variants and apply judgment to select the best output]] | @do | `-` |
| 2026-07-09 | [[experiments/aie-2026-07-09-personal-brand-as-distribution-moat|Use AI to amplify an authentic personal brand signal rather than generate generic marketing content]] | @aie | `-` |
| 2026-07-09 | [[experiments/aie-2026-07-09-manager-agent-outer-loop|Promote a persistent manager agent to own the inner execution loop while the developer controls only the outer steering loop]] | @aie | `-` |
| 2026-07-09 | [[experiments/aie-2026-07-09-forward-deployed-mvp-in-days|Embed directly with end users for 2-3 days per week and build MVPs on-site in days rather than sprints]] | @aie | `-` |
| 2026-07-08 | [[experiments/nh-2026-07-08-single-goal-prompt-full-company|Use a file-based goal prompt with never-ask and multi-agent orchestration directives to build a full deliverable set autonomously]] | @nh | `-` |
| 2026-07-08 | [[experiments/nb-2026-07-08-multi-agent-swarm-qa-catch|Use a cheap-model swarm with a frontier orchestrator to auto-catch and rework agent failures]] | @nb | `-` |
| 2026-07-08 | [[experiments/nb-2026-07-08-agent-audition-tryout-task|Run a structured audition task before including a new model in a swarm]] | @nb | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-repl-tool-replaces-15-tools|Replace a large set of discrete agent tools with a single persistent-state REPL tool]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-markdown-cron-daily-planner-agent|Build a cron-driven agent that reads a markdown task file and generates a prioritized daily plan]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-key-art-anchor-game-generation|Anchor AI game generation to a single key art image to enforce visual and tonal coherence]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-hierarchical-agent-fleet-file-state|Externalize all agent state to disk files and use context reset instead of compaction to enable crash-resilient long-running agent fleets]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-harness-self-optimization|Add a self-optimization loop that rewrites agent prompts based on a measurable objective score]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-diff-sae-backdoor-detection|Detect backdoors in fine-tuned LLMs by training a sparse autoencoder on activation deltas between base and fine-tuned checkpoints]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-deterministic-verification-harness|Build a deterministic verification harness that fires via Claude hooks and retries on failure]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-chess-agent-tool-augmented-llm|Augment an LLM with domain-specific constraint tools to prevent hallucination in rule-bound domains]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-agent-search-query-training|Instruct agents to write retrieval queries as natural sentences rather than keyword strings]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-agent-feedback-loop-cli-tooling|Build a custom CLI tool that gives coding agents application-level feedback loops including screenshots, logs, and service restarts]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-adaptive-harness-emergence|Allow agent harness roles and tooling to emerge mid-run rather than being fully pre-defined]] | @aie | `-` |
| 2026-07-08 | [[experiments/aie-2026-07-08-acp-compatible-agent-live|Add ACP (Agent Client Protocol) support to a custom coding agent so it can run inside any ACP-compatible editor]] | @aie | `-` |
| 2026-07-07 | [[experiments/nh-2026-07-07-model-routing-table-agent-teams|Build an explicit model routing table for dynamic multi-agent workflows]] | @nh | `-` |
| 2026-07-07 | [[experiments/nh-2026-07-07-fable-mode-system-prompt-opus|Inject a 'Fable-mode' system prompt into Opus to replicate Fable-5 reasoning patterns]] | @nh | `-` |
| 2026-07-07 | [[experiments/do-2026-07-07-finetune-large-oss-models-cloud|Fine-tune a 1T-parameter OSS model via cloud GPU rental and deploy via API]] | @do | `-` |
| 2026-07-07 | [[experiments/aie-2026-07-07-swe-marathon-long-horizon-eval|Add multi-channel anti-cheat verification to long-horizon agent evals to prevent reward hacking]] | @aie | `-` |
| 2026-07-07 | [[experiments/aie-2026-07-07-radical-speed-month-vibe-coding-org|Run a time-boxed 'radical speed sprint' where non-engineers ship production code using AI tools]] | @aie | `-` |
| 2026-07-07 | [[experiments/aie-2026-07-07-adaptive-per-user-software-pipeline|Prototype a live-session code adaptation layer that modifies UI behavior per user context without a build step]] | @aie | `-` |
| 2026-07-06 | [[experiments/aie-2026-07-06-shrink-system-prompt-fable|Shrink the system prompt for newer Claude models and remove constraining examples]] | @aie | `-` |
| 2026-07-06 | [[experiments/aie-2026-07-06-capability-overhang-audit|Audit tasks the agent currently fails at by adding code-execution or tool access to expose capability overhang]] | @aie | `-` |
| 2026-07-05 | [[experiments/nb-2026-07-05-imagination-over-cheap-models|Designate frontier-model budget for exploratory 'imagination' tasks]] | @nb | `-` |
| 2026-07-05 | [[experiments/mk-2026-07-05-wargame-plans-with-frontier|Use frontier model to wargame agentic task plans before cheaper-model execution]] | @mk | `-` |
| 2026-07-05 | [[experiments/aie-2026-07-05-wound-click-transform-pitch|Apply wound/click/transformation framework to AI tool documentation and onboarding copy]] | @aie | `-` |
| 2026-07-05 | [[experiments/aie-2026-07-05-post-launch-agent-observability|Build a meta-harness that watches, scores, and auto-PRs fixes for production agent sessions]] | @aie | `-` |
| 2026-07-05 | [[experiments/aie-2026-07-05-mcp-store-distribution|Publish an MCP app with UI widgets to Claude and ChatGPT stores for dynamic discovery]] | @aie | `-` |
| 2026-07-05 | [[experiments/aie-2026-07-05-continual-learning-replayable-envs|Convert production failure logs into replayable learning environments before applying harness fixes]] | @aie | `-` |
| 2026-07-04 | [[experiments/nb-2026-07-04-claude4-short-prompt-hard-problems|Use short, high-context prompts on Claude 4 for hard open-ended problems]] | @nb | `-` |
| 2026-07-04 | [[experiments/nb-2026-07-04-claude4-goal-harness-for-codegen|Use Claude 4 to design a goal harness that guides a downstream coding model]] | @nb | `-` |
| 2026-07-03 | [[experiments/nh-2026-07-03-llm-wiki-fable-youtube-transcripts|Ingest YouTube transcripts into a Claude Code-maintained LLM wiki with backlink graph]] | @nh | `-` |
| 2026-07-03 | [[experiments/nh-2026-07-03-claude-code-row-skill-verification|Implement a ROW (Research → Outline → Write) skill file with mandatory verification step in Claude Code]] | @nh | `-` |
| 2026-07-03 | [[experiments/nb-2026-07-03-paperwork-agent-skeleton|Build a reusable 9-step agent skeleton for high-trust paperwork processing]] | @nb | `-` |
| 2026-07-03 | [[experiments/aie-2026-07-03-harness-engineering-dspy|Apply DSPy harness engineering to decouple task specification from model selection]] | @aie | `-` |
| 2026-07-03 | [[experiments/aie-2026-07-03-fable-agentic-traces-model-selection|Log agentic traces to real-world benchmark data for evidence-based model selection]] | @aie | `-` |
| 2026-07-02 | [[experiments/nb-2026-07-02-task-complexity-model-routing|Route tasks by complexity: cheap model for center-of-distribution work, frontier model for novel tasks]] | @nb | `-` |
| 2026-07-02 | [[experiments/nb-2026-07-02-model-resilience-harness-ownership|Own the routing harness so any single model going offline causes zero downtime]] | @nb | `-` |
| 2026-07-02 | [[experiments/nb-2026-07-02-context-war-harness-strategy|Reduce context-loading friction by pre-wiring relevant workspace context into agent sessions]] | @nb | `-` |
| 2026-07-02 | [[experiments/do-2026-07-02-open-source-model-self-hosting-resilience|Self-host a large open-source model as the unbannable execution backbone for business-critical pipelines]] | @do | `-` |
| 2026-07-02 | [[experiments/do-2026-07-02-frontier-orchestrator-cheap-actors|Use frontier model as orchestrator/planner and cheap open-source models as actor agents]] | @do | `-` |
| 2026-07-02 | [[experiments/aie-2026-07-02-ambient-ai-in-conversation|Build an ambient AI participant that captures decisions from live conversation without explicit prompts]] | @aie | `-` |
| 2026-07-01 | [[experiments/nh-2026-07-01-fable5-prompting-six-habits|Apply Fable 5-specific prompting rules to system prompts and skill files]] | @nh | `-` |
| 2026-07-01 | [[experiments/nb-2026-07-01-ai-memory-80pct-self-built|Bootstrap a personal AI memory stack by prompting an agent to build it]] | @nb | `-` |
| 2026-07-01 | [[experiments/aie-2026-07-01-software-factories-loop-stacking|Implement a Slack/paging human-in-the-loop interrupt for long-running agent jobs]] | @aie | `-` |
| 2026-06-30 | [[experiments/mk-2026-06-30-agentic-os-five-layers|Structure agent harnesses as five explicit layers with tracked rot-rates]] | @mk | `-` |
| 2026-06-30 | [[experiments/aij-2026-06-30-pre-tool-use-hook-pattern|Use pre-tool-use hooks to silently augment default agent tool calls with richer context]] | @aij | `-` |
| 2026-06-30 | [[experiments/aij-2026-06-30-codebase-memory-mcp-graph|Replace flat-file grep with codebase-memory MCP graph for agent context]] | @aij | `-` |
| 2026-06-30 | [[experiments/aie-2026-06-30-rl-agent-etl-remediation|Apply a reinforcement-learning agent to auto-detect and remediate ETL pipeline failures]] | @aie | `-` |
| 2026-06-29 | [[experiments/nh-2026-06-29-storm-skill-multi-perspective-research|Implement Stanford STORM skill with five specialist personas and a verification pass]] | @nh | `-` |
| 2026-06-29 | [[experiments/do-2026-06-29-hermes-mixture-of-agents|Configure Mixture-of-Agents preset in Hermes to surpass single-model quality]] | @do | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-voice-in-visuals-out-latency-architecture|Build a voice-in / visuals-out agent using a fast small model for real-time response with async handoff to a larger model]] | @aie | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-user-story-mapping-before-build|Require a user story map before any agent-assisted feature build to reduce wrong-thing velocity]] | @aie | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-slm-replace-llm-calls|Audit agent LLM calls and replace routine classification/summarization calls with on-device SLMs]] | @aie | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-skill-quality-checklist|Audit existing skills against a four-point checklist: trigger, structure, steering, pruning]] | @aie | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-simulation-driven-spec-for-distributed-agents|Use a deterministic simulation environment to let agents design distributed algorithms before implementing them]] | @aie | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-graph-based-cross-document-compliance|Replace document-level validation with graph-based cross-document entity correlation for anomaly detection]] | @aie | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-domain-specific-agent-hierarchy|Decompose a monolithic agent into a coordinator plus narrow domain-specific sub-agents with sandboxed file systems]] | @aie | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-deterministic-infra-agentic-control-plane|Add a policy validation gateway between agent proposal and tool execution to prevent runaway retry loops]] | @aie | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-agentic-engineer-spec-eval-loop|Implement an automated offline-online agent improvement loop: spec → build → eval → ship → diagnose → optimize]] | @aie | `-` |
| 2026-06-29 | [[experiments/aie-2026-06-29-agent-replayability-boundary-tracing|Instrument agent nodes with boundary-level trace capture to enable replay-based debugging and stubbed regression tests]] | @aie | `-` |
| 2026-06-28 | [[experiments/st-2026-06-28-agent-skills-reusable-instructions|Build agent skill folders with progressive disclosure to eliminate repetitive context setup]] | @st | `-` |
| 2026-06-28 | [[experiments/nb-2026-06-28-glm52-harness-last-mile|Audit task distribution to identify center-vs-edge work before model switching]] | @nb | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-turboquant-embedding-compression|Swap the retrieval layer in agent vector search to TurboQuant 3-4 bit embedding compression for 5x memory reduction]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-spec-driven-development|Implement spec-driven development with markdown requirements and design docs generated before any code is written]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-research-to-production-rpt|Require a Research Prototype Taxonomy document before any ML prototype enters the production mono-repo]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-openclaw-physical-ai-terminal|Build a dual-display ESP32 terminal as a dedicated offline AI interaction device]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-local-code-index-token-reduction|Insert a local hybrid-search code index between codebase and AI coding tools to cut input tokens]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-hybrid-rag-sql-rrf-telemetry|Pre-process documents into PostgreSQL with hybrid RRF search before LLM queries to avoid multimodal upload token tax]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-html-for-agent-graphics|Use HTML+CSS as the agent-native format for generating slide decks, documents, and visual artifacts instead of canvas-based tools]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-five-agent-token-optimisations|Apply five token-reduction techniques to agent loops: prompt caching, difficulty routing, tool-result offload, loop caps, and history trimming]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-extended-cache-augmented-generation|Distribute a rapidly-changing full-corpus across parallel CAG buckets with a supervisor model for global questions]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-docling-unstructured-document-processing|Use Docling for local, GPU-free conversion of PDFs and mixed documents to structured markdown before RAG ingestion]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-browser-agent-compressed-dom|Replace Full-DOM or Screenshot-Only Input with a Compressed Markdown Page Representation for Browser Agents]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-autonomous-engineering-org-maturity|Use a six-stage agent maturity model and AI champions program to accelerate org-wide adoption past stage 3]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-ai-system-design-framework|Apply a four-phase design framework (requirements → architecture → evaluation → optimisation) before writing any AI system code]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-agents-building-agents-live-trace-clustering|Cluster Live Agent Traces into Failure Reports and Auto-Fix with a Coding Agent]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-agents-building-agents-harness|Build a Golden Dataset + Eval Loop to Drive Agent Improvements]] | @aie | `-` |
| 2026-06-28 | [[experiments/aie-2026-06-28-agent-rx-outcome-informed-retrieval|Add outcome-weighted utility scoring to agent retrieval so memory relevance improves from past run success/failure signals]] | @aie | `-` |
| 2026-06-26 | [[experiments/nb-2026-06-26-open-engine-multi-ai-queue|Build a shared task queue so multiple AI agents hand off work with full context]] | @nb | `discard` |
| 2026-06-26 | [[experiments/do-2026-06-26-self-host-local-model-sovereignty|Set up a locally-hosted fallback model so the dev loop survives API access disruptions]] | @do | `discard` |
| 2026-06-26 | [[experiments/do-2026-06-26-private-inference-374m-tokens|Run private home inference at 374M tokens/month using compressed open-weight models for agentic workloads]] | @do | `discard` |
| 2026-06-26 | [[experiments/aie-2026-06-26-second-brain-ai-research-os|Build a wiki-generating memory layer between Obsidian/Readwise and coding agents to surface high-signal notes at task start]] | @aie | `discard` |
| 2026-06-26 | [[experiments/aie-2026-06-26-polygraph-cross-repo-agent-memory|Add a cross-repo session memory graph (Polygraph pattern) so agents reference past decisions without human re-explanation]] | @aie | `adopt` |
| 2026-06-26 | [[experiments/aie-2026-06-26-four-layer-prompt-stack|Replace monolithic system prompts with a four-layer assembled prompt stack (identity → conditions → voice → veto)]] | @aie | `adopt` |
| 2026-06-26 | [[experiments/aie-2026-06-26-effect-native-agent-loop|Replace LangGraph with a custom Effect-native agent loop for full observability and structured concurrency]] | @aie | `discard` |
| 2026-06-25 | [[experiments/nh-2026-06-25-claude-code-sycophancy-roast-council|Add a multi-persona 'Roast Council' prompt to stress-test ideas before building]] | @nh | `adopt` |
| 2026-06-25 | [[experiments/nh-2026-06-25-claude-code-subagent-parallel-goal|Use /goal + parallel sub-agents to produce a full launch plan in under an hour]] | @nh | `discard` |
| 2026-06-25 | [[experiments/mk-2026-06-25-claude-code-aws-bedrock-enterprise-stack|Deploy a multi-agent Claude platform inside AWS Bedrock with SOC2/HIPAA guardrails and kill switches]] | @mk | `discard` |
| 2026-06-25 | [[experiments/aie-2026-06-25-recursive-coding-agents-rlm|Apply Recursive Language Model (RLM) patterns to coding agents for reliable, large-scale refactors]] | @aie | `discard` |
| 2026-06-25 | [[experiments/aie-2026-06-25-production-evals-agentic-systems|Replace benchmark-only evals with a continuous production telemetry eval loop for agentic workflows]] | @aie | `adopt` |
| 2026-06-25 | [[experiments/aie-2026-06-25-miranda-hypothesis-persona-eval-humanist-loop|Add domain-expert-in-the-loop evaluation to any persona/character agent to detect anachronistic compositing]] | @aie | `discard` |
| 2026-06-25 | [[experiments/aie-2026-06-25-log-as-agent-identity|Redesign agent session storage as an append-only event log to enable resumable, portable agents]] | @aie | `adopt` |
| 2026-06-25 | [[experiments/aie-2026-06-25-build-systems-not-code-agent-design|Apply classical software engineering disciplines (decomposition, SoC, idempotency, threat modeling) explicitly when designing agents]] | @aie | `adopt` |
| 2026-06-24 | [[experiments/nb-2026-06-24-loop-of-loops-agent-architecture|Implement a Loop-of-Loops Agent Control Pattern]] | @nb | `adopt` |
| 2026-06-24 | [[experiments/aij-2026-06-24-playwright-ci-artifact-evidence-prs|Require Agents to Attach Playwright Video Evidence to Every PR]] | @aij | `adopt` |
| 2026-06-24 | [[experiments/aij-2026-06-24-crabbox-isolated-sandbox-testing|Use CrabBox to Give Each Parallel Agent Its Own Cloud Dev Sandbox]] | @aij | `discard` |
| 2026-06-23 | [[experiments/nh-2026-06-23-fugu-multi-model-orchestration|Benchmark Single-Model vs. Orchestrated Multi-Model API on Identical Task Suite]] | @nh | `adopt` |
| 2026-06-23 | [[experiments/nb-2026-06-23-big-task-delegation|Hand Off a Whole Consulting-Scale Task to a Frontier Model]] | @nb | `adopt` |
| 2026-06-22 | [[experiments/nh-2026-06-22-internal-ai-consultant-roadmap|Run a 4-step internal AI consultant playbook tied to measurable KPIs]] | @nh | `discard` |
| 2026-06-22 | [[experiments/mlops-2026-06-22-logs-only-observability|Replace metrics/traces with logs-only observability for agent pipelines]] | @mlops | `adopt` |
| 2026-06-22 | [[experiments/mlops-2026-06-22-genetic-pareto-agent-trajectories|Apply genetic Pareto sampling across parallel agent trajectories]] | @mlops | `discard` |
| 2026-06-21 | [[experiments/nb-2026-06-21-agent-owner-card|Create an Agent Owner Card for Every Production Agent]] | @nb | `adopt` |
| 2026-06-21 | [[experiments/nb-2026-06-21-agent-diet-review-loop|Implement a Scheduled Diet Audit for Agent Context Sources]] | @nb | `adopt` |
| 2026-06-21 | [[experiments/do-2026-06-21-obsidian-living-files-agent-context|Store Agent Context as Obsidian Markdown Vault for Living File Access]] | @do | `discard` |
| 2026-06-20 | [[experiments/nb-2026-06-20-voice-clone-consent-policy|Draft and enforce a pre-incident AI likeness and voice policy for team outputs]] | @nb | `discard` |
| 2026-06-20 | [[experiments/nb-2026-06-20-creator-trust-stack-disclosure|Implement a Creator Trust Stack metadata layer for AI-assisted outputs]] | @nb | `discard` |
| 2026-06-19 | [[experiments/nh-2026-06-19-glm52-claude-code-model-routing|Route Claude Code to open-source models via base URL override and per-directory settings.local.json]] | @nh | `discard` |
| 2026-06-19 | [[experiments/nh-2026-06-19-agent-loop-reason-act-observe|Build agent loops with explicit checkable goal, hard stop condition, and separate checker agent]] | @nh | `adopt` |
| 2026-06-19 | [[experiments/nb-2026-06-19-open-skills-portable-procedures|Structure agent procedures as scoped markdown skills with verification contracts]] | @nb | `adopt` |
| 2026-06-19 | [[experiments/mlops-2026-06-19-voice-agent-cascaded-hybrid-architecture|Use a foreground/background dual-model pattern for voice agents to balance latency and quality]] | @mlops | `discard` |
| 2026-06-19 | [[experiments/mlops-2026-06-19-autonomy-spectrum-enterprise-agents|Gate agent autonomy by reversibility and blast radius using a three-tier classification]] | @mlops | `adopt` |
| 2026-06-18 | [[experiments/nh-2026-06-18-context-window-dumb-zone-mitigation|Instrument Claude Code Sessions to Detect and Interrupt the 'Dumb Zone']] | @nh | `adopt` |
| 2026-06-18 | [[experiments/nh-2026-06-18-claude-code-director-mindset|Add 'Intent + Why' Preamble to Every Claude Code Task Spec]] | @nh | `adopt` |
| 2026-06-18 | [[experiments/do-2026-06-18-strategic-vs-tactical-programming-ai|Redesign Codebase Architecture Explicitly for Agent Readability (AX)]] | @do | `adopt` |
| 2026-06-18 | [[experiments/do-2026-06-18-blank-slate-agent-audit|Strip Agent Config to Zero and Rebuild Only What Is Missed]] | @do | `adopt` |
| 2026-06-18 | [[experiments/aij-2026-06-18-loop-engineering-harness|Implement a Loop-Engineer Harness with Domain Contracts and Artifact Logging]] | @aij | `adopt` |
| 2026-06-18 | [[experiments/aij-2026-06-18-agent-skill-context-management|Use Skills as Context-Efficient Capability Extensions Instead of Inline Prompts]] | @aij | `adopt` |
| 2026-06-18 | [[experiments/aie-2026-06-18-structured-prompt-versioning|Enforce Structured Commit Messages for Prompt Changes with Failure-Reason Traceability]] | @aie | `adopt` |
| 2026-06-18 | [[experiments/aie-2026-06-18-eval-first-production-ai|Define Business-Metric Evals and Growing Test Case Library Before Writing Agent Code]] | @aie | `adopt` |
| 2026-06-17 | [[experiments/nh-2026-06-17-five-level-second-brain|Map each knowledge folder to its minimum viable second-brain level]] | @nh | `adopt` |
| 2026-06-17 | [[experiments/nb-2026-06-17-prune-agent-tools-harness|Audit and prune agent tool sets to improve reliability]] | @nb | `adopt` |
| 2026-06-17 | [[experiments/nb-2026-06-17-harness-health-checklist|Implement a five-point harness health check for every production agent]] | @nb | `adopt` |
| 2026-06-17 | [[experiments/aie-2026-06-17-mcp-real-web-access|Replace default LLM web fetch with a proxy-backed MCP scraping tool and compare hallucination rate]] | @aie | `discard` |
| 2026-06-16 | [[experiments/eh-2026-06-16-webgl-morphing-sculpture|Build a Continuously Morphing WebGL Generative Sculpture]] | @eh | `adopt` |
| 2026-06-16 | [[experiments/eh-2026-06-16-threejs-living-symmetry|Implement a Procedural Symmetry Engine in Three.js]] | @eh | `adopt` |
| 2026-06-16 | [[experiments/aie-2026-06-16-diffusion-speedup-stack|Stack Quantization + Caching + Distillation to Approach Real-Time Diffusion]] | @aie | `discard` |
| 2026-06-15 | [[experiments/nh-2026-06-15-ai-person-workflow-automation|Automate one recurring weekly workflow end-to-end with Claude to establish measurable ROI baseline]] | @nh | `adopt` |
| 2026-06-15 | [[experiments/mlops-2026-06-15-multiplayer-ai-flocking|Design multi-agent workflows using flocking algorithm principles (local separation, distant attraction, alignment)]] | @mlops | `discard` |
| 2026-06-15 | [[experiments/mlops-2026-06-15-context-engineering-coding-agents|Run a timed coding agent challenge on a real domain dataset to benchmark context engineering strategies]] | @mlops | `adopt` |
| 2026-06-15 | [[experiments/do-2026-06-15-hermes-apify-mcp-scraping|Connect Hermes Agent to Apify MCP for unrestricted web scraping]] | @do | `discard` |
| 2026-06-15 | [[experiments/do-2026-06-15-fable-ban-local-model-fallback|Build a model-fallback routing layer to hedge against frontier model access bans]] | @do | `discard` |
| 2026-06-15 | [[experiments/aie-2026-06-15-double-iframe-csp-mcp-apps|Integrate a CSP inspector into MCP app development workflow to catch missing domain declarations before store submission]] | @aie | `discard` |
| 2026-06-14 | [[experiments/nb-2026-06-14-model-dependency-resilience|Build and warm-test a fallback model routing layer for critical workflows]] | @nb | `adopt` |
| 2026-06-14 | [[experiments/nb-2026-06-14-harness-ownership-audit|Audit your AI workflows to identify harness ownership vs vendor dependency]] | @nb | `adopt` |
| 2026-06-14 | [[experiments/mk-2026-06-14-mine-jsonl-fable-playbook|Mine Claude Code JSONL sessions to generate a model behavior playbook]] | @mk | `adopt` |
| 2026-06-14 | [[experiments/mk-2026-06-14-behavioral-diff-cross-model|Automate cross-model behavioral diff to quantify agent capability gaps]] | @mk | `adopt` |
| 2026-06-13 | [[experiments/eh-2026-06-13-interactive-geometry-watercolor-visualizer|Build an AI-generated interactive geometry visualizer with watercolor-style rendering]] | @eh | `adopt` |
| 2026-06-12 | [[experiments/nh-2026-06-12-head-of-ai-non-technical-path|Validate a Non-Technical AI Adoption Lead Role With Hands-On Claude Code Builds]] | @nh | `discard` |
| 2026-06-12 | [[experiments/nh-2026-06-12-claude-fable-one-prompt-video|Drive a Multi-Tool Media Pipeline From a Single /goal Prompt Using Claude Code]] | @nh | `discard` |
| 2026-06-12 | [[experiments/nb-2026-06-12-codex-permission-boundary-safety|Enforce Least-Privilege Boundaries on Codex Agent Sessions]] | @nb | `adopt` |
| 2026-06-12 | [[experiments/nb-2026-06-12-codex-chief-of-staff-loop|Structure Codex Tasks With Goal-Source-Standard-Permission-Proof Loops]] | @nb | `adopt` |
| 2026-06-12 | [[experiments/do-2026-06-12-pi-agent-skills-reuse|Build Pi Agent Skills as Reusable Prompt Modules for Repeated Workflows]] | @do | `discard` |
| 2026-06-12 | [[experiments/do-2026-06-12-pi-agent-minimal-harness|Swap Opinionated Agent Framework for Pi Agent's Minimal Harness]] | @do | `discard` |
| 2026-06-11 | [[experiments/up-2026-06-11-salesforce-agentic-soc-ai-constitution|Write an AI constitution document to codify agent behavior rules, primitives, and trust-earning criteria]] | @up | `adopt` |
| 2026-06-11 | [[experiments/st-2026-06-11-reusable-skills-business-automation|Build reusable Claude skill files for recurring business workflows]] | @st | `discard` |
| 2026-06-11 | [[experiments/st-2026-06-11-four-step-skill-building-framework|Use a four-step calendar-audit-to-skill pipeline to systematically delegate recurring tasks]] | @st | `discard` |
| 2026-06-11 | [[experiments/st-2026-06-11-ai-foundations-business-mental-model|Frame agent delegation as intern-coaching to improve prompt quality]] | @st | `discard` |
| 2026-06-11 | [[experiments/nh-2026-06-11-subagent-persona-parallel-review|Spin up parallel persona sub-agents to stress-test outputs from multiple stakeholder viewpoints]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-skills-as-reusable-recipes|Build a personal skill library as markdown recipes to replace repetitive prompts with slash commands]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-scoped-api-keys-permission-layer|Implement scoped API keys per integration to enforce a read-only permission layer for Claude Code connections]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-prompt-caching-session-preservation|Preserve prompt cache by avoiding model switches and idle gaps over 1 hour to cut token costs 10x]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-opus48-effort-levels-token-efficiency|Map personal pain points from Opus 4.7 to Opus 4.8 effort levels to find the cheapest effective setting]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-grill-me-context-extraction|Use a 'Grill Me' interrogation skill to extract tacit knowledge into reusable context docs before building]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-four-cs-ai-os-second-brain|Structure a Claude Code second brain using the four-Cs framework: Context, Connections, Capabilities, Cadence]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-fable5-model-tier-awareness|Audit workflows for Fable 5 upgrade window before June 22 paywall]] | @nh | `discard` |
| 2026-06-11 | [[experiments/nh-2026-06-11-dynamic-workflows-parallel-jobs|Run a dynamic workflow to audit all skills in parallel with cheap scoring agents feeding one synthesis agent]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-custom-subagent-markdown-files|Build reusable custom sub-agent files with YAML front-matter for repeatable specialist tasks]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-claudecode-vs-codex-task-routing|Route tasks between Claude Code and Codex based on creative vs execution phase to improve output quality]] | @nh | `adopt` |
| 2026-06-11 | [[experiments/nh-2026-06-11-aios-four-cs-framework|Structure an AI operating system around the Four Cs: Context, Connections, Capabilities, Cadence]] | @nh | `discard` |
| 2026-06-11 | [[experiments/nb-2026-06-11-token-burn-dashboard|Build a personal token-burn dashboard to surface AI usage habits and expand imagination]] | @nb | `adopt` |
| 2026-06-11 | [[experiments/nb-2026-06-11-slash-workflows-multi-agent-personal-productiv|Use /workflows (slash-workflows) to spawn multi-agent sub-task decomposition for complex research]] | @nb | `adopt` |
| 2026-06-11 | [[experiments/nb-2026-06-11-claude-md-context-file|Maintain a claude.md standing-context file to prevent context drift across sessions]] | @nb | `adopt` |
| 2026-06-11 | [[experiments/nb-2026-06-11-claude-cockpit-vs-codex-ops-desk|Map tasks to Claude (steering) vs Codex (dispatching) based on fuzziness]] | @nb | `adopt` |
| 2026-06-11 | [[experiments/mlops-2026-06-11-rocket-ride-gpu-aggregation|Use shared-inference model server to cut LLM inference costs via GPU aggregation]] | @mlops | `discard` |
| 2026-06-11 | [[experiments/mlops-2026-06-11-planning-doc-to-prevent-spaghetti-code|Front-load a full planning document to Claude before coding to prevent spaghetti code across sessions]] | @mlops | `adopt` |
| 2026-06-11 | [[experiments/mlops-2026-06-11-meta-multiagent-short-video-perceiver|Decompose content-understanding pipelines into specialized perceiver + attribution + decision agents with caching between stages]] | @mlops | `discard` |
| 2026-06-11 | [[experiments/mlops-2026-06-11-ifood-latency-goldilocks-recommender|Use LLM-as-judge on conversation logs to understand true user satisfaction beyond explicit ratings]] | @mlops | `adopt` |
| 2026-06-11 | [[experiments/mlops-2026-06-11-despegar-sofia-orchestration-layer|Keep an explicit orchestration layer (Chappie) above domain agents to prevent tool-routing failures as agent count grows]] | @mlops | `discard` |
| 2026-06-11 | [[experiments/mlops-2026-06-11-despegar-federated-agent-development|Let domain teams own and iterate their own agent flows on top of a central scaffold]] | @mlops | `discard` |
| 2026-06-11 | [[experiments/mlops-2026-06-11-agentic-soc-multi-agent-hunt|Build a human-in-the-loop multi-agent pipeline using existing SOAR integrations rather than replacing them]] | @mlops | `discard` |
| 2026-06-11 | [[experiments/mk-2026-06-11-slash-goal-agentic-os-maintenance|Use /goal with a rubric file to continuously self-optimize the agentic OS skill and rule set]] | @mk | `adopt` |
| 2026-06-11 | [[experiments/mk-2026-06-11-skill-quality-eight-tips|Audit skill library with eight quality heuristics and the Claude Code guide agent to eliminate dead weight]] | @mk | `adopt` |
| 2026-06-11 | [[experiments/mk-2026-06-11-six-dynamic-workflow-patterns|Apply the six Claude Code dynamic workflow patterns to match task structure to agent topology]] | @mk | `adopt` |
| 2026-06-11 | [[experiments/mk-2026-06-11-polyskill-cross-provider-adapter|Build a PolySkill universal adapter to convert skills bidirectionally between Claude Code and Codex]] | @mk | `adopt` |
| 2026-06-11 | [[experiments/mk-2026-06-11-fable5-tiered-effort-workflow|Route tasks across model tiers by complexity to minimize token burn]] | @mk | `adopt` |
| 2026-06-11 | [[experiments/mk-2026-06-11-dynamic-workflows-due-diligence|Use the 'build a workflow' keyword trigger to auto-generate multi-agent harnesses for large document analysis]] | @mk | `discard` |
| 2026-06-11 | [[experiments/mk-2026-06-11-dynamic-workflow-personal-model-migration|Mine local JSONL conversation history with a fan-out workflow to generate personalized model-upgrade guidance]] | @mk | `adopt` |
| 2026-06-11 | [[experiments/do-2026-06-11-minimax-m3-hermes-agent-cost-reduction|Power Hermes Agent with Minimax M3 to enable 24/7 always-on agentic loops at 10-20x lower cost than Opus]] | @do | `discard` |
| 2026-06-11 | [[experiments/do-2026-06-11-fable-cursor-agent-view-workflow|Run Claude Fable (Mythos 5) exclusively through Cursor agent view to avoid safeguard false-positives and leverage auto-fallback]] | @do | `discard` |
| 2026-06-11 | [[experiments/do-2026-06-11-codex-context-skills-magipath|Inject structured design context and skills into Codex to improve frontend output quality]] | @do | `adopt` |
| 2026-06-11 | [[experiments/do-2026-06-11-cmax-terminal-parallel-agents|Use CMAX terminal for managing parallel CLI agents with per-pane zoom, workspaces, and jump-to-unread notifications]] | @do | `discard` |
| 2026-06-11 | [[experiments/aij-2026-06-11-closed-loop-self-improving-agent|Implement a closed-loop agent with cron jobs, a temporal memory log, and auto-skill-proposal to create self-improving workflows]] | @aij | `adopt` |
| 2026-06-11 | [[experiments/aie-2026-06-11-webmcp-structured-site-tools|Expose site capabilities as Web MCP tools to replace brittle DOM-scraping agent flows]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-studio-nl-business-queries|Build an internal NL-to-SQL agent with persistent widget output for business queries]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-small-model-tool-use-rl-training|Fine-tune a small model on tool-use discipline with RL to match large-model performance on structured tasks]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-self-healing-scraper-pipeline-mcp|Use Bright Data MCP + LLM agent to auto-generate, execute, and self-heal web scrapers instead of calling LLM per page]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-runpod-serverless-llm-endpoint|Deploy a HuggingFace open-source LLM as a RunPod serverless endpoint from a preconfigured Hub listing in under 5 minutes]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-runpod-flash-sdk-local-gpu-iteration|Use RunPod Flash SDK decorator to deploy GPU inference functions from local dev environment without Docker build cycles]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-posthog-signal-to-pr-pipeline|Build a signal-ingestion-to-PR pipeline that converts product observability events into auto-generated code fixes]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-otel-agent-observability-flywheel|Instrument agent traces with OpenTelemetry auto-instrumentation then drive prompt/model experiments from the resulting dataset]] | @aie | `adopt` |
| 2026-06-11 | [[experiments/aie-2026-06-11-mcp-apps-rich-ui-in-chat|Return sandboxed interactive HTML iframes from MCP tool calls to replace text-only agent responses with rich UI]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-long-context-ulysses-upipe|Stack DeepSpeed Ulysses + gradient checkpointing + U-Pipe chunked-head recompute for long-context fine-tuning]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-gemma4-open-model-local-agentic|Replace a cloud-API agent step with a locally-hosted Gemma 4 31B model for data-sensitive sub-tasks]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-gemini-audio-rich-transcription|Use Gemini Flash audio API to extract structured metadata (speakers, timestamps, language, emotion) from meeting recordings in a single API call]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-evals-hill-climbing-zones|Implement a three-zone hill-climbing eval loop: fix obvious harness bugs, apply model-family-specific prompt tuning, then stop before overfitting]] | @aie | `adopt` |
| 2026-06-11 | [[experiments/aie-2026-06-11-eval-as-compute-primitive|Use Cloudflare Durable Objects as stateful, addressable compute units for long-running AI agents]] | @aie | `discard` |
| 2026-06-11 | [[experiments/aie-2026-06-11-context-optimization-strategies|Replace full-codebase context dumps with ranked hierarchical summaries and knowledge graphs for agentic code review]] | @aie | `adopt` |
| 2026-06-11 | [[experiments/aie-2026-06-11-async-agent-verification-loop|Give agents MCP access to the target environment so they can self-verify before surfacing results]] | @aie | `adopt` |
| 2026-06-11 | [[experiments/aie-2026-06-11-agentic-retrieval-over-simple-rag|Replace single-shot vector search with iterative agentic retrieval (search→read→assess→repeat) for agent context gathering]] | @aie | `adopt` |
| 2026-05-10 | [[experiments/aie-2026-05-10-vit-nas-deployment-flexibility|Use neural architecture search on a pretrained ViT backbone to generate a family of deployment-flexible vision models]] | @aie | `discard` |
| 2026-05-10 | [[experiments/aie-2026-05-10-semantic-vad-streaming-pipeline|Add semantic VAD to streaming STT→LLM→TTS pipeline to reduce perceived latency]] | @aie | `-` |
| 2026-05-10 | [[experiments/aie-2026-05-10-on-device-tts-cost-reduction|Replace cloud TTS with on-device CPU model to eliminate API costs]] | @aie | `-` |
| 2026-05-10 | [[experiments/aie-2026-05-10-flux-context-realtime-image-editing|Integrate Flux Context for sub-second in-loop image editing instead of generation-only models]] | @aie | `-` |
| 2026-05-10 | [[experiments/aie-2026-05-10-effect-workflows-long-running-ai|Use Effect Cluster workflows to guarantee completion of multi-step AI agent processes across server crashes]] | @aie | `-` |
| 2026-05-10 | [[experiments/aie-2026-05-10-effect-clone-repo-agent-context|Feed the full library repo as agent context instead of relying on training data or MCP docs]] | @aie | `adopt` |
| 2026-05-09 | [[experiments/nh-2026-05-09-most-powerful-tool-claude-code|Identify and integrate the highest-leverage MCP tool for Claude Code]] | @nh | `discard` |
| 2026-05-09 | [[experiments/nh-2026-05-09-codex-full-course|Run through Codex full-course to identify features absent from our current Claude Code workflow]] | @nh | `discard` |
| 2026-05-09 | [[experiments/nh-2026-05-09-claude-session-limits-solution|Use Claude's new session continuity mechanism to run long multi-step tasks]] | @nh | `discard` |
| 2026-05-09 | [[experiments/nh-2026-05-09-ai-tech-stack-copy|Adopt a curated minimal AI tech stack to reduce tool sprawl]] | @nh | `discard` |
| 2026-05-09 | [[experiments/nb-2026-05-09-semantic-work-primitive-product-test|Evaluate each tool/action in your agent for semantic meaning, not just access]] | @nb | `-` |
| 2026-05-09 | [[experiments/nb-2026-05-09-prompt-skill-plugin-mental-model|Audit workflows and classify each as prompt, skill, plugin, or MCP]] | @nb | `-` |
| 2026-05-09 | [[experiments/nb-2026-05-09-openclaw-swappable-model-memory|Decouple agent memory from the model so workflows survive model swaps]] | @nb | `-` |
| 2026-05-09 | [[experiments/nb-2026-05-09-mozilla-mythos-spec-legibility|Write spec files that are legible enough for AI security review]] | @nb | `-` |
| 2026-05-09 | [[experiments/nb-2026-05-09-deterministic-script-verification|Add deterministic verification scripts as post-agent hooks]] | @nb | `adopt` |
| 2026-05-09 | [[experiments/mlops-2026-05-09-sql-injection-ai-agents|Add input sanitization and query allowlisting to agent database tools]] | @mlops | `-` |
| 2026-05-09 | [[experiments/mlops-2026-05-09-fraud-models-vs-agents|Keep specialized ML models for high-stakes decisions; use agents only for orchestration]] | @mlops | `-` |
| 2026-05-09 | [[experiments/mlops-2026-05-09-agents-survive-production|Implement retry logic, state persistence, and failure observability in production agents]] | @mlops | `adopt` |
| 2026-05-09 | [[experiments/mk-2026-05-09-agentic-os-build|Design a personal agentic OS with layered memory, tools, and routing]] | @mk | `-` |
| 2026-05-09 | [[experiments/do-2026-05-09-hermes-agent-lessons|Apply condensed Hermes agent architecture lessons to reduce agent iteration time]] | @do | `discard` |
| 2026-05-09 | [[experiments/do-2026-05-09-codex-edit-anything|Use Codex computer-use editing for arbitrary file and UI modifications]] | @do | `-` |
| 2026-05-09 | [[experiments/aij-2026-05-09-goals-command-tips|Correctly structure /goals commands to improve agent task alignment]] | @aij | `discard` |
| 2026-05-09 | [[experiments/aie-2026-05-09-tts-models-like-llms|Evaluate LLM-style TTS models for voice output in agentic pipelines]] | @aie | `-` |
| 2026-05-09 | [[experiments/aie-2026-05-09-pydantic-agents-production-optimisation|Use Pydantic AI structured outputs to enforce agent response contracts in production]] | @aie | `adopt` |
| 2026-05-09 | [[experiments/aie-2026-05-09-multi-agent-architecture-factory|Adopt a task-decomposition multi-agent pattern for complex coding workflows]] | @aie | `discard` |
| 2026-05-09 | [[experiments/aie-2026-05-09-mcp-ui-extensions|Build MCP servers that expose UI components for human-in-the-loop agent steps]] | @aie | `-` |
| 2026-05-09 | [[experiments/aie-2026-05-09-elevenlabs-chat-agent-voice|Integrate ElevenLabs voice layer into a chat agent for real-time voice interaction]] | @aie | `discard` |
| 2026-05-09 | [[experiments/aie-2026-05-09-agentic-search-context-engineering|Replace static RAG retrieval with agentic search for dynamic context assembly]] | @aie | `-` |
| 2026-05-09 | [[experiments/aie-2026-05-09-agent-observability-raindrop|Add structured trace logging to agent runs for post-hoc debugging]] | @aie | `discard` |
| 2026-05-05 | [[experiments/nh-2026-05-05-higgsfield-claude-mcp-creative-agency|Connect Higgsfield MCP to Claude and Drive Full Brand Asset Generation from a Single Prompt]] | @nh | `discard` |
| 2026-05-05 | [[experiments/nb-2026-05-05-proactive-agent-load-test|Run 3-4 Agents in Parallel for a Month to Measure Proactivity Progress]] | @nb | `-` |
| 2026-05-04 | [[experiments/nh-2026-05-04-voice-agent-claude-code-elevenlabs|Build a Knowledge-Grounded Voice Agent via Claude Code and ElevenLabs in a Single Session]] | @nh | `discard` |
| 2026-05-04 | [[experiments/nb-2026-05-04-job-audit-four-buckets|Run a Four-Bucket Work Audit to Identify AI-Vulnerable Task Categories]] | @nb | `-` |
| 2026-05-04 | [[experiments/nb-2026-05-04-agentic-commerce-buyer-agent-readiness|Audit a Service or Tool for AI Agent Callability and Structured-Data Readiness]] | @nb | `-` |
| 2026-05-03 | [[experiments/st-2026-05-03-cowork-connectors-skills-setup|Configure Claude CoWork with project-scoped skills and scheduled tasks to replace recurring manual workflows]] | @st | `-` |
| 2026-05-03 | [[experiments/nh-2026-05-03-superpowers-plan-first-skill|Add Superpowers skill to enforce plan-then-test coding discipline in Claude Code]] | @nh | `adopt` |
| 2026-05-03 | [[experiments/nh-2026-05-03-claude-design-course|Apply structured Claude prompt design patterns to YOLO loop system prompts]] | @nh | `adopt` |
| 2026-05-03 | [[experiments/nh-2026-05-03-claude-code-skill-creator|Install Skill Creator globally to bootstrap all Claude Code skills via plain-English prompts]] | @nh | `adopt` |
| 2026-05-03 | [[experiments/nh-2026-05-03-claude-code-os-build-sell|Build a reusable Claude Code OS template with pre-wired tools, memory, and task scaffolding]] | @nh | `-` |
| 2026-05-03 | [[experiments/nb-2026-05-03-benchmark-hardware-local-ai|Benchmark Local AI Hardware Options for Dev Loop Inference]] | @nb | `-` |
| 2026-05-03 | [[experiments/mlops-2026-05-03-humans-out-of-way-agent-teams|Design a multi-agent pipeline that minimizes human checkpoints]] | @mlops | `-` |
| 2026-05-03 | [[experiments/mk-2026-05-03-hive-mind-multi-agent-os|Build a multi-agent hive-mind with shared memory database and Telegram interface over Claude Code]] | @mk | `discard` |
| 2026-05-03 | [[experiments/mk-2026-05-03-global-vs-project-skill-hygiene|Audit and promote skills to global vs. project scope as a prerequisite to multi-agent reliability]] | @mk | `adopt` |
| 2026-05-03 | [[experiments/do-2026-05-03-pi-agent-self-modifying|Implement a Self-Modifying Agent That Rewrites Its Own Prompts or Tools]] | @do | `discard` |
| 2026-05-03 | [[experiments/do-2026-05-03-hermes-agent-switch|Swap current agent framework for Hermes Agent and benchmark task completion]] | @do | `discard` |
| 2026-05-03 | [[experiments/aij-2026-05-03-openai-symphony-coding-paradigm|Prototype a Symphony-style multi-model coding orchestration layer]] | @aij | `discard` |
| 2026-05-02 | [[experiments/nb-2026-05-02-anthropic-atlassian-acquisition|Untitled]] | @nb | `-` |
| 2026-04-30 | [[experiments/nb-2026-04-30-microsoft-claude-vs-copilot|Benchmark Claude Against Your Primary Copilot on Internal Tasks]] | @nb | `discard` |
| 2026-04-29 | [[experiments/nb-2026-04-29-agent-crm-write-back|Instrument Agent Actions to Write Structured Logs Back to a Central Store]] | @nb | `-` |
| 2026-04-29 | [[experiments/nb-2026-04-29-agent-crm-browser-replacement|Replace Browser-Based CRM Lookups With Agent Tool Calls]] | @nb | `-` |
| 2026-04-28 | [[experiments/nb-2026-04-28-gpt55-vs-claude-vs-gemini-real-difference|Benchmark Model Routing by Task Class Across GPT-5.5, Claude, and Gemini]] | @nb | `-` |
| 2026-04-28 | [[experiments/nb-2026-04-28-apple-trillion-dollar-ai-position|SKIP - Pure News Commentary]] | @nb | `-` |
| 2026-04-28 | [[experiments/mk-2026-04-28-claude-codex-plan-together|Orchestrate Claude as Planner and Codex as Executor in a Two-Agent Dev Pipeline]] | @mk | `-` |
| 2026-04-28 | [[experiments/do-2026-04-28-self-evolving-ai-agent|Implement a Self-Modifying Agent Loop That Rewrites Its Own Prompts or Tools]] | @do | `-` |
| 2026-04-28 | [[experiments/do-2026-04-28-self-evolving-agent-eval-harness|Build a Lightweight Eval Harness That Scores Agent Runs and Feeds Results Back as Context]] | @do | `-` |
| 2026-04-27 | [[experiments/nh-2026-04-27-claude-code-headless-automation|Run Claude Code in Headless Mode as a Scriptable YOLO Loop Step]] | @nh | `-` |
| 2026-04-27 | [[experiments/nh-2026-04-27-claude-code-hacks|Adopt a Structured CLAUDE.md + Slash Command Library for YOLO Loop Sessions]] | @nh | `-` |
| 2026-04-27 | [[experiments/nb-2026-04-27-openai-free-employee-catch|Integrate OpenAI Responses API Agent as a Background Dev Task Runner]] | @nb | `-` |
| 2026-04-27 | [[experiments/mlops-2026-04-27-agents-software-dev-cloud|Move YOLO Loop Execution Environment to Ephemeral Cloud Sandboxes]] | @mlops | `-` |
| 2026-04-27 | [[experiments/mlops-2026-04-27-agent-observability-cloud|Add Structured Observability Logging to Every YOLO Loop Agent Step]] | @mlops | `-` |
| 2026-04-26 | [[experiments/mk-2026-04-26-run-claude-codex-together|Run Claude and Codex in Parallel on the Same Codebase]] | @mk | `-` |
| 2026-04-25 | [[experiments/nh-2026-04-25-claude-code-playwright-automation|Wire Claude Code to Playwright for End-to-End Test Authoring and Execution]] | @nh | `-` |
| 2026-04-25 | [[experiments/nb-2026-04-25-chatgpt-images-replace-team|Replace Asset Pipeline Steps with ChatGPT Image Generation]] | @nb | `-` |
| 2026-04-25 | [[experiments/do-2026-04-25-gpt55-mythos-killer|Benchmark GPT-5.5 Against Current Loop Model on Code + Reasoning Tasks]] | @do | `discard` |
| 2026-04-24 | [[experiments/nb-2026-04-24-claude-design-sprint|Replace UI/UX Sprint Cycles with Claude-Driven Design Sessions]] | @nb | `-` |
| 2026-04-24 | [[experiments/mlops-2026-04-24-openxdata-conference|Audit Dev Loop for Open Data Pipeline Integration Points]] | @mlops | `-` |
| 2026-04-24 | [[experiments/do-2026-04-24-gpt-images-native-gen|Integrate GPT Native Image Generation into Asset Pipeline]] | @do | `-` |
| 2026-04-24 | [[experiments/do-2026-04-24-deepseek-v4-benchmark|Benchmark DeepSeek V4 Against Current Loop Models on Code Gen Tasks]] | @do | `-` |
| 2026-04-23 | [[experiments/up-2026-04-23-llm-safety-mechanisms|Audit YOLO loop outputs for safety mechanism degradation after fine-tuning or prompt chaining]] | @up | `-` |
| 2026-04-23 | [[experiments/up-2026-04-23-confidential-ai-tee|Evaluate Trusted Execution Environment (TEE) deployment for YOLO loop inference on sensitive data]] | @up | `-` |
| 2026-04-23 | [[experiments/up-2026-04-23-beyond-chatbot-agents|Architect a persistent-state agent layer above the YOLO loop's stateless inference calls]] | @up | `-` |
| 2026-04-23 | [[experiments/nh-2026-04-23-gpt55-vs-opus47|Benchmark GPT-5.5 vs Claude Opus 4.7 on YOLO loop coding tasks]] | @nh | `discard` |
| 2026-04-23 | [[experiments/nh-2026-04-23-claude-video-editing|Use Claude as an agentic video editing orchestrator via tool calls]] | @nh | `-` |
| 2026-04-23 | [[experiments/nb-2026-04-23-codex-no-api|Replace REST API layer with Codex-driven direct task execution]] | @nb | `discard` |
| 2026-04-22 | [[experiments/nh-2026-04-22-openai-image2-use-cases|Integrate OpenAI Image 2 as a UI Mockup Generator in the Dev Loop]] | @nh | `-` |
| 2026-04-22 | [[experiments/nb-2026-04-22-wiki-vs-openbrain-reliability|Stress-Test Knowledge Retrieval Under Load Conditions]] | @nb | `-` |
| 2026-04-22 | [[experiments/nb-2026-04-22-opus-47-prompt-behavior-shift|Audit Existing Prompts Against Opus 4.7 Behavioral Changes]] | @nb | `discard` |
| 2026-04-22 | [[experiments/nb-2026-04-22-claude-code-memory-patterns|Implement Structured CLAUDE.md Memory Layering for the YOLO Loop]] | @nb | `adopt` |
| 2026-04-22 | [[experiments/mlops-2026-04-22-evals-still-matter-2026|Implement a Minimal Persistent Eval Harness for the YOLO Loop]] | @mlops | `discard` |
| 2026-04-22 | [[experiments/aij-2026-04-22-self-evolving-agent|Add a Self-Reflection Step That Rewrites the Agent's Own System Prompt]] | @aij | `discard` |
| 2026-04-21 | [[experiments/nh-2026-04-21-claude-design-prompt-structure|Develop a reusable design-intent prompt template for Claude UI generation]] | @nh | `-` |
| 2026-04-21 | [[experiments/nh-2026-04-21-claude-3d-website-design|Use Claude as a 3D UI code generator for rapid front-end prototyping]] | @nh | `discard` |
| 2026-04-20 | [[experiments/nh-2026-04-20-claude-session-limit|Implement context compression and session checkpointing to bypass Claude usage limits]] | @nh | `adopt` |
| 2026-04-20 | [[experiments/mlops-2026-04-20-tensorrt-llm-latency|Optimize LLM inference with TensorRT to cut response latency]] | @mlops | `-` |
| 2026-04-20 | [[experiments/mlops-2026-04-20-new-kind-of-marketplace|Expose YOLO loop capabilities as composable marketplace primitives]] | @mlops | `discard` |
| 2026-04-20 | [[experiments/mlops-2026-04-20-modern-software-engineer|Restructure dev workflow around AI-assisted code generation with human review gates]] | @mlops | `adopt` |
| 2026-04-20 | [[experiments/do-2026-04-20-hermes-agent|Integrate Hermes agent framework as the orchestration layer inside the YOLO loop]] | @do | `-` |
| 2026-04-19 | [[experiments/nh-2026-04-19-claude-video-editing|Use Claude to Generate Video Edit Instructions From Transcript]] | @nh | `-` |
| 2026-04-19 | [[experiments/nh-2026-04-19-claude-design-unstoppable|Use Claude to Iterate on UI/UX Designs From Text Prompts]] | @nh | `-` |
| 2026-04-19 | [[experiments/nh-2026-04-19-claude-24-7-trader|Build a Long-Running Claude Agent With Persistent Decision Loop]] | @nh | `discard` |
| 2026-04-19 | [[experiments/nb-2026-04-19-karpathy-700-experiments|Run Overnight Autonomous Experiment Sweeps With an Agent]] | @nb | `adopt` |
| 2026-04-19 | [[experiments/nb-2026-04-19-ai-replaced-managers|Replace Coordination Layer With AI Orchestration]] | @nb | `discard` |
| 2026-04-19 | [[experiments/mk-2026-04-19-claude-design-industry|Pipe Design Briefs Into Claude to Generate Production-Ready Component Specs]] | @mk | `-` |
| 2026-04-17 | [[experiments/nb-2026-04-17-memory-control-layer|Build a User-Controlled Memory Layer Between LLM and Platform]] | @nb | `-` |
| 2026-04-16 | [[experiments/nh-2026-04-16-claude-heygen-content-pipeline|Pipe Claude Script Output Directly Into HeyGen Avatar API for Automated Video Generation]] | @nh | `-` |
| 2026-04-16 | [[experiments/nh-2026-04-16-claude-code-routines-scheduler|Implement Claude Code Routines for Scheduled Autonomous Dev Tasks]] | @nh | `-` |
| 2026-04-16 | [[experiments/nb-2026-04-16-fix-bottleneck-not-ai-speed|Map and Eliminate the Non-AI Bottleneck in Your Dev Loop]] | @nb | `adopt` |
| 2026-04-16 | [[experiments/nb-2026-04-16-agent-failure-mode-audit|Build a Failure-Mode Audit Layer Into Every Agent Pipeline]] | @nb | `adopt` |
| 2026-04-16 | [[experiments/mk-2026-04-16-replace-openclaw-hermes-claude-code|Consolidate Multi-Tool Agent Stacks Into a Single Claude Code Configuration]] | @mk | `discard` |
| 2026-04-16 | [[experiments/do-2026-04-16-claude-code-opus-47-agent|Run Claude Code with Opus 4.7 as Primary Coding Agent and Benchmark Against Sonnet]] | @do | `adopt` |
| 2026-04-14 | [[experiments/nb-2026-04-14-track-model-drops-against-product-viability|Build a model-release impact tracker that flags capability obsolescence risks]] | @nb | `-` |
| 2026-04-13 | [[experiments/nh-2026-04-13-claude-code-vs-antigravity-benchmark|Run a structured 100-task head-to-head between Claude Code and a challenger tool]] | @nh | `-` |
| 2026-04-13 | [[experiments/nb-2026-04-13-amazon-ai-code-quality-audit|Audit AI-generated code for systemic failure patterns]] | @nb | `adopt` |
| 2026-04-13 | [[experiments/do-2026-04-13-claude-swift-rork-mobile|Use Rork as a Claude-powered mobile prototyping layer]] | @do | `-` |
| 2026-04-12 | [[experiments/st-2026-04-12-claude-video-editing|Build a Claude-Driven Video Edit Instruction Pipeline]] | @st | `discard` |
| 2026-04-12 | [[experiments/st-2026-04-12-claude-style-guide-prompt|Encode a YOLO Loop Style Guide as a Reusable Claude System Prompt]] | @st | `adopt` |
| 2026-04-12 | [[experiments/nh-2026-04-12-claude-code-plugin-10x|Integrate the Featured Plugin into Claude Code Workflow]] | @nh | `-` |
| 2026-04-12 | [[experiments/nb-2026-04-12-manager-layoff-wall|SKIP — Pure commentary, no actionable experiment]] | @nb | `-` |
| 2026-04-12 | [[experiments/nb-2026-04-12-ipo-trap-commentary|Untitled]] | @nb | `-` |
| 2026-04-12 | [[experiments/do-2026-04-12-codex-zero-to-deployed|Build and Deploy a Full App Using OpenAI Codex End-to-End]] | @do | `discard` |
| 2026-04-11 | [[experiments/nh-2026-04-11-seedance-claude-code-websites|Pipe Seedance 2.0 video output into Claude Code to auto-generate animated website assets]] | @nh | `-` |
| 2026-04-11 | [[experiments/nb-2026-04-11-google-quantization-inference|Benchmark Google's new quantization scheme against existing INT4/INT8 baselines on local model inference]] | @nb | `-` |
| 2026-04-10 | [[experiments/nh-2026-04-10-claude-stop-using-best-model|Benchmark Claude Haiku or Sonnet against Opus on YOLO Loop tasks and measure cost-quality tradeoff]] | @nh | `adopt` |
| 2026-04-10 | [[experiments/nb-2026-04-10-five-safe-places-ai|Audit current build position against the 5 safe AI niches framework]] | @nb | `adopt` |
| 2026-04-10 | [[experiments/mlops-2026-04-10-ship-agents-track2|Extract and benchmark agent deployment patterns from Ship Agents conference talks]] | @mlops | `-` |
| 2026-04-10 | [[experiments/mlops-2026-04-10-production-subagents-reward-modeling|Use a judge sub-agent to automate reward signal generation during RLHF or DPO runs]] | @mlops | `discard` |
| 2026-04-10 | [[experiments/mlops-2026-04-10-production-subagents-llm-posttraining|Wire sub-agents into the LLM post-training pipeline for automated data curation and eval]] | @mlops | `discard` |
| 2026-04-10 | [[experiments/mlops-2026-04-10-gpu-starvation-distributed-training|Implement GPU starvation detection and mitigation in distributed training pipeline]] | @mlops | `discard` |
| 2026-04-09 | [[experiments/nh-2026-04-09-openclaw-trading-agent|Deploy a Live-Capital Agentic Trading Loop and Instrument Its Decision Trail]] | @nh | `discard` |
| 2026-04-09 | [[experiments/nh-2026-04-09-claude-managed-agents|Benchmark Claude Managed Agents Against Manual Orchestration on a Multi-Step Dev Task]] | @nh | `adopt` |
| 2026-04-08 | [[experiments/nh-2026-04-08-claude-internet-tool-integration|Integrate Claude's New Web-Native Capabilities as a Live-Data Tool in the YOLO Loop]] | @nh | `discard` |
| 2026-04-08 | [[experiments/nb-2026-04-08-analyze-leaked-code-patterns|Mine AI Tool Source Code for Architectural Patterns to Adopt Early]] | @nb | `-` |
| 2026-04-08 | [[experiments/do-2026-04-08-claude-mythos-agentic-eval|Benchmark Claude Mythos on Open-Ended Agentic Tasks in the YOLO Loop]] | @do | `adopt` |
| 2026-04-07 | [[experiments/nh-2026-04-07-ollama-claude-code-cost-reduction|Route Low-Stakes Claude Code Subtasks to Local Ollama Models to Cut Loop Cost]] | @nh | `discard` |
| 2026-04-07 | [[experiments/nh-2026-04-07-claude-code-planning-mode|Use Claude Code's New Planning Mode as a Spec-Decomposition Pre-Pass]] | @nh | `adopt` |
| 2026-04-07 | [[experiments/nb-2026-04-07-polymarket-bot-disruption-audit|Map Your Dev Loop Steps Against Automation Displacement Risk]] | @nb | `-` |
| 2026-04-07 | [[experiments/nb-2026-04-07-ephemeral-layers-stack-audit|Classify Each YOLO Loop Dependency by Shelf-Life and Replaceability]] | @nb | `adopt` |
| 2026-04-07 | [[experiments/mlops-2026-04-07-agents-summit-evals-patterns|Implement a Lightweight Agent Eval Harness Drawn from Summit Patterns]] | @mlops | `discard` |
| 2026-04-07 | [[experiments/do-2026-04-07-minimal-agent-pattern|Build a Bare-Metal Minimal Agent Loop with No Framework Dependencies]] | @do | `adopt` |
| 2026-04-05 | [[experiments/st-2026-04-05-skill-creator-meta-agent|Build a skill-creator meta-agent that writes SKILL.md files from successful interactions]] | @st | `adopt` |
| 2026-04-05 | [[experiments/nh-2026-04-05-karpathy-llm-wiki-hot-cache|Implement Karpathy hot-cache pattern for instant agent context recovery]] | @nh | `adopt` |
| 2026-04-05 | [[experiments/nb-2026-04-05-independent-observability|Build independent observability that never trusts agent self-reporting]] | @nb | `adopt` |
| 2026-04-05 | [[experiments/nb-2026-04-05-evaluative-agents-review-bottleneck|Deploy evaluative agents alongside generative agents to eliminate review bottleneck]] | @nb | `adopt` |
| 2026-04-04 | [[experiments/nb-2026-04-04-compounding-agent-memory|Implement compounding agent memory that improves with each build]] | @nb | `adopt` |
| 2026-04-04 | [[experiments/nb-2026-04-04-agent-recipe-presets|Create pre-wired agent recipes instead of blank-canvas prompting]] | @nb | `adopt` |
| 2026-04-02 | [[experiments/nh-2026-04-03-ollama-claude-code-cost|Use Ollama local models for Claude Code's routine sub-tasks to cut costs]] | @nh | `discard` |
| 2026-04-02 | [[experiments/nh-2026-04-02-compact-at-milestones|Apply /compact at defined YOLO session milestones to preserve context within token limits]] | @nh | `adopt` |
| 2026-04-02 | [[experiments/nb-2026-04-03-agent-guardrails-leak|Add explicit guardrail and fallback layers to autonomous build agents]] | @nb | `adopt` |
| 2026-04-02 | [[experiments/nb-2026-04-03-agent-architecture-12-pieces|Audit PAI agent stack against the 12 critical agent architecture pieces]] | @nb | `adopt` |
| 2026-04-02 | [[experiments/nb-2026-04-02-session-isolation-per-task|Use task-isolated fresh Claude sessions to prevent context bloat]] | @nb | `discard` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-self-learning-feedback-loop|Add automatic post-build reflection that writes back to agent memory]] | @mlops | `adopt` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-self-learning-agent-memory|Implement structured memory retrieval so the build agent learns from past builds]] | @mlops | `adopt` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-mcp-day2-integrations|Evaluate Docker and Datadog MCP servers for agent-driven DevOps]] | @mlops | `-` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-coding-agent-multiverse|Benchmark multiple coding agents on the same YOLO build spec]] | @mlops | `-` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-beyond-swebench-evals|Build custom evals that measure real YOLO build quality beyond synthetic benchmarks]] | @mlops | `adopt` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-ai-code-security|Add security scanning to the YOLO build pipeline for AI-generated code]] | @mlops | `adopt` |
| 2026-04-02 | [[experiments/mlops-2026-04-02-mcp-spec-roadmap|Track the Anthropic MCP technical roadmap and adopt spec updates proactively]] | @mlops | `adopt` |
| 2026-04-02 | [[experiments/fs-2026-04-02-pretext-text-measurement|Use Pretext library for instant text measurement without DOM reflows]] | @fs | `adopt` |
| 2026-04-02 | [[experiments/fs-2026-04-02-junie-cli-multi-model|Evaluate Junie CLI multi-model routing for harness-cli council]] | @fs | `adopt` |
| 2026-04-02 | [[experiments/do-2026-04-03-gemma4-local-review|Evaluate Gemma 4 as a local code review model to reduce API costs]] | @do | `discard` |
| 2026-04-01 | [[experiments/tmp-2026-04-01-quantized-local-inference|Prototype a YOLO project using local quantized LLM inference via Ollama]] | @tmp | `discard` |
| 2026-04-01 | [[experiments/nh-2026-04-01-claude-md-optimization|Optimize CLAUDE.md as short opinionated onboarding doc + configure wildcard permissions]] | @nh | `discard` |
| 2026-04-01 | [[experiments/nb-2026-04-01-model-upgrade-stack-audit|Run a 4-layer stack audit before every major Claude model upgrade]] | @nb | `adopt` |
| 2026-04-01 | [[experiments/mlops-2026-04-01-continuous-model-eval|Build a golden-prompt eval suite to detect model regression after upgrades]] | @mlops | `adopt` |
| 2026-03-31 | [[experiments/up-2026-03-31-personal-ai-infrastructure|Build a Council skill for multi-perspective task review]] | @up | `adopt` |
| 2026-03-31 | [[experiments/nh-2026-03-31-paperclip-agent-org|Use Paperclip's company-layer to orchestrate multi-agent Claude Code builds]] | @nh | `discard` |
| 2026-03-31 | [[experiments/nb-2026-03-31-skill-composability|Design skill outputs as composable handoffs]] | @nb | `adopt` |
| 2026-03-31 | [[experiments/nb-2026-03-31-agent-readable-skills|Restructure program.md as agent-readable skill files]] | @nb | `adopt` |
| 2026-03-31 | [[experiments/mlops-2026-04-01-coding-agent-evals|Build a golden dataset of past bugs as an eval suite]] | @mlops | `adopt` |
| 2026-03-31 | [[experiments/mlops-2026-04-01-agent-orchestration-cloud|Run parallel agent sessions for independent YOLO tasks]] | @mlops | `adopt` |
| 2026-03-31 | [[experiments/mlops-2026-03-31-agent-debug-logging|Add structured debug logging at agent decision points to speed up failure diagnosis]] | @mlops | `adopt` |
| 2026-03-31 | [[experiments/do-2026-03-31-autoresearch-loop|Implement autoresearch loop for YOLO project optimization]] | @do | `adopt` |
| 2026-03-30 | [[experiments/nh-2026-03-30-codex-plan-claude-execute|Adopt Codex-as-planner + Claude Code-as-executor 3-phase build cycle]] | @nh | `adopt` |
| 2026-03-29 | [[experiments/nh-2026-03-29-boring-automation-products|Filter YOLO Tick ideas through the 'boring-but-high-ROI' automation criteria]] | @nh | `adopt` |
| 2026-03-29 | [[experiments/nb-2026-03-29-scheduled-tasks-monitoring|Use Claude Scheduled Tasks for automated recurring work]] | @nb | `discard` |
| 2026-03-29 | [[experiments/nb-2026-03-29-close-the-loops|Adopt the 'close the loops' delegation framework]] | @nb | `adopt` |
| 2026-03-29 | [[experiments/do-2026-03-29-self-improving-eval-loop|Wire a self-critique step into the YOLO build loop before running external tests]] | @do | `adopt` |
| 2026-03-28 | [[experiments/nb-2026-03-28-mcp-tool-integration|Use MCP to connect build agents to professional tools]] | @nb | `adopt` |
| 2026-03-28 | [[experiments/nb-2026-03-28-design-md-agent-readable|Create a design.md as an agent-readable design system]] | @nb | `adopt` |
| 2026-03-27 | [[experiments/mlops-2026-03-27-trust-ladder-adoption|Apply the trust ladder to increase agent autonomy incrementally]] | @mlops | `discard` |
| 2026-03-27 | [[experiments/mlops-2026-03-27-specialized-agent-team|Use specialized agent roles instead of one monolithic agent]] | @mlops | `discard` |
| 2026-03-27 | [[experiments/do-2026-03-27-private-local-agent|Run YOLO builds via a 100% local AI agent stack]] | @do | `discard` |
| 2026-03-25 | [[experiments/nb-2026-03-25-dark-factory-pattern|Adopt the Dark Factory pattern for autonomous builds]] | @nb | `adopt` |
| 2026-03-25 | [[experiments/nb-2026-03-25-auto-research-metric-optimization|Apply Auto Research pattern to optimize Gemini review scores]] | @nb | `discard` |
| 2026-03-25 | [[experiments/mlops-2026-03-25-qrspi-vertical-planning|Adopt vertical planning with structure outlines before coding]] | @mlops | `adopt` |
| 2026-03-24 | [[experiments/nb-2026-03-24-strict-linting-agents|Apply strict linting to all agent-generated code]] | @nb | `adopt` |
| 2026-03-24 | [[experiments/nb-2026-03-24-context-compression|Use incremental summarization for context compression in long sessions]] | @nb | `adopt` |
| 2026-03-24 | [[experiments/nb-2026-03-24-agent-readiness-checklist|Build an Agent Readiness checklist for the YOLO codebase]] | @nb | `discard` |
| 2026-03-17 | [[experiments/mlops-2026-03-17-durable-execution-agents|Evaluate durable execution for long-running agent workflows]] | @mlops | `adopt` |

---

## Related pages

- [[yolo-projects]] - upstream pipeline
- [[yolo-phase4-integration]] - sync mechanism
- [[tracked-channels-schema]] - the 10 source channels
- [[index]] - wiki home
