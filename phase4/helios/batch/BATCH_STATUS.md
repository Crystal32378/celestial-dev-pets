# Helios Remaining-State Batch Status

Status: `COMPLETE — 6/6 rows accepted; full atlas QA passed`

## Runtime confirmation before batch

- Idle playback and loop: PASS.
- Running-right runtime movement: PASS.
- Running-left runtime movement: PASS.
- Both directions return naturally to idle.
- No clipping, wrong-row display, or flicker was observed.
- Pointer disappearance remains an App interaction behavior already reported to
  the upstream Codex project.

## Accepted rows

| State | Frames | Result |
|---|---:|---|
| `waving` | 4 | PASS |
| `jumping` | 5 | PASS after uniform-background retry |
| `waiting` | 6 | PASS |
| `running` | 6 | PASS; task execution in place, not locomotion |
| `review` | 6 | PASS |

All five rows passed official component extraction with exact frame counts and
no row-level errors or warnings. The supplied Sol motion sheet was used only
for motion semantics; forbidden shadows, motion marks, text, props, and detached
effects were not carried into the accepted frames.

## Blocking row

`failed`, eight frames: `FAIL — TECHNICAL FORMAT`.

Multiple generated candidates preserved Helios identity and clearly conveyed a
failed, sad, or exhausted state. Every candidate was rejected because the blue
background contained visible illumination, gradient, or darker patches rather
than a uniform removable chroma field.

The final failed candidate was recovered without regeneration using deterministic
border-sampled chroma removal, soft matte, and despill. It then passed component
extraction with eight frames, zero edge pixels, 0–3 chroma-adjacent pixels per
frame, and no row errors or warnings.

## Next allowed action

Use the complete atlas and smoke candidate under `phase4/helios/` for joint
review and controlled local runtime verification. Do not regenerate accepted
rows unless a true runtime defect is observed.
