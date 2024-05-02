def main():
    # all months
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    # use ISO 8601, an international standard that prescribes
    # that dates should be formatted in year-month-day (YYYY-MM-DD) order
    date = valid_date("Date: ", months)
    # display date
    print(date)

def valid_date(prompt, months):
    while True:
        # get user date in September 8, 1636, but 9/8/1636 format
        date = input(prompt)
        if "/" in date:
            month, day, year = date.split("/")
            # if month contain month's name
            try:
                month = int(month)
            except ValueError:
                continue
            day = int(day)
            year = int(year)
            # if day is more then 31 in month
            # also month is more than 12
            if day > 31 or month > 12:
                continue
            return f"{year}-{month:02}-{day:02}"
        else:
            month, day, year = date.split()
            if month in months:
                # find the position number of the month's name
                index = months.index(month)
                # adding 1 as index start from 0 
                index +=1
                if not "," in day:
                    continue
                day = day.replace(",", "")
                day = int(day)
                year = int(year)
                if day > 31 or index > 12:
                    continue
                return f"{year}-{index:02}-{day:02}"

if __name__ == "__main__":
    main()