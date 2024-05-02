import emoji

def main():
    # get text
    text = input("Input: ")
    # converter to emoji
    emoji_text = convert(text)
    # display
    print(f"Output: {emoji_text}")

def convert(txt):
    # get the emoji
    return emoji.emojize(txt)

if __name__ == "__main__":
    main()