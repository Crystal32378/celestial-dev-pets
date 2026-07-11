# Helios Remaining-State Batch Status

Status: `STOPPED — 5/6 rows accepted; failed row blocked on technical format`

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

No failed candidate was ingested. No incomplete full atlas or smoke-package
update was produced. This is one of the user-approved mid-batch stop conditions.

## Next allowed action

Resolve only the `failed` row's background-generation problem. Do not regenerate
the five accepted rows. After a valid failed row exists, compose the complete
nine-row atlas and run one unified visual and technical QA pass.
