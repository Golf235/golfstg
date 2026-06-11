import subprocess
import os
import json
from PIL import Image

seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/chrome_profile_coords_tablet'
os.makedirs(user_data_dir, exist_ok=True)

# Write a temp script to sevenclubgame.html to log coordinates on DOMContentLoaded
inject_js = f"""
<script>
document.addEventListener('DOMContentLoaded', () => {{
    const el = document.getElementById('shop');
    if (el) {{
        const rect = el.getBoundingClientRect();
        const style = window.getComputedStyle(el);
        console.log("COORD_JSON:" + JSON.stringify({{
            found: true,
            top: rect.top + window.scrollY,
            height: rect.height,
            display: style.display,
            visibility: style.visibility,
            opacity: style.opacity
        }}));
    }} else {{
        console.log("COORD_JSON:" + JSON.stringify({{found: false}}));
    }}
}});
</script>
"""

temp_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_inspect_coords_tablet.html'
with open(seven_file, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('</body>', inject_js + '\n</body>')
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(html)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--user-data-dir={user_data_dir}",
    "--enable-logging",
    "--v=1",
    "--window-size=768,8000",
    f"file://{temp_file}"
]

log_file = os.path.join(user_data_dir, 'chrome_debug.log')
if os.path.exists(log_file):
    os.remove(log_file)

try:
    subprocess.run(cmd, timeout=6, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.TimeoutExpired:
    pass

coord_info = None
if os.path.exists(log_file):
    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()
    for line in log_content.split('\n'):
        if "COORD_JSON:" in line:
            coord_info = line.split("COORD_JSON:")[-1].strip()
            break

print(f"Coordinates Info for Tablet: {coord_info}")

if os.path.exists(temp_file):
    os.remove(temp_file)
import shutil
shutil.rmtree(user_data_dir, ignore_errors=True)

# Now crop the tablet image based on coordinates if found
if coord_info:
    try:
        info = json.loads(coord_info)
        if info.get('found'):
            img_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/sevenclubgame_tablet_full.png"
            out_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292"
            if os.path.exists(img_path):
                img = Image.open(img_path)
                top = int(info['top'])
                height = int(info['height'])
                # Crop a little bit extra for padding (say 50px before/after)
                crop_top = max(0, top - 50)
                crop_bottom = min(img.size[1], top + height + 50)
                
                cropped_img = img.crop((0, crop_top, 768, crop_bottom))
                cropped_img.save(os.path.join(out_dir, "sevenclubgame_tablet_grid_section.png"))
                print(f"Successfully cropped tablet grid section (Y={crop_top} to {crop_bottom})")
            else:
                print("tablet full image not found for cropping.")
    except Exception as e:
        print(f"Error cropping: {e}")
