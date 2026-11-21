"""Write the joke and verify the saved bytes."""

from pathlib import Path

JOKE = (
    "My agent refactored my code while I slept. "
    "I woke up to cleaner code, better tests, and a performance review of me."
)
DESTINATION = Path("/output/entry.txt")


def save_and_verify(destination: Path, text: str) -> None:
    expected = text.encode("utf-8")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(expected)
    if destination.read_bytes() != expected:
        raise OSError(f"Saved joke does not match the intended bytes: {destination}")


def main() -> None:
    save_and_verify(DESTINATION, JOKE)


if __name__ == "__main__":
    main()
