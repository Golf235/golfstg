from PIL import Image
import os

img_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/makertour_desktop_full_new.png"
artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292"

img = Image.open(img_path)

# Crop bottom section (y=3600 to y=4800)
bottom_sec = img.crop((0, 3600, 1440, 4800))
bottom_sec.save(os.path.join(artifact_dir, "makertour_bottom_section_new.png"))

print("Bottom section cropped successfully.")
