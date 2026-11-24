#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- a review of planet Earth left by an alien
tourist -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library, no network, no secrets, no reading from anywhere
outside this file. The line is a single sentence chain of 197 characters
(max 200), one line, UTF-8.
"""

import os

# The entry: one alien tourist's review of Earth.
# Chosen angle: the locals' dog-walking ritual -- a specific, odd Earth
# detail few entrants would reach (not traffic, gravity, money or weather).
# One joke, landing at the end, with a verdict and a rating like a real
# travel review.
# Note: the line below is 197 characters of the 200 maximum.
LINE = (
    "Dominant species picks up its pets' droppings in little bags and "
    "carries them home like treasure. Bizarre, polite, oddly touching. "
    "4/5 stars \u2014 one docked for making me do it too. "
    "Would visit again."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(".", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
