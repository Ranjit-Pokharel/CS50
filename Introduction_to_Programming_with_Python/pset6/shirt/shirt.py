import os
import sys
from PIL import Image, ImageOps

def main():
    error_check(sys.argv)
    shirtificate(sys.argv[1],sys.argv[2])

def shirtificate(before,after):
    shirt = Image.open("shirt.png")
    with Image.open(before) as input:
        input = ImageOps.fit(input, shirt.size)
        input.paste(shirt, mask = shirt)
        input.save(after)

def error_check(argv):
    length = len(argv)
    # not valid if less then 2 argument or more then 2 argument
    if length < 3:
        sys.exit("Too few command-line arguments")

    if length > 3:
        sys.exit("Too many command-line arguments")

    # check for file exists
    for file_name in argv[1:]:
        if "." in file_name:
            file_extention = file_name.split(".")[1]
            if not file_extention.lower() in ["jpg", "jpeg", "png"]:
                sys.exit("Invalid output")

    if argv[1].split(".")[1] != argv[2].split(".")[1]:
        sys.exit("Input and output have different extensions")

    if not os.path.isfile(argv[1]):
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()