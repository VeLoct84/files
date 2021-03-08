import webbrowser
from fpdf import FPDF


class PdfReport:
    """
    Object that will generate filename in pdf format with name of flatmate
    and the amount bill to pay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # setting up pdf format
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # add icon img
        pdf.image(name="files/house.png", w=30, h=30)

        # set font, border, and size font
        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=100, h=80, txt="Flatmates Bills", border=0, align="c", ln=1)

        # set label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=25, txt="Period: ")
        pdf.cell(w=150, h=25, txt=bill.time, ln=1)

        # set name of flatmate1
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, )
        pdf.cell(w=150, h=25,
                 txt=str(round(flatmate1.pays(total_bill, flatmate2), 2)), ln=1
                 )

        # set name of flatmate2
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, )
        pdf.cell(w=150, h=25,
                 txt=str(round(flatmate2.pays(total_bill, flatmate1), 2)), ln=1
                 )

        pdf.output(name=self.filename)
        pdf.open()
