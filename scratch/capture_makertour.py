import subprocess
import os

makertour_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/maker-tour.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

# 1. Desktop Hero
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_desktop_hero.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2000",
    f"file://{makertour_path}"
])

# 2. Desktop Why Section
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_desktop_why.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{makertour_path}#why-maker"
])

# 3. Desktop Where Section
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_desktop_where.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{makertour_path}#where-play"
])

# 4. Desktop Specs Section
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_desktop_specs.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{makertour_path}#tech-specs"
])

# 5. Desktop For Who Section
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_desktop_for_who.png')}",
    "--window-size=1200,900",
    "--virtual-time-budget=2500",
    f"file://{makertour_path}#for-who"
])

# 6. Mobile Hero
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_mobile_hero.png')}",
    "--window-size=390,844",
    "--virtual-time-budget=2000",
    f"file://{makertour_path}"
])

# 7. Mobile Why Section
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_mobile_why.png')}",
    "--window-size=390,844",
    "--virtual-time-budget=2500",
    f"file://{makertour_path}#why-maker"
])

# 8. Mobile Specs Section
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_mobile_specs.png')}",
    "--window-size=390,844",
    "--virtual-time-budget=2500",
    f"file://{makertour_path}#tech-specs"
])

# 9. Mobile For Who Section
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(artifact_dir, 'makertour_mobile_for_who.png')}",
    "--window-size=390,844",
    "--virtual-time-budget=2500",
    f"file://{makertour_path}#for-who"
])

print("Maker Tour screenshots captured successfully!")
