import subprocess
import time
import os

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"

# Capture Shirt Detail Page
shirt_url = "http://localhost:8000/shirt.html"
shirt_img = os.path.join(artifact_dir, "shirt_detail_page.png")
print(f"Capturing Shirt page to {shirt_img}...")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={shirt_img}",
    "--window-size=1200,1600",
    shirt_url
]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Screenshot captured successfully!")
