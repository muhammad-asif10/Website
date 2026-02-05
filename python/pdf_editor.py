from pypdf import PdfReader, PdfWriter

reader = PdfReader("plug-in.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# 🔥 PDF Title (viewer title)
writer.add_metadata({
    "/Title": "plug-in-html"
})

with open("plug-in(html).pdf", "wb") as f:
    writer.write(f)

print("PDF title changed successfully")