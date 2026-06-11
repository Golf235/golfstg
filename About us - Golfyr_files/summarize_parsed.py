import os
import re

dir_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/About us - Golfyr_files/parsed_sections'
files = sorted(os.listdir(dir_path))

for filename in files:
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get length
    length = len(content)
    # Get first 150 chars
    first_chars = ' '.join(content[:250].split())
    # Extract headers (h1, h2, h3, h4)
    headers = re.findall(r'<h[1-6]\b[^>]*>(.*?)</h[1-6]>', content, re.DOTALL | re.I)
    headers_clean = [re.sub(r'<[^>]+>', '', h).strip() for h in headers]
    
    print(f"File: {filename} ({length} bytes)")
    print(f"  First Chars: {first_chars[:120]}...")
    if headers_clean:
        print(f"  Headers: {headers_clean}")
    # Let's search for images
    imgs = re.findall(r'<img[^>]*src=["\']([^"\']+)["\']', content, re.I)
    if not imgs:
        imgs = re.findall(r'data-rocket-src=["\']([^"\']+)["\']', content, re.I)
    if imgs:
        print(f"  Images: {imgs[:5]}")
    print()
