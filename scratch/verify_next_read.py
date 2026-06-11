import os
import re

html_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
app_js_path = os.path.join(html_dir, "rebuilt-app.js")

tech_pages = {
    "technology.html": "innovation.html",
    "innovation.html": "material.html",
    "material.html": "production.html",
    "production.html": "technology.html"
}

print("=== VERIFYING NEXT READ INTEGRATION ===")

# 1. Verify HTML Files
all_ok = True
for filename, next_target in tech_pages.items():
    filepath = os.path.join(html_dir, filename)
    if not os.path.exists(filepath):
        print(f"[ERROR] File does not exist: {filename}")
        all_ok = False
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "next-read-section" not in content:
        print(f"[ERROR] next-read-section class not found in {filename}")
        all_ok = False
        continue
        
    # Check link target
    href_pattern = r'href="\./' + re.escape(next_target) + r'"'
    matches = re.findall(href_pattern, content)
    if len(matches) < 2:
        # We expect at least two links (one for the image, one for the title)
        print(f"[WARNING] Found {len(matches)} links to {next_target} in {filename} (expected at least 2).")
        if len(matches) == 0:
            print(f"[ERROR] No link to {next_target} found in {filename}")
            all_ok = False
    else:
        print(f"[OK] {filename} correctly links to ./{next_target} ({len(matches)} times)")

# 2. Verify JS Translation Keys
if os.path.exists(app_js_path):
    with open(app_js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    required_keys = [
        "next-read-title",
        "next-read-category",
        "next-read-time-1m",
        "next-read-time-2m",
        "next-read-innovation-title",
        "next-read-innovation-desc",
        "next-read-material-title",
        "next-read-material-desc",
        "next-read-production-title",
        "next-read-production-desc",
        "next-read-tech-title",
        "next-read-tech-desc"
    ]
    
    # We expect these keys to be defined twice (once for en, once for de)
    for key in required_keys:
        matches = re.findall(r'"' + re.escape(key) + r'"', js_content)
        if len(matches) < 2:
            print(f"[ERROR] Key '{key}' not found twice in rebuilt-app.js (found {len(matches)} times)")
            all_ok = False
        else:
            print(f"[OK] Key '{key}' defined {len(matches)} times in rebuilt-app.js")
else:
    print(f"[ERROR] rebuilt-app.js not found at {app_js_path}")
    all_ok = False

if all_ok:
    print("\n[SUCCESS] All next-read verification checks passed successfully!")
else:
    print("\n[FAILED] Verification checks failed.")
