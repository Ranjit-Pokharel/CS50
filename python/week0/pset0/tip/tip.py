def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str):
    # TODO
    d = d.strip().replace("$", "")
    return float(d)

def percent_to_float(p: str):
    # TODO
    p = p.strip().replace("%", "")
    return float(p)/100

main()