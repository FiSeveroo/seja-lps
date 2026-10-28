---
name: "web-design-guidelines"
description: "Review UI code for Web Interface Guidelines compliance. Use when asked to \"review my UI\", \"check accessibility\", \"audit design\", \"review UX\", or \"check my site against best practices\"."
---

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines (source: vercel-labs/agent-skills).

## How it works

1. Fetch the latest guidelines from https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (WebFetch, or curl from the shell if WebFetch is blocked).
2. Read the specified files (or ask the user which files/pattern to review).
3. Check against all rules in the fetched guidelines (accessibility, focus states, forms, animation, typography, content handling, images, performance, navigation & state, touch, safe areas, theming, i18n, hover states, anti-patterns).
4. Output findings in the terse `file:line - issue` format the guidelines specify, grouped by file, `✓ pass` for clean files. No preamble.

## Notes for Seja Creator pages

- Pages are written in Portuguese (pt-BR): skip the guideline's English-only copy rules (Title Case, "&" over "and") and follow the Seja tone-of-voice rules instead.
- Still apply: curly quotes, `…`, `alt` text, explicit image width/height, `loading="lazy"` below the fold, visible `:focus-visible`, `prefers-reduced-motion`, no `transition: all`, no zoom blocking, `rel="noopener"` on external links.

## Usage

When a user provides a file or pattern argument, fetch the guidelines, read the files, apply all rules, output findings.
If no files specified, ask the user which files to review.