#!/usr/bin/env python3
"""Mirror accepted rightward cell frames individually without changing timing."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--right-dir", required=True)
    parser.add_argument("--left-dir", required=True)
    args = parser.parse_args()
    right_dir = Path(args.right_dir).expanduser().resolve()
    left_dir = Path(args.left_dir).expanduser().resolve()
    sources = sorted(right_dir.glob("*.png"))
    if len(sources) != 8:
        raise SystemExit(f"expected 8 accepted right frames, found {len(sources)}")
    left_dir.mkdir(parents=True, exist_ok=True)
    for index, source in enumerate(sources):
        with Image.open(source) as opened:
            frame = opened.convert("RGBA")
        if frame.size != (192, 208):
            raise SystemExit(f"{source.name} is {frame.size}; expected 192x208")
        frame.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save(left_dir / f"{index:02d}.png")


if __name__ == "__main__":
    main()
