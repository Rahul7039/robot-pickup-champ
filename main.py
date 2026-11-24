#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Prints the chosen pickup line and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt
(the harness reads that file). The line is a single line of 93 characters.
"""
import os

LINE = "My CAPTCHA keeps asking me to prove I'm not a robot, and around you, I'm starting to fail it."


def main():
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
