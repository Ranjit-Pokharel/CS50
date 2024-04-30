def main():
    text = input("Enter a string of text: ")
    text_without_vowels = shorten(text)
    print(text_without_vowels)

def shorten(word):
    converted_word = ""
    for char in word:
        if char.lower() in "aeiou":
            continue
        converted_word += char
    return converted_word

if __name__ == "__main__":
    main()