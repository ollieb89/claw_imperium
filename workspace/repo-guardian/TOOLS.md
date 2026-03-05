# TOOLS.md — Repo Guardian

## Environment Notes

- Workspace root: `~/.openclaw/workspace/`
- Agent workspaces: `~/.openclaw/workspace/[agent-name]/`

## CLI Aliases

- `validate-workspace [name]` — run full validation checklist
- `check-diff [name]` — review uncommitted changes
- `flag-secrets [path]` — scan for exposed credentials

## File Paths (for reference)

- OpenClaw docs: `/usr/local/lib/node_modules/openclaw/docs`
- Skills: `/usr/local/lib/node_modules/openclaw/skills/`
- Workspace skills: `~/.openclaw/workspace/skills/`

## Validation Commands

```bash
# Check workspace structure
ls -la ~/.openclaw/workspace/[agent-name]/

# Check for secrets (grep patterns)
grep -r "api_key\|password\|token\|secret" ~/.openclaw/workspace/[agent-name]/ --include="*.md"

# Git diff inspection
cd ~/.openclaw/workspace/[agent-name] && git diff --stat
```

---

Add environment-specific notes as needed.
