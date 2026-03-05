#!/usr/bin/env python3
"""
Ollama embedding generator for memory-curator.
Uses nomic-embed-text-v2-moe for high-quality text embeddings.
"""

import argparse
import json
import sys
import os

def get_ollama_client():
    """Get Ollama client, trying multiple import patterns."""
    try:
        import ollama
        return ollama
    except ImportError:
        try:
            from ollama import Client
            return Client()
        except ImportError:
            print("Error: ollama package not installed. Run: pip install ollama", file=sys.stderr)
            sys.exit(1)

def embed_text(text: str, model: str = 'nomic-embed-text-v2-moe') -> list:
    """Generate embeddings for a single text."""
    client = get_ollama_client()
    
    # Handle both module and client patterns
    if hasattr(client, 'embed'):
        # Module-level API
        response = client.embed(model=model, input=text)
        return response['embeddings'][0] if isinstance(response['embeddings'], list) and len(response['embeddings']) > 0 else response['embeddings']
    else:
        # Client API
        response = client.embed(model=model, input=text)
        return response['embeddings'][0] if isinstance(response['embeddings'], list) and len(response['embeddings']) > 0 else response['embeddings']

def embed_batch(texts: list, model: str = 'nomic-embed-text-v2-moe') -> list:
    """Generate embeddings for multiple texts."""
    client = get_ollama_client()
    
    if hasattr(client, 'embed'):
        response = client.embed(model=model, input=texts)
        return response['embeddings']
    else:
        response = client.embed(model=model, input=texts)
        return response['embeddings']

def similarity(embedding1: list, embedding2: list) -> float:
    """Calculate cosine similarity between two embeddings."""
    import math
    
    dot_product = sum(a * b for a, b in zip(embedding1, embedding2))
    magnitude1 = math.sqrt(sum(a * a for a in embedding1))
    magnitude2 = math.sqrt(sum(b * b for b in embedding2))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)

def main():
    parser = argparse.ArgumentParser(description='Generate embeddings using Ollama')
    parser.add_argument('text', nargs='?', help='Text to embed')
    parser.add_argument('--file', '-f', help='File containing text to embed')
    parser.add_argument('--batch', '-b', help='JSON file with array of texts')
    parser.add_argument('--model', '-m', default='nomic-embed-text-v2-moe', help='Ollama model to use')
    parser.add_argument('--similarity', '-s', help='Compare with another embedding file')
    parser.add_argument('--output', '-o', help='Output file for embedding')
    
    args = parser.parse_args()
    
    # Get text input
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.batch:
        with open(args.batch, 'r') as f:
            texts = json.load(f)
            embeddings = embed_batch(texts, model=args.model)
            result = {'embeddings': embeddings, 'model': args.model, 'count': len(embeddings)}
            print(json.dumps(result, indent=2))
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(result, f, indent=2)
            return
    elif args.text:
        text = args.text
    else:
        # Read from stdin
        text = sys.stdin.read()
    
    # Generate embedding
    embedding = embed_text(text, model=args.model)
    
    # Calculate similarity if requested
    if args.similarity:
        with open(args.similarity, 'r') as f:
            other = json.load(f)
            if 'embeddings' in other:
                other_embedding = other['embeddings'][0] if isinstance(other['embeddings'], list) else other['embeddings']
            else:
                other_embedding = other
        sim = similarity(embedding, other_embedding)
        result = {
            'embedding': embedding,
            'similarity': sim,
            'model': args.model
        }
    else:
        result = {
            'embedding': embedding,
            'model': args.model,
            'dimensions': len(embedding)
        }
    
    # Output
    output = json.dumps(result, indent=2)
    print(output)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)

if __name__ == '__main__':
    main()
