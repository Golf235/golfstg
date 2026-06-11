import os

html_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
files = ["technology.html", "innovation.html", "material.html", "production.html"]

target = '<section class="mag-more-section next-read-section"'
replacement = '<section id="next-read" class="mag-more-section next-read-section"'

for filename in files:
    path = os.path.join(html_dir, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        if target in content and replacement not in content:
            new_content = content.replace(target, replacement, 1)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Skipped {filename} (already updated or target not found)")
