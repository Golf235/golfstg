import subprocess
import os

sevenclubgame_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

# Ensure artifact dir exists
os.makedirs(artifact_dir, exist_ok=True)

# 1. Desktop Hero
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'sevenclubgame_desktop_hero.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2000",
    f"file://{sevenclubgame_path}"
])

# 2. Desktop Reimagined
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'sevenclubgame_desktop_reimagined.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{sevenclubgame_path}#reimagined"
])

# 3. Desktop Map
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'sevenclubgame_desktop_map.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{sevenclubgame_path}#sevenclubgame"
])

# 4. Desktop Newsletter
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'sevenclubgame_desktop_newsletter.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=4000", # Wait extra for HubSpot form rendering
    f"file://{sevenclubgame_path}#newsletter"
])

# 5. Mobile Hero
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'sevenclubgame_mobile_hero.png')}",
    "--window-size=390,844",
    "--virtual-time-budget=2000",
    f"file://{sevenclubgame_path}"
])

# 6. Mobile Map
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'sevenclubgame_mobile_map.png')}",
    "--window-size=390,844",
    "--virtual-time-budget=2500",
    f"file://{sevenclubgame_path}#sevenclubgame"
])

print("Sevenclubgame screenshots captured successfully!")
