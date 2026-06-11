import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
all_map_images = {}

for html in html_files:
    with open(html, 'r', encoding='utf-8') as f:
        content = f.read()
    images = re.findall(r'<img\s+[^>]*src="([^"]+)"', content, re.IGNORECASE)
    for img in images:
        if 'map' in img.lower() or 'butler' in img.lower() or 'opener' in img.lower() or 'mover' in img.lower() or 'riser' in img.lower() or 'pitcher' in img.lower() or 'maker' in img.lower() or 'saver' in img.lower():
            if img not in all_map_images:
                all_map_images[img] = []
            all_map_images[img].append(html)

for img, pages in sorted(all_map_images.items()):
    print(f"{img} -> found in {len(pages)} pages: {list(set(pages))}")
