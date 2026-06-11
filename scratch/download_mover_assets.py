import os
import urllib.request

urls = {
    "GFY_Sevenclubgame_Mover.gif": "https://golfyr.com/wp-content/uploads/2025/07/GFY_Sevenclubgame_Mover.gif",
    "why-the-mover-2.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-mover-2.jpg",
    "why-the-mover-3.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-mover-3.jpg",
    "why-the-mover-4.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-mover-4.jpg",
    "Mover.png": "https://golfyr.com/wp-content/uploads/2025/07/Mover.png",
    "techspecs-mover-loft.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-mover-loft.png",
    "techspecs-mover-swing-weight.png": "https://golfyr.com/wp-content/uploads/2025/09/techspecs-mover-swing-weight.png",
    "techspecs-mover-length.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-mover-length.png",
    "techspecs-mover-lie.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-mover-lie.png",
    "techspecs-mover-volume.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-mover-volume.png",
    "for-who-the-mover-430.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-mover-430-498x1024.jpg",
    "for-who-the-mover-768.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-mover-768-768x1024.jpg",
    "for-who-the-mover-1920.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-mover-1920.jpg"
}

output_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/The Mover - Golfyr_files"
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

print("All downloads complete.")
