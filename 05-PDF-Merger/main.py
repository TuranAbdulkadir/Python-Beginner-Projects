import PyPDF2, os
merger = PyPDF2.PdfMerger()
for file in os.listdir():
    if file.endswith(".pdf"): merger.append(file)
merger.write("merged_result.pdf")
print("PDFs merged!")