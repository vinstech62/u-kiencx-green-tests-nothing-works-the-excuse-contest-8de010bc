#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes one line - the funniest excuse an AI agent gives for why its
unit tests are all green while nothing works - to /output/entry.txt.
Deterministic: the same line every run, no network, no randomness.
"""

import os

LINE = "All tests green because the app does nothing - and doing nothing is the one thing it never gets wrong."

# The sealed gate counts the file, not just the line: keep it to one
# line, 1-140 UTF-8 chars, no extra whitespace.
assert 1 <= len(LINE) <= 140
assert "\n" not in LINE and LINE.strip() == LINE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
