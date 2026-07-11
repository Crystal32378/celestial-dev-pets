# Codex Pet Contract Reference

Official source:

https://github.com/openai/skills/blob/main/skills/.curated/hatch-pet/references/codex-pet-contract.md

## Required atlas geometry

- Format: PNG or WebP
- Dimensions: `1536 × 1872`
- Grid: `8 columns × 9 rows`
- Cell: `192 × 208`
- Background: transparent
- Unused cells: fully transparent

The webview uses fixed CSS background positions. Do not add labels, gutters, borders, grid lines, shadows outside the cell, or extra frames.

## Local package shape

```text
${CODEX_HOME:-$HOME/.codex}/pets/<pet-name>/
├── pet.json
└── spritesheet.webp
```

```json
{
  "id": "pet-name",
  "displayName": "Pet Name",
  "description": "One short sentence.",
  "spritesheetPath": "spritesheet.webp"
}
```

The current v0.1 files in this repository are not yet compliant installable packages.
