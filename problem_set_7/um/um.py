import re


def main():
    print(count(input("Text: ")))


def count(s):
    """Count the occurrence of the filler word as an integer."""
    return len(re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
