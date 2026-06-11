import os
from PIL import Image, ImageStat

full_desktop_img_path = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/sevenclubgame_desktop_full.png'

if os.path.exists(full_desktop_img_path):
    img = Image.open(full_desktop_img_path)
    width, height = img.size
    print(f"Full desktop image size: {width}x{height}")
    
    # Analyze variance by dividing the image into 100px vertical blocks and getting their standard deviations
    print("Vertical blocks (y-start to y-end) and standard deviation of pixel values:")
    for y in range(4000, height, 100):
        box = (0, y, width, min(y+100, height))
        block = img.crop(box)
        stat = ImageStat.Stat(block)
        # stat.stddev gives the standard deviation for R, G, B channels
        avg_stddev = sum(stat.stddev) / len(stat.stddev)
        print(f"y={y:4d} to {min(y+100, height):4d}: avg stddev = {avg_stddev:.2f}")

    # Check for similarity to Hero section (first 500px)
    hero_block = img.crop((0, 0, width, 500))
    hero_pixels = list(hero_block.getdata())
    hero_len = len(hero_pixels)
    
    # We sample a few pixels to speed up calculation
    sample_indices = list(range(0, hero_len, 1000))
    
    for y in range(4000, height - 500, 100):
        comp_block = img.crop((0, y, width, y + 500))
        comp_pixels = list(comp_block.getdata())
        
        diff_sum = 0
        for idx in sample_indices:
            p1 = hero_pixels[idx]
            p2 = comp_pixels[idx]
            diff_sum += sum((c1 - c2)**2 for c1, c2 in zip(p1, p2))
        
        rms = (diff_sum / len(sample_indices))**0.5
        if rms < 40.0:
            print(f"WARNING: Section at y={y} to {y+500} is very similar to top Hero section! RMS = {rms:.2f}")
            
else:
    print("Full image not found.")
