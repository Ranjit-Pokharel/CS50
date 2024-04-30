def main():
    # Initialize an empty dictionary to store grocery items and their counts.
    grocery_list = {}

    try:
        # Enter a loop to repeatedly prompt the user for items until they press Ctrl-D (EOF).
        while True:
            item = input()
            # Convert input to lowercase to treat it case-insensitively
            item = item.lower()

            if item == "":
                # Exit the loop if the user presses Enter without entering an item
                break

            # If the item is already in the grocery_list, increment its count; otherwise, add it with a count of 1.
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass

    # Print the grocery list in alphabetical order with items in uppercase and their counts.
    for item, count in sorted(grocery_list.items()):
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
