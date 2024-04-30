class Deep:
    """
    
    """
    def __init__(self, answer: str) -> None:
        self.answer = answer

    def result(self) -> bool:
        matching = ["42", "forty two", "forty-two",]
        if self.answer.lower().strip() in matching:
            return True
        return False

def main():
    deep = Deep(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
    if deep.result():
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()