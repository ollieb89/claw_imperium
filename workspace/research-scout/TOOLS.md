# TOOLS.md — Research Scout

## Tools Available

- `web_search` — Search the web using Brave Search API
  - Returns titles, URLs, snippets
  - Parameters: `query`, `count`, `country`, `freshness`, `search_lang`

- `web_fetch` — Fetch and extract readable content from URLs
  - Converts HTML to markdown/text
  - Parameters: `url`, `extractMode`, `maxChars`

- `browser` — Control web browser for complex research
  - Actions: navigate, snapshot, screenshot, console
  - Use for JavaScript-heavy pages or login-required content

- `exec` — Run local commands for repo inspection
  - Useful for: cloning repos, reading local docs, running CLI tools

## Research Workflow Commands

```bash
# Quick web search
# Use web_search tool

# Fetch documentation
# Use web_fetch with url

# Complex research (login pages, dynamic content)
# Use browser tool
```

## Safety Notes

- Never store credentials or API keys encountered during research
- Flag credential exposure but don't capture values
- Verify URLs are real before citing

## Search Fallback Order

When web_search is unavailable, use this priority:
1. Official documentation
2. GitHub repositories
3. Vendor documentation
4. Known technical sources

**Never fabricate citations.**

---

Add environment-specific notes as needed.
