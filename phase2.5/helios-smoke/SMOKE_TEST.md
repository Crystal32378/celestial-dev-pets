# Helios Phase 2.5 Local Runtime Smoke Test

Status: `PASS — completed rows verified; blank-state disappearance observed`

Date: 2026-07-11  
Installed identity: `helios-smoke`  
Install path: `~/.codex/pets/helios-smoke/`

## Confirmed in the real Codex App

- Custom pet discovery: PASS.
- Custom pet load: PASS.
- Visible rendering in the live Codex UI: PASS.
- UI scale and small-size recognition: PASS.
- Transparent background: PASS by screenshot inspection.
- Bottom-right positioning: PASS.
- Cropping and cell containment: PASS in the captured state.
- Wrong-row display: not observed in the captured state.
- Idle blink and loop playback: PASS by direct user observation.
- `running-right` event mapping and playback: PASS. Helios was dragged to the
  left side of the UI, allowed to return to idle, then approached from the
  left; the App moved him right and played the populated row 1 animation.
- Speech or notification bubble: observed as an App-provided overlay rather
  than pixels in the pet atlas.

Runtime evidence was reviewed directly by Crystal. Screenshots are intentionally
not stored in the public repository because they include unrelated desktop and
workspace information.

## Runtime observations

- Pointer approach near the default bottom-right position can make Helios
  temporarily disappear before he can be dragged.
- The overlay remains draggable with a deliberate grab.
- This disappearance is recorded as a state-change observation. It is
  consistent with the App selecting one of the seven unfinished transparent
  rows, but it is not attributed to a specific row without direct evidence.
- The behavior is not classified as a Helios asset defect.
- The speech or notification bubble content and behavior are controlled by the
  Codex App layer; the current four-field custom-pet manifest provides no
  per-pet bubble text, symbol, style, or visibility setting.

No atlas changes or image regeneration are authorized by this smoke test.
