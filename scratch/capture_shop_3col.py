import subprocess
import time
import os

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"

# Capture Shop Page Desktop size (1440x2500)
shop_url = "http://localhost:8000/shop.html"
shop_img_desktop = os.path.join(artifact_dir, "shop_page_desktop_3col.png")
print(f"Capturing Shop Desktop 3-col page to {shop_img_desktop}...")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={shop_img_desktop}",
    "--window-size=1440,2500",
    shop_url
]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Desktop screenshot captured successfully!")

# Capture Shop Page Tablet size (768x3000)
shop_img_tablet = os.path.join(artifact_dir, "shop_page_tablet_3col.png")
print(f"Capturing Shop Tablet 3-col page to {shop_img_tablet}...")
cmd_tablet = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={shop_img_tablet}",
    "--window-size=768,3000",
    shop_url
]
subprocess.run(cmd_tablet, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Tablet screenshot captured successfully!")
