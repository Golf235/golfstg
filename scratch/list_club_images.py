import os
import re

club_files = ['opener.html', 'mover.html', 'riser.html', 'pitcher.html', 'maker.html', 'maker-tour.html', 'saver.html', 'butler.html']

for club in club_files:
    if os.path.exists(club):
        with open(club, 'r', encoding='utf-8') as f:
            content = f.read()
        images = re.findall(r'<img\s+[^>]*src="([^"]+)"', content, re.IGNORECASE)
        print(f"=== Images in {club} ===")
        for img in set(images):
            if 'loft' not in img and 'logo' not in img and 'cart' not in img and 'climate' not in img and 'length' not in img and 'lie' not in img and 'swing' not in img:
                print(f"  {img}")
