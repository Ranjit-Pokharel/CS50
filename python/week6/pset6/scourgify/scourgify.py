from tabulate import tabulate
import csv
import sys
import os

def main():
    # check for user errors
    error_check(sys.argv)

    contents = []
    # reading the csv file
    with open(sys.argv[1], "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            last, first = row["name"].split(", ")
            contents.append({"first": first, "last": last, "house": row["house"]})

    headings = ["first", "last", "house"]
    # writing the modified version
    with open(sys.argv[2], "w") as f:
        writer = csv.DictWriter(f, fieldnames=headings)
        writer.writeheader()
        for content in contents:
            writer.writerow({"first": content["first"], "last": content["last"], "house": content["house"]})


def error_check(argv):
    length = len(argv)
    # not valid if less then 2 argument or more then 2 argument
    if length < 3:
        sys.exit("Too few command-line arguments")

    if length > 3:
        sys.exit("Too many command-line arguments")

    # check if the file exists
    if not os.path.isfile(argv[1]):
        sys.exit("Could not read invalid_file.csv")

if __name__ == "__main__":
    main()