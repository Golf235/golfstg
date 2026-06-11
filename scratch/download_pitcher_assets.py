import os
import urllib.request

urls = {
    "GFY_Sevenclubgame_Pitcher.gif": "https://golfyr.com/wp-content/uploads/2025/07/GFY_Sevenclubgame_Pitcher.gif",
    "why-the-pitcher-3.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-pitcher-3.jpg",
    "why-the-pitcher-4.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-pitcher-4.jpg",
    "Pitcher.png": "https://golfyr.com/wp-content/uploads/2025/07/Pitcher.png",
    "techspecs-pitcher-loft.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-pitcher-loft.png",
    "techspecs-pitcher-length.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-pitcher-length.png",
    "techspecs-pitcher-lie.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-pitcher-lie.png",
    "for-who-the-pitcher-1920.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-pitcher-1920.jpg",
    "for-who-the-pitcher-768.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-pitcher-768-768x1024.jpg",
    "for-who-the-pitcher-430.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-pitcher-430-498x1024.jpg"
}

output_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/The Pitcher - Golfyr_files"
os.makedirs(output_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, url in urls.items():
    dest = os.path.join(output_dir, filename)
    print(f"Downloading {url} -> {dest}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(dest, 'wb') as f:
                f.write(response.read())
        print(f"  Successfully downloaded {filename}")
    except Exception as e:
        print(f"  Error downloading {filename}: {e}")

print("All Pitcher downloads complete.")
