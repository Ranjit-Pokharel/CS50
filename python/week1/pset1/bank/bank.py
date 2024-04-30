class Bank:
    def __init__(self, greet: str) -> None:
        self.greet = greet.lower().strip()

    def calculate(self,) -> int:
        if self.greet.startswith("hello"):
            return 0
        elif self.greet.startswith("h"):
            return 20
        
        return 100


def main():
    # Greet the user
    greet = Bank(input("Greeting: "))

    # display price
    print(f"${greet.calculate()}")


if __name__ == "__main__":
    main()