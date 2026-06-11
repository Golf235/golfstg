import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

with open('sevenclubgame.html', 'r', encoding='utf-8') as f:
    seven_html = f.read()

# Extract the golf-map-section HTML from both
index_map = re.search(r'(<section class="golf-map-section".*?</section>)', index_html, re.DOTALL)
seven_map = re.search(r'(<section class="golf-map-section".*?</section>)', seven_html, re.DOTALL)

if not index_map or not seven_map:
    print("Could not extract map sections!")
else:
    index_str = index_map.group(1).strip()
    seven_str = seven_map.group(1).strip()
    
    # Strip whitespace differences
    index_clean = re.sub(r'\s+', ' ', index_str)
    seven_clean = re.sub(r'\s+', ' ', seven_str)
    
    if index_clean == seven_clean:
        print("[PASS] The golf-map-section HTML markup is identical in both files!")
    else:
        print("[FAIL] The HTML markup is NOT identical! Let's print the length differences:")
        print("Index map length:", len(index_str))
        print("Seven map length:", len(seven_str))
        
        # Write both to files for comparison
        with open('scratch/map_index_extracted.html', 'w', encoding='utf-8') as f:
            f.write(index_str)
        with open('scratch/map_seven_extracted.html', 'w', encoding='utf-8') as f:
            f.write(seven_str)
        print("Extracted HTML written to scratch/map_index_extracted.html and scratch/map_seven_extracted.html for visual diff.")
