import os
import urllib.request

urls = {
    # Hero images
    "260323_Marketing_Header_Images_016_1024x576-1-1024x576.jpg": "https://golfyr.com/wp-content/uploads/2026/03/260323_Marketing_Header_Images_016_1024x576-1-1024x576.jpg",
    "260323_Marketing_Header_Images_017_768x1024-1-768x1024.jpg": "https://golfyr.com/wp-content/uploads/2026/03/260323_Marketing_Header_Images_017_768x1024-1-768x1024.jpg",
    "260323_Marketing_Header_Images_018_498X1024-1-498x1024.jpg": "https://golfyr.com/wp-content/uploads/2026/03/260323_Marketing_Header_Images_018_498X1024-1-498x1024.jpg",
    
    # Why choose images
    "GFY_Sevenclubgame_Saver.gif": "https://golfyr.com/wp-content/uploads/2025/07/GFY_Sevenclubgame_Saver.gif",
    "why-the-saver-2.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-saver-2.jpg",
    "why-the-saver-3.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-saver-3.jpg",
    "why-the-saver-4.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-saver-4.jpg",
    
    # Graphic
    "Saver.png": "https://golfyr.com/wp-content/uploads/2025/07/Saver.png",
    
    # Tech specs
    "techspecs-saver-loft.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-saver-loft.png",
    "techspecs-saver-length.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-saver-length.png",
    "techspecs-saver-lie.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-saver-lie.png",
    
    # For who backgrounds
    "for-who-the-saver-1920.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-saver-1920.jpg",
    "for-who-the-saver-768-768x1024.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-saver-768-768x1024.jpg",
    "for-who-the-saver-430-498x1024.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-saver-430-498x1024.jpg",
}

output_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/The Saver - Golfyr_files"
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

print("All Saver downloads complete.")
