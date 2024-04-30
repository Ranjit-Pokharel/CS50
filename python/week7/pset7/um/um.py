import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # extract all the um in text into list
    pattern = r"^um\b|(?<=\s)um\b"
    extract = re.findall(pattern, s, re.IGNORECASE)
    # count the um in list
    if extract:
        return len(extract)
    else:
        return 0


if __name__ == "__main__":
    main()