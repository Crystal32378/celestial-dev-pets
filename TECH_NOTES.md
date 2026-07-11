# Technical Notes

## v0.1 preview assets

The images under `previews/` are optimized GitHub previews of the original 3 × 3 character-state studies. They are not runtime atlases.

## Production target

The production target is the official Codex pet contract documented in `CONTRACT.md`.

Before generating all animation rows:

1. Lock one canonical character reference.
2. Produce one `idle` row as a proof of consistency.
3. Validate transparency, alignment, baseline, silhouette, and looping.
4. Test in the actual Codex runtime.
5. Expand only after the single-row gate passes.
