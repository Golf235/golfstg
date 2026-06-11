import subprocess
import os

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

tests = [
    # Desktop tests (1440x900)
    ("configurator_desktop_closed.png", 1440, 900, "file:///Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/configurator.html"),
    ("configurator_desktop_open.png", 1440, 900, "file:///Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/configurator.html?test_help=1"),
    ("configurator_desktop_success.png", 1440, 900, "file:///Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/configurator.html?test_help=1&test_success=1"),
    
    # Mobile tests (400x900)
    ("configurator_mobile_closed.png", 400, 900, "file:///Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/configurator.html"),
    ("configurator_mobile_open.png", 400, 900, "file:///Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/configurator.html?test_help=1"),
    ("configurator_mobile_success.png", 400, 900, "file:///Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/configurator.html?test_help=1&test_success=1"),
]

for name, width, height, url in tests:
    out_path = f"/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/{name}"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_path}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=3000",
        url
    ]
    print(f"Capturing {name} ({width}x{height}) ...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Verification screenshots captured successfully!")
