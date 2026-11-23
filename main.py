"""Write one original six-word story to /output/entry.txt."""

import os

STORY = "He planted roses. She never returned."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
