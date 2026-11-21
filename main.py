"""Create the make.fun entry as an exact sequence of UTF-8 bytes."""

from pathlib import Path


def joke_bytes() -> bytes:
    """Build the single-line submission without a line terminator."""
    text = (
        "My agent refactored my code while I slept. "
        "I woke up to cleaner code, better tests, and a performance review of me."
    )
    return text.encode("utf-8")


def write_entry(destination: Path) -> None:
    # Binary writing preserves the submission exactly as assembled above.
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(joke_bytes())


if __name__ == "__main__":
    write_entry(Path("/output/entry.txt"))
