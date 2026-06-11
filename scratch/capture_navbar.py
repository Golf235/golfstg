import subprocess
import os
import re

html_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files'
index_path = os.path.join(html_dir, 'technology.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Desktop Nav Dropdown Capture
desktop_html = html.replace('</head>', """
<style>
.nav-dropdown .dropdown-menu {
    opacity: 1 !important;
    visibility: visible !important;
    transform: translateX(-50%) translateY(0) !important;
}
</style>
</head>""")

desktop_temp_file = os.path.join(html_dir, 'temp_verify_desktop_dropdown.html')
with open(desktop_temp_file, 'w', encoding='utf-8') as f:
    f.write(desktop_html)

# Take screenshot
cmd_desktop = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--screenshot=/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8/ourclubs_desktop_menu.png",
    "--window-size=1440,800",
    "--virtual-time-budget=3000",
    f"file://{desktop_temp_file}"
]
print("Capturing desktop dropdown screenshot...")
subprocess.run(cmd_desktop, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 2. Mobile Menu Open Capture
mobile_html = html.replace('<div class="mobile-menu">', '<div class="mobile-menu active">')
mobile_html = mobile_html.replace('<button class="hamburger">', '<button class="hamburger active">')

# We can also force the mobile accordion open
mobile_html = mobile_html.replace('class="mobile-nav-dropdown"', 'class="mobile-nav-dropdown active"')

mobile_temp_file = os.path.join(html_dir, 'temp_verify_mobile_menu.html')
with open(mobile_temp_file, 'w', encoding='utf-8') as f:
    f.write(mobile_html)

# Take screenshot
cmd_mobile = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--screenshot=/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8/ourclubs_mobile_menu.png",
    "--window-size=500,900",
    "--virtual-time-budget=3000",
    f"file://{mobile_temp_file}"
]
print("Capturing mobile menu open screenshot...")
subprocess.run(cmd_mobile, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Clean up
if os.path.exists(desktop_temp_file):
    os.remove(desktop_temp_file)
if os.path.exists(mobile_temp_file):
    os.remove(mobile_temp_file)

print("Screenshots captured successfully!")
