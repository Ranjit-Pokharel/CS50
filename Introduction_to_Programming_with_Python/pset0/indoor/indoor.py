"""
print the given text in lower case.
Github: Ranjit-Pokharel
E-Mail: rp.ranjitpokharel.pr@gmail.com
"""

class Lower:
    """
    A class to convert text to lowercase.
    ...
    
    Attributes
    ----------
    text : str
        text to be converted.
    
    Methods
    -------
    convert_to_lower()
        Converts the stored text to lowercase.
    """

    def __init__(self, text: str) -> None:
        """
        Parameters
        ----------
        text : str
            The input text to be converted.
        """
        self.text: str = text

    def convert_to_lower(self,) -> str:
        """
        Converts the stored text to lowercase.
        
        Returns
        -------
        str
            The converted lowercase text.
        """
        return self.text.lower()


def main() -> None:
    indoor: Lower = Lower(input())
    
    print(indoor.convert_to_lower())


if __name__ == "__main__":
    main()
