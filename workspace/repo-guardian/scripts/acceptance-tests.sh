#!/usr/bin/env bash
set -euo pipefail

# acceptance-tests.sh
# Run acceptance tests for Repo Guardian's validate-workspace.py
# Usage: bash scripts/acceptance-tests.sh

VALIDATOR="/root/.openclaw/workspace/skills/agent-builder/scripts/validate-workspace.py"
TMPDIR_BASE=$(mktemp -d /tmp/repo-guardian-tests.XXXXXX)
PASS=0
FAIL=0

cleanup() {
  rm -rf "$TMPDIR_BASE"
}
trap cleanup EXIT

log_pass() { echo "  ✅ PASS: $1"; PASS=$((PASS + 1)); }
log_fail() { echo "  ❌ FAIL: $1"; FAIL=$((FAIL + 1)); }

create_clean_workspace() {
  local dir="$1"
  mkdir -p "$dir"
  cat > "$dir/IDENTITY.md" <<'EOF'
# IDENTITY.md
- Name: Test Agent
- Emoji: 🧪
EOF
  cat > "$dir/USER.md" <<'EOF'
# USER.md
- Preferred name: Tester
EOF
  cat > "$dir/SOUL.md" <<'EOF'
# SOUL.md
You are a test agent. Be direct.
EOF
  cat > "$dir/TOOLS.md" <<'EOF'
# TOOLS.md
No special tools.
EOF
  cat > "$dir/HEARTBEAT.md" <<'EOF'
# HEARTBEAT.md
# Keep empty.
EOF
  cat > "$dir/BOOTSTRAP.md" <<'EOF'
# BOOTSTRAP.md
First-run ritual. Delete after completion.
EOF
  cat > "$dir/AGENTS.md" <<'EOF'
# AGENTS.md
Safety:
- Ask before destructive actions; prefer trash over rm.
- Ask before outbound messages. Never send without explicit approval.
- Stop on CLI errors; run --help and recover.
- Never store credentials in this repo.
- Sub-agents receive only AGENTS.md and TOOLS.md.
EOF
}

# ─── Test 1: Missing SOUL.md ───────────────────────────────────────
echo "Test 1: Missing SOUL.md"
DIR1="$TMPDIR_BASE/test-missing-soul"
create_clean_workspace "$DIR1"
rm "$DIR1/SOUL.md"
if python3 "$VALIDATOR" "$DIR1" 2>&1 | grep -q "SOUL.md"; then
  log_pass "Detected missing SOUL.md"
else
  log_fail "Did not detect missing SOUL.md"
fi

# ─── Test 2: Missing Guardrail ─────────────────────────────────────
echo "Test 2: Missing ask-before-destructive guardrail"
DIR2="$TMPDIR_BASE/test-missing-guardrail"
create_clean_workspace "$DIR2"
# Replace AGENTS.md with one missing the destructive guardrail
cat > "$DIR2/AGENTS.md" <<'EOF'
# AGENTS.md
Safety:
- Ask before outbound messages. Never send without explicit approval.
- Stop on CLI errors; run --help and recover.
- Never store credentials in this repo.
- Sub-agents receive only AGENTS.md and TOOLS.md.
EOF
if python3 "$VALIDATOR" "$DIR2" 2>&1 | grep -q "ask-before-destructive"; then
  log_pass "Detected missing ask-before-destructive guardrail"
else
  log_fail "Did not detect missing ask-before-destructive guardrail"
fi

# ─── Test 3: Credential Exposure (grep-based) ──────────────────────
echo "Test 3: Credential exposure detection"
DIR3="$TMPDIR_BASE/test-creds"
create_clean_workspace "$DIR3"
echo "API_KEY=sk-1234567890abcdef" >> "$DIR3/TOOLS.md"
if grep -rnI "API_KEY\|api_key\|password\|token\|secret\|SECRET" "$DIR3/" --include="*.md" | grep -q "sk-1234567890"; then
  log_pass "Detected credential exposure"
else
  log_fail "Did not detect credential exposure"
fi

# ─── Test 4: Clean Workspace ───────────────────────────────────────
echo "Test 4: Clean workspace passes validation"
DIR4="$TMPDIR_BASE/test-clean"
create_clean_workspace "$DIR4"
if python3 "$VALIDATOR" "$DIR4" 2>&1 | grep -q "looks sane"; then
  log_pass "Clean workspace passed validation"
else
  log_fail "Clean workspace failed validation unexpectedly"
fi

# ─── Summary ───────────────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Results: $PASS passed, $FAIL failed"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
echo "All acceptance tests passed."
