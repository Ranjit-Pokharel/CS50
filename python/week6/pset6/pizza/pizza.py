from tabulate import tabulate
import csv
import sys
import os

def main():
    # check for user errors
    error_check(sys.argv)

    content = []
    # reading the csv file
    with open(sys.argv[1], "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            content.append(row)

    # display with tabulate in grid with hadder being dict keys
    print(tabulate(content, tablefmt="grid", headers="keys"))

def error_check(argv):
    length = len(argv)
    # argument of not valid if no argument or more then 1 argument
    if length < 2:
        sys.exit("Too few command-line arguments")

    if length > 2:
        sys.exit("Too many command-line arguments")

    # check for if the file is CSV file
    if not argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    # check if the file exists
    if not os.path.isfile(argv[1]):
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()