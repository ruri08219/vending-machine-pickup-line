"""Vending Machine Pickup Line — make.fun entry.

Writes one pickup line, spoken by the vending machine itself,
to /output/entry.txt as UTF-8.
"""

import os

LINE = "Press B7 \u2014 my coils are already turning, because your smile is the only snack I can\u2019t stock."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if LINE != LINE.strip():
        raise ValueError("line must not have leading/trailing whitespace")
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data == LINE.encode("utf-8"), "round-trip mismatch"
    assert 1 <= len(data.decode("utf-8")) <= 200
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
