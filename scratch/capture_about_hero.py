import subprocess
import time
import os

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"

# Capture About Page Hero Section on Desktop (1440x900)
about_url = "http://localhost:8000/about.html"
hero_img_desktop = os.path.join(artifact_dir, "about_desktop_hero_bottom.png")
print(f"Capturing About Desktop Hero to {hero_img_desktop}...")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={hero_img_desktop}",
    "--window-size=1440,900",
    about_url
]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Desktop Hero screenshot captured successfully!")
