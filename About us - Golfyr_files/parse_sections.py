import re

file_path = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/4969/content.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for <section tags and print their classes or ids to see the layout sections in order
sections = re.findall(r'<section\s+[^>]*class=["\']([^"\']+)["\'][^>]*id=["\']([^"\']*)["\']', content, re.I)
if not sections:
    # Try without ID
    sections = re.findall(r'<section\s+[^>]*class=["\']([^"\']+)["\']', content, re.I)

print("--- SECTIONS FOUND IN ORDER ---")
for idx, s in enumerate(sections):
    if isinstance(s, tuple):
        print(f"Section {idx+1}: Class: '{s[0]}' | ID: '{s[1]}'")
    else:
        print(f"Section {idx+1}: Class: '{s}'")

# Let's search for other major layout tags like <header>, <main>, <footer>
print("\n--- MAJOR LAYOUT TAGS ---")
for tag in ['header', 'main', 'footer']:
    matches = re.findall(rf'<{tag}\b[^>]*>', content, re.I)
    print(f"<{tag}> occurrences: {len(matches)}")
