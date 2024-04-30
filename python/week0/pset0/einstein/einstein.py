"""
a program in Python that prompts the user for mass as an integer (in kilograms) 
and then outputs the equivalent number of Joules as an integer. 
Assume that the user will input an integer.

Github: Ranjit-Pokharel
E-Mail: rp.ranjitpokharel.pr@gmail.com
"""

class Einstein:
    """
    e = m*c*c
    ...

    Attributes
    ----------
    mass : int
        mass to be converted.

    Methods
    -------
    joules()->int
        convert mass to Joules
    """
    def __init__(self, mass: int, c: int=300000000) -> None:
        """
        Parameters
        ----------
        mass: int 
            mass of object.
        c: int (300000000)
            speed 
        """
        self.mass: int = mass
        self.c: int = c

    def joules(self) -> int:
        """
        e=m*c*c

        Returns
        -------
        int
            return energy joules
        """
        return self.mass * self.c * self.c
    
def main()-> None:
    energy: Einstein = Einstein(int(input("m: ")))
    print(f"E: {energy.joules()}")

if __name__ == "__main__":
    main()