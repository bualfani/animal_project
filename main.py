from fpdf import FPDF as fp
import glob
from pathlib import Path

pdf = fp(orientation='P', unit='mm', format='A4')

gb = glob.glob("Text+Files/*.txt")

for files in gb:
    pdf.add_page()

    filenames = Path(files).stem
    filepath = filenames.split("/")[0]
    pdf.set_font(family="Times", style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"{filepath.capitalize()}", align='L', ln=1)

pdf.output("animal.pdf")
