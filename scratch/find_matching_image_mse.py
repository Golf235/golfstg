import os
from PIL import Image, ImageChops, ImageStat

attached_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/633bc07e-1a63-423a-9de9-ae4a1302a620/media__1781191237520.png"
workspace_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"

attached_img = Image.open(attached_path).convert('RGB')
attached_size = attached_img.size

best_match = None
min_diff = float('inf')

print("Scanning and comparing images using ImageChops...")
for root, dirs, files in os.walk(workspace_dir):
    if "chrome_profile" in root or "scratch" in root:
        continue
    for file in files:
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.webp'):
            path = os.path.join(root, file)
            try:
                img = Image.open(path).convert('RGB')
                # Resize to target size for comparison
                img_resized = img.resize(attached_size, Image.Resampling.LANCZOS)
                
                # Calculate difference
                diff = ImageChops.difference(attached_img, img_resized)
                stat = ImageStat.Stat(diff)
                diff_sum = sum(stat.sum)
                
                if diff_sum < min_diff:
                    min_diff = diff_sum
                    best_match = path
                
                if diff_sum < 100000: # Close match threshold
                    print(f"Close match found: {path} (Diff sum: {diff_sum:.2f})")
            except Exception as e:
                pass

print(f"\nBest overall match: {best_match} (Diff sum: {min_diff:.2f})")
