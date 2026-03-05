# IMPERIUM_REGISTRY.md — The Agent Imperium Index

This registry prevents drift and chaos as the imperium scales.

## Rules
- Any new agent MUST:
  1) be built by Imperium Core (or approved equivalent)
  2) be validated by Repo Guardian
  3) pass its bootstrap tests (min 4)
  4) be registered here with an eval date
- Any agent change that touches AGENTS.md, safety rules, memory rules, or tool permissions MUST trigger re-eval.

## Legend
- Autonomy: Advisor / Operator / Autopilot
- Risk: Low / Medium / High / Critical
- Memory: None / Daily / Curated
- Last Eval: YYYY-MM-DD (Europe/Oslo)

## Registry

| Agent | Emoji | Mission | Autonomy | Risk | Memory | Workspace Path | Owner | Last Eval | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Imperium Core | 🦔 | Build/maintain OpenClaw agents from short specs | Operator | Medium | Curated | ~/.openclaw/workspace/ | Ollie | 2026-03-04 | Builder-of-builders |
| Repo Guardian | 🛡️ | Validate workspaces, diffs, guardrails, secret exposure | Operator | Low | Daily | ~/.openclaw/workspace/repo-guardian/ | Ollie | 2026-03-04 | Validator + compliance gate |
| Research Scout | 🔍 | Research w/ real sources + confidence + contradictions | Operator | Low | Daily | ~/.openclaw/workspace/research-scout/ | Ollie | 2026-03-04 | Uses docs fetch; web_search may be unavailable |
| Memory Curator | 🧹 | Dedupe learnings, promote durable rules, prune noise | Operator | Low | Daily | ~/.openclaw/workspace/memory-curator/ | Ollie | 2026-03-04 | Memory maintenance agent |

## Change log (optional)
- 2026-03-04: Registry created; foundational triangle registered.
- 2026-03-04: Added Memory Curator (agent #3).
