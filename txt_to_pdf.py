import sys

from fpdf import FPDF

txt_file = sys.argv[1]
pdf_file = sys.argv[2]

pdf = FPDF()
pdf.add_page()

with open(txt_file, "r") as file:
    for line in file:
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=line, ln=True)

pdf.output(pdf_file)
