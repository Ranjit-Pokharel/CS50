class Extensions:
    def __init__(self, file_name: str) -> None:
        self.name: str= file_name.lower().strip()

        if "." in self.name:
            self.extension = self.name.split(".")[-1]
        else:
            self.extension = "other"

    def evaluate(self) -> str:
        match self.extension:
            case "gif":
                return "image/gif"
            case "jpg" | "jpeg":
                return "image/jpeg"
            case "png":
                return "image/png"
            case "pdf":
                return "application/pdf"
            case "txt":
                return "text/plain"
            case "zip":
                return "application/zip"
            case _:
                return "application/octet-stream"


def main():
    # get file name
    file_type = Extensions(input("File name: "))
    # display file type
    print(file_type.evaluate())


if __name__ == "__main__":
    main()