import os
import urllib.request

urls = {
    # Hero images
    "260323_Marketing_Header_Images_019_1024x576-1-1024x576.jpg": "https://golfyr.com/wp-content/uploads/2026/03/260323_Marketing_Header_Images_019_1024x576-1-1024x576.jpg",
    "260323_Marketing_Header_Images_020_768x1024-1-768x1024.jpg": "https://golfyr.com/wp-content/uploads/2026/03/260323_Marketing_Header_Images_020_768x1024-1-768x1024.jpg",
    "260323_Marketing_Header_Images_021_498X1024-1-498x1024.jpg": "https://golfyr.com/wp-content/uploads/2026/03/260323_Marketing_Header_Images_021_498X1024-1-498x1024.jpg",
    
    # Why choose images
    "GFY_Sevenclubgame_Maker.gif": "https://golfyr.com/wp-content/uploads/2025/07/GFY_Sevenclubgame_Maker.gif",
    "why-the-maker-2.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-maker-2.jpg",
    "why-the-maker-3.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-maker-3.jpg",
    "why-the-maker-4.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-maker-4.jpg",
    
    # Graphic
    "Maker.png": "https://golfyr.com/wp-content/uploads/2025/07/Maker.png",
    
    # Tech specs
    "techspecs-maker-loft.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-maker-loft.png",
    "techspecs-maker-moi.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-maker-moi.png",
    "techspecs-maker-headtype.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-maker-headtype.png",
    "techspecs-maker-head-weight.png": "https://golfyr.com/wp-content/uploads/2025/09/techspecs-maker-head-weight.png",
    "techspecs-maker-hosel.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-maker-hosel.png",
    "techspecs-maker-lie.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-maker-lie.png",
    
    # For who backgrounds
    "for-who-the-maker-1920.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-maker-1920.jpg",
    "for-who-the-maker-768-768x1024.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-maker-768-768x1024.jpg",
    "for-who-the-maker-430-498x1024.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-maker-430-498x1024.jpg",
    
    # Footer Maker Tour image
    "39_Golfyr_Maker3_Tour_16513_V1_sRGB_300dpi-1-scaled-e1778584003794-887x1024.jpg": "https://golfyr.com/wp-content/uploads/2026/05/39_Golfyr_Maker3_Tour_16513_V1_sRGB_300dpi-1-scaled-e1778584003794-887x1024.jpg"
}

output_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/The Maker - Golfyr_files"
os.makedirs(output_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, url in urls.items():
    dest = os.path.join(output_dir, filename)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print(f"{filename} already exists and is not empty. Skipping.")
        continue
    print(f"Downloading {url} -> {dest}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(dest, 'wb') as f:
                f.write(response.read())
        print(f"  Successfully downloaded {filename}")
    except Exception as e:
        print(f"  Error downloading {filename}: {e}")

print("All Maker downloads complete.")
