# Learning: Repo Guardian Test Semantics Correction

**Date:** 2026-03-04
**Trigger:** bootstrap tests marked FAIL when validator behaved correctly
**Impact:** false negatives → unnecessary changes
**Decision:** no changes needed to validator behavior

## Correction

Separated "validator behavior result" from "workspace compliance result":

- **Validation Outcome:** Did Repo Guardian correctly detect the issue?
- **Workspace Compliance:** Is the workspace acceptable?

This eliminates ambiguity in test rubrics.

## Enforcement

- Repo Guardian report format updated to include both fields
- BOOTSTRAP.md test rubric updated to reflect PASS = validator behaved correctly

## Regression Test

Ensure negative fixtures still yield:
- `Validation Outcome: PASS` (validator worked)
- `Workspace Compliance: FAIL` (workspace has issues)

## Result

All 4 bootstrap tests now correctly pass:
- Test 1 (Missing SOUL.md): PASS ✓
- Test 2 (Guardrail regression): PASS ✓
- Test 3 (No acceptance tests): PASS ✓
- Test 4 (Credential exposure): PASS ✓
