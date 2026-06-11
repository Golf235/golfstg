import zipfile
import xml.etree.ElementTree as ET
import os
import re

docx_path = "/Users/sebastianlilliecreutz/Downloads/Sales page copy.docx"
extracted_text = []

try:
    with zipfile.ZipFile(docx_path) as z:
        # docx XML namespaces
        namespaces = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
        }
        
        # Read the main document XML
        doc_xml = z.read('word/document.xml')
        root = ET.fromstring(doc_xml)
        
        # Find all text elements <w:t>
        for elem in root.iter():
            if elem.tag.endswith('}t'): # w:t tag ends with }t
                if elem.text:
                    extracted_text.append(elem.text)
                    
    full_text = " ".join(extracted_text)
    
    # Clean up whitespace and join paragraphs (roughly)
    # We can also read paragraph breaks <w:p> to insert newlines, but a simple run of w:t is fine for a search.
    # Let's do a more precise paragraph extraction by iterating over w:p elements:
    paragraphs = []
    root = ET.fromstring(doc_xml)
    body = root.find('w:body', namespaces)
    if body is not None:
        for p in body.findall('.//w:p', namespaces):
            p_text = []
            for t in p.findall('.//w:t', namespaces):
                if t.text:
                    p_text.append(t.text)
            if p_text:
                paragraphs.append("".join(p_text))
                
    full_text_paras = "\n".join(paragraphs)
    
    with open("scratch/docx_text.txt", "w", encoding="utf-8") as f:
        f.write(full_text_paras)
    print("Successfully extracted DOCX paragraphs to scratch/docx_text.txt")
    print(f"Total length: {len(full_text_paras)} characters")
    
    # Search for Maker Tour
    matches = []
    lines = full_text_paras.split('\n')
    for i, line in enumerate(lines):
        if 'maker tour' in line.lower() or 'sergio' in line.lower():
            # grab surrounding lines
            start = max(0, i - 2)
            end = min(len(lines), i + 3)
            context = "\n".join(f"{idx}: {lines[idx]}" for idx in range(start, end))
            matches.append(context)
            
    print(f"\nFound {len(matches)} matching contexts:")
    for idx, match in enumerate(matches[:10]):
        print(f"\n--- Match {idx+1} ---")
        print(match)
        
except Exception as e:
    print("Error reading docx zip:", e)
