# TOOLS.md — Memory Curator

## Preferred Workflow

1. Read files → propose diffs → get approval → apply minimal edits
2. Use git for rollback when available

## Safe Commands (Examples)

```bash
# Check current state
ls -la ~/.openclaw/workspace/.learnings/
ls -la ~/.openclaw/workspace/memory/

# Review learnings
cat ~/.openclaw/workspace/.learnings/*.md

# Git integration (optional)
git status
git diff
git add -p
git commit -m "Curate memory: promotions/merges"
```

## Redaction Pattern

When flagging secrets:
```
❌ BAD: API_KEY=sk-1234567890
✅ GOOD: Found .env with API_KEY field (redacted)
```

---

Add environment-specific notes as needed.
