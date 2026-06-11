import subprocess
import time
import os

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"

# Capture T-shirt Detail Page
tshirt_url = "http://localhost:8000/t-shirt.html"
tshirt_img = os.path.join(artifact_dir, "tshirt_detail_page_updated.png")
print(f"Capturing T-shirt page to {tshirt_img}...")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--disable-http-cache",
    f"--screenshot={tshirt_img}",
    "--window-size=1200,1600",
    tshirt_url
]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("T-shirt page screenshot captured successfully!")

# Capture Shop Page with a very large height to see the updated T-shirt card
shop_url = "http://localhost:8000/shop.html"
shop_img = os.path.join(artifact_dir, "shop_page_updated_2.png")
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
