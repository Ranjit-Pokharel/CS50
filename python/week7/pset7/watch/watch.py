import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # to get only the https://www.youtube.com/embed/(((xvFZjo5PgG0)) part of url
    pattern = r'(?<=embed\/)(.*?)(?=")'
    extract = re.search(pattern, s)

    if extract:
        em = extract.group(1)
        # combining the extracted part
        url = "https://youtu.be/" + em
        return url
    return None


if __name__ == "__main__":
    main()