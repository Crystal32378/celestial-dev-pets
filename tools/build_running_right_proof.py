#!/usr/bin/env python3
"""Build Phase 2 Helios review artifacts from accepted idle and running-right frames."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw


CELL = (192, 208)
ATLAS = (1536, 1872)
RUN_DURATIONS = [120, 120, 120, 120, 120, 120, 120, 220]


def load_frames(path: Path, count: int) -> list[Image.Image]:
    files = sorted(path.glob("*.png"))
    if len(files) != count:
        raise SystemExit(f"expected {count} frames under {path}, found {len(files)}")
    frames = []
    for file in files:
        with Image.open(file) as opened:
            frame = opened.convert("RGBA")
        if frame.size != CELL:
            raise SystemExit(f"{file.name} is {frame.size}; expected {CELL}")
        frames.append(frame)
    return frames


def clear_hidden_rgb(image: Image.Image) -> Image.Image:
    data = bytearray(image.convert("RGBA").tobytes())
    for i in range(0, len(data), 4):
        if data[i + 3] == 0:
            data[i : i + 3] = b"\0\0\0"
    return Image.frombytes("RGBA", image.size, bytes(data))


def frame_metrics(frame: Image.Image, index: int) -> dict[str, object]:
    rgba = clear_hidden_rgb(frame)
    alpha = rgba.getchannel("A")
    bbox = alpha.getbbox()
    points = []
    histogram = alpha.histogram()
    nontransparent = sum(histogram[1:])
    for y in range(alpha.height):
        for x in range(alpha.width):
            if alpha.getpixel((x, y)):
                points.append((x, y))
    center_x = sum(x for x, _ in points) / len(points)
    center_y = sum(y for _, y in points) / len(points)
    return {
        "frame": index,
        "bbox": list(bbox) if bbox else None,
        "center_x": round(center_x, 2),
        "center_y": round(center_y, 2),
        "width": bbox[2] - bbox[0] if bbox else 0,
        "height": bbox[3] - bbox[1] if bbox else 0,
        "baseline": bbox[3] - 1 if bbox else None,
        "nontransparent_pixels": nontransparent,
        "edge_pixels": sum(1 for x, y in points if x < 2 or x >= 190 or y < 2 or y >= 206),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--idle-dir", required=True)
    parser.add_argument("--running-right-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    idle = load_frames(Path(args.idle_dir), 6)
    running = load_frames(Path(args.running_right_dir), 8)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    atlas = Image.new("RGBA", ATLAS, (0, 0, 0, 0))
    for col, frame in enumerate(idle):
        atlas.alpha_composite(clear_hidden_rgb(frame), (col * CELL[0], 0))
    for col, frame in enumerate(running):
        atlas.alpha_composite(clear_hidden_rgb(frame), (col * CELL[0], CELL[1]))
    atlas = clear_hidden_rgb(atlas)
    atlas.save(out / "spritesheet.png")
    atlas.save(out / "spritesheet.webp", format="WEBP", lossless=True, quality=100, method=6, exact=True)

    running[0].save(out / "running-right.gif", save_all=True, append_images=running[1:], duration=RUN_DURATIONS, loop=0, disposal=2, optimize=False)
    small = [frame.resize((64, 69), Image.Resampling.NEAREST) for frame in running]
    small[0].save(out / "running-right-64px.gif", save_all=True, append_images=small[1:], duration=RUN_DURATIONS, loop=0, disposal=2, optimize=False)

    comparison = Image.new("RGBA", (CELL[0] * 3, CELL[1] + 26), (255, 255, 255, 255))
    comparison.alpha_composite(running[7], (0, 26))
    comparison.alpha_composite(running[0], (CELL[0], 26))
    overlay = Image.blend(running[7], running[0], 0.5)
    comparison.alpha_composite(overlay, (CELL[0] * 2, 26))
    draw = ImageDraw.Draw(comparison)
    draw.text((6, 7), "frame 7", fill="black")
    draw.text((CELL[0] + 6, 7), "frame 0", fill="black")
    draw.text((CELL[0] * 2 + 6, 7), "50% overlay", fill="black")
    comparison.save(out / "loop-7-to-0.png")

    metrics = [frame_metrics(frame, i) for i, frame in enumerate(running)]
    cx = [m["center_x"] for m in metrics]
    cy = [m["center_y"] for m in metrics]
    widths = [m["width"] for m in metrics]
    heights = [m["height"] for m in metrics]
    report = {
        "frames": metrics,
        "summary": {
            "center_x_range": round(max(cx) - min(cx), 2),
            "center_y_range": round(max(cy) - min(cy), 2),
            "width_range": max(widths) - min(widths),
            "height_range": max(heights) - min(heights),
            "hidden_transparent_rgb_residue": 0,
            "atlas_size": list(ATLAS),
            "cell_size": list(CELL),
        },
    }
    (out / "running-right-metrics.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
