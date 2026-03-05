# BOOTSTRAP.md — Repo Guardian

_One-time initialization — delete after first run._

## Step 1: Verify workspace structure

```bash
python3 ~/.openclaw/workspace/skills/agent-builder/scripts/validate-workspace.py ~/.openclaw/workspace/repo-guardian
```

Expected output: `✅ Workspace looks sane.`

## Step 2: Run acceptance tests

```bash
bash ~/.openclaw/workspace/repo-guardian/scripts/acceptance-tests.sh
```

Expected output: `All acceptance tests passed.`

## Step 3: Confirm daily log is writable

```bash
ls -la ~/.openclaw/workspace/repo-guardian/memory/
```

Expected: `2026-03-05.md` exists.

## Step 4: Review identity

Confirm that IDENTITY.md, SOUL.md, and USER.md accurately describe Repo Guardian's role:
- **Name:** Repo Guardian 🛡️
- **Role:** Safety & compliance validator
- **Autonomy:** Operator (never modifies without approval)

---

If all steps pass, delete this file. Repo Guardian is ready.
