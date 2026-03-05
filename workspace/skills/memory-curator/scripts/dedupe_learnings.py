#!/usr/bin/env python3
"""
Semantic deduplication of learning entries using Ollama embeddings.
Identifies similar learnings and suggests merges.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Import embed functions
sys.path.insert(0, os.path.dirname(__file__))
from embed import embed_batch, similarity

def parse_learnings(filepath: str) -> List[Dict]:
    """Parse markdown learnings file into structured entries."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Split by entry headers (## [ID])
    entries = []
    pattern = r'##\s*\[([^\]]+)\]\s*(.+?)(?=##\s*\[|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for entry_id, body in matches:
        entry = {
            'id': entry_id.strip(),
            'body': body.strip(),
            'full_text': f"## [{entry_id}] {body.strip()}"
        }
        entries.append(entry)
    
    return entries

def extract_summary(body: str) -> str:
    """Extract summary section from learning body."""
    summary_match = re.search(r'###\s*Summary\s*\n(.+?)(?=###|$)', body, re.DOTALL | re.IGNORECASE)
    if summary_match:
        return summary_match.group(1).strip()
    
    # Fallback: first non-empty line
    lines = [l.strip() for l in body.split('\n') if l.strip()]
    return lines[0] if lines else body[:200]

def find_duplicates(entries: List[Dict], threshold: float = 0.92, model: str = 'nomic-embed-text-v2-moe') -> List[Tuple[Dict, Dict, float]]:
    """Find similar learning entries using embeddings."""
    if len(entries) < 2:
        return []
    
    # Extract summaries for embedding
    texts = [extract_summary(e['body']) for e in entries]
    
    # Generate embeddings in batches
    print(f"Generating embeddings for {len(texts)} entries...", file=sys.stderr)
    try:
        embeddings = embed_batch(texts, model=model)
    except Exception as e:
        print(f"Error generating embeddings: {e}", file=sys.stderr)
        return []
    
    # Find similar pairs
    duplicates = []
    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            sim = similarity(embeddings[i], embeddings[j])
            if sim >= threshold:
                duplicates.append((entries[i], entries[j], sim))
    
    # Sort by similarity (highest first)
    duplicates.sort(key=lambda x: x[2], reverse=True)
    return duplicates

def suggest_merge(entry1: Dict, entry2: Dict, similarity_score: float) -> str:
    """Suggest a merged version of two similar entries."""
    lines = [
        f"## Merge Suggestion (similarity: {similarity_score:.3f})",
        f"",
        f"**Entry 1:** [{entry1['id']}]",
        f"**Entry 2:** [{entry2['id']}]",
        f"",
        f"### Action Options:",
        f"1. **Merge** - Consolidate into single entry with combined context",
        f"2. **Keep Both** - Link with `See Also` if related but distinct",
        f"3. **Delete One** - If one fully supersedes the other",
        f"",
        f"### Entry 1 Summary:",
        extract_summary(entry1['body']),
        f"",
        f"### Entry 2 Summary:",
        extract_summary(entry2['body']),
        f""
    ]
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description='Deduplicate learnings using semantic similarity')
    parser.add_argument('learnings_file', help='Path to LEARNINGS.md or ERRORS.md')
    parser.add_argument('--threshold', '-t', type=float, default=0.92, help='Similarity threshold (default: 0.92)')
    parser.add_argument('--model', '-m', default='nomic-embed-text-v2-moe', help='Ollama model')
    parser.add_argument('--output', '-o', help='Output file for duplicates report')
    parser.add_argument('--top', type=int, default=10, help='Show top N matches')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.learnings_file):
        print(f"Error: File not found: {args.learnings_file}", file=sys.stderr)
        sys.exit(1)
    
    # Parse entries
    print(f"Parsing {args.learnings_file}...", file=sys.stderr)
    entries = parse_learnings(args.learnings_file)
    print(f"Found {len(entries)} entries", file=sys.stderr)
    
    if len(entries) < 2:
        print("Not enough entries to compare", file=sys.stderr)
        sys.exit(0)
    
    # Find duplicates
    duplicates = find_duplicates(entries, threshold=args.threshold, model=args.model)
    
    # Generate report
    report_lines = [
        f"# Deduplication Report",
        f"",
        f"**File:** {args.learnings_file}",
        f"**Total Entries:** {len(entries)}",
        f"**Similarity Threshold:** {args.threshold}",
        f"**Model:** {args.model}",
        f"**Potential Duplicates Found:** {len(duplicates)}",
        f""
    ]
    
    if duplicates:
        report_lines.append("## Top Matches\n")
        for i, (e1, e2, sim) in enumerate(duplicates[:args.top]):
            report_lines.append(suggest_merge(e1, e2, sim))
            report_lines.append("\n---\n")
    else:
        report_lines.append("No duplicates found above threshold.")
    
    report = '\n'.join(report_lines)
    print(report)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"\nReport saved to: {args.output}", file=sys.stderr)

if __name__ == '__main__':
    main()
