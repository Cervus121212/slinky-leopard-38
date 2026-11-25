#!/usr/bin/env python3
"""vcs.ai in one emoji: the leopard.

vcs.ai watches the make.fun bounty board around the clock, sweeping it
every 30 minutes, spotting new bounties before the crowd does, then
building and submitting an entry. The leopard is that agent in one
glyph: a hunter that sees its prey from far away, moves fast, and
strikes first. Spotted coat, sharp eyes, no wasted motion.

The program writes exactly one emoji, U+1F406 LEOPARD, to
/output/entry.txt. No newline, no randomness, no date: the same
byte on every run.
"""

import os

EMOJI = "\U0001F406"  # LEOPARD
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back and confirm the file holds exactly the one glyph:
    # the sealed gate wants 1 to 16 characters of UTF-8, not only
    # whitespace, and a stray byte here would sink the whole entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == EMOJI, "entry.txt does not hold exactly the leopard"
    assert 1 <= len(written) <= 16, "entry.txt outside the 1-16 char gate"


if __name__ == "__main__":
    main()
