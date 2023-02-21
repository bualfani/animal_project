from fpdf import FPDF as fp
import glob
from pathlib import Path


pdf = fp(orientation='P', unit='mm', format='A4')

gb = glob.glob("files/*.txt")

for files in gb:
    pdf.add_page()

    filenames = Path(files).stem
    pdf.set_font(family="Times", style='B', size=24)
    pdf.cell(w=50, h=12, txt=f"{filenames.capitalize()}", ln=1)

    with open(files, 'r') as file:
        line = file.read()

    pdf.set_font(family="Times", size=15)
    pdf.cell(w=0, h=8, txt=line)


pdf.output("animal.pdf")
