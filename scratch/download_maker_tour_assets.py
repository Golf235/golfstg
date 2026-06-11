import urllib.request
import os
import shutil

# Paths
base_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
asset_dir = os.path.join(base_dir, "Maker Tour - Golfyr_files")
maker_asset_dir = os.path.join(base_dir, "The Maker - Golfyr_files")

os.makedirs(asset_dir, exist_ok=True)

# 1. URLs to download
urls = {
    "background_01.jpg": "https://golfyr.com/wp-content/uploads/2025/10/260227_Marketing_Maker-Tour_Background_0-1.jpg",
    "background_02.jpg": "https://golfyr.com/wp-content/uploads/2025/10/260227_Marketing_Maker-Tour_Background_02-1.jpg",
    "background_03.jpg": "https://golfyr.com/wp-content/uploads/2025/10/260227_Marketing_Maker-Tour_Background_03-1.jpg",
    "background_04.jpg": "https://golfyr.com/wp-content/uploads/2025/10/260227_Marketing_Maker-Tour_Background_04-1.jpg",
    "background_05.jpg": "https://golfyr.com/wp-content/uploads/2025/10/260227_Marketing_Maker-Tour_Background_05-1.jpg",
    "background_06.jpg": "https://golfyr.com/wp-content/uploads/2025/10/260227_Marketing_Maker-Tour_Background_06-1.jpg",
    "background_07.jpg": "https://golfyr.com/wp-content/uploads/2025/10/260227_Marketing_Maker-Tour_Background_07-1.jpg",
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, url in urls.items():
    dest = os.path.join(asset_dir, filename)
    if not os.path.exists(dest):
        print(f"Downloading {filename} from {url}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            print(f"Successfully downloaded {filename} ({os.path.getsize(dest)} bytes)")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")
    else:
        print(f"{filename} already exists")

# 2. Copy techspecs icons from The Maker
spec_files = [
    "techspecs-maker-headtype.png",
    "techspecs-maker-loft.png",
    "techspecs-maker-lie.png",
    "techspecs-maker-head-weight.png",
    "techspecs-maker-hosel.png",
    "techspecs-maker-moi.png"
]

for sf in spec_files:
    src = os.path.join(maker_asset_dir, sf)
    dest = os.path.join(asset_dir, sf)
    if os.path.exists(src) and not os.path.exists(dest):
        shutil.copy2(src, dest)
        print(f"Copied {sf} from The Maker")
    elif os.path.exists(dest):
        print(f"{sf} already exists in Maker Tour")
    else:
        print(f"Could not find {sf} in The Maker")

# 3. Copy other local assets if any
src_sergio = os.path.join(base_dir, "Maker Tour - Golfyr_files", "sergio-garcia_person-845x1024.webp")
dest_sergio = os.path.join(asset_dir, "sergio-garcia_person-845x1024.webp")
if os.path.exists(src_sergio) and src_sergio != dest_sergio:
    shutil.copy2(src_sergio, dest_sergio)
    print("Copied sergio-garcia_person-845x1024.webp to local folder")

# Copy the ecommerce WebP image of Maker3 Tour if exists in configurator
src_tour_img = os.path.join(base_dir, "Golfyr Configurator V2_files", "GFY_eCommerce_422x490px_Maker3_Tour_02.webp")
dest_tour_img = os.path.join(asset_dir, "maker-tour-product.webp")
if os.path.exists(src_tour_img) and not os.path.exists(dest_tour_img):
    shutil.copy2(src_tour_img, dest_tour_img)
    print("Copied GFY_eCommerce_422x490px_Maker3_Tour_02.webp as maker-tour-product.webp")

print("All asset setup complete.")
