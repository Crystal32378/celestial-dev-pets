# Helios `running-right` Generation & Acceptance Contract

Status: APPROVED FOR GENERATION  
Scope: `running-right` only  
Frames: 8  
Atlas row: row 1  
Cell size: 192 × 208 px  
Canonical reference: signed-off Phase 1 Helios  
Next-state generation: BLOCKED until acceptance

> These project QA thresholds are stricter implementation gates for Helios. They supplement, but do not replace, the official Codex pet contract.

---

## 1. Scope Lock

This phase MUST:

- generate exactly 8 `running-right` frames
- use the approved canonical Helios as the visual source of truth
- preserve the accepted `idle` row unchanged
- leave `running-left` and every other unfinished row fully transparent
- produce only the artifacts required for review

This phase MUST NOT:

- regenerate or modify `idle`
- generate `running-left`
- generate `waving`, `jumping`, `failed`, `waiting`, `running`, or `review`
- install the pet locally
- merge into `main`
- proceed to another row before explicit acceptance

Any scope expansion is an automatic process failure.

---

## 2. State Semantics

### `running-right`

Helios is physically moving toward the right side of the interface.

The animation must read as directional locomotion:

- face and body orientation remain toward screen-right
- limb motion communicates rightward travel
- weight transfers through a recognizable step cycle
- the sprite remains contained within its own cell
- motion is shown through pose and rhythm, not decorative effects

### `running`

`running` means Codex is actively executing a task.

It is not literal locomotion and must not reuse the `running-right` gait.

These two states must remain visually and semantically distinct.

---

## 3. Required Eight-Frame Motion Structure

The sequence must contain a readable gait cycle with these phases:

| Frame | Intended phase |
|---:|---|
| 0 | first-foot contact |
| 1 | compression / weight acceptance |
| 2 | push-off |
| 3 | recovery / passing pose |
| 4 | opposite-foot contact |
| 5 | compression / weight acceptance |
| 6 | push-off |
| 7 | recovery leading naturally back to frame 0 |

The exact poses may vary, but the final sequence must visibly contain:

- contact
- compression
- propulsion
- recovery
- alternating weight transfer

Eight unrelated “running-like” poses do not constitute an animation.

---

## 4. Character Identity Lock

All frames must clearly depict the same signed-off Helios.

The following must not drift:

- face shape
- sunglasses shape and placement
- eye position behind the glasses
- mouth style
- body proportions
- arm and leg thickness
- sun-ray count
- sun-ray arrangement
- primary palette
- outline weight
- principal light direction
- overall rendering style

Small pose-driven deformation is allowed. Character redesign is not.

Automatic rejection examples:

- glasses changing shape between frames
- rays appearing or disappearing
- face width changing substantially
- limbs changing thickness
- highlights moving to the opposite side
- one frame resembling a different mascot

---

## 5. Direction and Pose Requirements

Every frame must consistently read as facing right.

Required:

- nose, face, torso and gait direction agree
- arms and legs support rightward motion
- silhouette remains readable without depending on the face alone
- no frame appears to reverse direction
- no ambiguous front-facing interruption in the middle of the cycle

The final atlas must not rely on metadata to explain the direction. The image itself must communicate it.

---

## 6. Cell Containment and Motion Illusion

Helios must appear to move right while remaining safely inside each 192 × 208 cell.

Required:

- no pixel crosses the cell boundary
- no ray, hand, foot or accessory is clipped
- no frame travels progressively farther right across the sequence
- no cumulative drift that would cause a visible snap at loop restart
- sufficient transparent padding remains around the silhouette

Recommended project QA thresholds:

- horizontal center-of-mass variation: within ±8 px of the sequence median
- vertical center-of-mass variation: within ±6 px of the sequence median
- apparent character scale variation: no more than approximately 5%
- contact-foot baseline variation during contact poses: within approximately 4 px

These are Helios project gates, not official Codex contract values.

---

## 7. Loop Quality

Frame 7 must connect naturally to frame 0.

The loop must pass all of the following:

- gait phase continues rather than resets abruptly
- body height does not jump
- horizontal position does not snap
- ray arrangement does not flicker
- glasses and face do not shift
- foot sequence alternates correctly
- timing does not introduce an unexplained pause

Review the loop at:

- normal speed
- half speed
- frame-by-frame
- at least five consecutive repetitions

A technically valid GIF with an obvious loop discontinuity is a FAIL.

---

## 8. Motion Style

The motion should feel:

- cheerful
- purposeful
- compact
- energetic without becoming frantic
- suitable for a small desktop companion

Helios should look like a tiny colleague heading to work, not:

- sprinting competitively
- falling forward
- marching militarily
- dancing
- bouncing in place
- sliding without foot contact
- vibrating
- teleporting between poses

---

## 9. Prohibited Effects

Do not use visual effects to fake speed.

Forbidden:

- speed lines
- dust clouds
- ground shadows
- detached sparkles
- motion blur
- afterimages
- ghost limbs
- trailing silhouettes
- floating symbols
- text
- labels
- arrows
- frame numbers embedded in the sprite
- effects extending beyond the character’s cell

Motion must come from pose, weight and timing.

---

## 10. Pixel and Transparency Quality

Every frame must satisfy:

- transparent background
- no checkerboard baked into the image
- no white or colored matte fringe
- no hidden RGB values under fully transparent pixels
- no semi-transparent debris detached from the character
- no isolated noise components
- clean pixel edges
- consistent outline treatment
- no unintended smoothing mismatch between frames

Required technical result:

```text
RGBA: PASS
hidden transparent RGB residue: 0
cell overflow: 0
unexpected detached components: 0
```

---

## 11. Small-Size Readability Gate

The animation must be reviewed around 64 px display size.

At that size, viewers must still be able to recognize:

- Helios
- the sunglasses
- the sun silhouette
- the right-facing direction
- an active walking/running cycle

The state must read as:

> Helios is moving right to begin work.

It must not read merely as:

- a shaking yellow circle
- an idle bounce
- an unclear dance
- generic movement without direction

---

## 12. Required Review Artifacts

Before acceptance, provide:

1. canonical reference used for generation
2. 8 individual transparent frames
3. `running-right.gif`
4. full-size contact sheet
5. 64 px preview GIF
6. loop-boundary comparison: frame 7, frame 0, and overlay or side-by-side
7. updated Phase 2 test atlas
8. frame extraction QA result
9. transparency and hidden-RGB report
10. center, scale and baseline measurements
11. written QA summary
12. commit SHA and branch name

The atlas validator may still report incomplete rows while the remaining states are intentionally transparent. That expected failure must be distinguished from geometry, alpha or row-level failures.

---

## 13. Automatic Rejection Conditions

Any one of the following causes a FAIL:

- frame count is not exactly 8
- any frame faces left or becomes directionally ambiguous
- canonical identity visibly changes
- a ray, limb or accessory is clipped
- sprite crosses a cell boundary
- visible checkerboard or background remains
- hidden transparent RGB residue is present
- speed is communicated mainly through prohibited effects
- loop visibly snaps from frame 7 to frame 0
- 64 px preview does not read as rightward locomotion
- unfinished rows contain non-transparent pixels
- accepted `idle` assets were altered
- another state was generated without approval

---

## 14. Acceptance Decision

### PASS

- visual, motion, technical and loop gates all pass
- Phase 2 may be signed off
- `running-left` may then be evaluated for safe deterministic mirroring

### CONDITIONAL PASS

- no regeneration required
- only timing, assembly or minor cleanup changes remain
- corrected artifacts must still be resubmitted

### FAIL — REPAIR

- one or more frames may be repaired while preserving the valid frames

### FAIL — REGENERATE ROW

- identity, gait structure or direction is fundamentally inconsistent

No next row begins until Crystal and 大 G explicitly record:

```text
Helios running-right final acceptance: PASS
```

---

## 15. Mirroring Gate for `running-left`

Passing `running-right` does not automatically authorize deterministic mirroring.

Before mirroring, inspect Helios for non-symmetric details, including:

- principal light direction
- sunglasses reflections
- highlight placement
- face or limb asymmetry
- ray arrangement

Geometry may be mirror-safe while lighting and character identity are not.
