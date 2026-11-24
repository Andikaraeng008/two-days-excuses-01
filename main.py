import os

TEXT = "I was 100% certain the deadline was a suggestion. My confidence interval has since been updated."


def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "gate: 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
