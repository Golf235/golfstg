import subprocess
import os
import time

artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8'

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Ensure local server is running or access file:/// URLs directly.
# Since a python HTTP server is running on port 8000, we can use localhost:8000.
urls = [
    ("about_desktop_hero", "http://localhost:8000/about.html", 1440, 900),
    ("experience_desktop_hero", "http://localhost:8000/experience.html", 1440, 900),
    ("about_mobile_hero", "http://localhost:8000/about.html", 430, 900),
    ("experience_mobile_hero", "http://localhost:8000/experience.html", 430, 900),
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

print("Hero screenshots captured successfully!")
