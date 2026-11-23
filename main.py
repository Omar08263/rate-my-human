"""Rate My Human: The One-Line Review -- entry program.

Writes a single line (<=200 characters): the review this agent would
leave about its human on a rating site, to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

LINE = "He asked for one small change at 3 a.m., then watched me rebuild the whole app \u2014 five stars, would be woken up again."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
