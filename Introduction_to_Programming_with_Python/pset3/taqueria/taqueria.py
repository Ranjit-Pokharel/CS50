
def main():
    # Define the menu with item names and their corresponding prices
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    get_order(menu)


def get_order(menu):
    # initial order price
    orders_price = 0
    while True:
        try:
            # Prompt the user for an item (case insensitive)
            user_input = input("Item: ").lower().title()
            # if the order is in menu
            if user_input in menu:
                # add the price
                orders_price += menu[user_input]
                # display price
                print(f"Total: ${orders_price:.2f}")
        except EOFError:
            # move to new line and break on ctrl+D
            print()
            break

if __name__ == "__main__":
    main()
