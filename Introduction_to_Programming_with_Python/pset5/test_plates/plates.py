def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Plate must start with at least two letters.
    for char in s[:2]:
        if not char.isalpha():
            return False

    # Plate must contain min of 2 and max of 6 characters (letters or numbers)
    if len(s) < 2 or len(s) > 6:
        return False

    # Plates starting number must not be 0
    for char in s:
        if char.isdigit():
            if char == "0":
                return False
            else:
                break

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    for i in range(len(s)):
        if s[i].isdigit():
            for alpha in s[i+1:]:
                if alpha.isalpha():
                    return False

    # No periods, spaces, or punctuation marks are allowed.
    if not s.isalnum():
        return False

    # If all requirements are met, the plate is valid.
    return True

if __name__ == "__main__":
    main()
