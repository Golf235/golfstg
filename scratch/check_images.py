import os
from PIL import Image

artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'
files = [
    'sevenclubgame_desktop_hero.png',
    'sevenclubgame_desktop_reimagined.png',
    'sevenclubgame_desktop_map.png',
    'sevenclubgame_desktop_newsletter.png',
    'sevenclubgame_mobile_hero.png',
    'sevenclubgame_mobile_map.png',
    'clean_index_slide_1.png',
    'clean_index_slide_2.png',
    'clean_sevenclubgame_slide_1.png',
    'clean_sevenclubgame_slide_2.png'
]

for filename in files:
    path = os.path.join(artifact_dir, filename)
    if not os.path.exists(path):
        print(f"{filename}: Does not exist")
        continue
    img = Image.open(path)
    colors = img.getcolors(maxcolors=256)
    if colors is not None and len(colors) <= 2:
        print(f"{filename}: Size={img.size}, bytes={os.path.getsize(path)}, Solid color! Colors: {colors}")
    else:
        print(f"{filename}: Size={img.size}, bytes={os.path.getsize(path)}, Good image (colors count > 256 or diverse)")
