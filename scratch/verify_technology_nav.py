import subprocess
import os
import time

artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8'
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

urls = [
    ("homepage_desktop_menu", "http://localhost:8000/index.html", 1440, 200),
    ("homepage_mobile_menu", "http://localhost:8000/index.html", 430, 200),
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

print("Navigation screenshots captured successfully!")
