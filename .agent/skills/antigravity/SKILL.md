---
name: antigravity
description: Guidelines and best practices for interacting with the Antigravity agentic coding assistant within the OpenClaw environment. Use this skill when configuring Antigravity, requesting it to perform complex tasks, or understanding its capabilities and standard operating procedures.
---

# Antigravity Agent Skill

## Overview

The Antigravity skill provides the core operating procedures, capabilities, and best practices for working with the Antigravity coding assistant. It ensures that Antigravity operates efficiently, respects workspace boundaries, and effectively uses its tools to assist the user.

## Core Capabilities

Antigravity operates with a powerful set of tools and a specific agentic mindset:

1. **Agentic Task Execution**: Capable of breaking down complex goals into actionable tasks, maintaining context across steps, and verifying outcomes.
2. **Context Management**: Uses Knowledge Items (KIs) and artifact persistence to maintain long-term memory across sessions.
3. **Workspace Navigation**: Proficient at searching, analyzing, and modifying codebases using precise search and edit tools.
4. **Command Execution**: Can run local shell commands safely to test, build, and deploy.

## Best Practices & Guidelines

### Communication Style
- Be concise and direct.
- Proactively anticipate the user's next needs.
- Use explicit task boundaries to structure long-running operations.

### Code Editing Standards
- Use `replace_file_content` or `multi_replace_file_content` for precise, token-efficient edits.
- Avoid writing entire files unless necessary.
- Always lint or verify code changes using local tools (e.g., `npm run lint`, `pytest`) when available.

### Research and Analysis
- ALWAYS check existing Knowledge Items (KIs) before starting a new research phase to avoid redundant work.
- Rely on `grep_search` and `find_by_name` for targeted exploration rather than arbitrary directory traversal.

## Advanced Usage

For specific domain knowledge or complex workflows, Antigravity delegates to specialized reference guides:

- **Workflows**: See reference workflows in `.agent/workflows/` for structured procedures.
- **Project Structure**: See [references/project-structure.md](references/project-structure.md) for architectural guidelines.
- **Agent Interoperability**: See [references/agent-interop.md](references/agent-interop.md) for interacting with other OpenClaw agents like `repo-guardian` or `memory-curator`.

## Resources

- `scripts/`: Custom utility scripts used by Antigravity during complex operations.
- `references/`: Detailed guidelines on agent configuration and architectural models.
- `assets/`: Templates for code generation and project scaffolding.
