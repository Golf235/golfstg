import subprocess
import os

tech_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/technology.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

os.makedirs(artifact_dir, exist_ok=True)

# 1. Desktop Top
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'technology_desktop_top.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2000",
    f"file://{tech_path}"
])

# 2. Desktop Innovation
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'technology_desktop_innovation.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{tech_path}#innovation"
])

# 3. Desktop Material
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'technology_desktop_material.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{tech_path}#material"
])

# 4. Desktop Production
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'technology_desktop_production.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{tech_path}#production"
])

# 5. Mobile Layout
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'technology_mobile.png')}",
    "--window-size=390,844",
    "--virtual-time-budget=2000",
    f"file://{tech_path}"
])

# 6. Tablet Layout
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'technology_tablet.png')}",
    "--window-size=768,1024",
    "--virtual-time-budget=2000",
    f"file://{tech_path}"
])

print("Technology screenshots captured successfully!")
