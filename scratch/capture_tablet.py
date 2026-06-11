import subprocess
import os

sevenclubgame_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

# Capture tablet viewport (768px width)
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'sevenclubgame_tablet_grid_before.png')}",
    "--window-size=768,1024",
    "--virtual-time-budget=2500",
    f"file://{sevenclubgame_path}#shop"
])

print("Tablet screenshot captured successfully!")
