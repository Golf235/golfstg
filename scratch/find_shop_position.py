import subprocess
import os
import json

seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/chrome_profile_inspect'
os.makedirs(user_data_dir, exist_ok=True)

# We will run a script in Chrome to extract the bounding box of the #shop section
js_code = """
const el = document.getElementById('shop');
if (el) {
    const rect = el.getBoundingClientRect();
    const style = window.getComputedStyle(el);
    console.log(JSON.stringify({
        found: true,
        top: rect.top + window.scrollY,
        height: rect.height,
        display: style.display,
        visibility: style.visibility,
        opacity: style.opacity
    }));
} else {
    console.log(JSON.stringify({found: false}));
}
"""

# We can run chrome headless and print console logs
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--user-data-dir={user_data_dir}",
    "--enable-logging",
    "--v=1",
    f"file://{seven_file}"
]

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

temp_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_inspect_coords.html'
with open(seven_file, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('</body>', inject_js + '\n</body>')
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(html)

cmd[-1] = f"file://{temp_file}"

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

print(f"Coordinates Info: {coord_info}")

if os.path.exists(temp_file):
    os.remove(temp_file)
import shutil
shutil.rmtree(user_data_dir, ignore_errors=True)
