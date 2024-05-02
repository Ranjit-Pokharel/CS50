"""
implemention accepts a str as input and returns that same input with any 
:) converted to 🙂 and any :( converted to 🙁
Github: Ranjit-Pokharel
E-Mail: rp.ranjitpokharel.pr@gmail.com
"""

class Faces:
    """
    a Faces class
    ...

    Attributes
    ----------
    text : str
        text contaning emoticon to be converted.

    Methods
    -------
    convert()->str
        convert the emoticon
    """

    def __init__(self, text: str) -> None:
        """
        Parameters
        ----------
        text : str
            The input text to be converted.
        """
        self.text: str = text

    def convert(self,) -> str:
        """
        Replace the emoticon

        Returns
        -------
        str
            the converted text
        """
        return self.text.replace(":)", "🙂").replace(":(", "🙁")
    
def main() -> None:
    text: Faces = Faces(input())
    print(text.convert())

if __name__ == "__main__":
    main()