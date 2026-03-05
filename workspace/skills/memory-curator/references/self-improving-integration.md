# Self-Improving Agent Integration

How memory-curator integrates with self-improving-agent patterns.

## Learning Entry Format

### Learning (LRN-YYYYMMDD-XXX)
```markdown
## [LRN-20250115-001] category

**Logged**: 2025-01-15T10:30:00Z
**Priority**: low | medium | high | critical
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Summary
One-line description

### Details
Full context

### Suggested Action
Specific fix

### Metadata
- Source: conversation | error | user_feedback | simplify-and-harden
- Related Files: path/to/file.ext
- Tags: tag1, tag2
- See Also: LRN-20250115-002
- Pattern-Key: simplify.dead_code (optional)
- Recurrence-Count: 1
- First-Seen: 2025-01-15
- Last-Seen: 2025-01-15
```

### Error (ERR-YYYYMMDD-XXX)
```markdown
## [ERR-20250115-001] command_name

**Logged**: 2025-01-15T10:30:00Z
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
Brief description

### Error
```
Actual error message
```

### Context
- Command attempted
- Parameters used

### Suggested Fix
Resolution approach

### Metadata
- Reproducible: yes | no | unknown
- Related Files: path/to/file.ext
```

## Curator Actions

### Deduplicate
- Use embeddings to find similar entries
- Suggest merges for >0.92 similarity
- Link with "See Also" for related entries

### Promote
| To | Criteria |
|----|----------|
| `AGENTS.md` | Cross-cutting operational rule |
| `MEMORY.md` | Durable user preference |
| `TOOLS.md` | Tool-specific gotcha |
| `SOUL.md` | Behavioral guideline |

### Prune
- Propose delete for: redundant, superseded, low-signal
- **Requires explicit approval**
- Never auto-delete

## Semantic Similarity Workflow

1. Extract summary from each entry
2. Generate embedding: `nomic-embed-text-v2-moe`
3. Calculate cosine similarity matrix
4. Flag pairs > threshold (default 0.92)
5. Suggest: merge, link, or keep separate

## Recurring Pattern Detection

Promotion rule: Promote to system prompt when:
- `Recurrence-Count >= 3`
- Seen across 2+ distinct tasks
- Within 30-day window

This prevents prompt bloat while capturing durable patterns.
