import subprocess
import time
import os

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"

# Capture Polo Detail Page
polo_url = "http://localhost:8000/short-sleeve-polo.html"
polo_img = os.path.join(artifact_dir, "polo_detail_page.png")
print(f"Capturing Polo page to {polo_img}...")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={polo_img}",
    "--window-size=1200,1600",
    polo_url
]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Screenshot captured successfully!")
