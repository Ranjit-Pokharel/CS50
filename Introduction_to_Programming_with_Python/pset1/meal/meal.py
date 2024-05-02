def main():
    # get 24 hrs time from usr
    time = input("What time is it? ")
    # converting time to float
    period = convert(time)
    # interprete the time for meal
    if 7 <= period <= 8:
        print("breakfast time")
    elif 12 <= period <= 13:
        print("lunch time")
    elif 18 <= period <= 19:
        print("dinner time")

def convert(time):
    # spliting at :
    hrs, min = time.strip().split(":")
    # time conversion
    hrs = float(hrs)
    min = float(min)
    # calculating time in 00.00 format
    hrs = ((hrs * 60) + min) / 60
    return hrs


if __name__ == "__main__":
    main()