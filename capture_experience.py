import subprocess
import time
import os
import re

# Read experience.html
with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/experience.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract head content
head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
head_content = head_match.group(1) if head_match else ''

# Extract all sections together (intro block, formats, and community)
section_regex = r'(<section class="large-text-block[^"]*">.*?</section>\s*<!--.*?-->\s*<section class="[^"]*(?:formats-section|mag-more-section)[^"]*"[^>]*>.*?</section>\s*<!--.*?-->\s*<section class="responsive-image-content[^"]*">.*?</section>)'
formats_match = re.search(section_regex, content, re.DOTALL)
formats_content = formats_match.group(1) if formats_match else ''

if not formats_content:
    # Fallback to loose matching if comment structure varies
    section_regex_loose = r'(<section class="large-text-block.*?</section>.*?<section class="responsive-image-content[^"]*">.*?</section>)'
    formats_match = re.search(section_regex_loose, content, re.DOTALL)
    formats_content = formats_match.group(1) if formats_match else ''

if not formats_content:
    print("Error: Could not extract intro block and formats section from experience.html!")
    exit(1)

# Build formats-only HTML page
formats_only_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {head_content}
    <style>
        body {{
            background: #ffffff !important;
            margin: 0;
            padding: 0;
        }}
    </style>
</head>
<body>
    <div style="padding: 20px 0;">
        {formats_content}
    </div>
</body>
</html>
"""

temp_file_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_formats_only.html'
with open(temp_file_path, 'w', encoding='utf-8') as f:
    f.write(formats_only_html)

url = "http://localhost:8000/temp_formats_only.html"
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8'

# 1. Capture Desktop View
desktop_img = os.path.join(artifact_dir, 'experience_desktop_formats.png')
print(f"Capturing desktop formats view to {desktop_img}...")
cmd_desktop = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={desktop_img}",
    "--window-size=1440,3200",
    url
]
subprocess.run(cmd_desktop, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 2. Capture Mobile View
mobile_img = os.path.join(artifact_dir, 'experience_mobile_formats.png')
print(f"Capturing mobile formats view to {mobile_img}...")
cmd_mobile = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={mobile_img}",
    "--window-size=430,4500",
    url
]
subprocess.run(cmd_mobile, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Clean up
time.sleep(1)
if os.path.exists(temp_file_path):
    os.remove(temp_file_path)

print("Screenshots captured successfully!")
