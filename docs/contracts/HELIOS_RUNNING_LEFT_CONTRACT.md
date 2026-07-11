# Helios `running-left` Generation & Acceptance Contract

Status: APPROVED FOR GENERATION  
Scope: `running-left` only  
Frames: 8  
Atlas row: row 2  
Cell size: 192 × 208 px  
Canonical reference: signed-off Phase 1 Helios

## Scope lock

- Generate exactly eight `running-left` frames.
- Preserve the accepted `idle` and `running-right` rows byte-for-byte.
- Do not generate any other state, install a new atlas, or merge into `main`.
- Stop after review artifacts and QA are committed.

## Motion and identity

- Every frame must face and physically travel toward screen-left.
- Use a readable alternating contact, compression, push-off, and recovery gait.
- Frame 7 must lead naturally back to frame 0.
- Preserve canonical face, glasses, ray count and arrangement, proportions,
  palette, outline, limb thickness, and overall pixel-art treatment.
- `running-right` may guide cadence, but the row must not be accepted through
  an unchecked whole-strip mirror.
- Preserve the canonical world's principal light direction and deliberately
  inspect sunglasses reflections and highlights; do not let lighting flip just
  because travel direction changes.

## Prohibited

- No speed lines, dust, ground shadows, blur, afterimages, ghost limbs,
  detached sparkles, text, labels, arrows, or guide marks.
- No progressive positional drift, clipping, cross-cell pixels, checkerboard,
  matte fringe, detached debris, or hidden RGB under transparent pixels.

## Project gates

- Horizontal center variation: within ±8 px of median.
- Vertical center variation: within ±6 px of median.
- Apparent scale variation: approximately 5% or less, allowing gait compression.
- Contact-pose baseline variation: approximately 4 px or less.
- At 64 px, the state must read as Helios moving left to work, not shaking,
  dancing, bouncing in place, or sliding.

## Required artifacts

1. Eight transparent frames.
2. `running-left.gif`.
3. 64 px preview GIF.
4. Contact sheet containing accepted idle, running-right, and candidate running-left.
5. Frame 7 to frame 0 comparison.
6. Updated partial test atlas.
7. Official frame review and atlas validation output.
8. Transparency, hidden-RGB, center, scale, and baseline metrics.
9. Written QA record, branch, and commit SHA.

No next row begins until Crystal and 大 G explicitly record:

```text
Helios running-left final acceptance: PASS
```
