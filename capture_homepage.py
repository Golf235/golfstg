import subprocess
import time
import os
import re

# Read index.html
with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract head content
head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
head_content = head_match.group(1) if head_match else ''

# Extract all sections together (clubs slider and maps slider)
section_regex = r'(<section class="volvo-clubs-section" id="shop">.*?</section>\s*<!--.*?-->\s*<section class="volvo-maps-section" id="volvo-maps">.*?</section>)'
clubs_match = re.search(section_regex, content, re.DOTALL)
clubs_content = clubs_match.group(1) if clubs_match else ''

if not clubs_content:
    print("Error: Could not extract volvo-clubs-section and volvo-maps-section from index.html!")
    exit(1)

# Build HTML page
homepage_only_html = """<!DOCTYPE html>
<html lang="en">
<head>
    __HEAD__
    <style>
        body {
            background: #ffffff !important;
            margin: 0;
            padding: 0;
        }
        .volvo-clubs-section, .volvo-maps-section {
            min-height: 900px !important;
            height: 900px !important;
        }
    </style>
    <!-- Include Swiper JS since the slider needs JS to initialize -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script src="./rebuilt-app.js" defer></script>
</head>
<body>
    <div style="padding: 20px 0;">
        __CONTENT__
    </div>
</body>
</html>
"""

homepage_only_html = homepage_only_html.replace('__HEAD__', head_content).replace('__CONTENT__', clubs_content)

temp_file_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_homepage_clubs.html'
with open(temp_file_path, 'w', encoding='utf-8') as f:
    f.write(homepage_only_html)

url = "http://localhost:8000/temp_homepage_clubs.html"
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

# 1. Capture Desktop View
desktop_img = os.path.join(artifact_dir, 'homepage_desktop_clubs.png')
print(f"Capturing desktop homepage view to {desktop_img}...")
cmd_desktop = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={desktop_img}",
    "--window-size=1440,3600",
    url
]
subprocess.run(cmd_desktop, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 2. Capture Mobile View
mobile_img = os.path.join(artifact_dir, 'homepage_mobile_clubs.png')
print(f"Capturing mobile homepage view to {mobile_img}...")
cmd_mobile = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={mobile_img}",
    "--window-size=430,5200",
    url
]
subprocess.run(cmd_mobile, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Clean up
time.sleep(1.5)
if os.path.exists(temp_file_path):
    os.remove(temp_file_path)

print("Screenshots captured successfully!")
