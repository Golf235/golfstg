import os
import re

directory = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
html_files = [f for f in os.listdir(directory) if f.endswith(".html")]

# Regex to match character before <br> tag (excluding whitespace and >)
br_pattern = re.compile(r'([^\s>])(<br\s*/?>)', re.IGNORECASE)

print("Starting replacement in HTML files...")
for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content, count = br_pattern.subn(r'\1 \2', content)
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {filename}: made {count} replacements.")

print("\nStarting replacement in rebuilt-app.js...")
js_filepath = os.path.join(directory, "rebuilt-app.js")
if os.path.exists(js_filepath):
    with open(js_filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We target translation strings with <br> inside JS quotes
    # E.g. "key": "value<br>value"
    # The same regex will match character before <br> tag (excluding whitespace and >)
    new_content, count = br_pattern.subn(r'\1 \2', content)
    if count > 0:
        with open(js_filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated rebuilt-app.js: made {count} replacements.")
else:
    print("rebuilt-app.js not found.")

print("\nFinished process.")
