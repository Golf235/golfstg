import subprocess
import os

artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8'
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

urls = [
    ("tech_desktop_hero", "http://localhost:8000/technology.html", 1440, 900),
    ("tech_mobile_hero", "http://localhost:8000/technology.html", 430, 900),
    ("innovation_desktop_hero", "http://localhost:8000/innovation.html", 1440, 900),
    ("innovation_mobile_hero", "http://localhost:8000/innovation.html", 430, 900),
    ("material_desktop_hero", "http://localhost:8000/material.html", 1440, 900),
    ("material_mobile_hero", "http://localhost:8000/material.html", 430, 900),
    ("production_desktop_hero", "http://localhost:8000/production.html", 1440, 900),
    ("production_mobile_hero", "http://localhost:8000/production.html", 430, 900),
]

for name, url, width, height in urls:
    out_img = os.path.join(artifact_dir, f"{name}.png")
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_img}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=3000",
        url
    ]
    print(f"Capturing {name} ({width}x{height}) from {url}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Screenshots captured successfully!")
