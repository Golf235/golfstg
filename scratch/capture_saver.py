import subprocess
import os
import urllib.parse
import time

saver_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/saver.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

# 1. Desktop Hero
out_img = os.path.join(artifact_dir, 'saver_desktop_hero.png')
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=1200,900",
    "--virtual-time-budget=2000",
    f"file://{saver_path}"
]
print("Capturing Saver Desktop Hero...")
subprocess.run(cmd)

# 2. Desktop Why Section
out_img = os.path.join(artifact_dir, 'saver_desktop_why.png')
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{saver_path}#why-pitcher"
]
print("Capturing Saver Desktop Why Section...")
subprocess.run(cmd)

# 3. Desktop Specs Section
out_img = os.path.join(artifact_dir, 'saver_desktop_specs.png')
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{saver_path}#tech-specs"
]
print("Capturing Saver Desktop Tech Specs...")
subprocess.run(cmd)

# 4. Mobile Hero
out_img = os.path.join(artifact_dir, 'saver_mobile_hero.png')
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=390,844",
    "--virtual-time-budget=2000",
    f"file://{saver_path}"
]
print("Capturing Saver Mobile Hero...")
subprocess.run(cmd)

# 5. Mobile Why Section
out_img = os.path.join(artifact_dir, 'saver_mobile_why.png')
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=390,844",
    "--virtual-time-budget=2500",
    f"file://{saver_path}#why-pitcher"
]
print("Capturing Saver Mobile Why Section...")
subprocess.run(cmd)

print("All Saver screenshots captured successfully!")
