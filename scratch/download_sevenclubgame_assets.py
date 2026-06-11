import os
import shutil
import urllib.request

# Target folder
target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Sevenclubgame - Golfyr_files'))
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

os.makedirs(target_dir, exist_ok=True)

# List of assets to download from live website
assets = {
    'hero_mobile.jpg': 'https://golfyr.com/wp-content/uploads/2026/05/10-112-1024x788.jpg',
    'hero_desktop.jpg': 'https://golfyr.com/wp-content/uploads/2026/05/11a-1024x512.jpg',
    'approach_forgiveness_en.png': 'https://golfyr.com/wp-content/uploads/2026/05/8-10-807x1024.png',
    'approach_forgiveness_de.png': 'https://golfyr.com/wp-content/uploads/2026/05/8-10-1-807x1024.png',
    'approach_simplicity.png': 'https://golfyr.com/wp-content/uploads/2026/05/8-102-807x1024.png',
    'approach_joy.png': 'https://golfyr.com/wp-content/uploads/2026/05/8-103-807x1024.png',
    'reimagined_mobile.jpg': 'https://golfyr.com/wp-content/uploads/2026/05/12-143-1024x1024.jpg',
    'reimagined_tablet.jpg': 'https://golfyr.com/wp-content/uploads/2026/05/12-14-1024x512.jpg',
    'reimagined_desktop.jpg': 'https://golfyr.com/wp-content/uploads/2026/05/10-scaled.jpg',
    'cartbag-gray.gif': 'https://golfyr.com/wp-content/uploads/2025/05/cartbag-gray.gif',
    # German maps
    'Map-mobile_opener_de.png': 'https://golfyr.com/wp-content/uploads/2025/02/Map-mobile_DE_Opener-2.png',
    'Map-mobile_mover_de.png': 'https://golfyr.com/wp-content/uploads/2025/02/Map-mobile_DE_Mover-2.png',
    'Map-mobile_riser_de.png': 'https://golfyr.com/wp-content/uploads/2025/02/Map-mobile_DE_Riser-2.png',
    'Map-mobile_pitcher_de.png': 'https://golfyr.com/wp-content/uploads/2025/02/Map-mobile_DE_Pitcher-2.png',
    'Map-mobile_maker_de.png': 'https://golfyr.com/wp-content/uploads/2025/02/Map-mobile_DE_Maker-2.png',
    'Map-mobile_saver_de.png': 'https://golfyr.com/wp-content/uploads/2025/02/Map-mobile_DE_Saver-2.png',
    'Map_Mobile_Butler_de.png': 'https://golfyr.com/wp-content/uploads/2026/03/Map_Mobile_Butler_DE.png',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("Starting asset downloads...")
for name, url in assets.items():
    dest = os.path.join(target_dir, name)
    if os.path.exists(dest):
        print(f"Asset {name} already downloaded, skipping.")
        continue
    try:
        print(f"Downloading {name} from {url}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f"Downloaded {name} successfully.")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

# Copy existing English map files from root
map_copies = {
    'Map-mobile_opener_eng.png': 'Map-mobile_opener_en.png',
    'Map-mobile_mover_eng.png': 'Map-mobile_mover_en.png',
    'Map-mobile_riser_eng.png': 'Map-mobile_riser_en.png',
    'Map-mobile_pitcher_eng.png': 'Map-mobile_pitcher_en.png',
    'Map-mobile_maker_eng.png': 'Map-mobile_maker_en.png',
    'Map-mobile_saver_eng.png': 'Map-mobile_saver_en.png',
    'Map_Mobile_Butler_EN.png': 'Map_Mobile_Butler_en.png',
}

print("\nCopying English map assets from root...")
for src_name, dest_name in map_copies.items():
    src_path = os.path.join(root_dir, src_name)
    dest_path = os.path.join(target_dir, dest_name)
    if os.path.exists(src_path):
        try:
            shutil.copy2(src_path, dest_path)
            print(f"Copied {src_name} to {dest_name} successfully.")
        except Exception as e:
            print(f"Error copying {src_name}: {e}")
    else:
        print(f"Warning: source map file {src_name} not found in root directory!")

print("\nAsset preparation completed.")
