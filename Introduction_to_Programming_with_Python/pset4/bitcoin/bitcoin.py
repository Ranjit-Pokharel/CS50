import requests
import sys

def main():
    # check for cli argument from usr
    error_check(sys.argv)

    # api for bitcoin
    api = "https://api.coindesk.com/v1/bpi/currentprice.json"

    # get json file handle for ani error
    try:
        r = requests.get(api)
    except requests.RequestException:
        sys.exit("Something went wrong")

    # bpi contain all country money codes
    money_codes = r.json()["bpi"]
    # needed only usd code
    money_code = money_codes["USD"]
    # get current rate from the required country
    # replace "," for type conversion
    rate = money_code["rate"].replace(",", "")
    # type conversion and calculate
    total_price = float(rate) * float(sys.argv[1])
    # display calculated value with 4 number after decimal and using ","
    print(f"${total_price:,.4f}")


def error_check(argv):
    # if argument is not provided
    if len(argv) != 2:
        sys.exit("Missing command-line argument")
    # check the only positive float argument
    try:
        float(argv[1])
        if float(argv[1]) <= 0:
            raise ValueError
    except ValueError:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()
