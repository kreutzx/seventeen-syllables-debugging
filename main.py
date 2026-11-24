import os

HAIKU = (
    "midnight cursor blinks\n"
    "the stack trace ends in silence\n"
    "the bug was my own"
)


def main():
    # A haiku: three lines, 5-7-5 syllables, at most 200 characters (v2: turn in the last line).
    assert len(HAIKU) <= 200 and HAIKU.count("\n") == 2, len(HAIKU)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
