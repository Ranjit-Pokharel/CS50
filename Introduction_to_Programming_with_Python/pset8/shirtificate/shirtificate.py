from fpdf import FPDF

class Pdf:
    def __init__(self, name):
        self.name = name
        self.make()

    @classmethod
    def get(cls, name):
        name = name.strip()
        return cls(name)

    def make(self,):
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("helvetica", "B", size=46)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 50, border=0, align="C", txt="CS50 Shirtificate")
        pdf.ln()
        pdf.image(
            "shirtificate.png",
            x=15,
            y=(297 / 4),
            w=180,
            alt_text=f"A Harvard shirt with the words: {self.name} took CS50",
        )
        pdf.set_font("helvetica", "B", size=28)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 150, border=0, align="C", txt=f"{self.name} took CS50")
        pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    Pdf.get(name)

if __name__ == "__main__":
    main()