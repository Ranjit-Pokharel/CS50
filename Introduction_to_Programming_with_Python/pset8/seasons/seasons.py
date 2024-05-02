from datetime import date
import sys
import inflect
import re

p = inflect.engine()

def main():
    # get usr date of birth
    dob = input("Date of Birth: ").strip()
    # validate dob if it in format yyyy-mm-dd
    year, month, day = validate(dob)
    # convert date to min till now and to words
    min_in_word = to_minutes(year, month, day)
    # display converted words
    print(min_in_word)

def validate(date):

    try:
        # using re pattern to validate for yyyy-mm-dd
        pattern = r"^(\d{4})-(0?[0-9]|1[0-2])-([0-2]?[0-9]|3[0-2])$"
        validate = re.search(pattern, date)
        if validate:
            year, month, day = validate.groups()
            # converted to int
            return (int(year), int(month), int(day))
        else:
            # if not valid raise valueerror
            raise ValueError
    except ValueError:
        sys.exit("Invalid date")

def to_minutes(year, month, day):
    # get today date
    today = date.today()
    # get date diffrence
    diff = today - date(year, month, day)
    # converted date to total min
    minutes = diff.days * 24 * 60
    # convert min to words
    return f"{p.number_to_words(minutes)} minutes".capitalize().replace("and ", "")


if __name__ == "__main__":
    main()