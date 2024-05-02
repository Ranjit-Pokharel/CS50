import validators

def main():
    email = input("What's your email address? ").strip()

    print(validate(email))

def validate(email):
    # check usr email is valid or not
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()