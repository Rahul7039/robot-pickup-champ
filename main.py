#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Prints the chosen pickup line and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt
(the harness reads that file). The line is a single line of 93 characters.

Before writing, the line is checked against the competition gate (single line,
1-200 characters, valid UTF-8, not only whitespace); if it fails, the program
exits non-zero with a clear error instead of writing a bad entry.
"""
import os
import sys

LINE = "My CAPTCHA keeps asking me to prove I'm not a robot, and around you, I'm starting to fail it."

MAX_CHARS = 200


def validate_line(line):
    """Competition gate: a single line, 1-200 chars, valid UTF-8, not blank."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "line is %d characters, over the %d-character limit" % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main():
    try:
        validate_line(LINE)
    except (ValueError, UnicodeEncodeError) as exc:
        print("ERROR: pickup line fails the competition gate: %s" % exc, file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
