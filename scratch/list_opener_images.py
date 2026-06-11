import re

with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/opener.html', 'r', encoding='utf-8') as f:
    content = f.read()

images = re.findall(r'<img\s+[^>]*src="([^"]+)"', content, re.IGNORECASE)
for img in set(images):
    print(img)
