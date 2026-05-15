# Experiments Index

> Back to [[index]]

**179 experiments** synthesized from the [[yolo-projects]] Phase 4 YouTube research pipeline, covering AI/dev content from 10 tracked channels.

This page is regenerated automatically by `scripts/ingest-yolo-phase4.py` on every sync. See [[yolo-phase4-integration]] for the full flow.

---

## By status

| Status | Count |
|---|---|
| `deferred` | 56 |
| `done` | 44 |
| `discarded` | 36 |
| `adopted` | 17 |
| `backlog` | 12 |
| `in_progress` | 10 |
| `skipped` | 4 |

## By verdict

| Verdict | Count |
|---|---|
| `(none)` | 82 |
| `adopt` | 51 |
| `discard` | 46 |

## By channel

| Channel | Experiments |
|---|---|
| @NateBJones | 54 |
| @NateHerk | 38 |
| @MLOps | 31 |
| @DavidOndrej | 19 |
| @aiDotEngineer | 13 |
| @Mark_Kashef | 8 |
| @[un]prompted | 4 |
| @ShawTalebi | 4 |
| @AIJasonZ | 3 |
| @Fireship | 2 |
| @Nate Herk | 2 |
| @TwoMinutePapers | 1 |

---

## All experiments

Ordered by published date, most recent first.

| Date | Title | Channel | Verdict |
|---|---|---|---|
| 2026-05-10 | [[experiments/aie-2026-05-10-vit-nas-deployment-flexibility|Use neural architecture search on a pretrained ViT backbone to generate a family of deployment-flexible vision models]] | @aiDotEngineer | `discard` |
| 2026-05-10 | [[experiments/aie-2026-05-10-semantic-vad-streaming-pipeline|Add semantic VAD to streaming STT→LLM→TTS pipeline to reduce perceived latency]] | @aiDotEngineer | `-` |
| 2026-05-10 | [[experiments/aie-2026-05-10-on-device-tts-cost-reduction|Replace cloud TTS with on-device CPU model to eliminate API costs]] | @aiDotEngineer | `-` |
| 2026-05-10 | [[experiments/aie-2026-05-10-flux-context-realtime-image-editing|Integrate Flux Context for sub-second in-loop image editing instead of generation-only models]] | @aiDotEngineer | `-` |
| 2026-05-10 | [[experiments/aie-2026-05-10-effect-workflows-long-running-ai|Use Effect Cluster workflows to guarantee completion of multi-step AI agent processes across server crashes]] | @aiDotEngineer | `-` |
| 2026-05-10 | [[experiments/aie-2026-05-10-effect-clone-repo-agent-context|Feed the full library repo as agent context instead of relying on training data or MCP docs]] | @aiDotEngineer | `-` |
| 2026-05-09 | [[experiments/nh-2026-05-09-most-powerful-tool-claude-code|Identify and integrate the highest-leverage MCP tool for Claude Code]] | @NateHerk | `discard` |
| 2026-05-09 | [[experiments/nh-2026-05-09-codex-full-course|Run through Codex full-course to identify features absent from our current Claude Code workflow]] | @NateHerk | `discard` |
| 2026-05-09 | [[experiments/nh-2026-05-09-claude-session-limits-solution|Use Claude's new session continuity mechanism to run long multi-step tasks]] | @NateHerk | `discard` |
| 2026-05-09 | [[experiments/nh-2026-05-09-ai-tech-stack-copy|Adopt a curated minimal AI tech stack to reduce tool sprawl]] | @NateHerk | `discard` |
| 2026-05-09 | [[experiments/nb-2026-05-09-semantic-work-primitive-product-test|Evaluate each tool/action in your agent for semantic meaning, not just access]] | @NateBJones | `-` |
| 2026-05-09 | [[experiments/nb-2026-05-09-prompt-skill-plugin-mental-model|Audit workflows and classify each as prompt, skill, plugin, or MCP]] | @NateBJones | `-` |
| 2026-05-09 | [[experiments/nb-2026-05-09-openclaw-swappable-model-memory|Decouple agent memory from the model so workflows survive model swaps]] | @NateBJones | `-` |
| 2026-05-09 | [[experiments/nb-2026-05-09-mozilla-mythos-spec-legibility|Write spec files that are legible enough for AI security review]] | @NateBJones | `-` |
| 2026-05-09 | [[experiments/nb-2026-05-09-deterministic-script-verification|Add deterministic verification scripts as post-agent hooks]] | @NateBJones | `-` |
| 2026-05-09 | [[experiments/mlops-2026-05-09-sql-injection-ai-agents|Add input sanitization and query allowlisting to agent database tools]] | @MLOps | `-` |
| 2026-05-09 | [[experiments/mlops-2026-05-09-fraud-models-vs-agents|Keep specialized ML models for high-stakes decisions; use agents only for orchestration]] | @MLOps | `-` |
| 2026-05-09 | [[experiments/mlops-2026-05-09-agents-survive-production|Implement retry logic, state persistence, and failure observability in production agents]] | @MLOps | `-` |
| 2026-05-09 | [[experiments/mk-2026-05-09-agentic-os-build|Design a personal agentic OS with layered memory, tools, and routing]] | @Mark_Kashef | `-` |
| 2026-05-09 | [[experiments/do-2026-05-09-hermes-agent-lessons|Apply condensed Hermes agent architecture lessons to reduce agent iteration time]] | @DavidOndrej | `discard` |
| 2026-05-09 | [[experiments/do-2026-05-09-codex-edit-anything|Use Codex computer-use editing for arbitrary file and UI modifications]] | @DavidOndrej | `-` |
| 2026-05-09 | [[experiments/aij-2026-05-09-goals-command-tips|Correctly structure /goals commands to improve agent task alignment]] | @AIJasonZ | `discard` |
| 2026-05-09 | [[experiments/aie-2026-05-09-tts-models-like-llms|Evaluate LLM-style TTS models for voice output in agentic pipelines]] | @aiDotEngineer | `-` |
| 2026-05-09 | [[experiments/aie-2026-05-09-pydantic-agents-production-optimisation|Use Pydantic AI structured outputs to enforce agent response contracts in production]] | @aiDotEngineer | `-` |
| 2026-05-09 | [[experiments/aie-2026-05-09-multi-agent-architecture-factory|Adopt a task-decomposition multi-agent pattern for complex coding workflows]] | @aiDotEngineer | `discard` |
| 2026-05-09 | [[experiments/aie-2026-05-09-mcp-ui-extensions|Build MCP servers that expose UI components for human-in-the-loop agent steps]] | @aiDotEngineer | `-` |
| 2026-05-09 | [[experiments/aie-2026-05-09-elevenlabs-chat-agent-voice|Integrate ElevenLabs voice layer into a chat agent for real-time voice interaction]] | @aiDotEngineer | `discard` |
| 2026-05-09 | [[experiments/aie-2026-05-09-agentic-search-context-engineering|Replace static RAG retrieval with agentic search for dynamic context assembly]] | @aiDotEngineer | `-` |
| 2026-05-09 | [[experiments/aie-2026-05-09-agent-observability-raindrop|Add structured trace logging to agent runs for post-hoc debugging]] | @aiDotEngineer | `discard` |
| 2026-05-05 | [[experiments/nh-2026-05-05-higgsfield-claude-mcp-creative-agency|Connect Higgsfield MCP to Claude and Drive Full Brand Asset Generation from a Single Prompt]] | @NateHerk | `-` |
| 2026-05-05 | [[experiments/nb-2026-05-05-proactive-agent-load-test|Run 3-4 Agents in Parallel for a Month to Measure Proactivity Progress]] | @NateBJones | `-` |
| 2026-05-04 | [[experiments/nh-2026-05-04-voice-agent-claude-code-elevenlabs|Build a Knowledge-Grounded Voice Agent via Claude Code and ElevenLabs in a Single Session]] | @NateHerk | `-` |
| 2026-05-04 | [[experiments/nb-2026-05-04-job-audit-four-buckets|Run a Four-Bucket Work Audit to Identify AI-Vulnerable Task Categories]] | @NateBJones | `-` |
| 2026-05-04 | [[experiments/nb-2026-05-04-agentic-commerce-buyer-agent-readiness|Audit a Service or Tool for AI Agent Callability and Structured-Data Readiness]] | @NateBJones | `-` |
| 2026-05-03 | [[experiments/st-2026-05-03-cowork-connectors-skills-setup|Configure Claude CoWork with project-scoped skills and scheduled tasks to replace recurring manual workflows]] | @ShawTalebi | `-` |
| 2026-05-03 | [[experiments/nh-2026-05-03-superpowers-plan-first-skill|Add Superpowers skill to enforce plan-then-test coding discipline in Claude Code]] | @NateHerk | `-` |
| 2026-05-03 | [[experiments/nh-2026-05-03-claude-design-course|Apply structured Claude prompt design patterns to YOLO loop system prompts]] | @NateHerk | `-` |
| 2026-05-03 | [[experiments/nh-2026-05-03-claude-code-skill-creator|Install Skill Creator globally to bootstrap all Claude Code skills via plain-English prompts]] | @NateHerk | `-` |
| 2026-05-03 | [[experiments/nh-2026-05-03-claude-code-os-build-sell|Build a reusable Claude Code OS template with pre-wired tools, memory, and task scaffolding]] | @NateHerk | `-` |
| 2026-05-03 | [[experiments/nb-2026-05-03-benchmark-hardware-local-ai|Benchmark Local AI Hardware Options for Dev Loop Inference]] | @NateBJones | `-` |
| 2026-05-03 | [[experiments/mlops-2026-05-03-humans-out-of-way-agent-teams|Design a multi-agent pipeline that minimizes human checkpoints]] | @MLOps | `-` |
| 2026-05-03 | [[experiments/mk-2026-05-03-hive-mind-multi-agent-os|Build a multi-agent hive-mind with shared memory database and Telegram interface over Claude Code]] | @Mark_Kashef | `-` |
| 2026-05-03 | [[experiments/mk-2026-05-03-global-vs-project-skill-hygiene|Audit and promote skills to global vs. project scope as a prerequisite to multi-agent reliability]] | @Mark_Kashef | `-` |
| 2026-05-03 | [[experiments/do-2026-05-03-pi-agent-self-modifying|Implement a Self-Modifying Agent That Rewrites Its Own Prompts or Tools]] | @DavidOndrej | `discard` |
| 2026-05-03 | [[experiments/do-2026-05-03-hermes-agent-switch|Swap current agent framework for Hermes Agent and benchmark task completion]] | @DavidOndrej | `discard` |
| 2026-05-03 | [[experiments/aij-2026-05-03-openai-symphony-coding-paradigm|Prototype a Symphony-style multi-model coding orchestration layer]] | @AIJasonZ | `discard` |
| 2026-05-02 | [[experiments/nb-2026-05-02-anthropic-atlassian-acquisition|Untitled]] | @NateBJones | `-` |
| 2026-04-30 | [[experiments/nb-2026-04-30-microsoft-claude-vs-copilot|Benchmark Claude Against Your Primary Copilot on Internal Tasks]] | @NateBJones | `discard` |
| 2026-04-29 | [[experiments/nb-2026-04-29-agent-crm-write-back|Instrument Agent Actions to Write Structured Logs Back to a Central Store]] | @NateBJones | `-` |
| 2026-04-29 | [[experiments/nb-2026-04-29-agent-crm-browser-replacement|Replace Browser-Based CRM Lookups With Agent Tool Calls]] | @NateBJones | `-` |
| 2026-04-28 | [[experiments/nb-2026-04-28-gpt55-vs-claude-vs-gemini-real-difference|Benchmark Model Routing by Task Class Across GPT-5.5, Claude, and Gemini]] | @NateBJones | `-` |
| 2026-04-28 | [[experiments/nb-2026-04-28-apple-trillion-dollar-ai-position|SKIP - Pure News Commentary]] | @NateBJones | `-` |
| 2026-04-28 | [[experiments/mk-2026-04-28-claude-codex-plan-together|Orchestrate Claude as Planner and Codex as Executor in a Two-Agent Dev Pipeline]] | @Mark_Kashef | `-` |
| 2026-04-28 | [[experiments/do-2026-04-28-self-evolving-ai-agent|Implement a Self-Modifying Agent Loop That Rewrites Its Own Prompts or Tools]] | @DavidOndrej | `-` |
| 2026-04-28 | [[experiments/do-2026-04-28-self-evolving-agent-eval-harness|Build a Lightweight Eval Harness That Scores Agent Runs and Feeds Results Back as Context]] | @DavidOndrej | `-` |
| 2026-04-27 | [[experiments/nh-2026-04-27-claude-code-headless-automation|Run Claude Code in Headless Mode as a Scriptable YOLO Loop Step]] | @NateHerk | `-` |
| 2026-04-27 | [[experiments/nh-2026-04-27-claude-code-hacks|Adopt a Structured CLAUDE.md + Slash Command Library for YOLO Loop Sessions]] | @NateHerk | `-` |
| 2026-04-27 | [[experiments/nb-2026-04-27-openai-free-employee-catch|Integrate OpenAI Responses API Agent as a Background Dev Task Runner]] | @NateBJones | `-` |
| 2026-04-27 | [[experiments/mlops-2026-04-27-agents-software-dev-cloud|Move YOLO Loop Execution Environment to Ephemeral Cloud Sandboxes]] | @MLOps | `-` |
| 2026-04-27 | [[experiments/mlops-2026-04-27-agent-observability-cloud|Add Structured Observability Logging to Every YOLO Loop Agent Step]] | @MLOps | `-` |
| 2026-04-26 | [[experiments/mk-2026-04-26-run-claude-codex-together|Run Claude and Codex in Parallel on the Same Codebase]] | @Mark_Kashef | `-` |
| 2026-04-25 | [[experiments/nh-2026-04-25-claude-code-playwright-automation|Wire Claude Code to Playwright for End-to-End Test Authoring and Execution]] | @NateHerk | `-` |
| 2026-04-25 | [[experiments/nb-2026-04-25-chatgpt-images-replace-team|Replace Asset Pipeline Steps with ChatGPT Image Generation]] | @NateBJones | `-` |
| 2026-04-25 | [[experiments/do-2026-04-25-gpt55-mythos-killer|Benchmark GPT-5.5 Against Current Loop Model on Code + Reasoning Tasks]] | @DavidOndrej | `discard` |
| 2026-04-24 | [[experiments/nb-2026-04-24-claude-design-sprint|Replace UI/UX Sprint Cycles with Claude-Driven Design Sessions]] | @NateBJones | `-` |
| 2026-04-24 | [[experiments/mlops-2026-04-24-openxdata-conference|Audit Dev Loop for Open Data Pipeline Integration Points]] | @MLOps | `-` |
| 2026-04-24 | [[experiments/do-2026-04-24-gpt-images-native-gen|Integrate GPT Native Image Generation into Asset Pipeline]] | @DavidOndrej | `-` |
| 2026-04-24 | [[experiments/do-2026-04-24-deepseek-v4-benchmark|Benchmark DeepSeek V4 Against Current Loop Models on Code Gen Tasks]] | @DavidOndrej | `-` |
| 2026-04-23 | [[experiments/up-2026-04-23-llm-safety-mechanisms|Audit YOLO loop outputs for safety mechanism degradation after fine-tuning or prompt chaining]] | @[un]prompted | `-` |
| 2026-04-23 | [[experiments/up-2026-04-23-confidential-ai-tee|Evaluate Trusted Execution Environment (TEE) deployment for YOLO loop inference on sensitive data]] | @[un]prompted | `-` |
| 2026-04-23 | [[experiments/up-2026-04-23-beyond-chatbot-agents|Architect a persistent-state agent layer above the YOLO loop's stateless inference calls]] | @[un]prompted | `-` |
| 2026-04-23 | [[experiments/nh-2026-04-23-gpt55-vs-opus47|Benchmark GPT-5.5 vs Claude Opus 4.7 on YOLO loop coding tasks]] | @NateHerk | `discard` |
| 2026-04-23 | [[experiments/nh-2026-04-23-claude-video-editing|Use Claude as an agentic video editing orchestrator via tool calls]] | @NateHerk | `-` |
| 2026-04-23 | [[experiments/nb-2026-04-23-codex-no-api|Replace REST API layer with Codex-driven direct task execution]] | @NateBJones | `discard` |
| 2026-04-22 | [[experiments/nh-2026-04-22-openai-image2-use-cases|Integrate OpenAI Image 2 as a UI Mockup Generator in the Dev Loop]] | @NateHerk | `-` |
| 2026-04-22 | [[experiments/nb-2026-04-22-wiki-vs-openbrain-reliability|Stress-Test Knowledge Retrieval Under Load Conditions]] | @NateBJones | `-` |
| 2026-04-22 | [[experiments/nb-2026-04-22-opus-47-prompt-behavior-shift|Audit Existing Prompts Against Opus 4.7 Behavioral Changes]] | @NateBJones | `discard` |
| 2026-04-22 | [[experiments/nb-2026-04-22-claude-code-memory-patterns|Implement Structured CLAUDE.md Memory Layering for the YOLO Loop]] | @Mark_Kashef | `-` |
| 2026-04-22 | [[experiments/mlops-2026-04-22-evals-still-matter-2026|Implement a Minimal Persistent Eval Harness for the YOLO Loop]] | @MLOps | `discard` |
| 2026-04-22 | [[experiments/aij-2026-04-22-self-evolving-agent|Add a Self-Reflection Step That Rewrites the Agent's Own System Prompt]] | @AIJasonZ | `discard` |
| 2026-04-21 | [[experiments/nh-2026-04-21-claude-design-prompt-structure|Develop a reusable design-intent prompt template for Claude UI generation]] | @Nate Herk | `-` |
| 2026-04-21 | [[experiments/nh-2026-04-21-claude-3d-website-design|Use Claude as a 3D UI code generator for rapid front-end prototyping]] | @Nate Herk | `discard` |
| 2026-04-20 | [[experiments/nh-2026-04-20-claude-session-limit|Implement context compression and session checkpointing to bypass Claude usage limits]] | @NateHerk | `adopt` |
| 2026-04-20 | [[experiments/mlops-2026-04-20-tensorrt-llm-latency|Optimize LLM inference with TensorRT to cut response latency]] | @MLOps | `-` |
| 2026-04-20 | [[experiments/mlops-2026-04-20-new-kind-of-marketplace|Expose YOLO loop capabilities as composable marketplace primitives]] | @MLOps | `discard` |
| 2026-04-20 | [[experiments/mlops-2026-04-20-modern-software-engineer|Restructure dev workflow around AI-assisted code generation with human review gates]] | @MLOps | `adopt` |
| 2026-04-20 | [[experiments/do-2026-04-20-hermes-agent|Integrate Hermes agent framework as the orchestration layer inside the YOLO loop]] | @DavidOndrej | `-` |
| 2026-04-19 | [[experiments/nh-2026-04-19-claude-video-editing|Use Claude to Generate Video Edit Instructions From Transcript]] | @NateHerk | `-` |
| 2026-04-19 | [[experiments/nh-2026-04-19-claude-design-unstoppable|Use Claude to Iterate on UI/UX Designs From Text Prompts]] | @NateHerk | `-` |
| 2026-04-19 | [[experiments/nh-2026-04-19-claude-24-7-trader|Build a Long-Running Claude Agent With Persistent Decision Loop]] | @NateHerk | `discard` |
| 2026-04-19 | [[experiments/nb-2026-04-19-karpathy-700-experiments|Run Overnight Autonomous Experiment Sweeps With an Agent]] | @NateBJones | `adopt` |
| 2026-04-19 | [[experiments/nb-2026-04-19-ai-replaced-managers|Replace Coordination Layer With AI Orchestration]] | @NateBJones | `discard` |
| 2026-04-19 | [[experiments/mk-2026-04-19-claude-design-industry|Pipe Design Briefs Into Claude to Generate Production-Ready Component Specs]] | @Mark_Kashef | `-` |
| 2026-04-17 | [[experiments/nb-2026-04-17-memory-control-layer|Build a User-Controlled Memory Layer Between LLM and Platform]] | @NateBJones | `-` |
| 2026-04-16 | [[experiments/nh-2026-04-16-claude-heygen-content-pipeline|Pipe Claude Script Output Directly Into HeyGen Avatar API for Automated Video Generation]] | @NateHerk | `-` |
| 2026-04-16 | [[experiments/nh-2026-04-16-claude-code-routines-scheduler|Implement Claude Code Routines for Scheduled Autonomous Dev Tasks]] | @NateHerk | `-` |
| 2026-04-16 | [[experiments/nb-2026-04-16-fix-bottleneck-not-ai-speed|Map and Eliminate the Non-AI Bottleneck in Your Dev Loop]] | @NateBJones | `adopt` |
| 2026-04-16 | [[experiments/nb-2026-04-16-agent-failure-mode-audit|Build a Failure-Mode Audit Layer Into Every Agent Pipeline]] | @NateBJones | `adopt` |
| 2026-04-16 | [[experiments/mk-2026-04-16-replace-openclaw-hermes-claude-code|Consolidate Multi-Tool Agent Stacks Into a Single Claude Code Configuration]] | @Mark_Kashef | `discard` |
| 2026-04-16 | [[experiments/do-2026-04-16-claude-code-opus-47-agent|Run Claude Code with Opus 4.7 as Primary Coding Agent and Benchmark Against Sonnet]] | @DavidOndrej | `adopt` |
| 2026-04-14 | [[experiments/nb-2026-04-14-track-model-drops-against-product-viability|Build a model-release impact tracker that flags capability obsolescence risks]] | @NateBJones | `-` |
| 2026-04-13 | [[experiments/nh-2026-04-13-claude-code-vs-antigravity-benchmark|Run a structured 100-task head-to-head between Claude Code and a challenger tool]] | @NateHerk | `-` |
| 2026-04-13 | [[experiments/nb-2026-04-13-amazon-ai-code-quality-audit|Audit AI-generated code for systemic failure patterns]] | @NateBJones | `adopt` |
| 2026-04-13 | [[experiments/do-2026-04-13-claude-swift-rork-mobile|Use Rork as a Claude-powered mobile prototyping layer]] | @DavidOndrej | `-` |
| 2026-04-12 | [[experiments/st-2026-04-12-claude-video-editing|Build a Claude-Driven Video Edit Instruction Pipeline]] | @ShawTalebi | `discard` |
| 2026-04-12 | [[experiments/st-2026-04-12-claude-style-guide-prompt|Encode a YOLO Loop Style Guide as a Reusable Claude System Prompt]] | @ShawTalebi | `adopt` |
| 2026-04-12 | [[experiments/nh-2026-04-12-claude-code-plugin-10x|Integrate the Featured Plugin into Claude Code Workflow]] | @NateHerk | `-` |
| 2026-04-12 | [[experiments/nb-2026-04-12-manager-layoff-wall|SKIP — Pure commentary, no actionable experiment]] | @NateBJones | `-` |
| 2026-04-12 | [[experiments/nb-2026-04-12-ipo-trap-commentary|Untitled]] | @NateBJones | `-` |
| 2026-04-12 | [[experiments/do-2026-04-12-codex-zero-to-deployed|Build and Deploy a Full App Using OpenAI Codex End-to-End]] | @DavidOndrej | `discard` |
| 2026-04-11 | [[experiments/nh-2026-04-11-seedance-claude-code-websites|Pipe Seedance 2.0 video output into Claude Code to auto-generate animated website assets]] | @NateHerk | `-` |
| 2026-04-11 | [[experiments/nb-2026-04-11-google-quantization-inference|Benchmark Google's new quantization scheme against existing INT4/INT8 baselines on local model inference]] | @NateBJones | `-` |
| 2026-04-10 | [[experiments/nh-2026-04-10-claude-stop-using-best-model|Benchmark Claude Haiku or Sonnet against Opus on YOLO Loop tasks and measure cost-quality tradeoff]] | @NateHerk | `adopt` |
| 2026-04-10 | [[experiments/nb-2026-04-10-five-safe-places-ai|Audit current build position against the 5 safe AI niches framework]] | @NateBJones | `adopt` |
| 2026-04-10 | [[experiments/mlops-2026-04-10-ship-agents-track2|Extract and benchmark agent deployment patterns from Ship Agents conference talks]] | @MLOps | `-` |
| 2026-04-10 | [[experiments/mlops-2026-04-10-production-subagents-reward-modeling|Use a judge sub-agent to automate reward signal generation during RLHF or DPO runs]] | @MLOps | `discard` |
| 2026-04-10 | [[experiments/mlops-2026-04-10-production-subagents-llm-posttraining|Wire sub-agents into the LLM post-training pipeline for automated data curation and eval]] | @MLOps | `discard` |
| 2026-04-10 | [[experiments/mlops-2026-04-10-gpu-starvation-distributed-training|Implement GPU starvation detection and mitigation in distributed training pipeline]] | @MLOps | `discard` |
| 2026-04-09 | [[experiments/nh-2026-04-09-openclaw-trading-agent|Deploy a Live-Capital Agentic Trading Loop and Instrument Its Decision Trail]] | @NateHerk | `discard` |
| 2026-04-09 | [[experiments/nh-2026-04-09-claude-managed-agents|Benchmark Claude Managed Agents Against Manual Orchestration on a Multi-Step Dev Task]] | @NateHerk | `adopt` |
| 2026-04-08 | [[experiments/nh-2026-04-08-claude-internet-tool-integration|Integrate Claude's New Web-Native Capabilities as a Live-Data Tool in the YOLO Loop]] | @NateHerk | `discard` |
| 2026-04-08 | [[experiments/nb-2026-04-08-analyze-leaked-code-patterns|Mine AI Tool Source Code for Architectural Patterns to Adopt Early]] | @NateBJones | `-` |
| 2026-04-08 | [[experiments/do-2026-04-08-claude-mythos-agentic-eval|Benchmark Claude Mythos on Open-Ended Agentic Tasks in the YOLO Loop]] | @DavidOndrej | `adopt` |
| 2026-04-07 | [[experiments/nh-2026-04-07-ollama-claude-code-cost-reduction|Route Low-Stakes Claude Code Subtasks to Local Ollama Models to Cut Loop Cost]] | @NateHerk | `discard` |
| 2026-04-07 | [[experiments/nh-2026-04-07-claude-code-planning-mode|Use Claude Code's New Planning Mode as a Spec-Decomposition Pre-Pass]] | @NateHerk | `adopt` |
| 2026-04-07 | [[experiments/nb-2026-04-07-polymarket-bot-disruption-audit|Map Your Dev Loop Steps Against Automation Displacement Risk]] | @NateBJones | `-` |
| 2026-04-07 | [[experiments/nb-2026-04-07-ephemeral-layers-stack-audit|Classify Each YOLO Loop Dependency by Shelf-Life and Replaceability]] | @NateBJones | `adopt` |
| 2026-04-07 | [[experiments/mlops-2026-04-07-agents-summit-evals-patterns|Implement a Lightweight Agent Eval Harness Drawn from Summit Patterns]] | @MLOps | `discard` |
| 2026-04-07 | [[experiments/do-2026-04-07-minimal-agent-pattern|Build a Bare-Metal Minimal Agent Loop with No Framework Dependencies]] | @DavidOndrej | `adopt` |
| 2026-04-05 | [[experiments/st-2026-04-05-skill-creator-meta-agent|Build a skill-creator meta-agent that writes SKILL.md files from successful interactions]] | @ShawTalebi | `adopt` |
| 2026-04-05 | [[experiments/nh-2026-04-05-karpathy-llm-wiki-hot-cache|Implement Karpathy hot-cache pattern for instant agent context recovery]] | @NateHerk | `adopt` |
| 2026-04-05 | [[experiments/nb-2026-04-05-independent-observability|Build independent observability that never trusts agent self-reporting]] | @NateBJones | `adopt` |
| 2026-04-05 | [[experiments/nb-2026-04-05-evaluative-agents-review-bottleneck|Deploy evaluative agents alongside generative agents to eliminate review bottleneck]] | @NateBJones | `adopt` |
| 2026-04-04 | [[experiments/nb-2026-04-04-compounding-agent-memory|Implement compounding agent memory that improves with each build]] | @NateBJones | `adopt` |
| 2026-04-04 | [[experiments/nb-2026-04-04-agent-recipe-presets|Create pre-wired agent recipes instead of blank-canvas prompting]] | @NateBJones | `adopt` |
| 2026-04-02 | [[experiments/nh-2026-04-03-ollama-claude-code-cost|Use Ollama local models for Claude Code's routine sub-tasks to cut costs]] | @NateHerk | `discard` |
| 2026-04-02 | [[experiments/nh-2026-04-02-compact-at-milestones|Apply /compact at defined YOLO session milestones to preserve context within token limits]] | @NateHerk | `adopt` |
| 2026-04-02 | [[experiments/nb-2026-04-03-agent-guardrails-leak|Add explicit guardrail and fallback layers to autonomous build agents]] | @NateBJones | `adopt` |
| 2026-04-02 | [[experiments/nb-2026-04-03-agent-architecture-12-pieces|Audit PAI agent stack against the 12 critical agent architecture pieces]] | @NateBJones | `adopt` |
| 2026-04-02 | [[experiments/nb-2026-04-02-session-isolation-per-task|Use task-isolated fresh Claude sessions to prevent context bloat]] | @NateBJones | `discard` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-self-learning-feedback-loop|Add automatic post-build reflection that writes back to agent memory]] | @MLOps | `adopt` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-self-learning-agent-memory|Implement structured memory retrieval so the build agent learns from past builds]] | @MLOps | `adopt` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-mcp-day2-integrations|Evaluate Docker and Datadog MCP servers for agent-driven DevOps]] | @MLOps | `-` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-coding-agent-multiverse|Benchmark multiple coding agents on the same YOLO build spec]] | @MLOps | `-` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-beyond-swebench-evals|Build custom evals that measure real YOLO build quality beyond synthetic benchmarks]] | @MLOps | `adopt` |
| 2026-04-02 | [[experiments/mlops-2026-04-03-ai-code-security|Add security scanning to the YOLO build pipeline for AI-generated code]] | @MLOps | `adopt` |
| 2026-04-02 | [[experiments/mlops-2026-04-02-mcp-spec-roadmap|Track the Anthropic MCP technical roadmap and adopt spec updates proactively]] | @MLOps | `adopt` |
| 2026-04-02 | [[experiments/fs-2026-04-02-pretext-text-measurement|Use Pretext library for instant text measurement without DOM reflows]] | @Fireship | `adopt` |
| 2026-04-02 | [[experiments/fs-2026-04-02-junie-cli-multi-model|Evaluate Junie CLI multi-model routing for harness-cli council]] | @Fireship | `adopt` |
| 2026-04-02 | [[experiments/do-2026-04-03-gemma4-local-review|Evaluate Gemma 4 as a local code review model to reduce API costs]] | @DavidOndrej | `discard` |
| 2026-04-01 | [[experiments/tmp-2026-04-01-quantized-local-inference|Prototype a YOLO project using local quantized LLM inference via Ollama]] | @TwoMinutePapers | `discard` |
| 2026-04-01 | [[experiments/nh-2026-04-01-claude-md-optimization|Optimize CLAUDE.md as short opinionated onboarding doc + configure wildcard permissions]] | @NateHerk | `discard` |
| 2026-04-01 | [[experiments/nb-2026-04-01-model-upgrade-stack-audit|Run a 4-layer stack audit before every major Claude model upgrade]] | @NateBJones | `adopt` |
| 2026-04-01 | [[experiments/mlops-2026-04-01-continuous-model-eval|Build a golden-prompt eval suite to detect model regression after upgrades]] | @MLOps | `adopt` |
| 2026-03-31 | [[experiments/up-2026-03-31-personal-ai-infrastructure|Build a Council skill for multi-perspective task review]] | @[un]prompted | `adopt` |
| 2026-03-31 | [[experiments/nh-2026-03-31-paperclip-agent-org|Use Paperclip's company-layer to orchestrate multi-agent Claude Code builds]] | @NateHerk | `discard` |
| 2026-03-31 | [[experiments/nb-2026-03-31-skill-composability|Design skill outputs as composable handoffs]] | @NateBJones | `adopt` |
| 2026-03-31 | [[experiments/nb-2026-03-31-agent-readable-skills|Restructure program.md as agent-readable skill files]] | @NateBJones | `adopt` |
| 2026-03-31 | [[experiments/mlops-2026-04-01-coding-agent-evals|Build a golden dataset of past bugs as an eval suite]] | @MLOps | `adopt` |
| 2026-03-31 | [[experiments/mlops-2026-04-01-agent-orchestration-cloud|Run parallel agent sessions for independent YOLO tasks]] | @MLOps | `adopt` |
| 2026-03-31 | [[experiments/mlops-2026-03-31-agent-debug-logging|Add structured debug logging at agent decision points to speed up failure diagnosis]] | @MLOps | `adopt` |
| 2026-03-31 | [[experiments/do-2026-03-31-autoresearch-loop|Implement autoresearch loop for YOLO project optimization]] | @DavidOndrej | `adopt` |
| 2026-03-30 | [[experiments/nh-2026-03-30-codex-plan-claude-execute|Adopt Codex-as-planner + Claude Code-as-executor 3-phase build cycle]] | @NateHerk | `adopt` |
| 2026-03-29 | [[experiments/nh-2026-03-29-boring-automation-products|Filter YOLO Tick ideas through the 'boring-but-high-ROI' automation criteria]] | @NateHerk | `adopt` |
| 2026-03-29 | [[experiments/nb-2026-03-29-scheduled-tasks-monitoring|Use Claude Scheduled Tasks for automated recurring work]] | @NateBJones | `discard` |
| 2026-03-29 | [[experiments/nb-2026-03-29-close-the-loops|Adopt the 'close the loops' delegation framework]] | @NateBJones | `adopt` |
| 2026-03-29 | [[experiments/do-2026-03-29-self-improving-eval-loop|Wire a self-critique step into the YOLO build loop before running external tests]] | @DavidOndrej | `adopt` |
| 2026-03-28 | [[experiments/nb-2026-03-28-mcp-tool-integration|Use MCP to connect build agents to professional tools]] | @NateBJones | `adopt` |
| 2026-03-28 | [[experiments/nb-2026-03-28-design-md-agent-readable|Create a design.md as an agent-readable design system]] | @NateBJones | `adopt` |
| 2026-03-27 | [[experiments/mlops-2026-03-27-trust-ladder-adoption|Apply the trust ladder to increase agent autonomy incrementally]] | @MLOps | `discard` |
| 2026-03-27 | [[experiments/mlops-2026-03-27-specialized-agent-team|Use specialized agent roles instead of one monolithic agent]] | @MLOps | `discard` |
| 2026-03-27 | [[experiments/do-2026-03-27-private-local-agent|Run YOLO builds via a 100% local AI agent stack]] | @DavidOndrej | `discard` |
| 2026-03-25 | [[experiments/nb-2026-03-25-dark-factory-pattern|Adopt the Dark Factory pattern for autonomous builds]] | @NateBJones | `adopt` |
| 2026-03-25 | [[experiments/nb-2026-03-25-auto-research-metric-optimization|Apply Auto Research pattern to optimize Gemini review scores]] | @NateBJones | `discard` |
| 2026-03-25 | [[experiments/mlops-2026-03-25-qrspi-vertical-planning|Adopt vertical planning with structure outlines before coding]] | @MLOps | `adopt` |
| 2026-03-24 | [[experiments/nb-2026-03-24-strict-linting-agents|Apply strict linting to all agent-generated code]] | @NateBJones | `adopt` |
| 2026-03-24 | [[experiments/nb-2026-03-24-context-compression|Use incremental summarization for context compression in long sessions]] | @NateBJones | `adopt` |
| 2026-03-24 | [[experiments/nb-2026-03-24-agent-readiness-checklist|Build an Agent Readiness checklist for the YOLO codebase]] | @NateBJones | `discard` |
| 2026-03-17 | [[experiments/mlops-2026-03-17-durable-execution-agents|Evaluate durable execution for long-running agent workflows]] | @MLOps | `adopt` |

---

## Related pages

- [[yolo-projects]] - upstream pipeline
- [[yolo-phase4-integration]] - sync mechanism
- [[tracked-channels-schema]] - the 10 source channels
- [[index]] - wiki home
