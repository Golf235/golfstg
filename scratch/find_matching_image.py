import os
from PIL import Image

attached_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/633bc07e-1a63-423a-9de9-ae4a1302a620/media__1781191237520.png"
workspace_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"

attached_img = Image.open(attached_path).convert('RGB')
attached_pixels = list(attached_img.getdata())
attached_size = attached_img.size

print(f"Attached image dimensions: {attached_size}")

matches = []
for root, dirs, files in os.walk(workspace_dir):
    if "chrome_profile" in root or "scratch" in root:
        continue
    for file in files:
        if file.endswith('.png'):
            path = os.path.join(root, file)
            try:
                img = Image.open(path)
                if img.size == attached_size:
                    img_rgb = img.convert('RGB')
                    pixels = list(img_rgb.getdata())
                    if pixels == attached_pixels:
                        matches.append(path)
            except Exception as e:
                pass

print("Matching files found:")
for m in matches:
    print(m)
