import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # pattern to get hrs:min am or pm
    reg = r"^([0-9]|1[0-2]):?([0-5][0-9])? ([A|P]M)? to ([0-9]|1[0-2]):?([0-5][0-9])? ([A|P]M)?$"
    # extract the time
    extract = re.search(reg, s)

    times = []
    time_24 = []
    if extract:
        # divide the whole extract to 2 time
        times.append(extract.groups()[:3])
        times.append(extract.groups()[3:])
    else:
        # if pattern doesnot match invalid
        raise ValueError

    # converting to 24 hrs format
    for time in times:
        # if pm adding 12 hrs
        if "PM" in time:
            # if it not 12:00 pm
            if time[0] != "12":
                hrs = int(time[0]) + 12
            else:
                hrs = time[0]
        else:
            hrs = int(time[0])
            # after 11:59 pm the time in 24 hrs should be 00:00 and not 12:00 am
            if time[0] == "12":
                hrs = 00
        # if min is not extracted then min is 00
        if time[1]:
            min = time[1]
        else:
            min = "00"
        time_24.append(f"{hrs:02}:{min}")

    return f"{time_24[0]} to {time_24[1]}"


if __name__ == "__main__":
    main()