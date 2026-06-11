import subprocess
import os

seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

out_img = os.path.join(artifact_dir, "sevenclubgame_tablet_full.png")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=768,8000",
    "--virtual-time-budget=3000",
    f"file://{seven_file}"
]
subprocess.run(cmd)
print(f"Captured full tablet page to {out_img}")
