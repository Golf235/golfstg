import subprocess
import os
import re
import json
from PIL import Image

seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
temp_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_tablet_fixed_heights.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

# We inject CSS overrides to force all 100vh sections to be 800px high,
# and a synchronous script to get coordinate info on load.
inject_html = """
<style>
.hero {
    height: 800px !important;
}
.hero-video-home-p1, .hero-video-default-p1 {
    min-height: 800px !important;
    height: 800px !important;
}
</style>
<script>
document.addEventListener('DOMContentLoaded', () => {
    const el = document.getElementById('shop');
    if (el) {
        const rect = el.getBoundingClientRect();
        console.log("COORD_JSON:" + JSON.stringify({
            found: true,
            top: rect.top + window.scrollY,
            height: rect.height
        }));
    }
});
</script>
"""

with open(seven_file, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('</body>', inject_html + '\n</body>')
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(html)

user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/chrome_profile_coords_fixed'
os.makedirs(user_data_dir, exist_ok=True)

out_img = os.path.join(artifact_dir, "sevenclubgame_tablet_full.png")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--user-data-dir={user_data_dir}",
    "--enable-logging",
    "--v=1",
    f"--screenshot={out_img}",
    "--window-size=768,8000",
    "--virtual-time-budget=3000",
    f"file://{temp_file}"
]

log_file = os.path.join(user_data_dir, 'chrome_debug.log')
if os.path.exists(log_file):
    os.remove(log_file)

print("Capturing 8000px high tablet screenshot and extracting coordinates...")
subprocess.run(cmd)

coord_info = None
if os.path.exists(log_file):
    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()
    for line in log_content.split('\n'):
        if "COORD_JSON:" in line:
            m = re.search(r'COORD_JSON:(\{.*?\})', line)
            if m:
                coord_info = m.group(1)
                break

print(f"Coordinates Info for Tablet: {coord_info}")

if os.path.exists(temp_file):
    os.remove(temp_file)
import shutil
shutil.rmtree(user_data_dir, ignore_errors=True)

# Crop
if coord_info and os.path.exists(out_img):
    try:
        info = json.loads(coord_info)
        img = Image.open(out_img)
        top = int(info['top'])
        height = int(info['height'])
        crop_top = max(0, top - 50)
        crop_bottom = min(img.size[1], top + height + 50)
        
        cropped_img = img.crop((0, crop_top, 768, crop_bottom))
        cropped_img.save(os.path.join(artifact_dir, "sevenclubgame_tablet_grid_section.png"))
        print(f"Successfully cropped tablet grid section to sevenclubgame_tablet_grid_section.png (Y={crop_top} to {crop_bottom})")
    except Exception as e:
        print(f"Error cropping: {e}")
