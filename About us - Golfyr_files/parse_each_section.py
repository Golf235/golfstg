import re
import os

file_path = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/4969/content.md'
output_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/About us - Golfyr_files/parsed_sections'
os.makedirs(output_dir, exist_ok=True)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find sections using regex
# We can find sections by splitting at `<section` or using regex to match `<section[^>]*>...</section>`
sections = re.findall(r'(<section\b[^>]*>.*?</section>)', content, re.DOTALL | re.I)

print(f"Total sections found: {len(sections)}")

for idx, sec in enumerate(sections):
    # Determine section class or ID to name the file
    class_match = re.search(r'class=["\']([^"\']+)["\']', sec, re.I)
    id_match = re.search(r'id=["\']([^"\']+)["\']', sec, re.I)
    
    class_name = class_match.group(1).replace(' ', '_') if class_match else 'no_class'
    id_name = id_match.group(1) if id_match else 'no_id'
    
    filename = f"section_{idx+1}_{class_name}_{id_name}.html"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as out_f:
        out_f.write(sec)
        
    print(f"Saved {filepath}")
