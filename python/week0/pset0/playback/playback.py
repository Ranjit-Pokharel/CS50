"""
implemention of a program in Python that prompts the user for input 
and then outputs that same input, replacing each space with (...).

Github: Ranjit-Pokharel
E-Mail: rp.ranjitpokharel.pr@gmail.com
"""

class PlayBack:
    """
    a PlayBack class
    ...

    Attributes
    ----------
    text : str
        text to be converted.

    Methods
    -------
    speed(replace_with: str)->str
        replace space with replacer default (...)
    """
    def __init__(self, text: str) -> None:
        """
        Parameters
        ----------
        text : str
            The input text to be converted.
        """
        self.text: str = text

    def speed(self, replace_with: str="...") -> str:
        """
        Replace space with given str default (...)
        ...

        Parameters
        ----------
        replace_with : str
            the replacer

        Returns
        -------
        str
            the speed down text
        """
        return self.text.replace(" ", replace_with)


def main() -> None:
    text: PlayBack = PlayBack(input())
    print(text.speed("..."))


if __name__ == "__main__":
    main()