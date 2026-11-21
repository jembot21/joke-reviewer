"""Write the competition joke exactly, without extra text or a trailing newline.

The output is the submitted entry, so every character must match the joke.
"""

from pathlib import Path


JOKE = "I asked my coding agent for a one-line fix; it returned a framework, a migration guide, and opinions."


def main() -> None:
    entry_path = Path("/output/entry.txt")
    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
