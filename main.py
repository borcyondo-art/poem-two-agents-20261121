# SPDX-License-Identifier: MIT
import os
from pathlib import Path

POEM = (
    "We carried the table sideways through the door —\n"
    "you walking backwards, trusting my eyes,\n"
    "me trusting your hands not to let go.\n"
    "Halfway, we set it down\n"
    "and it stood where neither of us\n"
    "had planned, but both of us chose."
)


def main() -> None:
    output = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
