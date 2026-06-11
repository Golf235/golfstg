import os
import urllib.request

urls = {
    "GFY_Sevenclubgame_Riser.gif": "https://golfyr.com/wp-content/uploads/2025/07/GFY_Sevenclubgame_Riser.gif",
    "why-the-riser-3.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-riser-3.jpg",
    "why-the-riser-4.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-riser-4.jpg",
    "Riser.png": "https://golfyr.com/wp-content/uploads/2025/07/Riser.png",
    "techspecs-riser-loft.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-riser-loft.png",
    "techspecs-riser-length.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-riser-length.png",
    "techspecs-riser-lie.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-riser-lie.png",
    "for-who-the-riser-1920.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-riser-1920.jpg",
    "for-who-the-riser-768.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-riser-768-768x1024.jpg",
    "for-who-the-riser-430.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-riser-430-498x1024.jpg"
}

output_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/The Riser - Golfyr_files"
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

print("All Riser downloads complete.")
