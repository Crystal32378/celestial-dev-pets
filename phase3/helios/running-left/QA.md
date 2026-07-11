# Helios `running-left` Phase 3 QA

## Attempt 1 — rejected before ingestion

Result: `FAIL — REGENERATE ROW`.

The freely generated strip remained predominantly front-facing and did not
unmistakably communicate screen-left travel. It was not copied into the run,
atlas, or review package. This is retained as evidence that direction semantics
are a hard acceptance gate.

## Attempt 2 — deterministic derivation

The accepted eight `running-right` cell frames were mirrored individually,
preserving frame order and timing. An initial strip-level derivation was
discarded because re-extraction changed the contact baseline difference to 8
px. Direct cell-frame derivation restored the accepted geometry.

### Technical result

- Eight frames: PASS.
- Direction reads screen-left: PASS.
- Official component frame review: PASS, no row errors or warnings.
- Horizontal center range: 0.79 px.
- Vertical center range: 3.34 px.
- Contact baseline difference, frames 0 and 4: 1 px.
- Hidden transparent RGB residue: 0.
- Cell containment and edge contact: PASS.
- Frame order, gait phase, and loop timing: preserved.

The full atlas validator fails only for the six intentionally unfinished rows.

### Visual result

Result: `FAIL — REPAIR`.

The same Helios, leftward gait, frame 7 to frame 0 loop, 64 px readability, and
clean containment pass. However, deterministic mirroring also flips canonical
world-light cues across body highlights, sunglasses reflections, and asymmetric
ray shading.

### Smallest authorized repair scope

Restore canonical world-light direction in all eight frames by locally
repainting only:

- body highlights;
- sunglasses reflections;
- asymmetric ray shading.

The repair must preserve silhouettes, frame order, gait, centers, scale, and
baselines exactly. No full-row regeneration, atlas installation, smoke-package
update, next-state generation, or `main` merge is authorized by this record.
