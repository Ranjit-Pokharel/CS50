def main():
    # Get a valid fraction from the user
    x, y = get_fraction()

    # Calculate the percentage and print the result
    result = calculate_percentage(x, y)
    print(result)

def get_fraction():
    while True:
        # Prompt the user for a fraction
        fraction = input("Fraction: ")
        try:
            # Split the input into numerator and denominator
            x, y = map(int, fraction.split('/'))

            # Check for division by zero and invalid fractions
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                continue

            # Return valid numerator and denominator
            return x, y
        except (ValueError, ZeroDivisionError):
            pass

def calculate_percentage(x, y):
    # Convert numerator and denominator to float for division
    x, y = float(x), float(y)

    # Calculate the percentage
    percentage = (x / y) * 100

    # Round the percentage
    percentage = round(percentage)

    # Determine the grade based on the percentage
    if percentage < 2:
        return "E"
    elif percentage > 98:
        return "F"
    else:
        return f"{int(percentage)}%"

if __name__ == "__main__":
    # Call the main function
    main()
