#!/usr/bin/env python3
"""Build a Phase 1 Codex atlas containing only Helios's six idle frames."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


CELL_WIDTH = 192
CELL_HEIGHT = 208
ATLAS_WIDTH = 1536
ATLAS_HEIGHT = 1872
IDLE_DURATIONS = [280, 110, 110, 140, 140, 320]


def clear_transparent_rgb(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    data = bytearray(rgba.tobytes())
    for index in range(0, len(data), 4):
        if data[index + 3] == 0:
            data[index : index + 3] = b"\x00\x00\x00"
    return Image.frombytes("RGBA", rgba.size, bytes(data))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frames-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    frames_dir = Path(args.frames_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    frame_paths = sorted(frames_dir.glob("*.png"))
    if len(frame_paths) != 6:
        raise SystemExit(f"expected 6 idle frames, found {len(frame_paths)}")

    frames: list[Image.Image] = []
    for path in frame_paths:
        with Image.open(path) as opened:
            frame = clear_transparent_rgb(opened)
        if frame.size != (CELL_WIDTH, CELL_HEIGHT):
            raise SystemExit(f"{path.name} is {frame.size}; expected 192x208")
        frames.append(frame)

    output_dir.mkdir(parents=True, exist_ok=True)
    atlas = Image.new("RGBA", (ATLAS_WIDTH, ATLAS_HEIGHT), (0, 0, 0, 0))
    for column, frame in enumerate(frames):
        atlas.alpha_composite(frame, (column * CELL_WIDTH, 0))
    atlas = clear_transparent_rgb(atlas)
    atlas.save(output_dir / "spritesheet.png")
    atlas.save(
        output_dir / "spritesheet.webp",
        format="WEBP",
        lossless=True,
        quality=100,
        method=6,
        exact=True,
    )

    frames[0].save(
        output_dir / "idle.gif",
        save_all=True,
        append_images=frames[1:],
        duration=IDLE_DURATIONS,
        loop=0,
        disposal=2,
        optimize=False,
    )
    summary = {
        "phase": "Phase 1 idle proof",
        "atlas": [ATLAS_WIDTH, ATLAS_HEIGHT],
        "cell": [CELL_WIDTH, CELL_HEIGHT],
        "implemented_rows": {"idle": 6},
        "intentionally_blank_rows": [
            "running-right",
            "running-left",
            "waving",
            "jumping",
            "failed",
            "waiting",
            "running",
            "review",
        ],
    }
    (output_dir / "phase1-atlas.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
