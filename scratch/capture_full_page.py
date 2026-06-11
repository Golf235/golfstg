import subprocess
import os

makertour_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/maker-tour.html'
temp_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/maker-tour-temp.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

# 1. Read maker-tour.html
with open(makertour_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Inject override for hero height
content_modified = content.replace('</head>', '<style>.hero { height: 900px !important; }</style></head>')

# 3. Write temp file
with open(temp_path, 'w', encoding='utf-8') as f:
    f.write(content_modified)

# 4. Capture screenshot
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_desktop_full_new.png')}",
    "--window-size=1440,4800",
    "--virtual-time-budget=3000",
    f"file://{temp_path}"
])

# 5. Clean up temp file
if os.path.exists(temp_path):
    os.remove(temp_path)

# 6. Crop sections for easy viewing
from PIL import Image
img = Image.open(os.path.join(artifact_dir, 'makertour_desktop_full_new.png'))

# Crop intro & why section (y=900 to y=2050)
why_sec = img.crop((0, 900, 1440, 2050))
why_sec.save(os.path.join(artifact_dir, 'makertour_why_section_new.png'))

# Crop specs section (y=2050 to y=2950)
specs_sec = img.crop((0, 2050, 1440, 2950))
specs_sec.save(os.path.join(artifact_dir, 'makertour_specs_section_new.png'))

# Crop who section (y=2950 to y=3950)
who_sec = img.crop((0, 2950, 1440, 3950))
who_sec.save(os.path.join(artifact_dir, 'makertour_who_section_new.png'))

print("Maker Tour full page screenshot and section crops captured successfully!")
