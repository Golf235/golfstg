from PIL import Image
import os

img_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/makertour_desktop_full_new.png"
out_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292"

img = Image.open(img_path)

# Crop sections
# 1. Why Maker Tour section (approx 1000px to 2000px height)
why_sec = img.crop((0, 950, 1440, 2000))
why_sec.save(os.path.join(out_dir, "makertour_why_section.png"))

# 2. Tech Specs section (approx 2000px to 3200px height)
specs_sec = img.crop((0, 2000, 1440, 3100))
specs_sec.save(os.path.join(out_dir, "makertour_specs_section.png"))

# 3. Who is it for section (approx 3100px to 4200px height)
who_sec = img.crop((0, 3100, 1440, 4200))
who_sec.save(os.path.join(out_dir, "makertour_who_section.png"))

print("Cropped images saved successfully.")
