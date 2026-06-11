import pypdf

pdf_path = "/Users/sebastianlilliecreutz/Downloads/2026_Vision_The_Maker_Tour.pdf"
try:
    reader = pypdf.PdfReader(pdf_path)
    print("Metadata:", reader.metadata)
    print("Number of pages:", len(reader.pages))
    for i, page in enumerate(reader.pages):
        print(f"\n--- Page {i+1} ---")
        text = page.extract_text()
        print(f"Extracted text length: {len(text)}")
        if text.strip():
            print("Snippet:", text[:200].strip())
        print("Images:", len(page.images))
except Exception as e:
    print("Error:", e)
