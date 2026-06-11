import subprocess
import os
from PIL import Image

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"
html_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

pages = [
    ("tech_desktop_nextread.png", "technology.html", 1440, 8000),
    ("tech_mobile_nextread.png", "technology.html", 390, 9500),
    ("innovation_desktop_nextread.png", "innovation.html", 1440, 5000),
    ("innovation_mobile_nextread.png", "innovation.html", 390, 6000),
    ("material_desktop_nextread.png", "material.html", 1440, 5000),
    ("material_mobile_nextread.png", "material.html", 390, 6000),
    ("production_desktop_nextread.png", "production.html", 1440, 6000),
    ("production_mobile_nextread.png", "production.html", 390, 7000)
]

print("=== CAPTURING AND AUTO-CROPPING BOTTOMS ===")

for filename, html_name, width, height in pages:
    temp_path = os.path.join(artifact_dir, f"temp_{filename}")
    dest_path = os.path.join(artifact_dir, filename.replace(".png", "_bottom.png"))
    url = f"file://{os.path.join(html_dir, html_name)}"
    
    # 1. Capture at very tall size
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={temp_path}",
        f"--window-size={width},{height}",
        url
    ]
    print(f"Capturing {html_name} -> {temp_path}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # 2. Load image and scan from bottom to find actual content bottom
    if os.path.exists(temp_path):
        img = Image.open(temp_path)
        img_data = img.load()
        w, h = img.size
        
        # Scan upwards from the bottom along the center column to find the first non-transparent/non-white pixel
        content_bottom = h - 1
        for y in range(h - 1, 0, -1):
            pixel = img_data[w // 2, y]
            # check if pixel is not transparent and not pure white (or very close to white)
            # pixel can be (r, g, b, a) or (r, g, b)
            is_empty = False
            if len(pixel) == 4:
                r, g, b, a = pixel
                if a == 0 or (r > 250 and g > 250 and b > 250):
                    is_empty = True
            else:
                r, g, b = pixel
                if r > 250 and g > 250 and b > 250:
                    is_empty = True
            
            if not is_empty:
                content_bottom = y
                break
        
        # Crop 1000px above the detected bottom (but clamp to 0)
        crop_top = max(0, content_bottom - 1000)
        crop_bottom = min(h, content_bottom + 50) # include a little bit of footer padding
        
        print(f"Detected content bottom at y={content_bottom}. Cropping from y={crop_top} to y={crop_bottom}...")
        cropped_img = img.crop((0, crop_top, w, crop_bottom))
        cropped_img.save(dest_path)
        
        # Remove temp file
        os.remove(temp_path)
    else:
        print(f"[ERROR] Failed to capture temp file for {html_name}")

print("All bottom screenshots captured and cropped successfully.")
