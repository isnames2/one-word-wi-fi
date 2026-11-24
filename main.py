"""One Word for Your Wi-Fi entry.

Writes the single word that best describes home Wi-Fi to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library.
"""

import os
from pathlib import Path

WORD = "Moody"  # Wi-Fi works when it feels like it, and sulks when it doesn't


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
