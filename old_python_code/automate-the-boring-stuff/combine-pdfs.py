#! python3

# combine-pdfs.py
# Combines all the PDFs in the current working directory into
# into a single PDF.

import PyPDF2
import os

pdf_files = []
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdf_files.append(filename)

pdf_writer = PyPDF2.PdfFileWriter()

for filename in pdf_files:
    pdf_file_obj = open(filename, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    for page_number in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_number)
        pdf_writer.addPage(page_number)

pdf_output = ("allminutes.pdf", "wb")
pdf_writer.write(pdf_output)
pdf_output.close()
