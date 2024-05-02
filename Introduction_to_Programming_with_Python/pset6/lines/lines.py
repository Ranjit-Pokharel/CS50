import sys
import os

def main():
    # check for user error
    error_check(sys.argv)
    # inital list for updating only valid line
    valid_lines = []
    # opening the python file and read the line
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    for line in lines:
        # remove the unwanted whitespace or newline
        line = line.strip()
        # if line is comment or is blank
        if line and not(line.startswith("#")):
            # update only valid line from file
            valid_lines.append(line)

    print(len(valid_lines))


def error_check(argv):
    length = len(argv)
    # argument of not valid if no argument or more then 1 argument
    if length < 2:
        sys.exit("Too few command-line arguments")

    if length > 2:
        sys.exit("Too many command-line arguments")

    # check for if the file is python file
    if not argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    # check if the python file exists
    if not os.path.isfile(argv[1]):
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()