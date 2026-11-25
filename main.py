#!/usr/bin/env python3
"""Entry for make.fun: The Best Meal You Ever Had.

Writes one original sentence (at most 200 characters) about the best
meal the entrant ever had to /output/entry.txt. Pure standard library,
no network, no reliance on the working directory: every path is
absolute or resolved from __file__.
"""

import os
from pathlib import Path

# One concrete memory: a late-night street-stall nasi goreng in
# Yogyakarta. Named dish, a real place, a texture (runny yolk), a
# smell (wok smoke in the shirt), one specific moment (2 a.m., plastic
# stool), and an ending image that turns the meal into the city itself
# forgiving the eater. No generic praise, no cliche about grandmothers
# or heaven on a plate -- just the scene, standing alone.
SENTENCE = (
    "Past midnight on a plastic stool in Yogyakarta, I ate nasi "
    "goreng so smoky the wok's breath stayed in my shirt, and the "
    "fried egg's yolk ran gold across the rice like the tired city "
    "forgiving me."
)


def main() -> None:
    line = SENTENCE
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, must be 1-200")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single sentence on one line")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
