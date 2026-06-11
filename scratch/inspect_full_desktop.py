from PIL import Image
import os

img_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/sevenclubgame_desktop_full.png"
out_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292"

if os.path.exists(img_path):
    img = Image.open(img_path)
    w, h = img.size
    print(f"Image dimensions: {w}x{h}")
    
    # Save 1000px chunks
    for y in range(0, h, 1000):
        end_y = min(y + 1000, h)
        chunk = img.crop((0, y, w, end_y))
        chunk.save(os.path.join(out_dir, f"seven_desktop_inspect_{y}.png"))
        print(f"Saved chunk for Y={y} to Y={end_y}")
else:
    print("Desktop full screenshot not found.")
