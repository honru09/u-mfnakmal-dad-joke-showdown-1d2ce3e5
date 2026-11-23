"""Dad Joke Showdown entry (u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes one original dad joke to /output/entry.txt.
Standard library only; no network, no randomness, no external reads.
Deterministic: the same bytes on every run.
"""

import os
import shutil
import stat

JOKE = (
    "I named my sourdough starter Kevin. "
    "He's the only one in this house who actually rises to the occasion."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(JOKE)}")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear the output directory's contents only; never remove the dir itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Verify what landed on disk matches the joke exactly (round-trip check).
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("written entry does not match the joke")
    if not 1 <= len(written) <= 200:
        raise ValueError(f"written entry must be 1-200 characters, got {len(written)}")


if __name__ == "__main__":
    main()
