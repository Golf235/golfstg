from PIL import Image
import os

img_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/sevenclubgame_tablet_full.png"
out_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292"

if os.path.exists(img_path):
    img = Image.open(img_path)
    # The tablet width is 768. Let's crop from Y=2000 to Y=6000 to cover the whole grid area
    # and save in chunks of 1500px height for easy viewing.
    
    # Chunk 1: Y=2000 to 3500
    chunk1 = img.crop((0, 2000, 768, 3500))
    chunk1.save(os.path.join(out_dir, "sevenclubgame_tablet_shop_c1.png"))
    
    # Chunk 2: Y=3500 to 5000
    chunk2 = img.crop((0, 3500, 768, 5000))
    chunk2.save(os.path.join(out_dir, "sevenclubgame_tablet_shop_c2.png"))
    
    # Chunk 3: Y=5000 to 6500
    chunk3 = img.crop((0, 5000, 768, 6500))
    chunk3.save(os.path.join(out_dir, "sevenclubgame_tablet_shop_c3.png"))
    
    print("Tablet grid chunks cropped successfully.")
else:
    print("Full tablet screenshot not found.")
