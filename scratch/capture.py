import subprocess

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
out_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/maker_images_catalog.png"

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_path}",
    "--window-size=1200,800",
    "--virtual-time-budget=3000",
    "http://localhost:8000/Golfyr%20Configurator%20V2_files/test_images.html"
]

print("Capturing catalog screenshot...")
subprocess.run(cmd)
print("Done!")
