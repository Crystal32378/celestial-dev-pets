# Helios Phase 2.5 Local Runtime Smoke Test

Status: `PARTIAL PASS — event-trigger verification pending`

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

Evidence: [`evidence/codex-runtime-loaded.png`](evidence/codex-runtime-loaded.png)

## Still pending

- Observe the idle animation over time, including its loop.
- Trigger interface movement that selects `running-right` and confirm the
  correct row plays.
- Record whether switching into one of the seven transparent unfinished rows
  makes the pet disappear, which is expected for this partial atlas.

No atlas changes or image regeneration are authorized by this smoke test.
