def main():
    amount_due = 50
    print(f"Amount Due: {amount_due}")
    # Continue looping until amount due is less than 0
    while amount_due > 0:
        # Prompt the user to insert a coin
        coin = int(input("Insert Coin: "))
        # Check if the inserted coin is a valid (25, 10, or 5 cents)
        if coin in [25, 10, 5]:
            # sub the value of the coin from the total amount due
            amount_due -= coin
            # Inform the user of the updated amount due
            if amount_due >= 0:
                print(f"Amount Due: {amount_due}")
        else:
            print(f"Amount Due: {amount_due}")

    # Calculate the change owed
    change_owed = -1 * amount_due
    # Display the amount of change owed to the user
    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()
