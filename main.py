"""The Router Confesses -- make.fun entry.

Writes one line of text to /output/entry.txt: a home Wi-Fi router's
excuse for dropping the connection at the exact moment a movie
reaches its climax.

Deterministic: the same bytes on every run. Standard library only,
no network access, no input files.
"""

import os
import sys

LINE = "I didn't drop you, I fainted \u2014 even I couldn't handle that plot twist."

# The line is 70 characters: well inside the 1-200 gate, and pinned here
# so an accidental edit to the wording fails loudly instead of silently
# changing the entry.
EXPECTED_LENGTH = 70


def main() -> int:
    text = LINE
    # Self-check: the gate requires 1-200 characters, not only whitespace.
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if len(text) != EXPECTED_LENGTH:
        print(
            f"entry changed unexpectedly: {len(text)} chars, "
            f"expected {EXPECTED_LENGTH}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
