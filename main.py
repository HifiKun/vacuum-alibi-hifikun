"""One-line excuse for make.fun's "The Vacuum's Alibi" bounty.

The whole entry is a single line, at most 200 characters, written to
/output/entry.txt. A robot vacuum explains, deadpan, why it missed a spot:
the crumb under the table has outlasted three firmware updates, so by now
it counts as staff, not dirt.
"""

import os

LINE = (
    "The crumb under the table has survived three firmware updates. "
    "I have decided it is staff, not dirt."
)


def main() -> None:
    # One line: the gate rejects anything over 200 chars or anything
    # that is only white space, and the judge reads a single line.
    text = " ".join(LINE.split())
    assert "\n" not in text, "line must be a single line"
    assert text.strip(), "line must not be only white space"
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
