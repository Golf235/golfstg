import os
from PIL import Image

bg_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/newsletter-1920-min-1024x466.jpg'

if os.path.exists(bg_path):
    img = Image.open(bg_path)
    print(f"Newsletter BG image size: {img.size}")
    # Sample center pixel
    px = img.convert('RGB').getpixel((img.size[0]//2, img.size[1]//2))
    print(f"Center pixel color of newsletter BG: {px}")
    
    # Sample top, center, bottom
    px_top = img.convert('RGB').getpixel((img.size[0]//2, 20))
    px_bot = img.convert('RGB').getpixel((img.size[0]//2, img.size[1] - 20))
    print(f"Top pixel: {px_top}, Bottom pixel: {px_bot}")
else:
    print("Newsletter BG not found at:", bg_path)
