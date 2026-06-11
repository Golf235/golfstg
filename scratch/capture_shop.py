import subprocess
import os

shop_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/shop.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

# 1. Desktop (1440x900)
out_img = os.path.join(artifact_dir, 'shop_desktop.png')
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=1440,900",
    "--virtual-time-budget=2000",
    f"file://{shop_path}"
]
print("Capturing Shop Desktop...")
subprocess.run(cmd)

# 2. Widescreen (1920x1080)
out_img = os.path.join(artifact_dir, 'shop_widescreen.png')
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=1920,1080",
    "--virtual-time-budget=2000",
    f"file://{shop_path}"
]
print("Capturing Shop Widescreen...")
subprocess.run(cmd)

# 3. Tablet (768x1024)
out_img = os.path.join(artifact_dir, 'shop_tablet.png')
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=768,1024",
    "--virtual-time-budget=2000",
    f"file://{shop_path}"
]
print("Capturing Shop Tablet...")
subprocess.run(cmd)

# 4. Mobile (390x844)
out_img = os.path.join(artifact_dir, 'shop_mobile.png')
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=390,844",
    "--virtual-time-budget=2000",
    f"file://{shop_path}"
]
print("Capturing Shop Mobile...")
subprocess.run(cmd)

print("All Shop screenshots captured successfully!")
