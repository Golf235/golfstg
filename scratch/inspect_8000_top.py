import os
from PIL import Image

img_path = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/sevenclubgame_desktop_8000.png'

if os.path.exists(img_path):
    img = Image.open(img_path)
    width, height = img.size
    print(f"Sampling top colors for 8000px image:")
    
    x_coords = [100, 720, 1340]
    
    print(f"{'y-coord':<8} | {'Left (x=100)':<15} | {'Center (x=720)':<15} | {'Right (x=1340)':<15}")
    print("-" * 60)
    for y in range(0, 3000, 100):
        c_left = img.getpixel((100, y))[:3]
        c_center = img.getpixel((720, y))[:3]
        c_right = img.getpixel((1340, y))[:3]
        print(f"{y:<8d} | {str(c_left):<15} | {str(c_center):<15} | {str(c_right):<15}")
else:
    print("Image not found:", img_path)
