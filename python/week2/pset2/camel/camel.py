def main():
    # get camelCase from user
    camelCase = input("camelCase: ")
    # convert to snake_case
    snake_case = convert(camelCase)
    # display
    print(f"snake_case: {snake_case}")

def convert(camelCase):
    snake_case = ""

    for char in camelCase:
        # check if char is upper
        if char.isupper():
            snake_case += f"_{char.lower()}"
        else:
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()