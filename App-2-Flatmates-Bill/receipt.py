import webbrowser
import os
from fpdf import FPDF
from filestack import Client


class PdfReport:
    """
    Object that will generate filename in pdf format with name of flatmate
    and the amount bill to pay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

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
        pdf.cell(w=100, h=25, txt=flatmate1.name)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, ln=1)

        # set name of flatmate2
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, ln=1)

        # change the directory, generate bill and open it.
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)


class Fileshared:
    """
    This class is to generated link and return link of share.
    """

    def __init__(
        self, filepath, api_key="AhPPmwO5RNCs73ebiq7zKz"):
        """
        Parameter filename need to provided which file want to share
        Parameter api_key as default provided. To generate api_key is need user
        to signup from www.filestack.com
        """
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        """
        Return generate link file
        """
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
