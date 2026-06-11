import subprocess
import os

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"
html_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

pages = [
    ("tech_desktop_nextread.png", "technology.html", 1440, 5200),
    ("tech_mobile_nextread.png", "technology.html", 390, 6800),
    ("innovation_desktop_nextread.png", "innovation.html", 1440, 2500),
    ("innovation_mobile_nextread.png", "innovation.html", 390, 3200),
    ("material_desktop_nextread.png", "material.html", 1440, 2500),
    ("material_mobile_nextread.png", "material.html", 390, 3200),
    ("production_desktop_nextread.png", "production.html", 1440, 3000),
    ("production_mobile_nextread.png", "production.html", 390, 4200)
]

print("=== CAPTURING SCREENSHOTS OF NEXT READ SECTIONS ===")

for filename, html_name, width, height in pages:
    dest_path = os.path.join(artifact_dir, filename)
    url = f"file://{os.path.join(html_dir, html_name)}"
    
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={dest_path}",
        f"--window-size={width},{height}",
        url
    ]
    print(f"Capturing {filename} ({width}x{height}) for {html_name}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("All screenshots captured successfully.")
