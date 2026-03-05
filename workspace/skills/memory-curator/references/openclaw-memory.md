# OpenClaw Memory Concepts

Reference guide for OpenClaw memory system integration.

## Memory Types

### 1. Session Memory (Transient)
- Lives for duration of session
- Includes conversation history
- Auto-compacted when token limit reached
- Not persisted across restarts

### 2. Daily Logs (`memory/YYYY-MM-DD.md`)
- Agent-scoped daily notes
- Simple markdown format
- Summarized, not curated
- Good for temporal recall

### 3. Curated Memory (`MEMORY.md`)
- Long-term persistent memory
- User preferences, constraints, facts
- Manually maintained
- Loaded into main session context

### 4. Learnings (`.learnings/`)
- Error corrections and discoveries
- Categorized by type (LRN, ERR, FEAT)
- Promotable to permanent memory
- Self-improvement feed

## Memory Lifecycle

```
Discovery → Log → Review → Promote → Curate
    ↑                              ↓
    └─────── Feedback loop ←───────┘
```

## Promotion Paths

| Source | Target | When |
|--------|--------|------|
| `.learnings/LEARNINGS.md` | `AGENTS.md` | Cross-cutting operational rule |
| `.learnings/LEARNINGS.md` | `MEMORY.md` | Durable user preference |
| `.learnings/ERRORS.md` | `TOOLS.md` | Tool gotcha/fix |
| Daily logs | `MEMORY.md` | Confirmed persistent fact |

## OpenClaw Tools

### Session Tools
- `sessions_list` - View active/recent sessions
- `sessions_history` - Read another session's transcript
- `sessions_send` - Send message to session
- `sessions_spawn` - Create sub-agent session

### Memory Tools
- `memory read` - Read from memory
- `memory write` - Write to memory
- `memory search` - Semantic search (if configured)

## Best Practices

1. **Log immediately** - Context is freshest after issue
2. **Be specific** - Future agents need quick understanding
3. **Link files** - Makes fixes easier
4. **Promote aggressively** - When in doubt, elevate
5. **Review weekly** - Stale learnings lose value

## Embedding Integration

For semantic search of memories:

```python
# Generate embedding
ollama.embed(
    model='nomic-embed-text-v2-moe',
    input='The sky is blue because of Rayleigh scattering'
)

# Use for:
# - Duplicate detection
# - Semantic search
# - Similarity clustering
# - Auto-tagging
```
