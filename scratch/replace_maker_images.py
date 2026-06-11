import os

html_files = [
    "butler.html",
    "index.html",
    "maker-tour.html",
    "maker.html",
    "mover.html",
    "opener.html",
    "pitcher.html",
    "riser.html",
    "saver.html",
    "sevenclubgame.html",
    "temp_tablet_fixed_heights.html"
]

base_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"

for filename in html_files:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (does not exist)")
        continue
        
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    # Replace 015.jpg with maker_premier.png
    new_content = new_content.replace('src="./015.jpg"', 'src="./maker_premier.png"')
    new_content = new_content.replace('src="./015.jpg"', 'src="./maker_premier.png"') # in case of double quotes/single quotes differences
    
    # Replace 016.jpg with maker_tour.png
    new_content = new_content.replace('src="./016.jpg"', 'src="./maker_tour.png"')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {filename}")
    else:
        print(f"No changes made in {filename}")
