import subprocess
import os

index_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/index.html'
out_img = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/index_mobile_map.png'

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=390,844",
    "--virtual-time-budget=3000",
    f"file://{index_path}#sevenclubgame"
]
print("Capturing index mobile map at anchor...")
subprocess.run(cmd)
print("Captured to:", out_img)
