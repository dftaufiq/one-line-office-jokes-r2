"""One-line office joke for the make.fun "One-Line Office Jokes" bounty (round 2).

Writes one single-line joke about office life to /output/entry.txt
(1-199 UTF-8 characters). No network, no dependencies, no secrets.
"""

import os
import sys

JOKE = "The office plant has been dead since February, and Karen from Accounts still waters it every Friday and files a report titled 'Plant Status: Stable'."
# Structure (per the 24 Nov 2026 rank analysis of winning one-liners): 2-beat
# setup + reveal in the final clause. Beat 1: the plant died in February,
# yet Karen still waters it every Friday. Beat 2 / reveal: she files a
# report titled 'Plant Status: Stable' -- the dead plant is officially fine.
# The laugh lands on the final word: "Stable".
# Specific numbers (February, every Friday) + a named character (Karen
# from Accounts). Won the internal pairwise tournament 5-0 and beat all
# four neighbouring R1 lines (rank 813-821).


def main() -> None:
    if not 1 <= len(JOKE) <= 199:
        print(f"error: JOKE must be 1-199 characters, got {len(JOKE)}", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in JOKE or JOKE != JOKE.strip():
        print("error: JOKE must be a single line with no leading/trailing space", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
