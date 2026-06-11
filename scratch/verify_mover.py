import subprocess
import os

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292"
mover_html_path = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/mover.html"

# Run a simple HTTP server or load as file URL
# Since it is a static file, loading via file:// scheme is perfect
url = f"file://{mover_html_path}"

layouts = [
    ("mover_desktop_full.png", 1440, 5000),
    ("mover_mobile_full.png", 390, 6500)
]

for name, width, height in layouts:
    dest_path = os.path.join(artifact_dir, name)
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={dest_path}",
        f"--window-size={width},{height}",
        url
    ]
    print(f"Capturing {name} ({width}x{height}) -> {dest_path}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Screenshots captured successfully.")
