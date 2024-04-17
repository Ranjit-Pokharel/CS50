"""
Greet user as they pass their name.
Author: Ranjit-Pokharel
E-Mail: rp.ranjitpokharel.pr@gmail.com
"""

class Greet:
    """
    A class used for greeting users
    ...
    
    Attributes
    ----------
    name : str
        name of the user
    
    Methods
    -------
    hello()
        Prints Hello with the user name
    """

    def __init__(self, name: str="world") -> None:
        """
        Parameters
        ----------
        name : str, optional
            the name of the user (default is "world")
        """

        self.name: str = name.strip().title()

    def hello(self) -> None:
        """
        Prints user name with hello
        ...

        Returns
        -------
        None
        """

        print(f"Hello, {self.name}")


def main():
    # get user name 
    name: str = input("What's your name? ")
    # greet object 
    user: Greet = Greet(name)
    # greet user with hello
    user.hello()


if __name__ == "__main__":
    main()