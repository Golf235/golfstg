import subprocess
import time
import os

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"

# Capture Bucket Hat Detail Page
hat_url = "http://localhost:8000/bucket-hat.html"
hat_img = os.path.join(artifact_dir, "buckethat_detail_page_updated.png")
print(f"Capturing Bucket Hat page to {hat_img}...")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={hat_img}",
    "--window-size=1200,1600",
    hat_url
]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Bucket Hat page screenshot captured successfully!")

# Capture Shop Page with a very large height to see the updated Bucket Hat card
shop_url = "http://localhost:8000/shop.html"
shop_img = os.path.join(artifact_dir, "shop_page_updated_3.png")
print(f"Capturing Shop page to {shop_img}...")
cmd_shop = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={shop_img}",
    "--window-size=1200,3500",
    shop_url
]
subprocess.run(cmd_shop, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Shop page screenshot captured successfully!")
