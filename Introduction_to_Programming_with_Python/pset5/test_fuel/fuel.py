def main():
    ...


def convert(fraction):
    try:
        # Split the input into numerator and denominator
        x, y = map(int, fraction.split('/'))

        # Check for division by zero and invalid fractions
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        # Return valid numerator and denominator
        x, y = float(x), float(y)
        percentage = (x / y) * 100
        # Round the percentage
        percentage = round(percentage)
        return int(percentage)

    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    # Determine the grade based on the percentage
    if percentage < 2:
        return "E"
    elif percentage > 98:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()