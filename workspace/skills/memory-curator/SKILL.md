---
name: memory-curator
description: "Memory curation and deduplication for OpenClaw agents using semantic embeddings. Use when: (1) Reviewing and deduplicating .learnings/ entries, (2) Promoting durable rules to AGENTS.md or MEMORY.md, (3) Pruning stale or redundant memory, (4) Analyzing learning patterns with semantic similarity, (5) Curating memory with Ollama embeddings (nomic-embed-text-v2-moe). Integrates self-improving-agent patterns with OpenClaw memory concepts."
---

# Memory Curator Skill

Curate agent memory using semantic embeddings and OpenClaw memory patterns. Deduplicate learnings, promote durable rules, and maintain clean memory stores.

## Quick Start

### Prerequisites
```bash
# Install Ollama and pull embedding model
ollama pull nomic-embed-text-v2-moe

# Install Python dependencies
pip install ollama
```

### Basic Workflow

```bash
# 1. Dedupe learnings using embeddings
cd ~/.openclaw/workspace
python3 skills/memory-curator/scripts/dedupe_learnings.py .learnings/LEARNINGS.md --threshold 0.92

# 2. Review and approve merge suggestions

# 3. Promote durable rules to AGENTS.md or MEMORY.md

# 4. Propose deletions (requires approval)
```

## Core Operations

### 1. Semantic Deduplication

Find similar learning entries using `nomic-embed-text-v2-moe` embeddings:

```bash
python3 skills/memory-curator/scripts/dedupe_learnings.py \
  .learnings/LEARNINGS.md \
  --threshold 0.92 \
  --top 10 \
  --output dedupe-report.md
```

**Threshold guidance:**
- `0.95+` - Near duplicates, strong merge candidate
- `0.92-0.95` - Similar, review for merge or link
- `0.85-0.92` - Related, consider "See Also" link
- `<0.85` - Likely distinct

### 2. Generate Embeddings

```bash
# Single text
python3 skills/memory-curator/scripts/embed.py "Text to embed"

# From file
python3 skills/memory-curator/scripts/embed.py --file input.txt --output embedding.json

# Batch
python3 skills/memory-curator/scripts/embed.py --batch texts.json --output embeddings.json

# Compare similarity
python3 skills/memory-curator/scripts/embed.py "Text A" --similarity embedding_b.json
```

### 3. Memory Curation Workflow

For each curation run:

```
1. SCAN → List all .learnings/ entries
2. EMBED → Generate embeddings for summaries
3. DEDUPE → Find similar entries (>0.92)
4. REVIEW → Present merge/promote/delete suggestions
5. ACT → Apply approved changes only
```

## Promotion Guidelines

### Promote to AGENTS.md when:
- Cross-cutting operational/safety invariant
- Fixes repeated failures across agents
- Global rule all agents must follow

### Promote to MEMORY.md when:
- Durable user preference
- User constraint or ongoing project note
- Operator-specific fact

### Promote to TOOLS.md when:
- Tool-specific gotcha or workaround
- Integration pattern

### Keep in .learnings/ when:
- Too specific to one situation
- Unproven or experimental
- One-off error correction

## Deliverable Format

Present curation results as:

```
## Memory Curation Report

### Summary
- Entries scanned: N
- Duplicates found: N
- Promotions suggested: N
- Deletions proposed: N

### Duplicate Suggestions
1. [LRN-001] ↔ [LRN-002] (sim: 0.94)
   Action: Merge
   Reason: Both describe same git workflow

### Promotion Candidates
1. → AGENTS.md: "Always validate before delete"
   Source: [LRN-003]
   Recurrence: 3x

### Proposed Deletions (REQUIRES APPROVAL)
1. [LRN-004] - Superseded by promoted rule
2. [ERR-001] - Fixed, no longer relevant

### Risks
- Deletion of [LRN-004] removes error context
- Merge of [LRN-001/002] may lose nuance
```

## Integration Points

### Self-Improving Agent
- Reads `.learnings/*.md` for curation
- Uses same entry format (LRN-, ERR-, FEAT-)
- Contributes to recurrence tracking

### OpenClaw Memory
- Curates `memory/YYYY-MM-DD.md` logs
- Maintains `MEMORY.md` (user preferences)
- Updates `AGENTS.md` (workflows)

### Ollama Embeddings
- Model: `nomic-embed-text-v2-moe`
- Dimensions: 768
- Optimized for semantic similarity
- Runs locally, no API keys needed

## Scripts Reference

| Script | Purpose |
|--------|---------|
| `embed.py` | Generate embeddings for text/files |
| `dedupe_learnings.py` | Find similar learning entries |

## Reference Files

- `references/openclaw-memory.md` - OpenClaw memory concepts
- `references/self-improving-integration.md` - Learning formats and workflows

## Best Practices

1. **Approval First** - Never delete without explicit operator approval
2. **Propose Diffs** - Show before/after for all changes
3. **Link Related** - Use "See Also" for related but distinct entries
4. **Track Recurrence** - Count pattern occurrences for promotion decisions
5. **Redact Secrets** - Never include actual credentials in reports
