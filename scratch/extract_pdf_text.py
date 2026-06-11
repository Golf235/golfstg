import sys

try:
    import PyPDF2
    print("PyPDF2 is installed")
except ImportError:
    print("PyPDF2 is NOT installed")

try:
    import pdfplumber
    print("pdfplumber is installed")
except ImportError:
    print("pdfplumber is NOT installed")

try:
    import pypdf
    print("pypdf is installed")
except ImportError:
    print("pypdf is NOT installed")

# Try to extract text using whatever is available
pdf_path = "/Users/sebastianlilliecreutz/Downloads/2026_Vision_The_Maker_Tour.pdf"
text = ""

# Try to extract text using whatever is available
pdf_path = "/Users/sebastianlilliecreutz/Downloads/2026_Vision_The_Maker_Tour.pdf"
text = ""

try:
    import pypdf
    reader = pypdf.PdfReader(pdf_path)
    print(f"pypdf: Found {len(reader.pages)} pages")
    for i, page in enumerate(reader.pages):
        t = page.extract_text()
        if t:
            text += f"\n--- Page {i+1} ---\n" + t
except Exception as e:
    print("Error with pypdf:", e)

if text:
    with open("scratch/pdf_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully extracted PDF text to scratch/pdf_text.txt")
else:
    print("Could not extract PDF text.")
