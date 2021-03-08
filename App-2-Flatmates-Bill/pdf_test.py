from fpdf import FPDF

pdf = FPDF(orientation="P", unit="pt", format="A4")
pdf.add_page()

# Add some text
pdf.set_font(family="Times", style="B", size=24)
pdf.cell(w=0, h=80, txt="Flatmates", align="c", border=1, ln=1)
pdf.cell(w=100, h=40, txt="Period: ", border=1)

pdf.output(name="bill.pdf")
