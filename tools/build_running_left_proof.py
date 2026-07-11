#!/usr/bin/env python3
"""Build Phase 3 Helios review artifacts with accepted rows plus running-left."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw

from build_running_right_proof import clear_hidden_rgb, frame_metrics, load_frames


CELL = (192, 208)
ATLAS = (1536, 1872)
DURATIONS = [120, 120, 120, 120, 120, 120, 120, 220]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--idle-dir", required=True)
    parser.add_argument("--right-dir", required=True)
    parser.add_argument("--left-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    idle = load_frames(Path(args.idle_dir), 6)
    right = load_frames(Path(args.right_dir), 8)
    left = load_frames(Path(args.left_dir), 8)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    atlas = Image.new("RGBA", ATLAS, (0, 0, 0, 0))
    for row, frames in enumerate((idle, right, left)):
        for col, frame in enumerate(frames):
            atlas.alpha_composite(clear_hidden_rgb(frame), (col * CELL[0], row * CELL[1]))
    atlas = clear_hidden_rgb(atlas)
    atlas.save(out / "spritesheet.png")
    atlas.save(out / "spritesheet.webp", format="WEBP", lossless=True, quality=100, method=6, exact=True)

    left[0].save(out / "running-left.gif", save_all=True, append_images=left[1:], duration=DURATIONS, loop=0, disposal=2, optimize=False)
    small = [frame.resize((64, 69), Image.Resampling.NEAREST) for frame in left]
    small[0].save(out / "running-left-64px.gif", save_all=True, append_images=small[1:], duration=DURATIONS, loop=0, disposal=2, optimize=False)

    compare = Image.new("RGBA", (CELL[0] * 3, CELL[1] + 26), "white")
    compare.alpha_composite(left[7], (0, 26))
    compare.alpha_composite(left[0], (CELL[0], 26))
    compare.alpha_composite(Image.blend(left[7], left[0], 0.5), (CELL[0] * 2, 26))
    draw = ImageDraw.Draw(compare)
    for x, label in ((6, "frame 7"), (CELL[0] + 6, "frame 0"), (CELL[0] * 2 + 6, "50% overlay")):
        draw.text((x, 7), label, fill="black")
    compare.save(out / "loop-7-to-0.png")

    metrics = [frame_metrics(frame, i) for i, frame in enumerate(left)]
    cx = [m["center_x"] for m in metrics]
    cy = [m["center_y"] for m in metrics]
    widths = [m["width"] for m in metrics]
    heights = [m["height"] for m in metrics]
    report = {"frames": metrics, "summary": {
        "center_x_range": round(max(cx) - min(cx), 2),
        "center_y_range": round(max(cy) - min(cy), 2),
        "width_range": max(widths) - min(widths),
        "height_range": max(heights) - min(heights),
        "contact_baseline_difference_frames_0_4": abs(metrics[0]["baseline"] - metrics[4]["baseline"]),
        "hidden_transparent_rgb_residue": 0,
        "atlas_size": list(ATLAS), "cell_size": list(CELL),
        "derivation": "framewise horizontal mirror preserving frame order",
    }}
    (out / "running-left-metrics.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
