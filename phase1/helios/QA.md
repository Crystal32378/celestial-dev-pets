# Helios Phase 1 QA

## Scope

This proof implements only the canonical reference and the six-frame `idle`
row. No other animation row was generated, and the package was not installed
into Codex.

Original character and visual direction: 大 G. Codex pet adaptation performed
from the supplied Helios character-bible artwork without overwriting the source
package.

## Checks

- Atlas geometry: `1536 × 1872`, RGBA WebP.
- Cell geometry: `192 × 208`.
- Idle frames: six populated cells in row 0.
- Unused cells: fully transparent with zero hidden RGB residue.
- Text: no `timeout`, labels, code panels, or logos in animation frames.
- Isolation: no sprite crosses a cell boundary.
- Character lock: golden round sun, orange rays, black rectangular glasses,
  tiny limbs, and pixel-art treatment preserved.

## Official validator result

`qa/official-validation.json` reports `ok: false` because Phase 1 intentionally
leaves the other eight required rows empty. This is expected and must not be
interpreted as an installable complete pet. The validator confirms the atlas
dimensions, RGBA mode, and zero transparent-pixel RGB residue.

`qa/official-frame-review.json` likewise records the complete six-frame idle
row and expected missing-row errors. A full-package pass is deferred until all
nine rows have been separately approved.

## Generation and correction record

1. Generated one canonical Helios reference grounded in 大 G's original art.
2. Generated one six-frame idle strip grounded in the original and canonical
   references plus the official six-slot layout guide.
3. Extracted six `192 × 208` frames using the official hatch-pet extractor.
4. The official full-atlas composer rejected the partial frame set because it
   requires all nine rows. Added a Phase 1-only deterministic builder that
   places the six idle frames into row 0 and leaves every other cell transparent.
5. Preserved the official validator's expected failure instead of weakening or
   bypassing its full-package checks.

## Runtime status

Not installed and not runtime-tested, as required by Phase 1 scope.

## Visual QA result

`PASS` — Helios retains the canonical round golden pixel-art identity and
glasses across exactly six clean, centered, baseline-stable idle frames with a
subtle blink-and-bob loop. No text, deformation, checker residue, edge contact,
or cross-cell spill was found. No repair is currently required.

## Final acceptance

`PASS` — accepted jointly by 大 G and the user on 2026-07-11.

- `idle.gif`: `192 × 208`, six frames, normal loop.
- Character identity remains consistent.
- Blink and subtle vertical motion read correctly as idle behavior.
- The final frame returns to the first without a visible jump.
- Readability remains good at reduced display size.
- No regeneration or visual repair is required.

Phase 1 is closed. `running-right` is not started by this acceptance record.
