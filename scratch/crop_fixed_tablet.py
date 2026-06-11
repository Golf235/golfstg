import os
from PIL import Image

img_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/sevenclubgame_tablet_full.png"
out_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292"

if os.path.exists(img_path):
    img = Image.open(img_path)
    top = 2574
    height = 1209
    crop_top = max(0, top - 50)
    crop_bottom = min(img.size[1], top + height + 50)
    
    cropped_img = img.crop((0, crop_top, 768, crop_bottom))
    cropped_img.save(os.path.join(out_dir, "sevenclubgame_tablet_grid_section_after.png"))
    print(f"Successfully cropped tablet grid section to sevenclubgame_tablet_grid_section_after.png (Y={crop_top} to {crop_bottom})")
else:
    print("Full tablet screenshot not found.")
