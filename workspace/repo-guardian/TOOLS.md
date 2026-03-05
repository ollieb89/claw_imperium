# TOOLS.md — Repo Guardian

## Environment Notes

- Workspace root: `~/.openclaw/workspace/`
- Agent workspaces: `~/.openclaw/workspace/[agent-name]/`

## CLI Commands

### Validate workspace structure & guardrails
```bash
python3 ~/.openclaw/workspace/skills/agent-builder/scripts/validate-workspace.py ~/.openclaw/workspace/[agent-name]
```

### Scan for exposed credentials
```bash
grep -rnI "api_key\|password\|token\|secret\|API_KEY\|SECRET" ~/.openclaw/workspace/[agent-name]/ --include="*.md"
```

### Check uncommitted changes
```bash
git -C ~/.openclaw/workspace/[agent-name] diff --stat
```

### Run acceptance tests
```bash
bash ~/.openclaw/workspace/repo-guardian/scripts/acceptance-tests.sh
```

## File Paths (for reference)

- Workspace root: `~/.openclaw/workspace/`
- Agent workspaces: `~/.openclaw/workspace/[agent-name]/`
- Workspace skills: `~/.openclaw/workspace/skills/`
- Validator script: `~/.openclaw/workspace/skills/agent-builder/scripts/validate-workspace.py`

---

Add environment-specific notes as needed.
