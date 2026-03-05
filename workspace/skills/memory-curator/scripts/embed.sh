#!/bin/bash
# Ollama embedding via CLI/HTTP API
# Usage: embed.sh "text to embed"

TEXT="$1"
MODEL="${2:-nomic-embed-text-v2-moe}"

if [ -z "$TEXT" ]; then
    echo "Usage: embed.sh 'text to embed' [model]"
    exit 1
fi

# Use Ollama HTTP API
curl -s http://localhost:11434/api/embed \
    -H "Content-Type: application/json" \
    -d "{
        \"model\": \"$MODEL\",
        \"input\": \"$TEXT\"
    }" | jq '.embeddings[0]'
