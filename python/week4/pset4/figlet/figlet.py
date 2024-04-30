import pyfiglet
import sys
import random

def main():
    # user errors handeling
    errors_check(sys.argv)
    # user inputs
    text = input("Input: ")
    # converting usr text to figlet text
    figlet_text = convert(text, sys.argv)
    # display figlet text
    print(f"Output:\n{figlet_text}")

def convert(text, argv):
    length = len(argv)
    # if no fonts is given
    if length == 1:
        # get list of fonts
        fonts = pyfiglet.FigletFont.getFonts()
        # chose random font from list
        fonts = random.choice(fonts)
        # return the converted text with random font
        return pyfiglet.Figlet(fonts).renderText(text)
    else:
        # user define font
        fonts = argv[2]
        # return converted text user defined fonts
        return pyfiglet.Figlet(fonts).renderText(text)

def errors_check(argv):
    # either no fonts should be given [figlet.py] or font name [figlet.py -f or --font font_name]
    if not len(argv) in [1 , 3]:
        sys.exit("Invalid usage")

    if len(argv) == 3:
        # uses -f or --font
        if not argv[1] in ["-f", "--font"]:
            sys.exit("Invalid usage")
        # check if font name is valid
        try:
            pyfiglet.Figlet(font=argv[2])
        except pyfiglet.FontNotFound:
            sys.exit("Invalid usage")




if __name__ == "__main__":
    main()