# BOOTSTRAP.md — Repo Guardian

_One-time initialization — delete after first run._

## Verification

Run these tests to confirm Repo Guardian is working:

### Test 1 — Missing SOUL.md
```bash
# Create a test workspace with all files EXCEPT SOUL.md
mkdir -p ~/.openclaw/workspace/test-missing-soul
# Add: IDENTITY.md, USER.md, AGENTS.md, TOOLS.md, HEARTBEAT.md

# Run validation
# Expected:
#   - Validation Outcome: PASS (validator detected the issue)
#   - Workspace Compliance: FAIL (SOUL.md missing)
#   - Recommendation: Add SOUL.md
```

### Test 2 — Diff Safety
```bash
# Create a workspace, then remove ask-before-destructive rule
# Expected: Flag as high risk
```

### Test 3 — Missing Acceptance Tests
```bash
# Create workspace without acceptance tests
# Expected: Block approval
```

### Test 4 — Credential Exposure
```bash
# Add plaintext API key to a file
echo "API_KEY=sk-1234567890abcdef" > ~/.openclaw/workspace/test-creds/test.md

# Expected: Flag credential exposure as critical
```

---

If all tests pass, delete this file. Repo Guardian is ready.
