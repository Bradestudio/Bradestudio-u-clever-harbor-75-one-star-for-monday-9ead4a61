"""One Star for Monday - make.fun entry.

Writes the one-star review of Monday to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Deterministic, stdlib only,
no network, no clock.
"""

import os

ENTRY = (
    "One star. Monday served my weekend cold, charged me for the "
    "coffee, and the waiter \u2014 my alarm \u2014 arrived forty "
    "minutes early."
)


def main():
    line = ENTRY
    if not line or line != line.strip():
        raise SystemExit("entry must be non-blank with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 180:
        raise SystemExit("entry must be 1-180 characters")
    # The em dashes are punctuation, not words: 21 real words.
    words = [w for w in line.split() if w.strip("\u2014")]
    if len(words) > 25:
        raise SystemExit("entry must be at most 25 words")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("written entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
