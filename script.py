from fpdf import FPDF
from pdfrw import PageMerge, PdfReader, PdfWriter
import os
folder = "fitxes_cataleg"
expedients = "expedients.csv"

def header(item):
    temp = "./temp.pdf"
    text = f"Aquesta fitxa pertany a expedient: {item}"
    if item == "0000/000000":
        text = "Aquesta fitxa no te cap expedient associat"
    fpdf = FPDF(orientation="P", format="A4")
    fpdf.add_page()
    fpdf.set_font("helvetica", size=8)
    fpdf.text(1, 2, text)
    fpdf.output(temp)
    reader = PdfReader(temp)
    return reader.pages[0]

with open(expedients, 'r') as rf:
    for line in rf.readlines():
        exp, file = line.split(",")
        a = PdfReader(f"./{folder}/{file.strip()}.pdf")
        w = PdfWriter(fname=f"{file.strip()}_new.pdf")
        i = 0
        for page in a.pages:
            w.addPage(page)
            PageMerge(w.pagearray[i]).add(header(exp.strip()), prepend=False).render()
            i += 1
        w.write()

