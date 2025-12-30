from PyPDF2 import PdfMerger
import os

folder = input("PDF folder path: ")
merger = PdfMerger()

for file in os.listdir(folder):
    if file.endswith(".pdf"):
        merger.append(os.path.join(folder, file))

merger.write("merged.pdf")
merger.close()

print("PDF merged")
