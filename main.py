#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes the phone's last words at 1% battery to /output/entry.txt.
One line, at most 199 characters, in the phone's own voice.
"""

SETUP = "To stretch my last 1%, I'm deleting your 6 a.m. alarm."
PAYOFF = "Sleep in \u2014 consider it my severance package."

ENTRY = SETUP + " " + PAYOFF
MAX_CHARS = 199


def main() -> None:
    line = ENTRY.strip()
    if not line or len(line) > MAX_CHARS:
        raise SystemExit("entry must be 1-%d characters, got %d"
                         % (MAX_CHARS, len(line)))
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
