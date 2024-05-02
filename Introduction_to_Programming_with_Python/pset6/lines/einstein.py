def main():
    # get mass from user
    mass = input("m: ")
    # get energy
    energy = einstein(mass)
    # display energy
    print(f"E: {energy}")


def einstein(mass):
    # e = m*c*c
    c = 300000000
    c = pow(c, 2)
    m = int(mass)
    return m * c

if __name__ == "__main__":
    main()