import subprocess
import os

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"
html_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

pages = [
    ("tech_desktop_nextread_bottom.png", "technology.html", 1440, 900),
    ("tech_mobile_nextread_bottom.png", "technology.html", 390, 800),
    ("innovation_desktop_nextread_bottom.png", "innovation.html", 1440, 900),
    ("innovation_mobile_nextread_bottom.png", "innovation.html", 390, 800),
    ("material_desktop_nextread_bottom.png", "material.html", 1440, 900),
    ("material_mobile_nextread_bottom.png", "material.html", 390, 800),
    ("production_desktop_nextread_bottom.png", "production.html", 1440, 900),
    ("production_mobile_nextread_bottom.png", "production.html", 390, 800)
]

print("=== CAPTURING VIEWPORTS OF NEXT READ ===")

for filename, html_name, width, height in pages:
    dest_path = os.path.join(artifact_dir, filename)
    url = f"file://{os.path.join(html_dir, html_name)}#next-read"
    
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={dest_path}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=3000",  # Wait for page to load & scroll
        url
    ]
    print(f"Capturing {filename} ({width}x{height}) targeting #next-read...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("All viewport screenshots captured successfully.")
