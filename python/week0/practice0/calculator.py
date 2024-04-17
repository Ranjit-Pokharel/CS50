"""
calculator.
Author: Ranjit-Pokharel
E-Mail: rp.ranjitpokharel.pr@gmail.com
status: inprogress
"""

class Calculate:
    """
    a calculator class
    ...

    Methods
    -------
    square(num: float)
        gives the square of the number
    """

    def __init__(self,) -> None:
        pass

    def square(self, num: float) -> float:
        """
        gives square of given number
        ...

        Parameters
        ----------
        num : float
            the number that needs to be square

        Returns
        -------
        float
            the squared number
        """
        return num * num
    

def main() -> None:
    # get the number
    number: float = float(input("Number: "))
    # calculator object
    cal: Calculate = Calculate()
    # printing the square of number
    print(f"{number} square is {cal.square(number)}")

if __name__ == "__main__":
    main()