import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # pattern for 1st number of ip (255)
    pattern = "(?:(?:25[0-5])|(?:2[0-4][0-9])|(?:[0-1]?[0-9]?[0-9]))"
    reg = r"^"
    # loop to complete pattern with . and ^ $
    for i in range(4):
        if i < 3:
            reg += (pattern + r"\.")
        else:
            reg += (pattern + "$")
    # checking for match
    matches = re.search(reg, ip)
    # if match valid else not
    if matches:
        return True
    return False



if __name__ == "__main__":
    main()