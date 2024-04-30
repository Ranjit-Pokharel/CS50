import inflect

def main():
    # get names
    names = get_names("Name: ")
    # sing adieu
    text = inflector(names)
    # paly song
    print(text)

def get_names(prompt):
    names = []
    # get names till ctrl+d is press
    while True:
        try:
            name = input(prompt)
            names.append(name)
        except EOFError:
            print()
            break
    return names

def inflector(names):
    # use inflect to join the names with adieu song
    text = "Adieu, adieu, to " + inflect.engine().join(names)
    return text

if __name__ == "__main__":
    main()