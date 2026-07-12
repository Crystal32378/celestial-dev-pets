# Helios `running-right` Phase 2 QA

## Scope

Exactly one eight-frame `running-right` row was generated from the signed-off
canonical Helios. The accepted `idle` row was reused unchanged. Every other row
remains fully transparent. Nothing was installed or merged into `main`.

Mandatory contract:
[`docs/contracts/HELIOS_RUNNING_RIGHT_CONTRACT.md`](../../../docs/contracts/HELIOS_RUNNING_RIGHT_CONTRACT.md)

## Automated row result

- Frame count: 8/8.
- Extraction method: official component extraction.
- Official row review: PASS, no row errors or warnings.
- Atlas: `1536 × 1872`, RGBA WebP.
- Cell size: `192 × 208`.
- Hidden RGB under fully transparent pixels: 0.
- Cell-edge pixels: 0 in every frame.
- Horizontal center range: 0.79 px.
- Vertical center range: 3.34 px.
- Bounding-width range: 9 px.
- Bounding-height range: 14 px, explained by the required compression phases.
- Contact-pose baseline difference, frames 0 and 4: 1 px.

The official full-atlas validator reports `ok: false` only because the seven
not-yet-approved rows remain empty. `idle` and `running-right` are populated;
geometry, RGBA mode, and transparent RGB residue checks pass.

## Visual and motion QA

Internal contract gate: `PASS`.

The eight frames consistently depict the canonical right-facing Helios with a
readable alternating gait, stable glasses, rays, face, palette, and lighting.
The sequence has clean cell containment, remains legible at 64 px, and frame 7
hands off naturally to frame 0. No prohibited speed effects, text, checkerboard,
detached debris, clipping, or identity drift were found.

Repair required: none.

## Acceptance state

Final acceptance: `PASS` — accepted jointly by Crystal and 大 G on 2026-07-11.

- Original-size GIF: PASS.
- 64 px GIF: PASS.
- Character consistency: PASS.
- Rightward gait direction: PASS.
- Loop transition: PASS.
- Small-size readability: PASS.
- Motion rhythm: PASS.
- Repair required: none.

Phase 2 is closed. The production line remains stopped; this acceptance does
not authorize `running-left` or any other state.
